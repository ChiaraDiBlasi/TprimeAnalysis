import ROOT
import math
import os
from samples.samples import sample_dict

# ============================================================
# PATH
# ============================================================

path = "/eos/user/f/fscrivan/tDM/postselector_results/2024/plots/plots/"
output_path = "/eos/user/f/fscrivan/tDM/postselector_results/2024/plots/"
output_paths = {
    plot_type: os.path.join(output_path, plot_type)
    for plot_type in ("efficiency", "significance")
}
for directory in output_paths.values():
    os.makedirs(directory, exist_ok=True)
allow_missing_nominal = True
lumi = 109.95
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)


def get_nominal_histogram(f, variable, region):
    hist_name = f"{variable}_{region}_nominal"
    h = f.Get(hist_name)
    if not h and allow_missing_nominal:
        h = f.Get(f"{variable}_{region}")
    if not h:
        raise RuntimeError(
            f"[ERROR HIST] file={f.GetName()}, hist={hist_name}, "
            f"allow_missing_nominal={allow_missing_nominal}"
        )
    return h

# ============================================================
# SIGNAL SAMPLES
# ============================================================

samples_DM = [
    "TBDM_s",
    "TBDM_ps",
    "TWDM_s",
    "TWDM_ps",
    "TWto2LDM_s",
    "TWto2LDM_ps",
    "TTDM_s",
    "TTDM_ps",
    "TTto2LDM_s",
    "TTto2LDM_ps",
]


# ============================================================
# Z + JETS COMPONENTS
# ============================================================

Z_samples = [
    "ZJetsToNuNu_2jets_PT40to100_1J_2024",
    "ZJetsToNuNu_2jets_PT100to200_1J_2024",
    "ZJetsToNuNu_2jets_PT200to400_1J_2024",
    "ZJetsToNuNu_2jets_PT400to600_1J_2024",
    "ZJetsToNuNu_2jets_PT600_1J_2024",

    "ZJetsToNuNu_2jets_PT40to100_2J_2024",
    "ZJetsToNuNu_2jets_PT100to200_2J_2024",
    "ZJetsToNuNu_2jets_PT200to400_2J_2024",
    "ZJetsToNuNu_2jets_PT400to600_2J_2024",
    "ZJetsToNuNu_2jets_PT600_2J_2024",
]


# ============================================================
# TT SAMPLES
# ============================================================

TT_samples = [
    "TT_semilep_2024",
    "TT_hadr_2024",
    "TT_dilep_2024",
]


# ============================================================
# BACKGROUND SAMPLES
# ============================================================

background_groups = {
    "ZJetsToNuNu_2J_2024": Z_samples,
    "WJets_2jets_2024": [s.label for s in sample_dict["WJets_2jets_2024"].components],
    "TW_2024": [s.label for s in sample_dict["TW_2024"].components],
    "QCD_2024": [s.label for s in sample_dict["QCD_2024"].components],
}
background_samples = TT_samples + [
    sample for components in background_groups.values() for sample in components
]


# ============================================================
# MASSE DI PHI
# ============================================================

masses = [
    10,
    50,
    100,
    150,
    200,
    250,
    300,
    350,
    400,
    500,
    600,
    700,
    800,
    1000,
]


# ============================================================
# REGIONS
# ============================================================

regions = [
    "SRTop_NO_lepVeto",
    "SRTop_loose_lepVeto",
    "SRTop_tight_lepVeto",
    "SRTop_looseORtight_lepVeto",
]


# ============================================================
# VARIABLES
# ============================================================

variables = [
    "PuppiMET_pt",

    # In futuro puoi aggiungere, per esempio:
    # "HT",
    # "nJet",
    # "LeadingJet_pt",
]


# ============================================================
# SIGNAL: DIZIONARI
# ============================================================

files = {}
histograms = {}


# ============================================================
# SIGNAL: APERTURA FILE E ISTOGRAMMI
# ============================================================

for sample in samples_DM:

    files[sample] = {}
    histograms[sample] = {}

    for mass in masses:

        file_name = f"{sample}_mPhi{mass}_mChi1_2024.root"

        f = ROOT.TFile.Open(os.path.join(path, file_name))

        if not f or f.IsZombie():

            raise RuntimeError(
                f"[ERROR FILE] "
                f"sample={sample}, "
                f"mPhi={mass}"
            )


        files[sample][mass] = f

        histograms[sample][mass] = {}


        # ====================================================
        # Loop sulle region
        # ====================================================

        for region in regions:

            histograms[sample][mass][region] = {}


            # =================================================
            # Loop sulle variabili
            # =================================================

            for variable in variables:

                hist_name = f"{variable}_{region}_nominal"

                h = get_nominal_histogram(f, variable, region)


                if not h:

                    raise RuntimeError(
                        f"[ERROR HIST] "
                        f"sample={sample}, "
                        f"mPhi={mass}, "
                        f"region={region}, "
                        f"variable={variable}, "
                        f"hist={hist_name}"
                    )


                histograms[sample][mass][region][variable] = h


                print(
                    f"[OK] "
                    f"sample={sample}, "
                    f"mPhi={mass}, "
                    f"region={region}, "
                    f"variable={variable}"
                )


