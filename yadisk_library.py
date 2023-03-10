import yadisk
from pprint import pprint
TOKEN = input(str("Введите токен: "))
y = yadisk.YaDisk(token=TOKEN)
if y.check_token():
    if not y.is_dir("/Нетология"):
        y.mkdir("/Нетология")
        print('Папка "Нетология" создана')
if y.upload('test_upload.txt', '/Нетология/test_upload.txt'):
    pprint('Файл успешно загружен')
else:
    print("Ошибка")