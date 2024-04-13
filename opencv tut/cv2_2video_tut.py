import numpy as np # NumPy
import cv2 #OpenCV

cap = cv2.VideoCapture(1) # will access active video input devices.
# the input for cv2.VideoCapture can be an integer to read the desired camera input.
# the input may also be the directory string to a video

while True:
    ret, frame = cap.read() # reads video capture
    # ret returns an output of whether or not the capture is still readable
    # frame returns the frame at a given time during the recording/broadcast
    
    # we want to create a unique take on the frame that has four picures in one
    # so as to not destroy the frame data, we make a new image based on its size and values:
    image = np.zeros(frame.shape, np.uint8)
    # write a new image that has the resolution of the camera because of frame.shape
    # np.uint8 will write each value as an unsigned integer of 8 bits. 
    # (the technical reason is because each value only needs 256 possible values to write color values in each bgr tuple pixel)

    # use .get() to get width, height, and many other unique stats about a capture
    width = int(cap.get(3)) # returns CAP_PROP_FRAME_WIDTH
    height = int(cap.get(4)) # returns CAP_PROP_FRAME_HEIGHT
    # NOTE: you MUST type cast them into ints, idk what type they are initially but its not int

    minimized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # set all four corners to new smaller image
    image[:height//2, :width//2] = minimized_frame
    image[height//2:, :width//2] = minimized_frame
    image[height//2:, width//2:] = minimized_frame
    image[:height//2, width//2:] = minimized_frame

    # show the four corner webcam capture
    cv2.imshow('frame', image) 

    # this will check if key pressed during the waitKey() time interval is "q" key
    # if the given "q" key is pressed, then it will break the loop.
    if cv2.waitKey(1) == ord('q'):
        break

cap.release() # clears usage of video capture
cv2.destroyAllWindows()