import datetime
import cv2
import shutil
start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
cap = cv2.VideoCapture("matplotlib.mp4")
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(15) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Save the Video to path
shutil.copy("opencv.mp4", "/home/dell/PycharmProjects/Capturing_videos")

# Closes all the frames
cv2.destroyAllWindows()
end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
total_time=(datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))
print(total_time)
