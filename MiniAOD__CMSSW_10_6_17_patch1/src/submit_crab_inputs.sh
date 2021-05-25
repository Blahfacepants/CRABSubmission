#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsenv
cd /uscms_data/d3/adas2/pythia-stuff/EXO-MCsampleProductions/FullSimulation/RunIISummer20UL18/MiniAOD__CMSSW_10_6_17_patch1/src/inputs/MiniAOD_Hplusplus_M800_13TeV_test4//
crab submit -c submit_crab.py
cd /uscms_data/d3/adas2/pythia-stuff/EXO-MCsampleProductions/FullSimulation/RunIISummer20UL18/MiniAOD__CMSSW_10_6_17_patch1/src/
