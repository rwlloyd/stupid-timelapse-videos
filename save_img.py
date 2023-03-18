# Script to capture an image from a webcam and save it to a fixed directory
# Script intended to be fired by crontab on a linux system 
# Images saved in accordance with ISO8601 naming https://en.wikipedia.org/wiki/ISO_8601 ... sort of
# Crontab line generated by https://crontab-generator.org/

# Don't forget to restart crom 'sudo service cron restart'
# Rob Lloyd. Lincoln 2023.

import argparse
import os
import cv2
import time
import logging

# Create an ArgumentParser object to handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True, default='newSequence', help='timelapse name')
parser.add_argument('--folder', default='/', help='path to save location')
parser.add_argument('--camera', type=int, default=0, help='frame rate of the output video')
args = parser.parse_args()

capture_name = args.name
folder_path = args.folder         # Replace "/path/to/folder"
camera_num = args.camera

# Set up logging to a file
logging.basicConfig(filename=capture_name + 'logfile.log', level=logging.DEBUG)

if not os.path.exists(folder_path):     # Check if the folder path exists or not
    os.makedirs(folder_path)            # If the folder path does not exist, create the folder

camera = cv2.VideoCapture(camera_num)            # Initialize the camera capture object
time.sleep(2)                           # Wait for 2 seconds to allow the camera to initialize

try:
    ret, frame = camera.read()              # Read a frame from the camera
    if ret:                             # Check if the frame was read successfully
        current_time = time.strftime("%Y%m%d-%H%M%S")  # Get the current timestamp to use as the image filename
        file_name = f"{current_time}.jpg"              # Create a unique filename for the image
        file_path = os.path.join(folder_path, file_name)  # Combine the folder path and filename to get the complete file path
        cv2.imwrite(file_path, frame)   # Save the image to the specified folder
        logging.info('%s Image saved to %s', capture_name, file_name)
    else:
        logging.error('Failed to capture image from webcam')
except Exception as e:
    logging.error('An Error occurred: %s', e)

camera.release()                        # Release the camera capture object
cv2.destroyAllWindows()                 # Destroy CV2!
