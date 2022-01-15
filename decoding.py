import cv2

#pip install numpy

# inputImage = cv2.imread("../Resources/R4S_QR7.jpg")
inputImage = cv2.imread('/Users/alex/Documents/Python_projects/car_CV/receipts/1.jpg')

#  Создание функции выводящей в отдельном окне изображение QR с синим обрамлением.
def display(im, bbox):
    n = len(bbox)

    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[(j + 1) % n][0]), (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im)

qrDecoder = cv2.QRCodeDetector() # создание объекта детектора

data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)

if bbox is not None:

    print("Decoded Data : {}".format(data)) # вывод декодированной строки

    display(inputImage, bbox)

    #rectifiedImage = np.uint8(rectifiedImage);

    #cv2.imshow("Rectified QRCode", rectifiedImage);

else:

    print("QR Code not detected")

    cv2.imshow("Results", inputImage)



cv2.waitKey(0)

cv2.destroyAllWindows()
