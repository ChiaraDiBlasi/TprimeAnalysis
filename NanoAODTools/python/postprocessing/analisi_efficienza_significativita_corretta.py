import ROOT

import math

# ============================================================

# PATH

# ============================================================

path = "/eos/user/f/fscrivan/tDM/postselector_results/2024/plots/plots/"
path_bkg = "/eos/user/f/fscrivan/tDM/postselector_results/2024/2024_Chiara/"

output_path = "/eos/user/f/fscrivan/tDM/postselector_results/2024/plots/"

ROOT.gROOT.SetBatch(True)

ROOT.gStyle.SetOptStat(0)

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

# In 2024_Chiara il fondo Z+jets e' gia' riunito in un solo file.
Z_samples = ["ZJetsToNuNu_2jets"]

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

background_samples = Z_samples + TT_samples

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

    "SRTop",

    "SRTop_LooseVetoCut",

    "SRTop_TightVetoCut",

    "SRTop_LooseORTightVetoCut",

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

# Nomi delle stesse selezioni nei file di 2024_Chiara (senza _nominal).
# Il denominatore deve essere la selezione senza veto sui leptoni.
background_regions = {
    "SRTop": "SRTop_NO_lepVeto",
    "SRTop_LooseVetoCut": "SRTop_loose_lepVeto",
    "SRTop_TightVetoCut": "SRTop_tight_lepVeto",
    "SRTop_LooseORTightVetoCut": "SRTop_looseORtight_lepVeto",
}

# ============================================================

# ============================================================
# HELPERS
# ============================================================

import os
os.makedirs(output_path, exist_ok=True)

def get_histogram(store, *keys):
    """Restituisce l'istogramma, o None se un file/istogramma manca."""
    current = store
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current

def integral_all(h):
    return h.Integral(0, h.GetNbinsX() + 1)

# ============================================================
# APERTURA FILE SIGNAL
# ============================================================
files = {}
histograms = {}
for sample in samples_DM:
    files[sample] = {}
    histograms[sample] = {}
    for mass in masses:
        file_name = f"{sample}_mPhi{mass}_mChi1_2024.root"
        f = ROOT.TFile.Open(os.path.join(path, file_name))
        if not f or f.IsZombie():
            print(f"[ERROR FILE] signal={sample}, mPhi={mass}")
            continue
        files[sample][mass] = f
        histograms[sample][mass] = {}
        for region in regions:
            histograms[sample][mass][region] = {}
            for variable in variables:
                hist_name = f"{variable}_{region}_nominal"
                h = f.Get(hist_name)
                if not h:
                    print(f"[ERROR HIST] signal={sample}, mPhi={mass}, hist={hist_name}")
                    continue
                histograms[sample][mass][region][variable] = h

# ============================================================
# APERTURA FILE BACKGROUND
# ============================================================
files_bkg = {}
histograms_bkg = {}
for sample in background_samples:
    file_path = os.path.join(path_bkg, f"{sample}.root")
    f = ROOT.TFile.Open(file_path)
    if not f or f.IsZombie():
        raise RuntimeError(f"[ERROR FILE] background={sample}, file={file_path}")
    files_bkg[sample] = f
    histograms_bkg[sample] = {}
    for region in regions:
        histograms_bkg[sample][region] = {}
        for variable in variables:
            hist_name = f"{variable}_{background_regions[region]}"
            h = f.Get(hist_name)
            if not h:
                raise RuntimeError(
                    f"[ERROR HIST] background={sample}, file={file_path}, hist={hist_name}"
                )
            histograms_bkg[sample][region][variable] = h

# ============================================================
# UNIONE Z+JETS (clone per non modificare il primo input)
# ============================================================
combined_Z = "ZJetsToNuNu_2J_2024"
histograms_bkg[combined_Z] = {}
for region in regions:
    histograms_bkg[combined_Z][region] = {}
    for variable in variables:
        h_sum = None
        for sample in Z_samples:
            h = get_histogram(histograms_bkg, sample, region, variable)
            if h is None:
                continue
            if h_sum is None:
                h_sum = h.Clone(f"{variable}_{region}_{combined_Z}")
                h_sum.SetDirectory(0)
            else:
                h_sum.Add(h)
        if h_sum is not None:
            histograms_bkg[combined_Z][region][variable] = h_sum

