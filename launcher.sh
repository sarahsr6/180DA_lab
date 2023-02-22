#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/newnewproj/180DA_lab
sudo python3 imuPublisher.py
cd /
