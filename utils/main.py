from utils import load_operation, change_date, change_cardnumber, change_accnumber

FILE = "operations.json"
#Операции разделены пустой строкой
def main():
    """
    Последние 5 выполненных (EXECUTED) операций выведены на экран
    """
    operations = load_operation(FILE)
    for operation in operations:
        operation["date"] = change_date(operation["date"])
        try:
            if "Счет" in operation["from"]:
                operation["from"] = change_accnumber(operation["from"])
            else:
                operation["from"] = change_cardnumber(operation["from"])
        except LookupError:
            operation["from"] = "Номер счета:"

        if "Счет" in operation["to"]:
            operation["to"] = change_accnumber(operation["to"])
        else:
            operation["to"] = change_cardnumber(operation["to"])
        print(operation["date"] + " " + operation["description"])
        print(operation["from"] + "->" + operation["to"])
        print(operation["operationAmount"]["amount"] + " " + operation["operationAmount"]["currency"]["name"], end="\n\n")

if __name__ == "__main__":
    main()
#    data = main()
#    for item in data:
#        print(item)