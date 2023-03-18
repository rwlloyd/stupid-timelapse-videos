# TIMELAPSE

An attempt to automate the collection and generation of timelape images using python scripts triggered by crontab

1. Save the image
2. Periodically convert the images into a video
3. Periodically copy all files to a backup server then delete originals (we won't delete them to begin with)
4. Profit?

## Hardware and Connectivity

- In the first instance, the target devices for this system are Raspberry pi with a webcam or ESP32-CAM modules. 
- Initial test areas will have wifi coverage or direct network connection
- raspberry pi should work off mains power or a suitable 5v power supply
- ESP32 can run off a 5v Supply or suitable supply down to 3.3v

## Scripts

### save_img.py 

Script to capture an image from a webcam and save it to a directory

Example Usage

    python save_img.py --name deleteme --folder /home/pi/scripts/images --camera 2

- Name (default='newSequence)
- folder (default='/') 
- camera (default=0)

Example cron line

    */5 * * * * python3 /home/pi/scripts/save_img.py >/dev/null 2>&1

### make_video.py 
Script to make a video from a folder full of time lapse images

    python script.py --input /path/to/images --output /path/to/output.mp4 --fps 30

## Using Crontab

Cron is the default task scheduler utility on Linux-based operating systems like the Raspberry Pi OS. It’s the perfect tool for this application as it can start programs and shell scripts on boot or at regular intervals. Cron is widely used in automating recurring tasks such as sending sensor data reports, updating the weather daily, watering the plants, etc. 

You can read more about it here; https://www.circuitbasics.com/starting-programs-automatically-using-cron-on-a-raspberry-pi/

## Using SCP

    PS C:\Users\Rob> scp pi@automationserver.local:/home/pi/scripts/video/garden/gardenTest11-15fps.mp4 'D:\dev\timelapse\scp'
    pi@automationserver.local's password:
    gardenTest11-15fps.mp4                                                                100%   90MB  10.7MB/s   00:08


windows get files from linux
scp pi@automationserver.local:/home/pi/scripts/images/garden/*.jpg 'D:\dev\timelapse\gardenImages\'

## Next steps

1. Run test with raspberry pi
2. Set up ESP32 cam and work out how to save the images back to a server