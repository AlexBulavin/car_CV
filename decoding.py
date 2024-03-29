import cv2

# Не забыть установить numpy
# filename = '/Users/alex/Documents/Python_projects/car_CV/receipts/1.jpg'
filename = f'receipts/1.jpg'  # f'Resources/R4S_QR9.jpg'

# read the QRCODE image
img = cv2.imread(filename, 0)  # Параметр 0 переводит имидж в grayscale
img1 = cv2.imread(filename)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox[0])  # Поскольку bbox = [[[float, float]]], необходимо
    # перейти к int и идти по первому элементу массива
    bbox1 = bbox.astype(int)  # Преобразовали координаты к целочисленным
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox1[0, [i][0]])
        point2 = tuple(bbox1[0, [(i + 1) % n_lines][0]])
        cv2.line(img1, point1, point2, color=(255, 0, 0), thickness=2)

    # QR code has 6 variables respectively as:
    # Size of QR code image
    # Top
    # Right
    # Bottom
    # Left
    # Unit

    # display the result
    cv2.imshow("result", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("QR code not detected")
