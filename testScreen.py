from subprocess import run
from time import sleep

for i in range(5):
  run('tvservice --off', shell=False)
  sleep(1)
  run('vcgencmd display_power 1', shell=True)
  sleep(1)
