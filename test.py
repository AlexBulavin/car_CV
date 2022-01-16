import numpy as np
import cv2

#Example 1
# cap = cv2.VideoCapture('http://192.168.1.109/')
#
# while(cap.isOpened()):
#     ret, image = cap.read()
#     loadedImage = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     cv2.imshow('frame', loadedImage)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# #Example 2
# # Open a sample video available in sample-videos
# vcap = cv2.VideoCapture('http://192.168.1.109/')
# if not vcap.isOpened():
#    print("File Cannot be Opened")
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = vcap.read()
#     #print cap.isOpened(), ret
#     if frame is not None:
#         # Display the resulting frame
#         cv2.imshow('frame',frame)
#         # Press q to close the video windows before it ends if you want
#         if cv2.waitKey(22) & 0xFF == ord('q'):
#             break
#     else:
#         print("Frame is None")
#         break
#
# # When everything done, release the capture
# vcap.release()
# cv2.destroyAllWindows()
# print ("Video stop")

#Example 3
cap = cv2.VideoCapture(0);               # Видео вывод с веб камеры компьютера, при включенной камере
#cap = cv2.VideoCapture("VIDEO0102.mp4"); # Вывод с видео файла

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Вывод в консоли размера нашего окна.

cap.set(3,1280) # Установление длины окна
cap.set(4,700)  # Ширина окна

print(cap.get(3))
print(cap.get(4))

while (True):
    ret, frame = cap.read()
    frame = cv2.rectangle(frame, (384, 0), (510, 128), (0, 0, 255), 2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Перевод массива кадров в черно-белую градацию
    gray = cv2.GaussianBlur(gray, (7, 7), 1.5)  # Параметры позволяют регулировать шумность

    edges = cv2.Canny(gray, 1, 50)  # Нахождение контуров
    cv2.imshow("edges", edges)  # обработанный вариант

    print(frame)

    cv2.imshow("frame", frame)  # оригинальный вариант

cap.release()
cv2.destroyAllWindows()