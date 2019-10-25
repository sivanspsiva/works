#Importing Libraries
import cv2
import shutil
#Create a VideoCapture Object and read from input file
cap=cv2.VideoCapture("Road.mp4")
#To Conert from float to integer
frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
shutil.copy("Road.mp4","/home/dell/PycharmProjects")
print("Total Frames is: ",frames)
while True:
    has_frame, frame = cap.read()
    if not has_frame:
        print('Reached the end of the video')
        break

    cv2.imshow('frame', frame)
    cap.set(1, 10)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()