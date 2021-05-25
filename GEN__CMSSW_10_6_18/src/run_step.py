import os
import time

#make sure the input csv is ready before you call this script!

os.system("python config_GEN.py inputs.csv")
time.sleep(0.1)
os.system("chmod +x submit_crab_inputs.sh")
os.system("./submit_crab_inputs.sh")
