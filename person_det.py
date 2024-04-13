import numpy as np
import cv2

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 6, 0, [30, 30])

    for (x, y, a, b) in faces:
        cv2.rectangle(frame, (x, y), (x + a, y + b), (0, 0, 255), 5)
        roi_gray = gray_frame[x:x+a, y:y+a]
        roi_color = frame[x:x+b, y:y+a]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ea, eb) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ea, ey+ eb), (0, 255, 0), 3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()