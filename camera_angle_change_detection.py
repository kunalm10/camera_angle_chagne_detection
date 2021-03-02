import cv2
from PIL import Image
import imagehash

camera_angle_change_detected = False
threshold = 20  # Threshold sets the intensity at which camera angle change detection works.
# If the threshold too small then the algorithm will return camera angle change even if there is small change in the
# background due to clouds or moving vehicles. If it is set to be too high, it might miss potential camera angle
# changes.
font = cv2.FONT_HERSHEY_SIMPLEX
frame_list = []
frame_diff = 50


def cropping_and_color_to_gray(image):
    """
    Purpose

    This function is used for 2 purposes.
    1. Crop the frame - We just want to majorly compare the background of different frames of the highway,
    so we crop/throw away the lower half of the image
    2.convert a color image into a grayscale image
    -------

    :param image: (frame) This function takes original RGB image as a input.
    -------

    :return: (frame) It will return a image which will be cropped and it's RGB channel will be converted to grayscale.
    -------

    """
    height = image.shape[0]
    width = image.shape[1]
    image_rgb_crop = image[20:1 + int(height / 2), 1:1 + int(width)]
    image_gray = cv2.cvtColor(image_rgb_crop, cv2.COLOR_BGR2GRAY)
    # image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    return image_gray


def camera_angle_change_detection(image_gray_1, image_gray_2):
    """
    Purpose This function creates hash string of 2 frames and then calculate the hamming distance(hash difference) to
    predict the camera angle change
    -------

    :param image_gray_1: (frame) This is first gray and cropped image passed to this function from cropping_and_color_to_gray().
    :param image_gray_2: (frame) This is second gray and cropped image passed to this function from cropping_and_color_to_gray().

    :return: (flag: Boolean) It returns the flag:camera_angle_change_detected value as True/False.
    -------


    """

    hash1 = imagehash.dhash(Image.fromarray(image_gray_1))
    hash2 = imagehash.dhash(Image.fromarray(image_gray_2))
    print('hash difference = ', hash1 - hash2)

    if hash1 - hash2 < threshold:
        # cv2.putText(frame1, 'camera change not detected ', (50, 50), font, 1, (255, 0, 0), 2, cv2.LINE_4)
        # cv2.putText(frame1, str(hash1 - hash2), (50, 80), font, 1, (255, 0, 0), 2, cv2.LINE_4)
        camera_angle_change_detected = False
        # print('camera_angle_change_not_detected', camera_angle_change_detected)

    else:
        # cv2.putText(frame1, 'camera change detected', (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_4)
        # cv2.putText(frame1, str(hash1 - hash2), (50, 80), font, 1, (0, 0, 255), 2, cv2.LINE_4)
        camera_angle_change_detected = True
        # print('camera_angle_change_detected = ', camera_angle_change_detected)
    return camera_angle_change_detected


def main_camera_angle_change_ELS(frame1, frame2):
    """
    Purpose

    This module is used to detect camera angle change in Environment Learning Stage.
    This main code calls 2 functions internally
    1. cropping_and_color_to_gray(image)
    2. camera_angle_change_detection(image_gray_1, image_gray_2)
    --------

    :param frame1: (frame) This is supposed to be first RGB frame when ELS starts.
    :param frame2: (frame) This is supposed to be last RGB frame when ELS ends.
    --------

    :return: It will set the flag: camera_angle_change_detected as True/False

    """

    image_gray_1 = cropping_and_color_to_gray(frame1)
    image_gray_2 = cropping_and_color_to_gray(frame2)
    # cv2.imshow('frame_1', image_gray_1)
    # cv2.waitKey(100)
    # cv2.destroyAllWindows()
    # cv2.imshow('frame_2', image_gray_2)
    # cv2.waitKey(100)
    # cv2.destroyAllWindows()

    camera_angle_change_detected = camera_angle_change_detection(image_gray_1, image_gray_2)
    return camera_angle_change_detected


def main_camera_angle_change_PS(frame, frame_count):
    """
    Purpose

    This module is used to detect camera angle change in Post-Processing Stage.
    This main code calls 2 functions internally
    1. cropping_and_color_to_gray(image)
    2. camera_angle_change_detection(image_gray_1, image_gray_2)


    --------

    :param frame: (frame) This is supposed to be a RGB frame.
    :param frame_count: (int) This is supposed to be count of the frame of video.
    --------

    :return: (flag: Boolean) It will set the flag: camera_angle_change_detected as True/False

    """

    camera_angle_change_detected = False
    # print('frame_count % frame_diff = ', frame_count%frame_diff)
    if frame_count % frame_diff == 0 or frame_count == 1:
        image_gray = cropping_and_color_to_gray(frame)
        print('frame_count = ', frame_count, '\n')
        frame_list.append(image_gray)
        if len(frame_list) == 2:
            cv2.imshow('gray_image_1', frame_list[0])
            cv2.imshow('gray_image_2', frame_list[1])
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
            camera_angle_change_detected = camera_angle_change_detection(frame_list[0], frame_list[1])
            frame_list.pop(0)
    return camera_angle_change_detected
