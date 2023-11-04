import numpy as np
import pandas as pd
import cv2


#Read an image
img = cv2.imread('invoice.jpg')

#Function to draw the bbox
list_coordinates = []

def drawBoundingBox(event, x,y,flags,params):

    global drawing, list_coordinates, ix,iy;
    
    if event == cv2.EVENT_LBUTTONDOWN:
        initinal_coordinates = (x,y)
        list_coordinates.append(initinal_coordinates)
        
    if event == cv2.EVENT_FLAG_MBUTTON:
        final_coordinates = (x,y)
        list_coordinates.append(final_coordinates)

        pt1 = list_coordinates[len(list_coordinates)-2]
        pt2 = list_coordinates[len(list_coordinates)-1]

        #Drawing a bbox
        cv2.rectangle(img, pt1=pt1, pt2=pt2, color=(255,25,140), thickness=2)
        print('choosen coordinates are here')
        print(pt1, pt2)

        

#Taking the mouse callbacks
cv2.namedWindow('invoice')

cv2.setMouseCallback('invoice',drawBoundingBox)

# Showing the image in another window.
while True:
    cv2.imshow('invoice',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()