from datetime import datetime

FILE = "operations.json"


# Операции разделены пустой строкой
def load_operation(FILE):
    """
    Последние 5 выполненных (EXECUTED) операций выведены на экран
    """
    with open(FILE, "r", encoding="utf-8") as file:
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


# Операции разделены пустой строкой
def change_date(data):
    """
    Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)
    """
    newdate = datetime.fromisoformat(data)
    return newdate.strftime("%d.%m.%Y")


# Операции разделены пустой строкой
def change_cardnumber(cardnumber=""):
    """
    Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX
    """
    new = cardnumber.split(" ")
    new_number = new[-1][:4] + " " + new[-1][4:6] + "**" + " " + "****" + " " + new[-1][-4:]
    new[-1] = new_number
    return " ".join(new)


def change_accnumber(accnumber):
    """
    Номер счета замаскирован и не отображается целиком в формате  **XXXX
    """
    account = accnumber.split(" ")
    new_account = "**" + account[-1][-4:]
    account[-1] = new_account
    return " ".join(account)


# Операции разделены пустой строкой
# print(change_number("Maestro 1234567890123456"))
# print(change_number("Счет 1234567890123456"))

print(load_operation(FILE))
