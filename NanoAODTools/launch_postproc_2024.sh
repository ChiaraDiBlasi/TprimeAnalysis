#!/bin/bash
# Produzione DM 2024: eseguire dopo source /afs/cern.ch/user/f/fscrivan/tDM.sh
# Il submitter scrive su Legnaro in /store/user/fscrivan/Run3Analysis_Tprime/.
# --syst abilita le correzioni JME e le variazioni nel post-processing.
set -e

cd -- "$(dirname -- "${BASH_SOURCE[0]}")/condor"

### Fondi MC
#python3 postproc_submitter.py -d TT_2024 --tier legnaro --syst -s
#python3 postproc_submitter.py -d ZJetsToNuNu_2jets_2024 --tier legnaro --syst -s
#python3 postproc_submitter.py -d WJets_2jets_2024 --tier legnaro --syst -s
#python3 postproc_submitter.py -d TW_2024 --tier legnaro --syst -s
#python3 postproc_submitter.py -d QCD_2024 --tier legnaro --syst -s

### Dati
#python3 postproc_submitter.py -d DataJetMET_2024 --tier legnaro --syst -s
#python3 postproc_submitter.py -d DataEGamma_2024 --tier legnaro --syst -s
#python3 postproc_submitter.py -d DataMuon_2024 --tier legnaro --syst -s

### Segnali DM: scalare e pseudoscalare
python3 postproc_submitter.py -d TBDM_s_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TBDM_ps_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TWDM_s_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TWDM_ps_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TWto2LDM_s_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TWto2LDM_ps_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TTDM_s_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TTDM_ps_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TTto2LDM_s_2024 --tier legnaro --syst -s
python3 postproc_submitter.py -d TTto2LDM_ps_2024 --tier legnaro --syst -s
