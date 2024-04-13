import numpy as np # NumPy
import cv2 # OpenCV

img = cv2.imread('png test-assets/sponge.jpg')
img = cv2.resize(img, (0, 0), fx=3, fy=3)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# using the shi-tomasi algorithm for corner detection,
# we must first convert any images into grayscale

# the following is a function for their algorithm, named after a paper
# the first parameter is the image itself
# the second parameter is the number of corners to track
# the third parameter is the "quality" of corners to track. 1 being extremely sharp, 0 being probably not a corner at all
# the fourth parameter is the euclidean distance between tracked corners, should be somewhere above 0 to avoid repeat corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.25, 10)

# goodFeaturesToTrack will return arrays of FLOATING POINT VALUES
# we must convert corners to integers
corners = np.intp(corners)
# now draw a circle for each corner
for corner in corners:
    x, y = corner.ravel() # ravel() will flatten the corner from an array to its x and y integer
    # now we can draw a small circle for where each tracked corner
    cv2.circle(img, (x, y),  2, (0, 0, 255), -1)

# now to see the connections between the corners, we will draw a line between each one
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        # the following is just for randomly picking a new color for the line
        # tbh i dont understand the whole map lambda thing, but wtv
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)


cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# now going to demonstrate corner detection in video capture

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 100, 0.25, 10)
    for corner in corners:
        x, y = corner.ravel() # ravel() will flatten the corner from an array to its x and y integer
        # now we can draw a small circle for where each tracked corner
        x = int(x)
        y = int(y)
        cv2.circle(frame, (x, y),  2, (0, 0, 255), -1)


    cv2.imshow('frame', frame) 

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()
