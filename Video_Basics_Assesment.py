import cv2
import matplotlib.pyplot as plt

def drawCircle(event,x,y,flags,params):

    global pt1, buttonClicked;
    
    if buttonClicked == True:
        buttonClicked = False
    
    if event == cv2.EVENT_LBUTTONUP:
        pt1 = (x,y)
        buttonClicked = True
    

pt1 = (0,0)
buttonClicked = False

capture = cv2.VideoCapture(0)

cv2.namedWindow('MyVideo')
cv2.setMouseCallback('MyVideo',drawCircle)

while True:
    ret, frame = capture.read()
    
    if buttonClicked == True:
        # print('heyy')
        cv2.circle(frame,pt1,50,(0,0,255),2)

    cv2.imshow('MyVideo',frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()