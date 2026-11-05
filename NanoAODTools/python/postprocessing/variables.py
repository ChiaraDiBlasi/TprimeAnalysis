import math
import numpy as np
class variable(object):
    def __init__(self, name, title, taglio=None, nbins=None, xmin=None, xmax=None, xarray=None, MConly = False, noUnOvFlowbin = False):
        self._name = name
        self._title = title
        self._taglio = taglio
        self._nbins = nbins
        self._xmin = xmin
        self._xmax = xmax
        self._xarray = xarray
        self._MConly = MConly
        self._noUnOvFlowbin = noUnOvFlowbin
    def __str__(self):
        return  '\"'+str(self._name)+'\",\"'+str(self._title)+'\",\"'+str(self._taglio)+'\",'+str(self._nbins)+','+str(self._xmin)+','+str(self._xmax)
#variable("Top_pt", "Top p_T [GeV]", nbins = 50, xmin = 0 , xmax = 1000)
class variable2D(object):
    def __init__(self, name, xname, yname, xtitle, ytitle, taglio=None, nxbins=None, xmin=None, xmax=None, xarray=None, 
                    nybins=None, ymin=None, ymax=None, yarray=None):
        self._name = name
        self._xname = xname
        self._yname = yname
        self._xtitle = xtitle
        self._ytitle = ytitle
        self._taglio = taglio
        self._nxbins = nxbins
        self._xmin = xmin
        self._xmax = xmax
        self._xarray = xarray
        self._nybins = nybins
        self._ymin = ymin
        self._ymax = ymax
        self._yarray = yarray
    def __str__(self):
        return  '\"'+str(self._name)+'\",\"'+str(self._xtitle)+'\",\"'+str(self._ytitle)+'\",\"'+str(self._taglio)+'\",'+str(self._nxbins)+','+str(self._xmin)+','+str(self._xmax)+','+str(self._nybins)+','+str(self._ymin)+','+str(self._ymax)


### Definition of requeriments for plots (cut), variables and regions

requirements = ""#"leptonveto" #"leptonveto && MET_pt>150 && MinDelta_phi>0.6"

######## 1D variables for histos

vars = []

# vars.append(variable(name = "SFbtag_nominal", title= "#omega_{b-tag SF}", nbins = 100, xmin = 0, xmax=2, MConly = True))

# vars.append(variable(name = "MET_pt", title= "p_{T}^{miss} [GeV]", nbins = 6, xmin = 200, xmax=800))
# vars.append(variable(name = "MET_phi", title= "MET #phi", nbins = 6, xmin = -math.pi, xmax=math.pi))
# vars.append(variable(name = "PuppiMET_pt", title= "p_{T}^{miss}(Puppi) [GeV]", nbins = 12, xmin = 200, xmax=800))
# vars.append(variable(name = "PuppiMET_phi", title= "MET #phi (Puppi) [GeV]", nbins = 6, xmin = -math.pi, xmax=math.pi))
vars.append(variable(name = "PuppiMET_T1_pt_nominal", title= "p_{T}^{miss}(Puppi) nominal [GeV]", nbins = 12, xmin = 250, xmax=850))
vars.append(variable(name = "PuppiMET_T1_phi_nominal", title= "Puppi MET #phi nominal", nbins = 6, xmin = -math.pi, xmax=math.pi))

vars.append(variable(name = "LeadingJetPt_pt", title= "Leading Jet p_{T} [GeV]", nbins = 8, xmin = 50, xmax=850))
# vars.append(variable(name = "LeadingJetPt_eta", title= "Leading Jet #eta", nbins = 8, xmin = -4, xmax=4))
# vars.append(variable(name = "LeadingJetPt_phi", title= "Leading Jet #phi", nbins = 6, xmin = -math.pi, xmax=math.pi))
# vars.append(variable(name = "LeadingJetPt_mass", title= "Leading Jet mass [GeV]", nbins = 10, xmin = 50, xmax=550))

