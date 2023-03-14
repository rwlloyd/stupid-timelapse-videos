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

### save_garden_img.py 

Script to capture an image from a webcam and save it to a fixed directory

Example cron line

    */5 * * * * python3 /home/pi/scripts/save_garden_img.py >/dev/null 2>&1

### make_video.py 
Script to make a video from a folder full of time lapse images

    python script.py --input /path/to/images --output /path/to/output.mp4 --fps 30

### Next steps

1. Run test with raspberry pi
2. Set up ESP32 cam and work out how to save the images back to a server