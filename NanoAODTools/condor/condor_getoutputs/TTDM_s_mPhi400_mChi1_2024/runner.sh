#!/usr/bin/bash

echo "X509_USER_PROXY: ${X509_USER_PROXY}"
voms-proxy-info
echo "===== Job started ====="
echo "Host: $(hostname)"
echo "Date: $(date)"
echo "Dataset: TTDM_s_mPhi400_mChi1_2024"

cd /afs/cern.ch/user/f/fscrivan/
source tDM.sh
cd condor/

echo "Running command:"
echo "python3 getoutputs.py -d TTDM_s_mPhi400_mChi1_2024 -o dict_samples_DM_2024.json --tier legnaro"

python3 getoutputs.py -d TTDM_s_mPhi400_mChi1_2024 -o dict_samples_DM_2024.json --tier legnaro

echo "===== Job finished ====="
echo "Date: $(date)"
