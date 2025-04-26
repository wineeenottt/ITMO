
import re

XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n' # статическая переменная
STANDARD_SPACE_LEN = 4 # cтатическая переменная
LEVEL_OF_NESTING_PROCESSING = 1 #статическая переменная

def structure_xml(object, tag, level_nesting=0):
    indent = " " * STANDARD_SPACE_LEN * level_nesting
    xml_text = ""

    if isinstance(object, dict):
        xml_text += f"{indent}<{tag}>\n"
        for key, value in object.items():
            xml_text += structure_xml(value, key, level_nesting + LEVEL_OF_NESTING_PROCESSING)
        xml_text += f"{indent}</{tag}>\n"
    elif isinstance(object, list):
        xml_text += f"{indent}<{tag}>\n"
        for i in object:
            xml_text += structure_xml(i, "element", level_nesting + LEVEL_OF_NESTING_PROCESSING)
        xml_text += f"{indent}</{tag}>\n"
    else:
        xml_text += f"{indent}<{tag}>{object}</{tag}>\n"
    return xml_text

# Основная функция
def json_to_xml(json_text):
    json_text = json_text.replace('true','True') # Использование РВ
    json_text = eval(json_text)
    xml_data = XML_HEADER
    xml_data += structure_xml(json_text, "timetable_1_semester")
    return xml_data


# Открытие файла JSON и запись результата в XML
with open("schedule.json", "r", encoding="utf-8") as file:
    json_text = file.read()

xml_result = json_to_xml(json_text)

with open("schedule.xml", "w", encoding="utf-8") as xml_file:
    xml_file.write(xml_result)