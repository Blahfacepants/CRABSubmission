import os
import time
import datetime
import sys

os.remove("inputs.csv")
with open("inputs.csv", 'w') as f:
    f.write("DIGIPremix_" + datetime.strftime("%y%m%d%H%M%S") + ',' + sys.argv[0])


os.system("python config_DIGIPremix.py inputs.csv")
time.sleep(0.1)
os.system("chmod +x submit_crab_inputs.sh")
os.system("./submit_crab_inputs.sh")
