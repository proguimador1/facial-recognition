"""import tkinter
import os
import sys
"""
import cv2

cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()