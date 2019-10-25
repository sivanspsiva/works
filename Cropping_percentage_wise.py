#Importing Libraries
import cv2
from moviepy.editor import *

#To count the time for the Video
cap=cv2.VideoCapture("Road.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
time_for_video=int(float(frames)/float(fps))

#For Cropping the video and saving
req_length=int(input("enter a req percentage: "))
for clip_num in range(int((time_for_video/100)*req_length),time_for_video+int((time_for_video/100)*req_length),int((time_for_video/100)*req_length)):
    print(clip_num)
    myvideo = VideoFileClip("Road.mp4")
    myvideo_edited = myvideo.subclip(clip_num - int((time_for_video/100)*req_length), clip_num)
    if clip_num<=time_for_video:
        myvideo_edited.write_videofile("clip"+str(clip_num)+".mp4", codec="libx264")
    else:
        myvideo_edited=myvideo.subclip(clip_num-int((time_for_video/100)*req_length),time_for_video)
        myvideo_edited.write_videofile("clip"+str((time_for_video/100)*req_length-time_for_video)+".mp4",codec="libx264")

#Counting the frames of cropping video
my=VideoFileClip("clip.mp4")
frames_cutting_video=my.reader.nframes
print("Total Frames is: ",frames_cutting_video)