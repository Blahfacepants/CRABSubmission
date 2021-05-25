from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "GEN_Hpp_NEW_test"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "run_crab.py"
#config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.outputPrimaryDataset = "GEN_Hpp_NEW_test"
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())#FIXME
config.Data.outputDatasetTag = "RunIISummer20UL18_GEN"
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 20
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

config.Site.storageSite = "T3_US_FNALLPC"
