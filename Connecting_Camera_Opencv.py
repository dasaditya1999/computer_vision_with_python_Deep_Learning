import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt

capture = cv2.VideoCapture(0)

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

#Windows - VIDX video codec format
#Macos, Linux - XVID video codec format

writer = cv2.VideoWriter('mysupervideo.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(width, height))

while True:
    ret, frame = capture.read()

    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    writer.write(frame)

    cv2.imshow('my_first_video',frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()