vars.append(variable(name = "LeadingFatJetPt_pt", title= "Leading FatJet p_{T} [GeV]", nbins = 8, xmin = 50, xmax=850))
# vars.append(variable(name = "LeadingFatJetPt_eta", title= "Leading FatJet #eta", nbins = 8, xmin = -4, xmax=4))
# vars.append(variable(name = "LeadingFatJetPt_phi", title= "Leading FatJet #phi", nbins = 6, xmin = -math.pi, xmax=math.pi))
# vars.append(variable(name = "LeadingFatJetPt_mass", title= "Leading FatJet mass [GeV]", nbins = 10, xmin = 50, xmax=550))
# vars.append(variable(name = "LeadingFatJetPt_msoftdrop", title= "Leading FatJet m_{SD} [GeV]", nbins = 20, xmin = 70, xmax=110))
# vars.append(variable(name = "LeadingMuonPt_pt", title= "Leading Muon p_{T} [GeV]", nbins = 30, xmin = 0, xmax=300))
# vars.append(variable(name = "LeadingMuonPt_eta", title= "Leading Muon #eta", nbins = 8, xmin = -4, xmax=4))
# vars.append(variable(name = "LeadingMuonPt_phi", title= "Leading Muon #phi", nbins = 6, xmin = -math.pi, xmax=math.pi))
# vars.append(variable(name = "LeadingElectronPt_pt", title= "Leading Electron p_{T} [GeV]", nbins = 30, xmin = 0, xmax=300))
# vars.append(variable(name = "LeadingElectronPt_eta", title= "Leading Electron #eta", nbins = 8, xmin = -4, xmax=4))
# vars.append(variable(name = "LeadingElectronPt_phi", title= "Leading Electron #phi", nbins = 6, xmin = -math.pi, xmax=math.pi))

# vars.append(variable(name = "nTightTopMerged",      title= "# Top Candidate Merged",    nbins = 40, xmin = -0.5, xmax=80.5))
# vars.append(variable(name = "nTightTopMixed",       title= "# Top Candidate Mixed",     nbins = 40, xmin = -0.5, xmax=80.5))
# vars.append(variable(name = "nTightTopResolved",    title= "# Top Candidate Resolved",  nbins = 25, xmin = -0.5, xmax=49.5))
vars.append(variable(name = "nJet",                 title = "# Jet",                    nbins = 10, xmin = -0.5, xmax=9.5))
vars.append(variable(name = "nFatJet",              title = "# FatJet",                 nbins = 5,  xmin = -0.5, xmax=4.5))
vars.append(variable(name = "nGoodJet",             title = "# Good Jet",               nbins = 10, xmin = -0.5, xmax=9.5))
vars.append(variable(name = "nGoodFatJet",          title = "# Good FatJet",            nbins = 5,  xmin = -0.5, xmax=4.5))
vars.append(variable(name = "JetBTagScore",         title = "b-Jet Score",              nbins = 40, xmin = 0,    xmax=1, noUnOvFlowbin = True))
vars.append(variable(name = "nJetBtagLoose",        title = "# b-Jet (L) ",             nbins = 5,  xmin = -0.5, xmax = 4.5))
vars.append(variable(name = "nJetBtagMedium",       title = "# b-Jet (M)",              nbins = 5,  xmin = -0.5, xmax = 4.5))
vars.append(variable(name = "nJetBtagTight",        title = "# b-Jet (T)",              nbins = 5,  xmin = -0.5, xmax = 4.5))
vars.append(variable(name = "MinDelta_phi", title= "min #Delta #phi", nbins = 18, xmin = 0, xmax = math.pi))
# vars.append(variable(name = "MaxEta_jet", title= "max #eta jet", nbins = 5, xmin = 0, xmax = 5, noUnOvFlowbin=True))
vars.append(variable(name = "HT_eventHT", title= "event HT", nbins = 20, xmin = 0, xmax = 2000))
# vars.append(variable(name = "run", title= "Run Number", nbins = 5142, xmin = 315251.5, xmax = 320393.5))

