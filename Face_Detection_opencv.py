import cv2
import matplotlib.pyplot as plt

denis = cv2.imread('Denis_Mukwege.jpg',0)
nadia = cv2.imread('Nadia_Murad.jpg',0)
solvay = cv2.imread('solvay_conference.jpg',0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(image):
    image_copy = image.copy()

    face_rectangles_list = face_cascade.detectMultiScale(image_copy)

    while True:

        for x,y,w,h in face_rectangles_list:
            cv2.rectangle(image_copy, (x,y), (x+w, y+h), (255,0,0), 4)

        cv2.imshow('image',image_copy)
    
        if cv2.waitKey(1) & 0xFF == 27:
            break

face_detector(solvay)       