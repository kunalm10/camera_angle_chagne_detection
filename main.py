import cv2
import numpy as np
from PIL import Image
import imagehash
from camera_angle_change_detection_ELS import main as camera_change
from camera_angle_change_detection_PS import main_ELS as camera_change_ELS
from camera_angle_change_detection_PS import main_PS as camera_change_PS


frame_count = 0
camera_angle_change_detection = False
# Always a good idea to check if the video was acutally there
# If you get an error at thsi step, triple check your file path!!
video_file = "E:\RA python code\camera change detection test videos\\1-465-023-1-1+2020-07-25+20.0.mp4.mp4"
# video_file = 'E:\\RA python code\\camera change detection test videos\\65_2540_3+2019-10-03+13.50.mp4'        ##special video
# video_file = "E:\\RA python code\\camera change detection test videos\\1-465-047-2-1+2020-07-16+16.7.mp457.18_to_57.48.mp4"

cap = cv2.VideoCapture(video_file)
if cap.isOpened() == False:
    print(
        "Error opening the video file. Please double check your file path for typos."
        "Or move the movie file to the same location as this script/notebook")

# While the video is opened
# while cap.isOpened():
#     frame_count += 1
#     print(frame_count)
#     # Read the video file.
#     ret, frame = cap.read()
#
#     if ret == True:
#         if frame_count == 1:
#             first_frame = frame
#
#         cv2.imshow('frame1', frame)
#
#         if frame_count == 300:
#             second_frame = frame
#             print(camera_change(first_frame, second_frame))
#             if camera_change(first_frame, second_frame):
#                 break
#
#         # cv2.imshow('frame1', image_gray)
#         # Press q to quit
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     # Or automatically break this whole loop if the video is over.
#     else:
#         break


# While the video is opened
while cap.isOpened():
    frame_count += 1
    print(frame_count)
    # Read the video file.
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('original_video', frame)
        camera_angle_change_detection = camera_change_PS(frame, frame_count)
        print(camera_angle_change_detection)
        if camera_angle_change_detection == True:
            break



        # cv2.imshow('frame1', image_gray)
        # Press q to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Or automatically break this whole loop if the video is over.
    else:
        break

cap.release()
# Closes all the frames
cv2.destroyAllWindows()