# Conserva soltanto il fondo Z combinato e i campioni TT
background_samples = [combined_Z] + TT_samples

# ============================================================
# CONTEGGIO EVENTI BACKGROUND
# La struttura [region][variable] evita ambiguita' se aggiungi variabili.
# ============================================================
n_eventi_bkg = {}
for region in regions:
    n_eventi_bkg[region] = {}
    for variable in variables:
        B = 0.0
        for bkg in background_samples:
            h = get_histogram(histograms_bkg, bkg, region, variable)
            if h is None:
                print(f"[WARN] Fondo mancante: {bkg}, {region}, {variable}")
                continue
            B += integral_all(h)
        n_eventi_bkg[region][variable] = B

# ============================================================
# EFFICIENZA E SIGNIFICATIVITA' DEL SEGNALE
# ============================================================
efficiency_histograms = {}
significance_histograms = {}
ratio = []
for sample in samples_DM:
    efficiency_histograms[sample] = {}
    significance_histograms[sample] = {}
    for region in regions:
        if region == "SRTop":
            continue
        efficiency_histograms[sample][region] = {}
        significance_histograms[sample][region] = {}
        for variable in variables:
            h_eff = ROOT.TH1D(
                f"h_eff_{sample}_{region}_{variable}",
                f"{sample} - {region};m_{{#phi}} [GeV];N(region) / N(SRTop)",
                len(masses), 0, len(masses)
            )
            h_sig = ROOT.TH1D(
                f"h_sig_{sample}_{region}_{variable}",
                f"{sample} - {region};m_{{#phi}} [GeV];S/#sqrt{{B}}",
                len(masses), 0, len(masses)
            )
            h_eff.SetDirectory(0)
            h_sig.SetDirectory(0)
            B = n_eventi_bkg[region][variable]
            for i, mass in enumerate(masses, start=1):
                h_eff.GetXaxis().SetBinLabel(i, str(mass))
                h_sig.GetXaxis().SetBinLabel(i, str(mass))
                h_den = get_histogram(histograms, sample, mass, "SRTop", variable)
                h_num = get_histogram(histograms, sample, mass, region, variable)
                if h_den is None or h_num is None:
                    print(f"[WARN] Signal hist mancante: {sample}, {mass}, {region}, {variable}")
                    continue
                den = integral_all(h_den)
                num = integral_all(h_num)
                if den != 0:
                    r = num / den
                    ratio.append(r)
                    h_eff.SetBinContent(i, r)
                if B > 0:
                    h_sig.SetBinContent(i, num / math.sqrt(B))
            efficiency_histograms[sample][region][variable] = h_eff
            significance_histograms[sample][region][variable] = h_sig

# ============================================================
# EFFICIENZA DEL BACKGROUND
# ============================================================
efficiency_histograms_bkg = {}
ratio_bkg = []
for region in regions:
    if region == "SRTop":
        continue
    efficiency_histograms_bkg[region] = {}
    for variable in variables:
        h = ROOT.TH1D(
            f"h_eff_bkg_{region}_{variable}",
            "Background efficiency;Background;N(region) / N(SRTop)",
            len(background_samples), 0, len(background_samples)
        )
        h.SetDirectory(0)
        for i, sample in enumerate(background_samples, start=1):
            h.GetXaxis().SetBinLabel(i, sample)
            h_den = get_histogram(histograms_bkg, sample, "SRTop", variable)
            h_num = get_histogram(histograms_bkg, sample, region, variable)
            if h_den is None or h_num is None:
                continue
            den = integral_all(h_den)
            num = integral_all(h_num)
            if den != 0:
                r = num / den
                ratio_bkg.append(r)
                h.SetBinContent(i, r)
        efficiency_histograms_bkg[region][variable] = h