vars.append(variable(name = "MHT", title= "event HT", nbins = 20, xmin = 0, xmax = 2000))
vars.append(variable(name = "PV_npvsGood", title= "Number of PV", nbins = 25, xmin = -0.5, xmax = 49.5))

vars.append(variable(name = "TopResolved_TopScore_nominal",     title= "Top Resolved Score",    nbins = 40, xmin = 0, xmax=1, noUnOvFlowbin = True))
vars.append(variable(name = "TopMixed_TopScore_nominal",        title= "Top Mixed Score",       nbins = 40, xmin = 0, xmax=1, noUnOvFlowbin = True))
vars.append(variable(name = "TopMerged_TopScore_nominal",       title= "Top Merged Score",      nbins = 40, xmin = 0, xmax=1, noUnOvFlowbin = True))


vars.append(variable(name = "EventTopCategory", title= "Top Category", nbins = 7, xmin = 0.5, xmax = 7.5))
# vars.append(variable(name = "Top_truth", title= "Top Truth", nbins = 4, xmin = -0.5, xmax = 3.5, MConly = True))
# vars.append(variable(name = "EventTopCategoryWithTruth", title= "Top Category (only true)", nbins = 4, xmin = 0.5, xmax = 4.5, MConly = True))
vars.append(variable(name = "Top_mass",         title= "Top mass [GeV]", nbins = 30, xmin = 100, xmax=250, noUnOvFlowbin = True))
vars.append(variable(name = "Top_pt",           title= "Top p_{T} [GeV]", nbins = 30, xmin = 100, xmax=1000, noUnOvFlowbin = True))
vars.append(variable(name = "Top_score",        title= "Top Score", nbins = 40, xmin = 0, xmax=1, noUnOvFlowbin = True))
vars.append(variable(name = "MT_T",             title= "M_{T} [GeV]", nbins = 30, xmin = 500, xmax=2000, noUnOvFlowbin = True))
# vars.append(variable(name = "FatJet_msoftdrop_nominal", title= "FatJet m_{SD} [GeV]", nbins = 20, xmin = 70, xmax=110))


# vars.append(variable(name = "Top_isolationPtJetsdR04", title= "Top Iso p_{T} (#Delta R=0.4)", nbins = 20, xmin = 0, xmax=2, noUnOvFlowbin = True))
# vars.append(variable(name = "Top_isolationPtJetsdR06", title= "Top Iso p_{T} (#Delta R=0.6)", nbins = 20, xmin = 0, xmax=2, noUnOvFlowbin = True))
# vars.append(variable(name = "Top_isolationPtJetsdR08", title= "Top Iso p_{T} (#Delta R=0.8)", nbins = 20, xmin = 0, xmax=2, noUnOvFlowbin = True))
# vars.append(variable(name = "Top_isolationPtJetsdR12", title= "Top Iso p_{T} (#Delta R=1.2)", nbins = 20, xmin = 0, xmax=2, noUnOvFlowbin = True))
# vars.append(variable(name = "Top_isolationNJetsdR04", title= "Top Iso n_{jet}  (#Delta R=0.4)", nbins = 11, xmin = -0.5, xmax=10.5, noUnOvFlowbin = True))
# vars.append(variable(name = "Top_isolationNJetsdR06", title= "Top Iso n_{jet}  (#Delta R=0.6)", nbins = 11, xmin = -0.5, xmax=10.5, noUnOvFlowbin = True))
# vars.append(variable(name = "Top_isolationNJetsdR08", title= "Top Iso n_{jet}  (#Delta R=0.8)", nbins = 11, xmin = -0.5, xmax=10.5, noUnOvFlowbin = True))
# vars.append(variable(name = "Top_isolationNJetsdR12", title= "Top Iso n_{jet}  (#Delta R=1.2)", nbins = 11, xmin = -0.5, xmax=10.5, noUnOvFlowbin = True))


