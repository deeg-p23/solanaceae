import cv2
import numpy as np
cap = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')



while True:
    ret, frame = cap.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3,5)
    rightface = face_cascade2.detectMultiScale(gray_frame,1.3,5)
    flipped = cv2.flip(gray_frame,1)
    leftface = face_cascade2.detectMultiScale(flipped,1.3,5)
     
    for (x, y, a, b) in faces:
        cv2.rectangle(frame, (x, y), (x + a, y + b), (0, 0, 255), 5)
        
     
    for (x, y, a, b) in rightface:
        cv2.rectangle(frame, (x, y), (x + a, y + b), (0, 0, 255), 5)
       
            
    # for (x, y, a, b) in leftface:
    #     width  = int(cap.get(3)) 
    #     height = int(cap.get(4))
    #     cv2.rectangle(frame, (x,y), (width - a, width - b), (0, 0, 255), 5)
       
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() # clears usage of video capture
cv2.destroyAllWindows()