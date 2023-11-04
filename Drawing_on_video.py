import numpy as np
import cv2
import matplotlib.pyplot as plt


capture = cv2.VideoCapture(0)

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Top Left coordinate for the rectangle drawing
x = width // 2
y = height // 2

#  width & height of the rectangle
w = width // 4
h = height // 4


while True:
    ret, frame = capture.read()

    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), 5)
    
    cv2.imshow('myvideo', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break;


capture.release()
cv2.destroyAllWindows()