# ============================================================
# BACKGROUND: DIZIONARI
# ============================================================

files_bkg = {}
histograms_bkg = {}


# ============================================================
# BACKGROUND: APERTURA FILE E ISTOGRAMMI
# ============================================================

for sample in background_samples:

    file_name = f"{sample}.root"

    f = ROOT.TFile.Open(os.path.join(path, file_name))


    if not f or f.IsZombie():

        raise RuntimeError(
            f"[ERROR FILE] "
            f"sample={sample}"
        )


    files_bkg[sample] = f

    histograms_bkg[sample] = {}


    # ========================================================
    # Loop sulle region
    # ========================================================

    for region in regions:

        histograms_bkg[sample][region] = {}


        # ====================================================
        # Loop sulle variabili
        # ====================================================

        for variable in variables:

            hist_name = f"{variable}_{region}_nominal"

            h = get_nominal_histogram(f, variable, region)


            if not h:

                raise RuntimeError(
                    f"[ERROR HIST] "
                    f"sample={sample}, "
                    f"region={region}, "
                    f"variable={variable}, "
                    f"hist={hist_name}"
                )


  
            histograms_bkg[sample][region][variable] = h


            print(
                f"[OK] "
                f"sample={sample}, "
                f"region={region}, "
                f"variable={variable}"
            )

# ============================================================
# UNIONE DELLE COMPONENTI DI Z, W, TW E QCD
# ============================================================

for group, components in background_groups.items():
    histograms_bkg[group] = {}
    for region in regions:
        histograms_bkg[group][region] = {}
        for variable in variables:
            h_sum = histograms_bkg[components[0]][region][variable].Clone(
                f"{variable}_{region}_{group}"
            )
            h_sum.SetDirectory(0)
            for sample in components[1:]:
                h_sum.Add(histograms_bkg[sample][region][variable])
            histograms_bkg[group][region][variable] = h_sum
    for sample in components:
        del histograms_bkg[sample]

efficiency_histograms = {}
significance_histograms = {}
ratio = []
h_eff = {}
background_samples = [
    "ZJetsToNuNu_2J_2024",
    "TT_semilep_2024",
    "TT_hadr_2024",
    "TT_dilep_2024",
    "WJets_2jets_2024",
    "TW_2024",
    "QCD_2024",
]


# ============================================================
#calcolo numero di eventi bkg
# ============================================================
n_eventi_bkg = {}

for region in regions:
    n_eventi_bkg[region] = {}
    for variable in variables:
        n_eventi = 0
        for bkg in background_samples:
            n_eventi_histo = histograms_bkg[bkg][region][variable]

            n_eventi += n_eventi_histo.Integral(
                1, n_eventi_histo.GetNbinsX()
            )

        if not math.isfinite(n_eventi) or n_eventi <= 0:
            raise ValueError(
                f"Background non positivo o non finito: "
                f"region={region}, variable={variable}, B={n_eventi}"
            )
        n_eventi = n_eventi * lumi
        n_eventi_bkg[region][variable] = n_eventi
        

