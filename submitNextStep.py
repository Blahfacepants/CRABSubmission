import os
import subprocess

##How to use this file
# If starting the steps from the beginning delete currentStep.txt
# Every time you run the file it will check if there is an output dataset available from CRAB and use that dataset as input to run the step currently in currentStep.txt
# This will still run even if all of the jobs are not done within the previous task, since CRAB still gives an output dataset name! Make sure to wait until the previous crab job is done to run this script
# If for some reason you need to run a step again (since the submission didn't work) change the step name in currentStep.txt to the folder name of the step you want to run and rerun this script
# After all the steps in the steps list are done the script will delete currentStep.txt to be ready for the next round of CRAB tasks.

## ALSO: If you want to change the number of events/jobs you have to go into each folder and change the inputs.csv file.
def scrape_dataset_name():
    output = subprocess.getoutput("crab status")
   # print(output)
    if("Output dataset:" in output):
        lines = output.split('\n')
        for line in lines:
            #print(line)
            if("Output dataset:" in line):
                print("crab task completed, returning dataset name")
                print(line.split()[2])
                return line.split()[2]
    print("Dataset name not found - either the job wasn't completed or the crab status has expired")
    os.system("cd ..")
    raise ValueError("task not finished running or never submitted in the first place, no output dataset name available")

steps = ["GEN__CMSSW_10_6_18", "SIM__CMSSW_10_6_17_patch1", "DIGIPremix__CMSSW_10_6_17_patch1", "HLT__CMSSW_10_2_16_UL", "RECO__CMSSW_10_6_17_patch1", "MiniAOD__CMSSW_10_6_17_patch1"]

# os.system("cd GEN__CMSSW_10_6_18/src")
# os.system("python run_step.py")
# running = True
# while(running):
#     try:
#         setname = scrape_dataset_name()
#         running = False
#     except ValueError:
#         time.sleep(10000)
#         pass
# os.system("cd ../..")

# running = True
try:
    with open("currentStep.txt") as f:
        currentStep = f.read()
except FileNotFoundError:
    currentStep = "GEN__CMSSW_10_6_18"

print(currentStep)
try:
    if(currentStep == "GEN__CMSSW_10_6_18"):
        setname = ""
    else:
        setname = scrape_dataset_name()
except ValueError:
    print("not done with previous job!")
    os.exit()

os.system("pwd")
os.chdir(currentStep + "/src")
os.system("pwd")
os.system("python run_step.py " + setname)
os.system("cd ../..")

try:
    nextStep = steps[steps.index(currentStep)+1]
    with open("currentStep.txt", 'w') as f:
        f.write(nextStep)
except IndexError:
    os.remove("currentStep.txt")
    print("last step completed, no more steps to run")
