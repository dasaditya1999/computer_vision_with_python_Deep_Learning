import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

#Create a blank image
img = np.zeros(shape=(715,712,3), dtype=np.uint8)
# img = np.random.randint(low=0,high=255,size=(700,750,3), dtype=np.uint8)

### Define some Functions like draw circle, draw rectangle, draw lines, draw polylines ###
def drawCircle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        cv2.circle(img, (x,y), 50, (0,0,255), thickness=5)

    if event == cv2.EVENT_FLAG_MBUTTON:
        print(x,y)
        cv2.rectangle(img, pt1 = (x,y),pt2 = (x+50,y+50), thickness=5, color=(255,0,0))

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.line(img, pt1 =(x,y) , pt2 = (x+20,y+20), color=(255,255,255), thickness=6)

    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.line(img, pt1=(x,y),pt2 = (x+10,y+10), color=(0,255,0), thickness=6)
        
cv2.namedWindow(winname='blank_image')

cv2.setMouseCallback('blank_image',drawCircle)


while True:
    cv2.imshow('blank_image',img)

    if cv2.waitKey(20) & 0xFF==27:
        break;

cv2.destroyAllWindows()