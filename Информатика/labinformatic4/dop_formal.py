import re

XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n' # статическая переменная
STANDARD_SPACE_LEN = 4 # cтатическая переменная
LEVEL_OF_NESTING_PROCESSING = 1 #статическая переменная

# Функция, для замены с помощью РВ (использование регулярных выражений)
def replace_boolean(object):
    object = re.sub(r'\btrue\b', 'True', object)
    object = re.sub(r'\bfalse\b', 'False', object)
    object = re.sub(r'\bnull\b', 'None', object)
    return object

def structure_xml(object, tag, level_nesting=0):
    indent = " " * STANDARD_SPACE_LEN * level_nesting
    xml_text = ""

    if isinstance(object, dict):
        xml_text += f"{indent}<{tag}>\n"
        for key, value in object.items():
            xml_text += structure_xml(value, key, level_nesting + LEVEL_OF_NESTING_PROCESSING)
        xml_text += f"{indent}</{tag}>\n"
    elif isinstance(object, list):
        for i in object:
            xml_text += structure_xml(i, tag, level_nesting)
    else:
        xml_text += f"{indent}<{tag}>{object}</{tag}>\n"
    return xml_text

# Основная функция
def json_to_xml(json_text):
    json_text = replace_boolean(json_text)  # Использование РВ
    json_text = eval(json_text)
    xml_data = XML_HEADER
    xml_data += structure_xml(json_text, "timetable_1_semester")
    return xml_data


# Открытие файла JSON и запись результата в XML
with open("test.json", "r", encoding="utf-8") as file:
    json_text = file.read()

xml_result = json_to_xml(json_text)

with open("test.xml", "w", encoding="utf-8") as xml_file:
    xml_file.write(xml_result)