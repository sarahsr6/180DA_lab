from subprocess import run
from time import sleep

for i in range(5):
  vcgencmd display_power 0
  #run('vcgencmd display_power 0', shell=True)
  sleep(1)
  #run('vcgencmd display_power 1', shell=True)
  vcgencmd display_power 1
  sleep(1)
