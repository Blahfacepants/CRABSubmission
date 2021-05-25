# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/Pythia_fragment.py --fileout file:step0.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 110X_mcRun4_realistic_v3 --beamspot HLLHC14TeV --step GEN,SIM --nThreads 8 --geometry Extended2026D49 --era Phase2C9 --python_filename Pythia_fragment_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.source.numberEventsInLuminosityBlock=cms.untracked.uint32(3000) -n 3000
import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
        maxEventsToPrint = cms.untracked.int32(1),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        filterEfficiency = cms.untracked.double(1.0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        comEnergy = cms.double(13000),
        PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'Tune:pp 5', 
            'Tune:ee 3', 
            'PartonLevel:MPI = on', 
            'PartonLevel:ISR = on', 
            'PartonLevel:FSR = on', 
            'LeftRightSymmmetry:ffbar2HLHL = on', 
            '9900041:onMode = off', 
            '9900041:m0 = 800', 
            '9900041:onIfAll = 24 24', 
            'LeftRightSymmmetry:coupHee = 0', 
            'LeftRightSymmmetry:coupHmue = 0', 
            'LeftRightSymmmetry:coupHmumu = 0', 
            'LeftRightSymmmetry:coupHtaue = 0', 
            'LeftRightSymmmetry:coupHtaumu = 0', 
            'LeftRightSymmmetry:coupHtautau = 0', 
            'LeftRightSymmmetry:vL = 5',
            '24:onMode = off',
            '24:onifAny = 11 13'
        ),
            parameterSets = cms.vstring('pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings',
            'processParameters',
            )
        )
)
