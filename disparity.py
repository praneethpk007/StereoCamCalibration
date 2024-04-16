import numpy as np
import cv2
from matplotlib import pyplot as plt

class DepthMap:
    def __init__(self, stereoMap):
        self.stereoMap = stereoMap

    def computeDepthMapSGBM(self, frame_left_rectified, frame_right_rectified): 
        stereoMapL_x, stereoMapL_y, stereoMapR_x, stereoMapR_y = self.stereoMap

        window_size = 7
        min_disp = 0  # Adjust as needed
        num_disp = 32  # Adjust as needed

        stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
                                    numDisparities=num_disp,
                                    blockSize=15,
                                    mode=cv2.STEREO_SGBM_MODE_HH)

        # Undistort and rectify images
        gray_right = cv2.remap(frame_right_rectified, stereoMapR_x, stereoMapR_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
        gray_left = cv2.remap(frame_left_rectified, stereoMapL_x, stereoMapL_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)

        # Compute disparity map
        disparity = stereo.compute(gray_left, gray_right)

        # Normalize disparity values for better visualization
        disparity_normalized = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        return gray_left, gray_right, disparity_normalized

# Camera parameters to undistort and rectify images
cv_file = cv2.FileStorage()
cv_file.open('stereoMap.xml', cv2.FileStorage_READ)
stereoMapL_x = cv_file.getNode('stereoMapL_x').mat()
stereoMapL_y = cv_file.getNode('stereoMapL_y').mat()
stereoMapR_x = cv_file.getNode('stereoMapR_x').mat()
stereoMapR_y = cv_file.getNode('stereoMapR_y').mat()
stereoMap = (stereoMapL_x, stereoMapL_y, stereoMapR_x, stereoMapR_y)

# Create DepthMap object
depth_map = DepthMap(stereoMap)

# Open both cameras
cap_right = cv2.VideoCapture(2)
cap_left = cv2.VideoCapture(0)

while(cap_right.isOpened() and cap_left.isOpened()):
    success_right, frame_right = cap_right.read()
    success_left, frame_left = cap_left.read()

    if not success_right or not success_left:
        print("Failed to grab frames")
        break

    # Compute disparity map using StereoSGBM algorithm
    gray_left, gray_right, disparity_normalized = depth_map.computeDepthMapSGBM(frame_left, frame_right)

    # Display images and disparity map
    cv2.imshow("Left Image", gray_left)
    cv2.imshow("Right Image", gray_right)
    cv2.imshow("Disparity Map", disparity_normalized)

    # Check for keypress 'q' to quit the program
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release and destroy all windows before termination
cap_right.release()
cap_left.release()
cv2.destroyAllWindows()

