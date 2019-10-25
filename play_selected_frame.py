import numpy as np
import cv2
cap = cv2.VideoCapture("Road.mp4") #video_name is the video being called
cap.set(1,10); # Where frame_no is the frame you want
ret, frame = cap.read() # Read the frame
cv2.imshow('window_name', frame) # show frame on window