#  aggiungere plot per controllare la preselection dei fatjet
#  a bassa ed alto eta



######## 1D variables for histos
vars2D = []

# vars2D.append(variable2D(name = "nTightTopMixedVsnTightTopResolved", xname = "nTightTopMixed", yname = "nTightTopResolved", xtitle = "# of Top Mixed", ytitle = "# of Top Merged", nxbins = 6, xmin = -0.5, xmax = 5.5, nybins = 6, ymin = -0.5, ymax = 5.5))

################## December 2023    
nocut = ""
hemveto = "(isMC || (year != 2018) || (HEMVeto || run<319077.))" 
met_filters = "(Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_ecalBadCalibFilter && Flag_eeBadScFilter)"
hlt_filters = "(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60 || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight || HLT_Ele32_WPTight_Gsf || HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200 || HLT_IsoMu24)"
hlt2_filters = "(HLT_PFMET120_PFMHT120_IDTight || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight)"
hlt3_filters = "(HLT_PFMET140_PFMHT140_IDTight || HLT_PFMETNoMu140_PFMHTNoMu140_IDTight)"
metcut = "(MET_pt>250)"
hltmet_filters = "(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60 || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight)"
hltmu_filters = "(HLT_IsoMu24)"
################## January 2024
# TightMuon_Jets_minimumDistance      = "Muon_minDeltaR_fromGoodJets[TightMuon_idx[0]] >= 0.4"
# VetoMuon_Jets_minimumDistance       = "Muon_minDeltaR_fromGoodJets[VetoMuon_idx[0]] >= 0.4"
# TightElectron_Jets_minimumDistance  = "Electron_minDeltaR_fromGoodJets[TightElectron_idx[0]] >= 0.4"
# VetoElectron_Jets_minimumDistance   = "Electron_minDeltaR_fromGoodJets[VetoElectron_idx[0]] >= 0.4"
# singleLep   = "((nTightElectron == 1 && nVetoElectron == 1 && nTightMuon == 0 && nVetoMuon == 0 && " + TightElectron_Jets_minimumDistance + " && " + VetoElectron_Jets_minimumDistance + ")||(nTightElectron == 0 && nVetoElectron == 0 && nTightMuon == 1 && nVetoMuon == 1 && " + TightMuon_Jets_minimumDistance + " && " + VetoMuon_Jets_minimumDistance + "))"
# singleMu    = "(nTightElectron == 0 && nVetoElectron == 0 && nTightMuon == 1 && nVetoMuon == 1 && " + TightMuon_Jets_minimumDistance + " && " + VetoMuon_Jets_minimumDistance + ")"
# singleE     = "(nTightElectron == 1 && nVetoElectron == 1 && nTightMuon == 0 && nVetoMuon == 0 && " + TightElectron_Jets_minimumDistance + " && " + VetoElectron_Jets_minimumDistance + ")"
singleLep   = "((nTightElectron == 1 && nVetoElectron == 1 && nTightMuon == 0 && nVetoMuon == 0)||(nTightElectron == 0 && nVetoElectron == 0 && nTightMuon == 1 && nVetoMuon == 1))"
singleMu    = "(nTightElectron == 0 && nVetoElectron == 0 && nTightMuon == 1 && nVetoMuon == 1)"
singleE     = "(nTightElectron == 1 && nVetoElectron == 1 && nTightMuon == 0 && nVetoMuon == 0)"
SRPresel    = "PuppiMET_T1_pt_nominal>250 && MinDelta_phi>0.6 && (nVetoElectron==0 && nVetoMuon ==0) && nJetBtagLoose>0"


