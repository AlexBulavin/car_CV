#Из этого примера: https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/
# https://bitesofcode.wordpress.com/2018/09/16/augmented-reality-with-python-and-opencv-part-2/

import urllib.request
import cv2
import numpy as np

MIN_MATCHES = 15

url = 'http://192.168.1.112/cam.mjpeg'
try:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img_from_mjpeg = cv2.imdecode(imgNp, -1)
    cv2.imshow('stream', img_from_mjpeg)
    cap = cv2.imread(img_from_mjpeg, 0)
    model = cv2.imread(f'Resources/R4S_QR7.jpg', 0)
    # ORB keypoint detector
    orb = cv2.ORB_create()
    # create brute force  matcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # Compute model keypoints and its descriptors
    kp_model, des_model = orb.detectAndCompute(model, None)
    # Compute scene keypoints and its descriptors
    kp_frame, des_frame = orb.detectAndCompute(cap, None)
    # Match frame descriptors with model descriptors
    matches = bf.match(des_model, des_frame)
    # Sort them in the order of their distance
    matches = sorted(matches, key=lambda x: x.distance)

    if len(matches) > MIN_MATCHES:
        # draw first 15 matches.
        cap = cv2.drawMatches(model, kp_model, cap, kp_frame,
                              matches[:MIN_MATCHES], 0, flags=2)
        # show result
        cv2.imshow('frame', cap)
        cv2.waitKey(0)
    else:
        print("Not enough matches have been found - %d/%d" % (len(matches),
                                                              MIN_MATCHES))
    if ord('q') == cv2.waitKey(10):
        exit(0)
except:
    pass