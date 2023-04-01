import os
import argparse
import shutil
from datetime import datetime, timedelta

# Parse the command-line arguments
parser = argparse.ArgumentParser(description="Sort through image files in a directory based on their capture time.")
parser.add_argument("--folder", required=True, help="Path to the directory containing the image files.")
parser.add_argument("--time", default="12:00:00", help="Time of interest in the format HH:MM:SS (e.g. 12:00:00 for midday).")
parser.add_argument("--period", type=int, default=5, help="-/+ Period of interest in minutes.")
parser.add_argument("--target", help="Path to the directory to copy the matching images to.")
args = parser.parse_args()

# Get the path to the directory containing the image files
path_to_directory = args.folder

# Get the time of day to filter for
time_of_day = datetime.strptime(args.time, "%H:%M:%S").time()

# Get the period of interest
period_of_interest = timedelta(minutes=args.period)

# Get the path to the target directory to copy the matching images to
target_directory = args.target

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Iterate through each image file in the directory
for filename in os.listdir(path_to_directory):
    # Get the date and time from the filename (assuming the format is "YYYYMMDD-HHMMSS.jpg")
    date_string, time_string = filename.split("-")
    year = int(date_string[:4])
    month = int(date_string[4:6])
    day = int(date_string[6:8])
    hour = int(time_string[:2])
    minute = int(time_string[2:4])
    second = int(time_string[4:6])
    file_datetime = datetime(year, month, day, hour, minute, second)

    # Calculate the time difference between the image capture time and the desired time of day
    image_time = file_datetime.time()
    time_difference = abs((datetime.combine(datetime.min, image_time) - datetime.combine(datetime.min, time_of_day)).total_seconds())
    
    # Check if the image was taken within the specified period of time around the desired time of day
    if time_difference <= period_of_interest.total_seconds():
        # If so, copy the file to the target directory
        source_path = os.path.join(path_to_directory, filename)
        target_path = os.path.join(target_directory, filename)
        shutil.copy(source_path, target_path)
        print(f"Copied {filename} to {target_directory}")

