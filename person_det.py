import cv2
import numpy as np
# change when using different camera
cap = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
fullbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# config_file = 'obj_det models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
# frozen_model = 'frozen_inference_graph.pb'

# object_model = cv2.dnn_DetectionModel(frozen_model, config_file)

# object_label = ['Mobile phone']

# object_model.setInputSize(320, 320)
# object_model.setInputScale(1.0/127.5)
# object_model.setInputScale((127.5, 127,5,127.5))
# object_model.setInputSwapRB(True)

object_font_scale = 3
object_font = cv2.FONT_HERSHEY_PLAIN

face_drawn = False

width  = int(cap.get(3)) 
height = int(cap.get(4))

while True:
    ret, frame = cap.read()

    face_drawn = False

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3,5)
    rightface = face_cascade2.detectMultiScale(gray_frame,1.3,5)
    flipped = cv2.flip(gray_frame, 1)
    leftface = face_cascade2.detectMultiScale(flipped,1.3,5)
    fullbody = fullbody_cascade.detectMultiScale(gray_frame,1.15,5)

    for (x, y, a, b) in faces:
        cv2.rectangle(frame, (x, y), (x + a, y + b), (0, 0, 255), 5)
        face_drawn = True
        
     
    for (x, y, a, b) in rightface:
        if not face_drawn:
            cv2.rectangle(frame, (x, y), (x + a, y + b), (0, 0, 255), 5)
       

    for (x, y, a, b) in leftface:
        if not face_drawn:
            cv2.rectangle(frame, (width - x,y), (width - (x + a), y + b), (0, 0, 255), 5)
       
       
    for (x, y, a, b) in fullbody:
        cv2.rectangle(frame, (x, y), (x + a, y + b), (0, 0, 255), 5)
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() # clears usage of video capture
cv2.destroyAllWindows()