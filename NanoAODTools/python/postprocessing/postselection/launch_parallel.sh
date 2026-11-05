####################################################################################################
#How to use postSelector_submitter_large.py 
# ### ==> Main features: 
# You can split jobs with --partsize X, where it will create jobs running on X root files each  
# There are several working options that you can select with the -m (or --mode) option:  
# -m s --> submits
# -m r --> resubmits failed jobs by looking at the condor output (still perfectible)
# -m c --> checks failed jobs by looking at the condor output
# -m h --> hadd files together after is finished.
# NOTA BENE: there are two paths :
# --mergepath is for MERGED files, i.e. the TRUE FOLDER you will use for plots 
# --outpath is the path for SPLIT files, i.e. you DO NOT have to use it for plots
#
### ==> Sequence of operations:
# first run it with -s, then with -r to resubmit failed jobs (usually after a few minutes the jobs that had to fail will fail
# Both -r and -c options will tell you how many jobs are resubmitted / to resubmit.
# 
# ### ==> Other options:
# you can customize the config with the --config_paths option
# you can just prepare the condor folders with the --dryrun option
# the option --verbose (number) makes it so some extra printouts are shown
# ### ==> Examples:
# Below you find examples (with a semi-optimized partsize selection) for each file. Just be mindful of changing the paths! 
# For simplicity, it's done with bash variables here - make your scripting however you want! 
####################################################################################################

export OPT=h
export OUTPATH="/eos/user/f/fscrivan/tDM/postselector_results/2024/n_split"
export MERGEPATH="/eos/user/f/fscrivan/tDM/postselector_results/2024/plots_new2"
#vecchi versione

#versioni mie

#TTBar
#python3 postSelector_submitter_large.py -d TT_2024 --suffix TestParallel_v4 --syst --noSFbtag --noTrotaSF --partsize 10 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"
#python3 postSelector_submitter_large.py -d TT_dilep_2024 --suffix TestParallel --syst --noSFbtag --noTrotaSF --partsize 10 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"
### ZJets
#python3 postSelector_submitter_large.py -d ZJetsToNuNu_2jets_2024 --suffix TestParallel_v4 --syst --noSFbtag --noTrotaSF --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

### WJets
python3 postSelector_submitter_large.py -d WJets_2jets_2024 --suffix TestParallel_v4 --syst --noSFbtag --noTrotaSF --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"
#python3 postSelector_submitter_large.py -d WJets_2jets_ENu_0J_2024 --suffix TestParallel --syst --noSFbtag --noTrotaSF --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"
### Single top TW
#python3 postSelector_submitter_large.py -d TW_2024 --suffix TestParallel_v3 --syst --noSFbtag --noTrotaSF --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

### QCD
#python3 postSelector_submitter_large.py -d QCD_2024 --suffix TestParallel_v4 --syst --noSFbtag --noTrotaSF --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json" 

###Data
#python3 postSelector_submitter_large.py -d DataJetMET_2024 --suffix TestParallel_v4 --noSFbtag --noTrotaSF --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

#python3 postSelector_submitter_large.py -d DataEGamma_2024 --suffix TestParallel --syst --noSFbtag --noTrotaSF --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

#python3 postSelector_submitter_large.py -d DataMuon_2024 --suffix TestParallel --syst --noSFbtag --noTrotaSF --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

##TDM
#python3 postSelector_submitter_large.py -d TBDM_s_2024,TBDM_ps_2024,TTDM_s_2024,TTDM_ps_2024,TWDM_s_2024,TWDM_ps_2024,TWto2LDM_s_2024,TWto2LDM_ps_2024,TTto2LDM_s_2024,TTto2LDM_ps_2024 --suffix TestParallel_v4 --syst --noSFbtag --noTrotaSF --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"
#python3 postSelector_submitter_large.py -d TBDM_s_2024 --suffix TestParallel --syst --noSFbtag --noPuWeight --noTrotaSF --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

