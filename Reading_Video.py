import cv2
import numpy as np
import pandas as pd
import time

capture = cv2.VideoCapture('mysupervideo.mp4')

while capture.isOpened():
    ret, frame = capture.read()

    if ret == True:

        time.sleep(1/50)
        cv2.imshow('My video', frame)
    
        if cv2.waitKey(5) & 0xFF == 27:
            break;
    else:
        break
# print(capture)

capture.release()
cv2.destroyAllWindows()