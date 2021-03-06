import numpy as np
import cv2

video = cv2.VideoCapture(0)

while(True):

    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
