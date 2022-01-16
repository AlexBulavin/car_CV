# """Access IP Camera in Python OpenCV"""
#
# import cv2
# import numpy as np
#
# stream = cv2.VideoCapture('http://192.168.1.109:81/stream')# 81-й порт открыт на камере.
#
# # Use the next line if your camera has a username and password
# # stream = cv2.VideoCapture('protocol://username:password@IP:port/1')
#
# while True:
#
#     r, f = stream.read()
#     cv2.imshow('IP Camera stream', f)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# stream.release()
# cv2.destroyAllWindows()

#Код работает в связке со скетчем roboCar2_ESP32_CAM_jan16.ino
#С цветными QR работает очень плохо

import urllib.request
import cv2
import numpy as np

#Выбрать URL в зависимости от работоспособности системы, скорости передачи данных и т.д.
#url = 'http://192.168.1.109/cam-lo.jpg'
#url = 'http://192.168.1.112/cam.mjpeg'
url = 'http://192.168.1.112/cam-hi.jpg'
#url = 'http://192.168.1.109/cam.bmp'
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()


while True:
    try:
        imgResp = urllib.request.urlopen(url)
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)

        # detect and decode
        data, bbox, straight_qrcode = detector.detectAndDecode(img)

        # if there is a QR code
        if bbox is not None:
            print(f"QRCode data:\n{data}")
            # display the image with lines
            # length of bounding box
            n_lines = len(
                bbox[0])  # Поскольку bbox = [[[float, float]]], необходимо перейти к int и идти по первому элементу массива
            bbox1 = bbox.astype(int)  # Преобразовали координаты к целочисленным
            for i in range(n_lines):
                # draw all lines
                point1 = tuple(bbox1[0, [i][0]])
                point2 = tuple(bbox1[0, [(i + 1) % n_lines][0]])
                cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

        # all the opencv processing is done here
        cv2.imshow('stream', img)
        if ord('q') == cv2.waitKey(10):
            exit(0)
    except:
        pass


