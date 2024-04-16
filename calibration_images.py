import cv2

# Function to adjust camera settings
def set_camera_settings(capture, property_id, value):
    capture.set(property_id, value)

# Function to create trackbars for adjusting settings
def create_trackbars(window_name, capture):
    cv2.namedWindow(window_name)
    cv2.createTrackbar('Brightness', window_name, int(capture.get(cv2.CAP_PROP_BRIGHTNESS)), 255, lambda x: set_camera_settings(capture, cv2.CAP_PROP_BRIGHTNESS, x))
    cv2.createTrackbar('Contrast', window_name, int(capture.get(cv2.CAP_PROP_CONTRAST)), 255, lambda x: set_camera_settings(capture, cv2.CAP_PROP_CONTRAST, x))

# Open the default cameras
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)

# Check if the cameras opened successfully
if not cap.isOpened() or not cap2.isOpened():
    print("Error: Couldn't open one or more cameras")
    exit()

# Create trackbars for adjusting settings for each camera
create_trackbars('Settings1', cap)
create_trackbars('Settings2', cap2)

num = 0

while cap.isOpened() and cap2.isOpened():
    succes1, img = cap.read()
    succes2, img2 = cap2.read()
    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('images/stereoLeft/imageL' + str(num) + '.png', img)
        cv2.imwrite('images/stereoRight/imageR' + str(num) + '.png', img2)
        print("images saved!")
        num += 1
    cv2.imshow('Img 1',img)
    cv2.imshow('Img 2',img2)

# Release and destroy all windows before termination
cap.release()
cap2.release()
cv2.destroyAllWindows()

