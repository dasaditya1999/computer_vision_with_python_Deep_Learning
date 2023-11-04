import numpy as np
import pandas as pd
import cv2

def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, leftbuttondown, leftbuttonup

    if leftbuttonup == True and leftbuttondown == True:
        leftbuttondown = False
        leftbuttonup = False

    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left Button Up')
        pt1 = (x,y)
        leftbuttondown = True
        # print(x,y)
    if event == cv2.EVENT_LBUTTONUP:
        print('Left button down')
        pt2 = (x,y)
        leftbuttonup = True
        # print(x,y)
        # cv2.rectangle()

# Not started Drawing yet
pt1 = (0,0)
pt2 = (0,0)
leftbuttondown = False
leftbuttonup = False

capture = cv2.VideoCapture(0)

cv2.namedWindow('myvideo')
cv2.setMouseCallback('myvideo',draw_rectangle)

while True:
    ret, frame = capture.read()

    if leftbuttondown == True and leftbuttonup == True:
        cv2.rectangle(frame,pt1,pt2,(255,0,0),5)
    
    cv2.imshow('myvideo', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break;

capture.release()
cv2.destroyAllWindows()