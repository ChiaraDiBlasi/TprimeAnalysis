import ROOT

# ============================================================
# PATH
# ============================================================

path = "/eos/user/f/fscrivan/tDM/postselector_results/2024/plots"

output_path = "/eos/user/f/fscrivan/tDM/postselector_results/2024/plots/"
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# ============================================================
# SIGNAL SAMPLES
# ============================================================

samples = [
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
# REGIONS / ISTOGRAMMI
# ============================================================

regions = {
    "SRTop":
        "PuppiMET_pt_SRTop_nominal",

    "SRTop_LooseVetoCut":
        "PuppiMET_pt_SRTop_LooseVetoCut_nominal",

    "SRTop_TightVetoCut":
        "PuppiMET_pt_SRTop_TightVetoCut_nominal",

    "SRTop_LooseORTightVetoCut":
        "PuppiMET_pt_SRTop_LooseORTightVetoCut_nominal",
}


# ============================================================
# REGION DA NORMALIZZARE A SRTop
# ============================================================

ratio_regions = [
    "SRTop_LooseVetoCut",
    "SRTop_TightVetoCut",
    "SRTop_LooseORTightVetoCut",
]


# ============================================================
# SIGNAL: APERTURA FILE + RECUPERO ISTOGRAMMI
# ============================================================

files = {}
histograms = {}

for sample in samples:

    files[sample] = {}
    histograms[sample] = {}

    for mphi in masses:

        filename = f"{sample}_mPhi{mphi}_mChi1_2024.root"
        filepath = path + filename

        print(f"\nOpening signal: {filepath}")

        f = ROOT.TFile.Open(filepath)

        if not f or f.IsZombie():

            print(
                f"[ERROR FILE] "
                f"sample={sample}, "
                f"mPhi={mphi}"
            )

            continue

        files[sample][mphi] = f
        histograms[sample][mphi] = {}

        for region, hist_name in regions.items():

            h = f.Get(hist_name)

            if not h:

                print(
                    f"[ERROR HIST] "
                    f"sample={sample}, "
                    f"mPhi={mphi}, "
                    f"region={region}, "
                    f"hist={hist_name}"
                )

                continue

            histograms[sample][mphi][region] = h

            print(
                f"[OK] "
                f"sample={sample}, "
                f"mPhi={mphi}, "
                f"region={region}"
            )


# ============================================================
# SIGNAL: ISTOGRAMMI DI EFFICIENZA VS mPhi
# ============================================================

efficiency_histograms = {}

for sample in samples:

    efficiency_histograms[sample] = {}

    for region in ratio_regions:

        h_eff = ROOT.TH1D(
            f"h_eff_{sample}_{region}",
            f"{sample} - {region};m_{{#phi}} [GeV];N(region) / N(SRTop)",
            len(masses),
            0,
            len(masses)
        )

        h_eff.SetDirectory(0)

        for i, mphi in enumerate(masses, start=1):

            h_eff.GetXaxis().SetBinLabel(
                i,
                str(mphi)
            )

            if mphi not in histograms[sample]:
                continue

            if "SRTop" not in histograms[sample][mphi]:
                continue

            if region not in histograms[sample][mphi]:
                continue


            # SRTop SENZA veto
            h_den = histograms[sample][mphi]["SRTop"]

            # SRTop CON veto
            h_num = histograms[sample][mphi][region]


            # Numero totale di eventi
            # include underflow + overflow
            n_den = h_den.Integral(
                0,
                h_den.GetNbinsX() + 1
            )

            n_num = h_num.Integral(
                0,
                h_num.GetNbinsX() + 1
            )


            if n_den > 0:

                ratio = n_num / n_den

                h_eff.SetBinContent(
                    i,
                    ratio
                )

                print(
                    f"{sample:20s} "
                    f"mPhi={mphi:4d} "
                    f"{region:35s} "
                    f"N_num={n_num:10.3f} "
                    f"N_SRTop={n_den:10.3f} "
                    f"ratio={ratio:.4f}"
                )

        efficiency_histograms[sample][region] = h_eff


# ============================================================
# SIGNAL: DISEGNO
# ============================================================

canvases = {}
legends = {}

for sample in samples:

    c = ROOT.TCanvas(
        f"c_{sample}",
        sample,
        1000,
        700
    )

    canvases[sample] = c


    h_loose = efficiency_histograms[sample][
        "SRTop_LooseVetoCut"
    ]

    h_tight = efficiency_histograms[sample][
        "SRTop_TightVetoCut"
    ]

    h_looseORtight = efficiency_histograms[sample][
        "SRTop_LooseORTightVetoCut"
    ]


    h_loose.SetTitle(
        f"{sample};m_{{#phi}} [GeV];N(region) / N(SRTop)"
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


    h_loose.SetMinimum(h_loose.GetMinimum()-0.2)
    max= h_loose.GetMaximum()
    h_loose.SetMaximum(max+0.2)


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

    legends[sample] = legend

    c.Update()


# ============================================================
# SIGNAL: SALVATAGGIO
# ============================================================

for sample, c in canvases.items():

    c.SaveAs(
        output_path
        + f"{sample}_SRTop_efficiency_vs_mPhi.png"
    )


# ============================================================
#
#               BACKGROUNDS
#
# ============================================================


# ============================================================
# Z + JETS COMPONENTS
# Questi vengono sommati insieme
# ============================================================
"""
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
# TT
# Questi NON vengono sommati
# ============================================================

TT_samples = [
    "TT_semilep_2024",
    "TT_hadr_2024",
    "TT_dilep_2024",
]


# ============================================================
# APERTURA BACKGROUND FILE
# ============================================================

background_samples = Z_samples + TT_samples

background_files = {}
background_histograms = {}


for sample in background_samples:

    filename = f"{sample}.root"
    filepath = path + filename

    print(f"\nOpening background: {filepath}")

    f = ROOT.TFile.Open(filepath)

    if not f or f.IsZombie():

        print(
            f"[ERROR FILE] "
            f"sample={sample}"
        )

        continue


    background_files[sample] = f
    background_histograms[sample] = {}


    for region, hist_name in regions.items():

        h = f.Get(hist_name)

        if not h:

            print(
                f"[ERROR HIST] "
                f"sample={sample}, "
                f"region={region}, "
                f"hist={hist_name}"
            )

            continue


        background_histograms[sample][region] = h

        print(
            f"[OK] "
            f"sample={sample}, "
            f"region={region}"
        )


# ============================================================
# ISTOGRAMMI BACKGROUND
#
# 4 bin:
#
# 1 -> Z
# 2 -> TT semilep
# 3 -> TT hadr
# 4 -> TT dilep
#
# ============================================================

background_efficiency_histograms = {}


for region in ratio_regions:

    h_eff = ROOT.TH1D(
        f"h_background_eff_{region}",
        ";Process;N(region) / N(SRTop)",
        4,
        0,
        4
    )

    h_eff.SetDirectory(0)

    h_eff.GetXaxis().SetBinLabel(
        1,
        "Z"
    )

    h_eff.GetXaxis().SetBinLabel(
        2,
        "TT semilep"
    )

    h_eff.GetXaxis().SetBinLabel(
        3,
        "TT hadr"
    )

    h_eff.GetXaxis().SetBinLabel(
        4,
        "TT dilep"
    )


    # ========================================================
    # BIN 1 -> Z
    #
    # Somma di tutti i componenti Z
    # ========================================================

    Z_den_total = 0.0
    Z_num_total = 0.0


    for sample in Z_samples:

        if sample not in background_histograms:
            continue

        if "SRTop" not in background_histograms[sample]:
            continue

        if region not in background_histograms[sample]:
            continue


        # SRTop SENZA veto
        h_den = background_histograms[sample][
            "SRTop"
        ]

        # SRTop CON veto
        h_num = background_histograms[sample][
            region
        ]


        n_den = h_den.Integral(
            0,
            h_den.GetNbinsX() + 1
        )

        n_num = h_num.Integral(
            0,
            h_num.GetNbinsX() + 1
        )


        Z_den_total += n_den
        Z_num_total += n_num


    if Z_den_total > 0:

        Z_ratio = (
            Z_num_total
            /
            Z_den_total
        )

        h_eff.SetBinContent(
            1,
            Z_ratio
        )

        print(
            f"Z "
            f"{region:35s} "
            f"N_num={Z_num_total:10.3f} "
            f"N_SRTop={Z_den_total:10.3f} "
            f"ratio={Z_ratio:.4f}"
        )


    # ========================================================
    # BIN 2,3,4 -> TT
    #
    # I tre TT rimangono SEPARATI
    # ========================================================

    for i, sample in enumerate(
        TT_samples,
        start=2
    ):

        if sample not in background_histograms:
            continue

        if "SRTop" not in background_histograms[sample]:
            continue

        if region not in background_histograms[sample]:
            continue


        # SRTop SENZA veto
        h_den = background_histograms[sample][
            "SRTop"
        ]

        # SRTop CON veto
        h_num = background_histograms[sample][
            region
        ]


        n_den = h_den.Integral(
            0,
            h_den.GetNbinsX() + 1
        )

        n_num = h_num.Integral(
            0,
            h_num.GetNbinsX() + 1
        )


        if n_den > 0:

            ratio = n_num / n_den

            h_eff.SetBinContent(
                i,
                ratio
            )

            print(
                f"{sample:20s} "
                f"{region:35s} "
                f"N_num={n_num:10.3f} "
                f"N_SRTop={n_den:10.3f} "
                f"ratio={ratio:.4f}"
            )


    background_efficiency_histograms[
        region
    ] = h_eff


# ============================================================
# RECUPERO ISTOGRAMMI BACKGROUND
# ============================================================

h_loose_bkg = background_efficiency_histograms[
    "SRTop_LooseVetoCut"
]

h_tight_bkg = background_efficiency_histograms[
    "SRTop_TightVetoCut"
]

h_looseORtight_bkg = background_efficiency_histograms[
    "SRTop_LooseORTightVetoCut"
]


# ============================================================
# STILE BACKGROUND
# ============================================================

h_loose_bkg.SetLineColor(
    ROOT.kViolet + 6
)

h_loose_bkg.SetLineWidth(2)


h_tight_bkg.SetLineColor(
    ROOT.kTeal - 6
)

h_tight_bkg.SetLineWidth(2)


h_looseORtight_bkg.SetLineColor(
    ROOT.kOrange - 3
)

h_looseORtight_bkg.SetLineWidth(2)

h_looseORtight_bkg.SetLineStyle(2)


# ============================================================
# RANGE Y
# ============================================================

h_loose_bkg.SetMinimum(0)
h_loose_bkg.SetMaximum(0.6)


# ============================================================
# CANVAS BACKGROUND
# ============================================================

c_background = ROOT.TCanvas(
    "c_background",
    "Background efficiencies",
    1000,
    700
)


# ============================================================
# DISEGNO BACKGROUND
# ============================================================

h_loose_bkg.Draw("HIST")

h_tight_bkg.Draw(
    "HIST SAME"
)

h_looseORtight_bkg.Draw(
    "HIST SAME"
)


# ============================================================
# LEGENDA BACKGROUND
# ============================================================

legend_background = ROOT.TLegend(
    0.52,
    0.70,
    0.88,
    0.88
)

legend_background.SetBorderSize(0)
legend_background.SetFillStyle(0)


legend_background.AddEntry(
    h_loose_bkg,
    "Loose veto",
    "l"
)

legend_background.AddEntry(
    h_tight_bkg,
    "Tight veto",
    "l"
)

legend_background.AddEntry(
    h_looseORtight_bkg,
    "Loose OR Tight veto",
    "l"
)


legend_background.Draw()

c_background.Update()


# ============================================================
# SALVATAGGIO BACKGROUND
# ============================================================

c_background.SaveAs(
    output_path
    + "Background_SRTop_efficiency.png"
)
"""