for sample in samples_DM:

    efficiency_histograms[sample] = {}
    significance_histograms[sample] = {}
    h_eff = {}
    h_sig ={}

    for region in regions:

        # SRTop_NO_lepVeto serve solo come denominatore
        if region == "SRTop_NO_lepVeto":
            continue

        h_eff[region] = {}
        h_sig[region] ={}
  

        for variable in variables:

            h = ROOT.TH1D(
                f"h_eff_{sample}_{region}_{variable}",
                f"{sample} - {region};m_{{#phi}} [GeV];N(region) / N(SRTop_NO_lepVeto)",
                len(masses),
                0,
                len(masses)
            )
            h2 = ROOT.TH1D(
                f"h_sig_{sample}_{region}_{variable}",
                f"{sample} - {region};m_{{#phi}} [GeV];Sig/#sqrt{{Bkg}}",
                len(masses),
                0,
                len(masses)
            )


            h.SetDirectory(0)
            h2.SetDirectory(0)

            for i, mass in enumerate(masses, start=1):

                # label del bin
                h.GetXaxis().SetBinLabel(i, str(mass))
                h2.GetXaxis().SetBinLabel(i, str(mass))

                

                # Istogramma SRTop_NO_lepVeto senza taglio
                h_den = histograms[sample][mass]["SRTop_NO_lepVeto"][variable]

                # Istogramma SRTop con il taglio
                h_num = histograms[sample][mass][region][variable]

                den = h_den.Integral(
                    1,
                    h_den.GetNbinsX()
                )

                num = h_num.Integral(
                    1,
                    h_num.GetNbinsX()
                )

                if not math.isfinite(den) or den == 0 or not math.isfinite(num):
                    raise ValueError(
                        f"Efficienza non calcolabile: sample={sample}, "
                        f"mPhi={mass}, region={region}, variable={variable}, "
                        f"num={num}, den={den}"
                    )
                r = num / den
                ratio.append(r)
                h.SetBinContent(i, r)
                num = num * lumi
                # Il background e' gia' stato validato come positivo e finito.
                s = num / math.sqrt(n_eventi_bkg[region][variable])
                h2.SetBinContent(i, s)

            h_eff[region][variable] = h
            h_sig[region][variable] = h2

    efficiency_histograms[sample] = h_eff
    significance_histograms[sample] = h_sig

# ============================================================
#BKG: ISTOGRAMMI DI EFFICIENZA VS mPhi
# ============================================================       
efficiency_histograms_bkg = {}
ratio_bkg = []
h_eff_bkg = {}

for region in regions:

    if region == "SRTop_NO_lepVeto":
        continue

    efficiency_histograms_bkg[region] = {}
    h_eff_bkg[region] = {}

    for variable in variables:

        h = ROOT.TH1D(
            f"h_eff_{region}_{variable}",
            f"Background efficiency;Background;N(region) / N(SRTop_NO_lepVeto)",
            len(background_samples),
            0,
            len(background_samples)
        )

        h.SetDirectory(0)

        for i, sample in enumerate(background_samples, start=1):

            # label del bin
            h.GetXaxis().SetBinLabel(i, str(sample))

            # Istogramma SRTop_NO_lepVeto senza taglio
            h_den = histograms_bkg[sample]["SRTop_NO_lepVeto"][variable]

            # Istogramma SRTop con il taglio
            h_num = histograms_bkg[sample][region][variable]

            den = h_den.Integral(
                1,
                h_den.GetNbinsX()
            )

            num = h_num.Integral(
                1,
                h_num.GetNbinsX()
            )

            if not math.isfinite(den) or den == 0 or not math.isfinite(num):
                raise ValueError(
                    f"Efficienza background non calcolabile: sample={sample}, "
                    f"region={region}, variable={variable}, num={num}, den={den}"
                )
            r = num / den
            ratio_bkg.append(r)
            h.SetBinContent(i, r)

        h_eff_bkg[region][variable] = h
        efficiency_histograms_bkg[region][variable] = h
# ============================================================
# SIGNAL: DISEGNO
# ============================================================

canvases = {}
legends = {}
legends_sig = {}
istograms = ["efficiency", "significance"]

histograms_by_type = {
    "efficiency": efficiency_histograms,
    "significance": significance_histograms
}
type_of_istograms ={}
for type in histograms_by_type:
    canvases[type] = {}
    legends[type]={}
    for sample in samples_DM:
        

        canvases[type][sample] = {}
        legends[type][sample] = {}


        for variable in variables:

            c = ROOT.TCanvas(
                f"c_{type}_{sample}_{variable}",
                f"{sample} - {variable}",
                1000,
                700
            )

            canvases[type][sample][variable] = c
            #efficiency
            h_loose = histograms_by_type[type][sample][
                "SRTop_loose_lepVeto"
            ][variable]

            h_tight = histograms_by_type[type][sample][
                "SRTop_tight_lepVeto"
            ][variable]

            h_looseORtight = histograms_by_type[type][sample][
                "SRTop_looseORtight_lepVeto"
            ][variable]
            if type == "significance":
                h_loose.SetTitle(
                    f"{sample}-significance;m_{{#phi}} [GeV];Sig/#sqrt{{Bkg}}"
                )
            if type == "efficiency":
                h_loose.SetTitle(
                    f"{sample}_efficiency;m_{{#phi}} [GeV];N(region) / N(SRTop_NO_lepVeto)"
                )

            # Loose
            h_loose.SetLineColor(ROOT.kViolet + 6)
            h_loose.SetLineWidth(2)

            # Tight
            h_tight.SetLineColor(ROOT.kTeal - 6)
            h_tight.SetLineWidth(2)

            # Loose OR Tight
            h_looseORtight.SetLineColor(ROOT.kOrange - 3)
            h_looseORtight.SetLineWidth(2)
            h_looseORtight.SetLineStyle(2)
            curves = (h_loose, h_tight, h_looseORtight)
            ymin = min(curve.GetMinimum() for curve in curves)
            ymax = max(curve.GetMaximum() for curve in curves)
            margin = 0.1 * max(ymax - ymin, abs(ymax), 1e-6)
            h_loose.SetMinimum(min(0.0, ymin - margin))
            h_loose.SetMaximum(ymax + margin)

            h_loose.Draw("HIST")
            h_tight.Draw("HIST SAME")
            h_looseORtight.Draw("HIST SAME")


            legend = ROOT.TLegend(
                0.52,
                0.70,
                0.88,
                0.88
            )

            legend.SetBorderSize(0)
            legend.SetFillStyle(0)

            legend.AddEntry(
                h_loose,
                "Loose veto",
                "l"
            )

            legend.AddEntry(
                h_tight,
                "Tight veto",
                "l"
            )

            legend.AddEntry(
                h_looseORtight,
                "Loose OR Tight veto",
                "l"
            )

            legend.Draw()

            legends[type][sample][variable] = legend

            c.Update()





