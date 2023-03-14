# Script to make a video from a folder full of time lapse images
# USAGE: python script.py --input /path/to/images --output /path/to/output.mp4 --fps 30
# Rob Lloyd. Lincoln 2023

import argparse
import cv2
import logging
import os

# Create an ArgumentParser object to handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='path to input folder containing images')
parser.add_argument('--output', required=True, help='path to output video file')
parser.add_argument('--fps', type=int, default=30, help='frame rate of the output video')
args = parser.parse_args()

# Set up logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the output video filename and codec
out_filename = args.output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Get a list of all the image files in the input folder and sort them using sorted()
image_files = [os.path.join(args.input, f) for f in sorted(os.listdir(args.input)) if os.path.isfile(os.path.join(args.input, f))]
print(f"Found {len(image_files)} image files in input folder")
logging.info(f"Found {len(image_files)} image files in input folder")

# Check the frame size of the first image
img = cv2.imread(image_files[0])
height, width, _ = img.shape
print(f"Input image size: {width}x{height}")
logging.info(f"Input image size: {width}x{height}")

# Create a VideoWriter object to write the output video
out = cv2.VideoWriter(out_filename, fourcc, args.fps, (width, height))

# Loop through the image files, read each image and write it to the output video
for image_file in image_files:
    img = cv2.imread(image_file)
    if img.shape[0:2] != (height, width):
        print(f"Error: Image {image_file} has a different size than the first image")
        logging.error(f"Error: Image {image_file} has a different size than the first image")
        break
    out.write(img)
    print(f"Processed image file: {image_file}")
    logging.info(f"Processed image file: {image_file}")

# Release the VideoWriter object and close the output video file
out.release()
print(f"Output video saved to: {out_filename}")
logging.info(f"Output video saved to: {out_filename}")
