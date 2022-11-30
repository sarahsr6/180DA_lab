import subprocess
from time import sleep

y=(0.1)
subprocess.Popen(["python", 'testScreen.py'])
sleep(y)
subprocess.Popen(["python", 'test.py'])

#y=(0.1)
#subprocess.run(["python", 'BerryNew.py'])
#sleep(y)
#subprocess.run(["python", 'testScreen.py']) & subprocess.run(["python", 'BerryNew.py'])

 