# ============================================================
# LEPTON VETO DEFINITIONS
# ============================================================
#
# Four possible selections:
#
# NO           -> no lepton veto
# loose        -> loose lepton veto
# tight        -> tight lepton veto
# looseORtight -> loose OR tight lepton veto
#
# The dictionary values are C++ expressions interpreted
# by ROOT.RDataFrame.Filter().
# ============================================================

lepVetos = {

    "NO": "1",

    "loose": (
        "(nVetoElectron_loose + nVetoMuon_loose == 0)"
    ),

    "tight": (
        "(nVetoElectron_tight + nVetoMuon_tight == 0)"
    ),

    "looseORtight": (
        "(nVetoElectron_looseORtight + "
        "nVetoMuon_looseORtight == 0)"
    )
}

# ============================================================
# SIGNAL REGION PRESELECTION WITHOUT LEPTON VETO
# ============================================================
#
# IMPORTANT:
# Do not include any lepton veto here.
# It will be added automatically for each configuration.
# ============================================================

SRBase = (
    "PuppiMET_T1_pt_nominal>250 && "
    "MinDelta_phi>0.6 && "
    "nJetBtagLoose>0"
)

# Keep a veto-free preselection for possible external use.
SRPresel = SRBase


# ============================================================
# SIGNAL REGIONS WITHOUT LEPTON VETO
# ============================================================
#
# Define each signal region only once.
# All veto configurations will be generated automatically.
# ============================================================

