import numpy as np
import pandas as pd
import cv2

def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeftClicked, botRightClicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeftClicked == True and botRightClicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeftClicked = False
            botRightClicked = False
        
        if topLeftClicked == False:
            pt1 = (x,y)
            topLeftClicked = True
            
        elif botRightClicked == False:
            pt2 = (x,y)
            botRightClicked = True


# Not started Drawing yet
pt1 = (0,0)
pt2 = (0,0)
topLeftClicked = False
botRightClicked = False

capture = cv2.VideoCapture(0)

cv2.namedWindow('myvideo')
cv2.setMouseCallback('myvideo',draw_rectangle)


while True:
    ret, frame = capture.read()

    if topLeftClicked == True:
        cv2.circle(frame,pt1,5,(255,0,0),-1)

    if botRightClicked == True and topLeftClicked==True:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),5)
    
    cv2.imshow('myvideo', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break;

capture.release()
cv2.destroyAllWindows()