# ============================================================
# SIGNAL: SALVATAGGIO
# ============================================================
for type in istograms:
    for sample in samples_DM:

        for variable in variables:

                c = canvases[type][sample][variable]

                c.SaveAs(
                    os.path.join(output_paths[type],
                                 f"{type}_{sample}_{variable}_SRTop_vs_mPhi.png")
                )

                c.SaveAs(
                    os.path.join(output_paths[type],
                                 f"{type}_{sample}_{variable}_SRTop_vs_mPhi.pdf")
                )

                c.SaveAs(
                    os.path.join(output_paths[type],
                                 f"{type}_{sample}_{variable}_SRTop_vs_mPhi.C")
                )


# ============================================================
# BKG: DISEGNO
# ============================================================

type_of_istograms ={}
canvases_bkg ={}
legends_bkg ={}
histograms_by_type_bkg = {
    "efficiency": efficiency_histograms_bkg
}
for type in histograms_by_type_bkg:
    canvases_bkg[type] = {}
    legends_bkg[type] = {}


    for variable in variables:
        c = ROOT.TCanvas(
            f"c_bkg_{variable}",
            f"Background - {variable}",
            1000,
            700
        )

        canvases_bkg[type][variable] = c

        h_loose = histograms_by_type_bkg[type][
            "SRTop_loose_lepVeto"
        ][variable]

        h_tight = histograms_by_type_bkg[type][
            "SRTop_tight_lepVeto"
        ][variable]

        h_looseORtight = histograms_by_type_bkg[type][
            "SRTop_looseORtight_lepVeto"
        ][variable]

        h_loose.SetTitle(
            f"Background efficiency - {variable};Background;N(region) / N(SRTop_NO_lepVeto)"
        )

        # Loose
        h_loose.SetLineColor(ROOT.kViolet + 6)
        h_loose.SetLineWidth(2)

        # Tight
        h_tight.SetLineColor(ROOT.kTeal - 6)
        h_tight.SetLineWidth(2)

        # Loose OR Tight
        h_looseORtight.SetLineColor(ROOT.kOrange - 3)
        h_looseORtight.SetLineWidth(2)
        h_looseORtight.SetLineStyle(2)

        h_loose.SetMinimum(0.0)
        h_loose.SetMaximum(1.1)

        h_loose.Draw("HIST")
        h_tight.Draw("HIST SAME")
        h_looseORtight.Draw("HIST SAME")

        legend = ROOT.TLegend(
            0.52,
            0.70,
            0.88,
            0.88
        )

        legend.SetBorderSize(0)
        legend.SetFillStyle(0)

        legend.AddEntry(
            h_loose,
            "Loose veto",
            "l"
        )

        legend.AddEntry(
            h_tight,
            "Tight veto",
            "l"
        )

        legend.AddEntry(
            h_looseORtight,
            "Loose OR Tight veto",
            "l"
        )

        legend.Draw()

        legends_bkg[type][variable] = legend

        c.Update()


# ============================================================
# BKG: SALVATAGGIO
# ============================================================
for type in histograms_by_type_bkg:
    for variable in variables:
        c = canvases_bkg[type][variable]
        for ext in ("png", "pdf", "C"):
            c.SaveAs(
                os.path.join(output_paths[type], f"{variable}_SRTop_{type}_vs_BKG.{ext}")
            )
