import numpy as np
import pandas as pd
import cv2


#Read an image
img = cv2.imread('invoice.jpg')

#Function to draw the bbox
drawing = False
ix,iy = -1,-1

def drawBoundingBox(event, x,y,flags,params):

    global drawing, list_coordinates, ix,iy;
    
    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy = (x,y)
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(255,200,100), thickness=2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    

#Taking the mouse callbacks
cv2.namedWindow('invoice')

cv2.setMouseCallback('invoice',drawBoundingBox)

# Showing the image in another window.
while True:
    cv2.imshow('invoice',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()