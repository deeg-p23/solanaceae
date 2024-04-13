import numpy as np # NumPy
import cv2 #OpenCV

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    # the following will draw a line, the params are as so:
    # frame is the image the line is drawn on
    # (0, 0) is the starting coordinate
    # (width, height) is the ending coordinate
    # (255, 0, 0) is the color
    # 10 is the line thickness
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 100)

    # following will draw a rectangle, similar parameters
    # (200, 200) is the first point of a rectangle
    # (250, 250) is the parallel point of a rectangle
    img = cv2.rectangle(frame, (200, 200), (250, 250), (100, 100, 100), 10)

    # following will draw a circle, similar paramters
    # (300, 300) is the origin of the circle
    # 60 is the radius
    # -1 is the line thickness still, but NOTE: -1 will fill it
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_DUPLEX # register what font we will use. all fonts in doc

    # following will draw font
    # 'Lorem ipsum' is the text input parameter
    # (200, height - 10) is the CENTERED location of the text
    # font is the font we previously defined
    # 1 is the font size
    # (0, 0, 0) is the font color
    # 2 is the line thickness
    # cv2.LINE_AA is necessary, it writes the text finer, better explained in doc
    img = cv2.putText(img, 'Lorem ipsum', (10, height - 10), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame) 

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()