import os.path
import re
import time
from send2trash import send2trash

start_time = time.time()

dirname = 'D:\iCloudphoto'  # директория с импортированными файлами
files = os.listdir(dirname)

for file in files:
    cropname1 = re.sub(r'MOV', "", file)
    cropname = re.sub(r'JPG', "", cropname1)
    if os.path.exists(f'{dirname}\\{cropname}JPG') and os.path.exists(f'{dirname}\\{cropname}MOV'):
        send2trash(f'{dirname}\\{cropname}MOV')
        # print(f'D:\iCloudPhoto_Test\{cropname}JPG')

print(f"Видеодубликаты успешно перемещены в корзину за {time.time() - start_time} секунд")
