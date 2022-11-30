#import subprocess
#from time import sleep

#y=(0.1)
#subprocess.Popen(["python", 'testScreen.py'])
#sleep(y)
#subprocess.Popen(["python", 'test.py'])

#import os

#os.system("python testScreen.py &")
#os.system("python test.py &")

import berryIMUfunction
 
if(berryIMUfunction.power() = 0):
    subprocess.run('vcgencmd display_power 0', shell=True)
else:
    subprocess.run('vcgencmd display_power 1', shell=True)
