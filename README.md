# Slit-Stitch
Virtual Slit Scanning environment using Pure Data &amp; Python

# About

Open GL software that enables for real time segmenting and stitching of images & video. This is done in order to achieve similar effects to that of slit scan photography. The purpose of this project was to virtualize a scanning bed. My art at the time was primarly process focused & involved a lot of manual scanning to achieve interesting distortions. I got tired of having to rely on hardware to do this so I coded it in Python and Pure Data. The use of Pure Data allows for complex automation and even sound based controls of scanning. 

Theoretically, with some tweaking - one could scan an image or video using the light in a room as a control for the media's movement. This would flatten the light's gesture into a 2 dimensional array of distorted pixels

# ⌜Requirements⌟
### 1. Pure Data - https://puredata.info/downloads/pure-data

   *PD Vanilla* requires externals installed: GEM, Cyclone, ggee. 
   Pure Data Extended has everything bundled  - https://puredata.info/downloads/pd-extended
  
### 2. Python3 

   *Pillow* External required. Install via pip [pip3 install pillow](https://pillow.readthedocs.io/en/stable/)
   
# ⌜How to Run⌟
  1. Open Display Window
  2. Load Image/Video
  3. Set save location and filename
  4. In the Display window, move Image/Video to desired starting location. Left Click mouse to begin recording.
  5. Hit Stitch button! Stitched image should now be saved as "slittest.png" in the assigned save folder
  
# ⌜Controls⌟
  Move images with mouse
  Begin and end recording by lect clicking mouse
  Start and restart videos by tapping the spacebar
  
