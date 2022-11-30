#import subprocess
#from time import sleep

#y=(0.1)
#subprocess.Popen(["python", 'testScreen.py'])
#sleep(y)
#subprocess.Popen(["python", 'test.py'])

import os

os.system("python testScreen.py &")
os.system("python test.py &")

 
