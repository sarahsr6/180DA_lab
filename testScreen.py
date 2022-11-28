from subprocess import run
from time import sleep

for i in range(5):
  run('xrandr --output HDMI-1 --off', shell=True)
  sleep(1)
  run('xrandr --output HDMI-1 --auto', shell=True)
 # run('vcgencmd display_power 1', shell=True)
  sleep(1)
