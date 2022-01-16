import urllib.request
import cv2
import numpy as np

#Делаем дескриптор для описания якорных изображений
original_img = cv2.imread(f'Resources/R4S_QR7.jpg', 0)

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(original_img, None) #ORB (Oriented FAST and Rotated BRIEF) - один из алгоритмов
#используемых для создания дескриптора
#Подробности здесь: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_orb/py_orb.html
#Другие алгоритмы для дескрипторов:
#SIFT http://aishack.in/tutorials/sift-scale-invariant-feature-transform-introduction/
#SURF http://www.vision.ee.ethz.ch/~surf/eccv06.pdf
#Harris http://aishack.in/tutorials/harris-corner-detector/

# compute the descriptors with ORB
kp, des = orb.compute(original_img, kp)

# compute the descriptors with SIFT
#gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp_sift = sift.detect(original_img, None)
sift_img = cv2.drawKeypoints(original_img, kp_sift, original_img)
cv2.imwrite('sift_keypoints.jpg', sift_img)

# #SURF
# # Create SURF object. You can specify params here or later.
# # Here I set Hessian Threshold to 400
# surf = cv2.xfeatures2d.SURF_create(400)
# # Find keypoints and descriptors directly
# kp_surf, des_surf = surf.detectAndCompute(original_img, None)
# len(kp_surf)



# draw only keypoints location,not size and orientation
secondary_img = cv2.drawKeypoints(original_img, kp, original_img, color=(0, 255, 0), flags=0)
cv2.imshow('keypoints', secondary_img)
cv2.waitKey(0)
