import json
from datetime import datetime
#Операции разделены пустой строкой
def load_5operation(FILE):
    """
    Последние 5 выполненных (EXECUTED) операций выведены на экран
    """
    with open(FILE, "r", encoding="utf -8") as file:
        result = json.load(file)
        result_executed = []
        for operation in result:
            try:
                if operation["state"] == "EXECUTED":
                    result_executed.append(operation)
            except LookupError:
                result_error = "Операция не выполнена"
        sorted_operations = sorted(result_executed, key=lambda x: x["date"], reverse=True)
        last_operations = sorted_operations[:5]
        return last_operations
#Операции разделены пустой строкой
def change_date(data):
    """
    Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)
    """
    thedate = datetime.fromisoformat(data)
    date_formatted = thedate.strftime("%d.%m.%Y")
    return date_formatted
#Операции разделены пустой строкой
def change_number(str_):
    """
    Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX
    """
    str_list = str_.split(' ')
    number = str_list[-1]
    if len(str_list) > 2 :
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
    else:
        if str_list[0] == 'Счет':
            return '**' + number[-4:]
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
#Операции разделены пустой строкой
#print(change_number("Maestro 1234567890123456"))
#print(change_number("Счет 1234567890123456"))