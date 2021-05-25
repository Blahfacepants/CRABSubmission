#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsenv
cd /uscms_data/d3/adas2/pythia-stuff/EXO-MCsampleProductions/FullSimulation/RunIISummer20UL18/GEN__CMSSW_10_6_18/src/inputs/GEN_Hpp_NEW_test//
crab submit -c submit_crab.py
cd /uscms_data/d3/adas2/pythia-stuff/EXO-MCsampleProductions/FullSimulation/RunIISummer20UL18/GEN__CMSSW_10_6_18/src/
