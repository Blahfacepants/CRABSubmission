#!/bin/bash
cmsDriver.py Configuration/GenProduction/python/GEN_Hpp_NEW_test.py --no_exec --mc --python_filename run_crab.py --fileout GEN.root --eventcontent RAWSIM --datatier GEN --step GEN --geometry DB:Extended -n 6284 --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --era Run2_2018
