import cv2
import matplotlib.pyplot as plt

solvay = cv2.imread('solvay_conference.jpg',0) 
nadia = cv2.imread('Nadia_Murad.jpg',0)
denis = cv2.imread('Denis_Mukwege.jpg',0)
puppy = cv2.imread('00-puppy.jpg',0)

eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect_eye(image):

    image_copy = image.copy()
    
    list_rectangles_eye = eye_cascade.detectMultiScale(image_copy, scaleFactor=1.2, minNeighbors=5)

    while True:
        for x,y,w,h in list_rectangles_eye:
            cv2.rectangle(image_copy, (x,y), (x+w, y+h), (255,0,0), 4)
    
        cv2.imshow('image_eye_detector',image_copy)

        if cv2.waitKey(1) & 0xFF == 27:
            break

detect_eye(denis)
        