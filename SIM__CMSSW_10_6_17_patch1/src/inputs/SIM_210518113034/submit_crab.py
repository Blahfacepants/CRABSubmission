from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "SIM_210518113034"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab.py"
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 4

config.Data.inputDataset = "/GEN_Hpp_NEW_test/ardas-RunIISummer20UL18_GEN-42b65214d01566d851ba74f16b93e2b1/USER" 
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())
config.Data.outputDatasetTag = "RunIISummer20UL18_SIM"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.storageSite = "T3_US_FNALLPC"
config.Site.whitelist = ["T2_*","T3_*"]
