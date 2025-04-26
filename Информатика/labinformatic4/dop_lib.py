# json -> xml библиотека
# Импортируем библиотеку,которая содежит функции для преобразования из формата json в xml
from json2xml import json2xml
# Импортируем функцию для чтения файла-json
from json2xml.utils import readfromjson
# Читаем файл и записываем его в переменную
json_file  = readfromjson('schedule.json')
# Открываем файл для записи данных
with open('schedule_lib.xml', 'w', encoding='utf-8') as xml_file:
    # Создается объект, к которому применяется метод ковертации
    xml_file.write(json2xml.Json2xml(json_file, attr_type=False).to_xml())
