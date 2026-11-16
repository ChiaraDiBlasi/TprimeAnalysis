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
# ### ==> Sequence of operations:
# s --> c (and r) until the queue is empty and "total to rerun: 0" --> h --> d
# Use the SAME options in every mode, only OPT changes: e.g. -m h without the --noXXX/--weightset options
# of the submission looks for the parts in another weightset folder and does not find them
#
# ### ==> Weightsets (which weights enter the event weight):
# --noSFbtag, --noPuWeight, --noTopPtWeight, --noTrotaSF   remove that weight from every weightset
# --weightset X (repeatable)                              adds one weightset, X = allWeights or the weights to remove
#                                                         separated by commas, e.g. --weightset noSFbtag,noPuWeight
# Each weightset has its own folder <OUTPATH>/<label>/, label = removed weights joined by _ (allWeights if none),
# e.g. "--noTrotaSF --weightset allWeights --weightset noSFbtag" -> noTrotaSF/ and noSFbtag_noTrotaSF/
# No --weightset and no --noXXX: a single weightset, allWeights/
#
# ### ==> Paths:
# --outpath   folder of the job outputs (parts/ of the split samples)
# --mergepath folder of the merged files (plots/), i.e. the one used for the stacks; same as --outpath if not given
#
# ### ==> Other options:
# --varfile    variables and regions (default ../variables.py)
# --syst       systematic variations (MC only, not for data)
# --config_paths, --dict_samples_file   other config / samples file
# --dryrun     only prepares the condor folders;  --verbose N   extra printouts
#
# The standalone environment (standalone/env_standalone.sh) must already be sourced.
# Below: an example for one year, change the variables at the top.
####################################################################################################

export OPT=h
export OUTPATH="/eos/user/f/fscrivan/tDM/postselector_results/2024/postselector_outpath_syst"
export MERGEPATH="/eos/user/f/fscrivan/tDM/postselector_results/2024/plots_syst"
#ho cambiato i nomi aggiungendo il suffisso "_syst"

### TTBar
python3 postSelector_submitter_large.py -d TT_2024 --suffix TestParallel --noSFbtag --noTrotaSF --syst --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"


### ZJets

#python3 postSelector_submitter_large.py -d ZJetsToNuNu_2jets_2024 --suffix TestParallel --noSFbtag --noTrotaSF --syst --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

### WJets
#python3 postSelector_submitter_large.py -d WJets_2jets_2024 --suffix TestParallel --noSFbtag --noTrotaSF --syst --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

### Single top TW

#python3 postSelector_submitter_large.py -d TW_2024 --suffix TestParallel --noSFbtag --noTrotaSF --syst --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"

### QCD

##python3 postSelector_submitter_large.py -d QCD_2024 --suffix TestParallel --noSFbtag --noTrotaSF --syst --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"


###Data

#python3 postSelector_submitter_large.py -d DataJetMET_2024 --suffix TestParallel_dati --noSFbtag --noTrotaSF --partsize 20 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"


#python3 postSelector_submitter_large.py -d DataEGamma_2024 --suffix TestParallel --noSFbtag --noPuWeight --noTrotaSF --noTopPtWeight --config_paths "../config/config.yaml" --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH
#python3 postSelector_submitter_large.py -d DataEGamma_2024 --suffix TestParallel_v1 --noSFbtag --noTrotaSF --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH 



#python3 postSelector_submitter_large.py -d DataMuon_2024 --suffix TestParallel --noSFbtag --noPuWeight --noTrotaSF --noTopPtWeight --config_paths "../config/config.yaml" --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH
#python3 postSelector_submitter_large.py -d DataMuon_2024 --suffix TestParallel_v1 --noSFbtag --noTrotaSF --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH

###TDM
#python3 postSelector_submitter_large.py -d TBDM_s_2024,TBDM_ps_2024,TTDM_s_2024,TTDM_ps_2024,TWDM_s_2024,TWDM_ps_2024,TWto2LDM_s_2024,TWto2LDM_ps_2024,TTto2LDM_s_2024,TTto2LDM_ps_2024 --suffix TestParallel --noSFbtag --noTrotaSF --syst --partsize 25 -m $OPT --mergepath $MERGEPATH --outpath $OUTPATH --dict_samples_file "/afs/cern.ch/user/f/fscrivan/tDM/NanoAODTools/python/postprocessing/samples/dict_samples_2024_syst.json"






