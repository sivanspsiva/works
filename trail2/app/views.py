from django.shortcuts import render
import cv2
import shutil

def Index(request):
    return render(request,"index.html")

def Design(request):
    return render(request,"design.html")

#To play the particular frame of video
def Play(request):
    number=int(request.POST.get("num"))
#Create a VideoCapture Object and read from input file
    cap=cv2.VideoCapture("Road.mp4")
    while True:
       has_frame, frame = cap.read()
       frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
       if not has_frame:
           print('Reached the end of the video')
           break
       if number<=frames:
        cv2.imshow('frame',frames)
        cap.set(1, number)
        if cv2.waitKey(25) & 0xFF == ord('q'):
           break
       else:
           message="you entered morethan a frames ,Video has only ",int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),"frames"
           return render(request,"index.html",{"message":message})
    cv2.destroyAllWindows()
    message="Success"
    return render(request,"index.html",{"message":message})

#To find the number of frames in video
def Find(request):
    # Create a VideoCapture Object and read from input file
    cap = cv2.VideoCapture("Road.mp4")
    # To Conert from float to integer
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return render(request,"index.html",{"message":frames})

#To play the offline cam videos and save it
def Offline(request):

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture('Road.mp4')
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
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Save the Video to path
    shutil.copy("Road.mp4", "/home/dell/PycharmProjects/Capturing_videos")

    # Closes all the frames
    cv2.destroyAllWindows()
    message="Success"
    return render(request,"index.html",{"message":message})

#To paly the offline videos and save it
def Online(request):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Unable to read camera feed")

    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    while (True):
        ret, frame = cap.read()

        if ret == True:

            # Write the frame into the file 'output.avi'
            out.write(frame)

            # Display the resulting frame
            cv2.imshow('frame', frame)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

        # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

    # Save the Video to path
    shutil.copy("outpy.avi", "/home/dell/PycharmProjects/Capturing_videos_online")

    # Closes all the frames
    cv2.destroyAllWindows()
    message = "Success"
    return render(request, "index.html", {"message": message})


