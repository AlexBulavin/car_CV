import cv2 as cv
import numpy as np
from urllib.request import urlopen
import os
import datetime
import time
import sys

# change to your ESP32-CAM ip
url = "http://192.168.1.109/cam.mjpeg"
CAMERA_BUFFRER_SIZE = 16384 #8192 #4096
stream = urlopen(url)
bts = b''
i = 0
detector = cv.QRCodeDetector()

while True:
    try:
        bts += stream.read(CAMERA_BUFFRER_SIZE)
        jpghead = bts.find(b'\xff\xd8')
        jpgend = bts.find(b'\xff\xd9')
        if jpghead > -1 and jpgend > -1:
            jpg = bts[jpghead:jpgend + 2]
            bts = bts[jpgend + 2:]
            img = cv.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv.IMREAD_UNCHANGED)
            # img=cv.flip(img,0) #>0:#Поворот по вертикали, 0:Поворот по горизонтали, <0:Отразить по вертикали и по горизонтали
            # h,w=img.shape[:2]
            # print('Размер изображения по высоте:' + str(h) + 'ширине：' + str(w))
            img = cv.resize(img, (640, 480))

            # Display traffic light
            # cv.ellipse(img, (320, 265), (131, 131), 0, -90, val, (255, 180, 0), 27)
            # cv2.circle(image, center_coordinates, radius, color, thickness)
            cv.circle(img, (600, 30), 20, (0, 00, 255), 1)#Read
            cv.circle(img, (600, 75), 20, (0, 255, 255), 1)#Yellow
            cv.circle(img, (600, 120), 20, (0, 255, 0), 1)#Green

            # detect and decode
            data, bbox, straight_qrcode = detector.detectAndDecode(img)

            # if there is a QR code
            if bbox is not None:
                print(f"QRCode data:\n{data}")
                if data == "https://readyforsky.com":
                    #Display traffic light BGR color scheme
                    #cv.ellipse(img, (320, 265), (131, 131), 0, -90, val, (255, 180, 0), 27)
                    #cv2.circle(image, center_coordinates, radius, color, thickness)
                    cv.circle(img, (600, 30), 20, (0, 00, 255), -1)#Read
                elif data == "Traffic light 12345":
                    cv.circle(img, (600, 75), 20, (0, 255, 255), -1)#Yellow
                elif data == "Traffic light 1.1":
                    cv.circle(img, (600, 120), 20, (0, 255, 0), -1)#Green
                # display the image with lines
                # length of bounding box
                n_lines = len(
                    bbox[
                        0])  # Поскольку bbox = [[[float, float]]], необходимо перейти к int и идти по первому элементу массива
                bbox1 = bbox.astype(int)  # Преобразовали координаты к целочисленным
                for i in range(n_lines):
                    # draw all lines
                    point1 = tuple(bbox1[0, [i][0]])
                    point2 = tuple(bbox1[0, [(i + 1) % n_lines][0]])
                    cv.line(img, point1, point2, color=(255, 0, 0), thickness=2)

            cv.imshow("stream", img)
        k = cv.waitKey(1)
    except Exception as e:
        print("Error:" + str(e))
        bts = b''
        stream = urlopen(url)
        continue

    k = cv.waitKey(1)
    # Нажмите a, чтобы сделать фото и сохранить
    if k & 0xFF == ord('a'):
        cv.imwrite(str(i) + ".jpg", img)
        i = i + 1
    # Нажмите q, чтобы выйти
    if k & 0xFF == ord('q'):
        break
cv.destroyAllWindows()