import numpy as np
import cv2

cap = cv2.VideoCapture(0)

template = cv2.imread('solanaceae/solanaceae/opencv tut/png test-assets/test_object.jpg', 0)

height, width = template.shape


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    for method in methods:
        img2 = gray.copy()

        template.astype(np.uint8)
        img2.astype(np.uint8)

        print(template.shape)
        print(img2.shape)

        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        


        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        bottom_right_loc = (location[0] + width, location[1] + height)
        cv2.rectangle(img2, location, bottom_right_loc, (0, 0, 255), 5)
        cv2.imshow('frame', img2)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()
