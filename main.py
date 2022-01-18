import os
# pip install pyzbar qrcode opencv-python glob
import qrcode #Нужно установить библиотеку qrcode
#Также python3 -m pip install --upgrade Pillow

# os.scandir() и pathlib.Path() #Чтобы получить список всех файлов и папок в определенном каталоге
# Подробнее https://www.python.org/dev/peps/pep-0471/
#Пример кода взят отсюда: https://chel-center.ru/python-yfc/2021/10/24/rabota-s-fajlami-v-python/

from pathlib import Path
from PIL import Image #pip install pillow

entries = Path('/Users/alex/Documents/Python_projects/car_CV')
for entry in entries.iterdir():#iterdir() - итератор для получения списка всех файлов и каталогов в my_directory.
    print(entry.name)

#Объекты, возвращаемые Path, являются объектами PosixPath или WindowsPath в зависимости от ОС.

# List all files in a directory using scandir()
basepath = '/Users/alex/Documents/Python_projects/car_CV'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

# Вывести список всех подкаталогов с помощью scandir()
basepath = '/Users/alex/Documents/Python_projects/car_CV'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)

#Создание директории
p = Path('/Users/alex/Documents/Python_projects/car_CV/Resources')

#Для нескольких каталогов: p = Path('2018/10/05')

try:
    p.mkdir(parents=True)
    #С заданием прав p.mkdir(parents=True)
    # #https://docs.python.org/3/library/os.html#os.makedirs

except FileExistsError as exc:
    print(exc)


# Создаём собственный QR code с логотипом:
logo = Image.open('/Users/alex/Documents/Python_projects/car_CV/Resources/r4s_logo_tablet.png')
qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_Q
)
#Параметр version может быть от 1 до 40, от 21х21 до 177х177 пикселей, не учитывая поля.

#Параметр box_size отвечает за количество пикселей в каждом квадрате QR-кода.

#Параметр border создает границу вокруг QR-кода.

#Параметр Error_correction служит для восстановления кода, если код повредился и плохо читаем.

#Каждый уровень указывает на процент данных для восстановления.
#ERROR_CORRECT_L = 7%
#ERROR_CORRECT_M = 15%
#ERROR_CORRECT_Q = 25%
#ERROR_CORRECT_H = 30%

qr_data = "Traffic light 11"

qr.add_data(f"QRCode for: {qr_data}")
img = qr.make_image(back_color=(47, 48, 70), fill_color=(255, 255, 255)).convert('RGB') #Задаём параметры для файла и конвертируем в RGB чтобы логотип был цветным
img1 = qr.make_image()
pos = (
    (img.size[0] - logo.size[0]) // 2,
    (img.size[1] - logo.size[1]) // 2,
)
# img.paste(logo, pos)
img1.save(f'Resources/{qr_data}.jpg', 'JPEG') #Указываем папку в которую нужно сохранить файл

