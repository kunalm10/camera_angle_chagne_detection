# camera_angle_chagne_detection

USING COMPUTER VISION TECHNIQUES TO SOLVE HIGHWAY INCIDENT DETECTION PROBLEMs

## DESCRIPTION

Camera Angle Change Detection - This module is created in order to automatically detect any change in the camera angle. That change can occur due to several reasons like rotation of camera on its axis, zooming in zooming out, change in the pitch angle of the camera, etc.

The algorith uses Imagehash funtion to create hash strings of two frames which are several frames apart (in our case this frame gap is 50, which can be changed according to the requirement). We use hamming distance to compare the two hash strings we generated from frames. This process goes on continously for whole video. Whenever the hamming distance goes above 20, the algorithm will result that camera angle is changed.

Several things which can be changed over the course of time according to the requirement of project can be frame gap difference and hamming distance threshold, this is pretty easy to do because these are just numeric integers.

## INSTALLATION

Import the following python libraries for this module to work:
The versions mentioned below were used at the time of development; the latest versions of these libraries should support the code, but if not, then degrade the version to these specified versions
	
	PIL/Pillow – 7.0.0 to facilitate reading and loading images. 
	https://pypi.org/project/Pillow/

	ImageHash – 4.1.0, which contains our implementation of Hash. https://pypi.org/project/ImageHash/

	OpenCV module – 4.1.0.25, which helps to read and display images and videos.
	https://pypi.org/project/opencv-python/

	NumPy/SciPy – 1.16.6, which are required by ImageHash.
	https://pypi.org/project/numpy/
  
## METHOD

Input: Original Video frames which are directly fetched from INDOT, do not give processed frames, this might give some faulty result.

Output: 2 possible return statements - 
"Camera Angle Change Detected" and
"Camera Angle Change not Detected"
	
This program can be run seperately to detect camera change, but in our main project it will be called internally from another python script. 
