from subprocess import run
from time import sleep

for i in range(5):
  run('vcgencmd display_power 0 7', shell=True)
  sleep(1)
  #run('xrandr --output HDMI-1 --auto', shell=True)
  run('vcgencmd display_power 1 7', shell=True)
  sleep(1)
