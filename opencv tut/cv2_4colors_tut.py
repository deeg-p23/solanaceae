import numpy as np # NumPy
import cv2 #OpenCV

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    # converts frame color values from BGR to HSV (hue, saturation, value)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # NOTE: the following is a simple way to take a sample BGR pixel and write it in HSV
    # BGR_color = np.array([[[255, 0, 0]]])
    # x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)

    # setting some lower/upper bounds of what blues we desire to see
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # .inRange will mask an image based on desired values as bounds
    masked_frame = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # compare the value bits in frame to the masked_frame, and out into frame
    # this makes it so ALL blue values within the masks' bounds remain
    result = cv2.bitwise_and(frame, frame, mask=masked_frame)

    cv2.imshow('frame', result) 

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()