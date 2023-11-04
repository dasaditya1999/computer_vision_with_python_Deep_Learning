import numpy as np
import pandas as pd
import cv2

#Reading the image
img = cv2.imread('dog_backpack.jpg')


##Function to draw circle every time the user click on the image.
def drawCircle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (255,0,0), 5)


##setting up the window name and getting the callback from the mouse
cv2.namedWindow('dog')
cv2.setMouseCallback('dog', drawCircle)


#Displaying the image
while True:
    cv2.imshow('dog',img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()