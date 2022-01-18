import cv2 as cv
import numpy as np
from urllib.request import urlopen
import time
import os
import datetime
import time
import sys

tl_0 = time.time()#Задаём начальное время отсчёта при старте программы
tl_1 = 5 #Определяем задержку для переключения цветов светофора типа tl_1 в секундах
tl_2 = 5 #Определяем задержку для переключения цветов светофора типа tl_2 в секундах
tl_3 = 5 #Определяем задержку для переключения цветов светофора типа tl_3 в секундах
tl_4 = 5 #Определяем задержку для переключения цветов светофора типа tl_4 в секундах
ph_1 = 0 #Определяем фазовое смещение для светофора в секундах относительно общей лоя системы нулевой точки
ph_2 = 3 #Определяем фазовое смещение для светофора в секундах относительно общей лоя системы нулевой точки
ph_3 = 5 #Определяем фазовое смещение для светофора в секундах относительно общей лоя системы нулевой точки
ph_4 = 10 #Определяем фазовое смещение для светофора в секундах относительно общей лоя системы нулевой точки
counter_tl_1 = tl_0 #Задали сначение для счётчика времени каждого светофора
counter_tl_2 = tl_0 #Задали сначение для счётчика времени каждого светофора
counter_tl_3 = tl_0 #Задали сначение для счётчика времени каждого светофора
counter_tl_4 = tl_0 #Задали сначение для счётчика времени каждого светофора
counter_tl_5 = tl_0 #Задали сначение для счётчика времени каждого светофора
id_tl_1 = "https://readyforsky.com"
id_tl_2 = "Traffic light 12345"
id_tl_3 = "Traffic light 11"

# change to your ESP32-CAM ip
url = "http://192.168.1.109/cam.mjpeg"
CAMERA_BUFFRER_SIZE = 16384 #8192 #4096
stream = urlopen(url)
bts = b''
i = 0
detector = cv.QRCodeDetector()

while True:
    #Задаём установку цветов для светофора 1
    if time.time() + ph_1 - counter_tl_1 < tl_1:
        tl_1_color = 'red'
    elif time.time() + ph_1 - counter_tl_1 < 2 * tl_1:
        tl_1_color = 'yellow'
    elif time.time() + ph_1 - counter_tl_1 < 3 * tl_1:
        tl_1_color = 'green'
    else:
        counter_tl_1 = time.time()

    # Задаём установку цветов для светофора 2
    if time.time() + ph_2 - counter_tl_2 < tl_2:
        tl_2_color = 'red'
    elif time.time() + ph_2 - counter_tl_2 < 2 * tl_2:
        tl_2_color = 'yellow'
    elif time.time() + ph_2 - counter_tl_2 < 3 * tl_2:
        tl_2_color = 'green'
    else:
        counter_tl_2 = time.time()

    # Задаём установку цветов для светофора 3
    if time.time() + ph_3 - counter_tl_3 < tl_3:
        tl_3_color = 'red'
    elif time.time() + ph_3 - counter_tl_3 < 2 * tl_3:
        tl_3_color = 'yellow'
    elif time.time() + ph_3 - counter_tl_3 < 3 * tl_3:
        tl_3_color = 'green'
    else:
        counter_tl_3 = time.time()

    try:
        bts += stream.read(CAMERA_BUFFRER_SIZE)
        jpghead = bts.find(b'\xff\xd8')
        jpgend = bts.find(b'\xff\xd9')
        if jpghead > -1 and jpgend > -1:
            jpg = bts[jpghead:jpgend + 2]
            bts = bts[jpgend + 2:]
            img = cv.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv.IMREAD_UNCHANGED)
            # img=cv.flip(img,0) #>0:#Поворот по вертикали, 0:Поворот по горизонтали, <0:Отразить по вертикали и по горизонтали
            # h, w = img.shape[:2]
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
                if data == id_tl_1:
                    #После обновления python до 3.10 можно будет использовать инструкцию match-case
                    #Example
                    # http_code = "418"
                    #
                    # match http_code:
                    #     case "200":
                    #         print("OK")
                    #         do_something_good()
                    #     case "404":
                    #         print("Not Found")
                    #         do_something_bad()
                    #     case "418":
                    #         print("I'm a teapot")
                    #         make_coffee()
                    #     case _:
                    #         print("Code not found")
                    print('tl_1_color', tl_1_color)
                    if tl_1_color == 'red':
                        #Display traffic light BGR color scheme
                        #cv.ellipse(img, (320, 265), (131, 131), 0, -90, val, (255, 180, 0), 27)
                        #cv2.circle(image, center_coordinates, radius, color, thickness)
                        cv.circle(img, (600, 30), 20, (0, 00, 255), -1)#Read
                    elif tl_1_color == 'yellow':
                        cv.circle(img, (600, 75), 20, (0, 255, 255), -1)  # Yellow
                    elif tl_1_color == 'green':
                        cv.circle(img, (600, 120), 20, (0, 255, 0), -1)  # Green
                if data == id_tl_2:
                    print('tl_2_color', tl_2_color)
                    if tl_2_color == 'red':
                         cv.circle(img, (600, 30), 20, (0, 00, 255), -1)  # Read
                    elif tl_2_color == 'yellow':
                        cv.circle(img, (600, 75), 20, (0, 255, 255), -1)  # Yellow
                    elif tl_2_color == 'green':
                        cv.circle(img, (600, 120), 20, (0, 255, 0), -1)  # Green
                if data == id_tl_3:
                    print('tl_3_color', tl_3_color)
                    if tl_3_color == 'red':
                        cv.circle(img, (600, 30), 20, (0, 00, 255), -1)  # Read
                    elif tl_3_color == 'yellow':
                        cv.circle(img, (600, 75), 20, (0, 255, 255), -1)  # Yellow
                    elif tl_3_color == 'green':
                        cv.circle(img, (600, 120), 20, (0, 255, 0), -1)  # Green

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