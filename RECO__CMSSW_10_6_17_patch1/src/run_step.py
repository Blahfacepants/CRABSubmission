import os
import time
import datetime
import sys

os.remove("inputs.csv")
with open("inputs.csv", 'w') as f:
    f.write("RECO_" + datetime.now().strftime("%y%m%d%H%M%S") + ',' + sys.argv[1])


os.system("python config_RECO.py inputs.csv")
time.sleep(0.1)
os.system("chmod +x submit_crab_inputs.sh")
os.system("./submit_crab_inputs.sh")