SRregions = {

    # --------------------------------------------------------
    # Inclusive signal regions
    # --------------------------------------------------------

    "SR":
        SRBase,

    "SR0fjets":
        SRBase + " && nForwardJet==0",

    "SRatleast1fjets":
        SRBase + " && nForwardJet>0",


    # --------------------------------------------------------
    # Tight Top - Resolved (category 1)
    # --------------------------------------------------------

    "SRTopRes":
        SRBase + " && EventTopCategory==1",

    "SRTopRes0fjets":
        SRBase + " && EventTopCategory==1 && nForwardJet==0",

    "SRTopResatleast1fjets":
        SRBase + " && EventTopCategory==1 && nForwardJet>0",


    # --------------------------------------------------------
    # Tight Top - Mixed (category 2)
    # --------------------------------------------------------

    "SRTopMix":
        SRBase + " && EventTopCategory==2",

    "SRTopMix0fjets":
        SRBase + " && EventTopCategory==2 && nForwardJet==0",

    "SRTopMixatleast1fjets":
        SRBase + " && EventTopCategory==2 && nForwardJet>0",


    # --------------------------------------------------------
    # Tight Top - Merged (category 3)
    # --------------------------------------------------------

    "SRTopMer":
        SRBase + " && EventTopCategory==3",

    "SRTopMer0fjets":
        SRBase + " && EventTopCategory==3 && nForwardJet==0",

    "SRTopMeratleast1fjets":
        SRBase + " && EventTopCategory==3 && nForwardJet>0",


    # --------------------------------------------------------
    # Inclusive Tight Top (categories 1, 2, 3)
    # --------------------------------------------------------

    "SRTop":
        SRBase + " && EventTopCategory>=1 && EventTopCategory<=3",

    "SRTop0fjets":
        SRBase + " && EventTopCategory>=1 && EventTopCategory<=3 && nForwardJet==0",

    "SRTopatleast1fjets":
        SRBase + " && EventTopCategory>=1 && EventTopCategory<=3 && nForwardJet>0",


    # --------------------------------------------------------
    # Inclusive Loose Top (categories 4, 5, 6)
    # --------------------------------------------------------

    "SRTopLoose":
        SRBase + " && EventTopCategory>=4 && EventTopCategory<=6",

    "SRTop0fjetsLoose":
        SRBase + " && EventTopCategory>=4 && EventTopCategory<=6 && nForwardJet==0",

    "SRTopatleast1fjetsLoose":
        SRBase + " && EventTopCategory>=4 && EventTopCategory<=6 && nForwardJet>0",


    # --------------------------------------------------------
    # Loose Top - Resolved (category 4)
    # --------------------------------------------------------

    "SRTopResLoose":
        SRBase + " && EventTopCategory==4",

    "SRTop0fjetsResLoose":
        SRBase + " && EventTopCategory==4 && nForwardJet==0",

    "SRTopatleast1fjetsResLoose":
        SRBase + " && EventTopCategory==4 && nForwardJet>0",


    # --------------------------------------------------------
    # Loose Top - Mixed (category 5)
    # --------------------------------------------------------

    "SRTopMixLoose":
        SRBase + " && EventTopCategory==5",

    "SRTop0fjetsMixLoose":
        SRBase + " && EventTopCategory==5 && nForwardJet==0",

    "SRTopatleast1fjetsMixLoose":
        SRBase + " && EventTopCategory==5 && nForwardJet>0",


    # --------------------------------------------------------
    # Loose Top - Merged (category 6)
    # --------------------------------------------------------

    "SRTopMerLoose":
        SRBase + " && EventTopCategory==6",

    "SRTop0fjetsMerLoose":
        SRBase + " && EventTopCategory==6 && nForwardJet==0",

    "SRTopatleast1fjetsMerLoose":
        SRBase + " && EventTopCategory==6 && nForwardJet>0",




    
    # --------------------------------------------------------
    # AH CONTROL REGION
    # --------------------------------------------------------

    "AH":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi<0.6 && "
        "nJetBtagLoose>0",

    "AHTight":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi<0.6 && "
        "nJetBtagMedium>0 && "
        "EventTopCategory>=1 && EventTopCategory<=3",

    "AHLoose":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi<0.6 && "
        "nJetBtagMedium>0 && "
        "EventTopCategory>=4 && EventTopCategory<=6",


    # --------------------------------------------------------
    # SINGLE LEPTON CONTROL REGION
    # --------------------------------------------------------

    "SL":
        singleLep +
        " && nJetBtagLoose>0 && "
        "PuppiMET_T1_pt_nominal>250",

    "SLTight":
        singleLep +
        " && nJetBtagMedium>0 && "
        "EventTopCategory>=1 && EventTopCategory<=3",

    "SLLoose":
        singleLep +
        " && nJetBtagMedium>0 && "
        "EventTopCategory>=4 && EventTopCategory<=6",


    # --------------------------------------------------------
    # W CONTROL REGION
    # --------------------------------------------------------

    "AH1lWR":
        singleLep +
        " && nGoodJet>=3 && "
        "MT<=140 && "
        "nJetBtagLoose==0 && "
        "PuppiMET_T1_pt_nominal>250",

    "AH1lWRTight":
        singleLep +
        " && nGoodJet>=3 && "
        "MT<=140 && "
        "nJetBtagMedium==0 && "
        "EventTopCategory>=1 && EventTopCategory<=3",

    "AH1lWRLoose":
        singleLep +
        " && nGoodJet>=3 && "
        "MT<=140 && "
        "nJetBtagMedium==0 && "
        "EventTopCategory>=4 && EventTopCategory<=6",


    # --------------------------------------------------------
    # Z CONTROL REGION
    # --------------------------------------------------------

    "AH0lZR":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi>2.5 && "
        "nJetBtagLoose==0",

    "AH0lZRTight":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi>2.5 && "
        "nJetBtagLoose==0 && "
        "EventTopCategory>=1 && EventTopCategory<=3",

    "AH0lZRLoose":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi>2.5 && "
        "nJetBtagLoose==0 && "
        "EventTopCategory>=4 && EventTopCategory<=6",
}


