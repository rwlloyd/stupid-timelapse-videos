# stupid-timelapse-videos
Quick tutorial on using ffmpeg to create timelapse videos from a stack of images

![Banner Image](/ffmpeg-timelapse.png)

Creating a timelapse from a stack of images can be easily done in Adobe Premiere or even the old Windows Movie Maker. However, if you're a sadist or want to be able to script the creation of timelapse videos from a stack of images, you might like to try ffmpeg.

## Installation

### Windows

First off, I'd suggest you install chocolaty https://chocolatey.org/install it's basically apt for windows.

then open an administartor window and

    choco install ffmpeg
  
I suggest this, because it adds to the path to the environemt and all that shizzle.

### Ubuntu

    sudo apt install ffmpeg
  
## Configuring things

This is the command i used

    ffmpeg -framerate 24 -r 24 -start_number 2183 -i IMG_%04d.jpg -s:v 1920x1080 -c:v libx264 -pix_fmt yuv420p -r 24 birthday-garden-24fps.mp4

## References.

To save you the google-foo and picking through the rather dense documentation, I got a lot of help from:

https://matt.guide/how-to-create-open-source-time-lapse-videos/
