import cv2
import matplotlib.pyplot as plt

capture = cv2.VideoCapture(0)

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    ret, frame = capture.read()

    list_rectangles = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=5)

    for x,y,w,h in list_rectangles:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),5)

    cv2.imshow('video', frame)

    if cv2.waitKey(2) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()