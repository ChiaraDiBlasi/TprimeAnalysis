#!/usr/bin/bash

echo "X509_USER_PROXY: ${X509_USER_PROXY}"
voms-proxy-info
echo "===== Job started ====="
echo "Host: $(hostname)"
echo "Date: $(date)"
echo "Dataset: QCD_HT1200to1500_2022EE"

cd /afs/cern.ch/user/f/fscrivan/
source tDM.sh
cd condor/

echo "Running command:"
echo "python3 getoutputs.py -d QCD_HT1200to1500_2022EE -o dict_samples_2022.json --tier legnaro"

python3 getoutputs.py -d QCD_HT1200to1500_2022EE -o dict_samples_2022.json --tier legnaro

echo "===== Job finished ====="
echo "Date: $(date)"
