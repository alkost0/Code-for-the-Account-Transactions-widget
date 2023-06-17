from utils.utils import change_date, change_cardnumber, change_accnumber, load_operation

FILE = 'operations.json'


# Операции разделены пустой строкой
def test_change_date():
    assert change_date("2019-08-16T04:23:41.621065") == "16.08.2019"
    assert change_date("2018-07-06") == "06.07.2018"
    assert change_date("2018-02-13T04:43:11.374324") == "13.02.2018"
    assert change_date("2018-01-23") == "23.01.2018"


# Операции разделены пустой строкой
def test_change_accnumber():
    assert change_accnumber("Счет 72645194281643232984") == "Счет **2984"
    assert change_accnumber("Счет 95782287258966264115") == "Счет **4115"
    assert change_accnumber("Счет 11492155674319392427") == "Счет **2427"
    assert change_accnumber("Счет 59986621134048778289") == "Счет **8289"


def test_change_cardnumber():
    assert change_cardnumber("МИР 1582474475547301") == "МИР 1582 47** **** 7301"
    assert change_cardnumber("Maestro 1913883747791351") == "Maestro 1913 88** **** 1351"
    assert change_cardnumber("MasterCard 8826230888662405") == "MasterCard 8826 23** **** 2405"
    assert change_cardnumber("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"


# Операции разделены пустой строкой
def test_load_operation():
    file_list = [
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961"
        },
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880"
        },
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873"
        },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412"
        }
    ]
    assert load_operation(FILE) == file_list
