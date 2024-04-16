# Stereo Camera Setup with Raspberry Pi

This project presents an implementation of a stereo vision camera setup using two Logitech C-310 USB cameras and a Raspberry Pi Model 3B+ as part of a project. It can also be perfectly (even better) run on Windows/Linux platforms.
This setup can later be used for various implementations of 3D reconstruction and depth estimation.

## Requirements

- **Hardware:** 
  - Any two cameras (same model will increase the ease of calibration)
  - PC

  We have used an Raspberry Pi Model 3B+ as part of our project.

- **Software:**
  - Python 3.x
  - OpenCV Python
  
## Installation

   Install the opencv-python package using pip and install it's dependencies.
   Before running the code, create an empty folder named 'images' with subfolders 'stereoLeft' and 'stereoRight'. These folders will store captured frames for calibration.

## Calibration Process

1. **Capture Calibration Frames:**
   
   Capture around 20-30 chessboard frames with different angles using both cameras.

2. **Run Calibration Script:**
   
   Execute the calibration script. It processes the captured frames and performs stereo calibration.

3. **Run Disparity Calculation:**
   
   Utilize the disparity code to calculate the disparity map, measuring the accuracy of the calibration.

## Running the Code

A simple bash script is provided to run all the necessary files at once.

