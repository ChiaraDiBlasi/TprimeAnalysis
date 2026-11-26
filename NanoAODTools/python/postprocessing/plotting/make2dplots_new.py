import sys
sys.path.append('../')
import ROOT
import os
import cmsstyle
from samples.samples import *
import json
ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat(0)
ROOT.TH1.AddDirectory(False)

lumi = 109.82 # fb-1
def createcanv(name_canv ):
    ############ CREATE CANVAS AND PADS ############ 
    cmsstyle.SetEnergy(13.6)
    cmsstyle.SetLumi(lumi, unit="fb", round_lumi=False)
    cmsstyle.SetExtraText("")
    # Scientific notation
    # Shift multiplier position
    ROOT.TGaxis.SetExponentOffset(-0.10, 0.01, "Y")
    canv = cmsstyle.cmsCanvas(name_canv, -0.5, 5.5, -0.5, 5.5, "# Top Mixed", "# Top Merged", square=True, with_z_axis=True, iPos=0)
    # hdf.GetZaxis().SetMaxDigits(2)
    # canv.SetLeftMargin(0.15)
    # canv.SetBottomMargin(0.15)
    canv.SetRightMargin(0.2)
    # canv.SetTopMargin(0.15)
    return canv

with open("/afs/cern.ch/user/c/cdiblasi/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json", "r") as f:
    filejson = json.load(f)


folder = "/eos/user/c/cdiblasi/tDM/postselector_results/2024/postselector_outpath/noTrotaSF/plots"
samples = []
filelist = []

for filename in sorted(os.listdir(folder)):
    if not filename.endswith(".root"):
        continue

    label = filename[:-5]  # rimuove .root
    if not label.startswith(("TBDM")):
        continue
    if label not in sample_dict:
        raise KeyError(f"Campione non definito: {label}")

    filelist.append(os.path.join(folder, filename))
    samples.append(sample_dict[label])





for wp in ["nTightTopMixedVsnTightTopMerged", "nXTightTopMixedVsnXTightTopMerged"]:
    for t in ["SR0ResFarFromMix", "SR1ResFarFromMix", "SRge2ResFarFromMix"]:
        canv = createcanv(f"{wp}_{t}")

        histogram_fin_bkg = ROOT.TH2D("", "", 6, -0.5, 5.5, 6, -0.5, 5.5)

        for filepath, sample in zip(filelist, samples):
            if "DM" in sample.label:
                continue
            histname = f"{wp}_{t}_tight_lepVeto"
            print("Loading histogram:", histname, "from file:", filepath)
            file = ROOT.TFile.Open(filepath)
            hist = file.Get(histname)
            xsec = sample.sigma if sample.sigma is not None else 1.0
            
            print(hist)
            hist.Scale(sample.sigma * 1000)
            histogram_fin_bkg.Add(hist)
            
            if not hist:
                print(f"Histogram {histname} not found in file {filepath}")
                continue
            canv.Close()
            file.Close()
        h1 = histogram_fin_bkg.Clone()
        #h1.Scale(1.0 / histogram_fin_bkg.Integral())

        cmsstyle.SetAlternative2DColor(h1, style=ROOT.gStyle)

        cmsstyle.cmsObjectDraw(h1,f"COLZ text")

        #cmsstyle.SaveCanvas(canv, f"/eos/user/f/fscrivan/www/tDM/plots/2024/efficiency/{wp}_{t}_bkg.png",  close=False)
        #cmsstyle.SaveCanvas(canv, f"/eos/user/f/fscrivan/www/tDM/plots/2024/efficiency/{wp}_{t}_bkg.pdf")

        histogram_fin ={}
        for filepath, sample in zip(filelist, samples):
            if "DM" not in sample.label:
                continue
            
            canv = createcanv(f"{wp}_{t}_{sample.label}")
            histogram_fin[sample.label] = ROOT.TH2D("", "", 6, -0.5, 5.5, 6, -0.5, 5.5)
            histname = f"{wp}_{t}_tight_lepVeto"
            # hist = load_2Dhist(filepath, histname)
            file = ROOT.TFile.Open(filepath)
            hist = file.Get(histname)
            xsec = sample.sigma if sample.sigma is not None else 1.0
            

            if hist is None:
                print(f"Histogram {histname} not found in file {filepath}")
                continue
            hist.Scale(1.0 / (sample.sigma * 1000))
            
            print(hist)
            histogram_fin[sample.label].Add(hist)
            h1 = histogram_fin[sample.label].Clone()
            h1.GetZaxis().SetTitle("Efficiency")

            #h1.Scale(1.0 / histogram_fin[sample.label].Integral())

            cmsstyle.SetAlternative2DColor(h1, style=ROOT.gStyle)

            cmsstyle.cmsObjectDraw(h1,f"COLZ text")
            
            label = ROOT.TLatex()
            label.SetNDC(True)
            label.SetTextFont(42)
            label.SetTextSize(0.025)

            wp_label = "Extra Tight" if "XTight" in wp else "Tight"
            label.DrawLatex(0.16, 0.86, sample.label)
            label.DrawLatex(0.16, 0.82, t)
            label.DrawLatex(0.16, 0.78, wp_label)
            outdir = os.path.join(
                "/eos/user/c/cdiblasi/www/tDM/plots/2024/efficiency",
                sample.label,
            )
            os.makedirs(outdir, exist_ok=True)
            cmsstyle.SaveCanvas(
                canv, os.path.join(outdir, f"{wp}_{t}.png"), close=False
            )
            cmsstyle.SaveCanvas(
                canv, os.path.join(outdir, f"{wp}_{t}.pdf")
            )
            canv.Close()
            file.Close()
"""
        for i in range(1, histogram_fin_bkg.GetNbinsX()+1):
            for j in range(1, histogram_fin_bkg.GetNbinsY() + 1):
                content = histogram_fin_bkg.GetBinContent(i, j)
                if content > 0:
                    histogram_fin_bkg.SetBinContent(i, j, content**0.5)

        for k in histogram_fin.keys():
            outdir = os.path.join("/eos/user/f/fscrivan/www/tDM/plots/2024","significance", k)
            os.makedirs(outdir, exist_ok=True)
            canv = createcanv(f"{wp}_{t}_{k}_significance")
            hdf = cmsstyle.GetcmsCanvasHist(canv)
            hdf.GetZaxis().SetTitle("Significance")
            hist_significance = histogram_fin[k].Clone()
            hist_significance.Divide(histogram_fin_bkg)
            cmsstyle.SetAlternative2DColor(hist_significance, style=ROOT.gStyle)
            cmsstyle.cmsObjectDraw(hist_significance, "COLZ text")
            canv.cd()

            label = ROOT.TLatex()
            label.SetNDC(True)
            label.SetTextFont(42)
            label.SetTextSize(0.025)
            wp_label = "Extra Tight" if "XTight" in wp else "Tight"

            label.DrawLatex(0.16, 0.86, k)
            label.DrawLatex(0.16, 0.82, t)
            label.DrawLatex(0.16, 0.78, wp_label)
            canv.cd()
            label = ROOT.TLatex()
            label.SetNDC(True)
            label.SetTextFont(42)
            label.SetTextSize(0.025)
            cmsstyle.SaveCanvas(canv, os.path.join(outdir, f"{wp}_{t}_significance.png"), close=False)
            cmsstyle.SaveCanvas(canv, os.path.join(outdir, f"{wp}_{t}_significance.pdf"))
"""