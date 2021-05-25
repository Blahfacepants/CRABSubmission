import os
import time
import datetime
import sys

os.remove("inputs.csv")
with open("inputs.csv", 'w') as f:
    f.write("SIM_" + datetime.datetime.now().strftime("%y%m%d%H%M%S") + ',' + sys.argv[1])


os.system("python config_SIM.py inputs.csv")
time.sleep(0.1)
os.system("chmod +x submit_crab_inputs.sh")
os.system("./submit_crab_inputs.sh")
