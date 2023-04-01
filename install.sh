#!/bin/bash

# update the package list and upgrade the installed packages
sudo apt-get update
sudo apt-get upgrade -y

# install necessary packages
sudo apt-get install -y python3 python3-pip python3-picamera python3-opencv git

pip3 install tqdm

# clone the github repo
git clone https://github.com/rwlloyd/stupid-timelapse-videos.git

# write a new cronjob to the crontab file (this default fires every minute of the day)
echo "* * * * * python3 ~/stupid-timelapse-videos/save_img.py --name defaultTimelapse --folder /home/pi/defaultTimelapse --camera 0 >/dev/null 2>&1" >> /etc/crontab