# ============================================================
# DISEGNO E SALVATAGGIO SIGNAL (EFFICIENCY + SIGNIFICANCE)
# ============================================================
canvases = {}
legends = {}
histograms_by_type = {
    "efficiency": efficiency_histograms,
    "significance": significance_histograms,
}
regions_to_draw = (
    ("SRTop_LooseVetoCut", "Loose veto", ROOT.kViolet + 6, 1),
    ("SRTop_TightVetoCut", "Tight veto", ROOT.kTeal - 6, 1),
    ("SRTop_LooseORTightVetoCut", "Loose OR Tight veto", ROOT.kOrange - 3, 2),
)
for hist_type, hist_dict in histograms_by_type.items():
    canvases[hist_type] = {}
    legends[hist_type] = {}
    for sample in samples_DM:
        canvases[hist_type][sample] = {}
        legends[hist_type][sample] = {}
        for variable in variables:
            c = ROOT.TCanvas(
                f"c_{hist_type}_{sample}_{variable}",
                f"{sample} - {variable} - {hist_type}", 1000, 700
            )
            canvases[hist_type][sample][variable] = c
            hs = []
            for region, label, color, style in regions_to_draw:
                h = hist_dict[sample][region][variable]
                h.SetLineColor(color)
                h.SetLineWidth(2)
                h.SetLineStyle(style)
                hs.append((h, label))
            h_first = hs[0][0]
            y_title = "N(region) / N(SRTop)" if hist_type == "efficiency" else "S/#sqrt{B}"
            h_first.SetTitle(f"{sample} - {hist_type};m_{{#phi}} [GeV];{y_title}")
            h_first.SetMinimum(max(0,h_first.GetMinimum()-0.1))
            if hist_type == "efficiency":
                h_first.SetMaximum(min(1.0,h_first.GetMaximum()+0.1))
            else:
                ymax = max(h.GetMaximum() for h, _ in hs)
                h_first.SetMaximum(1.2 * ymax if ymax > 0 else 1.0)
            c.cd()
            for j, (h, _) in enumerate(hs):
                h.Draw("HIST" if j == 0 else "HIST SAME")
            legend = ROOT.TLegend(0.52, 0.70, 0.88, 0.88)
            legend.SetBorderSize(0)
            legend.SetFillStyle(0)
            for h, label in hs:
                legend.AddEntry(h, label, "l")
            legend.Draw()
            legends[hist_type][sample][variable] = legend
            c.Update()
            filename = f"{sample}_{variable}_SRTop_{hist_type}_vs_mPhi"
            for ext in ("png", "pdf", "C"):
                c.SaveAs(os.path.join(output_path, f"{filename}.{ext}"))

# ============================================================
# DISEGNO E SALVATAGGIO EFFICIENZA BACKGROUND
# ============================================================
canvases_bkg = {}
legends_bkg = {}
for variable in variables:
    c = ROOT.TCanvas(f"c_bkg_{variable}", f"Background - {variable}", 1000, 700)
    canvases_bkg[variable] = c
    hs = []
    for region, label, color, style in regions_to_draw:
        h = efficiency_histograms_bkg[region][variable]
        h.SetLineColor(color)
        h.SetLineWidth(2)
        h.SetLineStyle(style)
        hs.append((h, label))
    h_first = hs[0][0]
    h_first.SetTitle(f"Background efficiency - {variable};Background;N(region) / N(SRTop)")
    h_first.SetMinimum(max(0,h_first.GetMinimum()-0.1))
    h_first.SetMaximum(min(1.0,h_first.GetMaximum()+0.2))
    c.cd()
    for j, (h, _) in enumerate(hs):
        h.Draw("HIST" if j == 0 else "HIST SAME")
    legend = ROOT.TLegend(0.52, 0.70, 0.88, 0.88)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    for h, label in hs:
        legend.AddEntry(h, label, "l")
    legend.Draw()
    legends_bkg[variable] = legend
    c.Update()
    filename = f"{variable}_SRTop_efficiency_vs_BKG"
    for ext in ("png", "pdf", "C"):
        c.SaveAs(os.path.join(output_path, f"{filename}.{ext}"))