# ============================================================
# CONTROL REGIONS
# ============================================================
#
# These regions are kept unchanged with respect to the
# original code.
#
# The automatic lepton veto loop will be applied only
# to the Signal Regions.
# ============================================================
regions = {}
"""
regions = {

    # --------------------------------------------------------
    # AH CONTROL REGION
    # --------------------------------------------------------

    "AH":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi<0.6 && "
        "(nVetoMuon+nVetoElectron)==0 && "
        "nJetBtagLoose>0",

    "AHTight":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi<0.6 && "
        "(nVetoMuon+nVetoElectron)==0 && "
        "nJetBtagMedium>0 && "
        "EventTopCategory>=1 && EventTopCategory<=3",

    "AHLoose":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi<0.6 && "
        "(nVetoMuon+nVetoElectron)==0 && "
        "nJetBtagMedium>0 && "
        "EventTopCategory>=4 && EventTopCategory<=6",


    # --------------------------------------------------------
    # SINGLE LEPTON CONTROL REGION
    # --------------------------------------------------------

    "SL":
        singleLep +
        " && nJetBtagLoose>0 && "
        "PuppiMET_T1_pt_nominal>250",

    "SLTight":
        singleLep +
        " && nJetBtagMedium>0 && "
        "EventTopCategory>=1 && EventTopCategory<=3",

    "SLLoose":
        singleLep +
        " && nJetBtagMedium>0 && "
        "EventTopCategory>=4 && EventTopCategory<=6",


    # --------------------------------------------------------
    # W CONTROL REGION
    # --------------------------------------------------------

    "AH1lWR":
        singleLep +
        " && nGoodJet>=3 && "
        "MT<=140 && "
        "nJetBtagLoose==0 && "
        "PuppiMET_T1_pt_nominal>250",

    "AH1lWRTight":
        singleLep +
        " && nGoodJet>=3 && "
        "MT<=140 && "
        "nJetBtagMedium==0 && "
        "EventTopCategory>=1 && EventTopCategory<=3",

    "AH1lWRLoose":
        singleLep +
        " && nGoodJet>=3 && "
        "MT<=140 && "
        "nJetBtagMedium==0 && "
        "EventTopCategory>=4 && EventTopCategory<=6",


    # --------------------------------------------------------
    # Z CONTROL REGION
    # --------------------------------------------------------

    "AH0lZR":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi>2.5 && "
        "(nVetoMuon+nVetoElectron)==0 && "
        "nJetBtagLoose==0",

    "AH0lZRTight":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi>2.5 && "
        "(nVetoMuon+nVetoElectron)==0 && "
        "nJetBtagLoose==0 && "
        "EventTopCategory>=1 && EventTopCategory<=3",

    "AH0lZRLoose":
        "PuppiMET_T1_pt_nominal>250 && "
        "MinDelta_phi>2.5 && "
        "(nVetoMuon+nVetoElectron)==0 && "
        "nJetBtagLoose==0 && "
        "EventTopCategory>=4 && EventTopCategory<=6",
}
"""


# ============================================================
# AUTOMATIC SIGNAL REGION GENERATION
# ============================================================
#
# For every signal region, generate four versions:
#
#   _NO_lepVeto
#   _loose_lepVeto
#   _tight_lepVeto
#   _looseORtight_lepVeto
#
# Example:
#
#   SRTop_NO_lepVeto
#   SRTop_loose_lepVeto
#   SRTop_tight_lepVeto
#   SRTop_looseORtight_lepVeto
#
# ============================================================

for vetoName, vetoCut in lepVetos.items():

    for regionName, regionCut in SRregions.items():

        newRegionName = f"{regionName}_{vetoName}_lepVeto"

        newRegionCut = f"({regionCut}) && ({vetoCut})"

        regions[newRegionName] = newRegionCut


# ============================================================
# OPTIONAL CHECKS
# ============================================================
#
# Uncomment these lines to inspect the generated regions.
# ============================================================

# print("Number of base signal regions:", len(SRregions))
# print("Number of veto configurations:", len(lepVetos))
# print("Total number of generated SR:", len(SRregions) * len(lepVetos))
# print("Total number of regions (SR + CR):", len(regions))
#
# for regionName, regionCut in regions.items():
#     print(regionName, ":", regionCut)
