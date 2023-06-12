from utils.utils import change_date, change_number, load_5operation

FILE = "utils/operations.json"
#Операции разделены пустой строкой
def test_change_date():
    assert change_date("2019-08-16T04:23:41.621065") == "16.08.2019"
    assert change_date("2018-07-06T22:32:10.495465") == "06.07.2018"
    assert change_date("2018-02-13T04:43:11.374324") == "13.02.2018"
    assert change_date("2018-01-23") == "23.01.2018"
#Операции разделены пустой строкой
def test_change_number():
    assert change_number("Счет 72645194281643232984") == "Счет **2984"
    assert change_number("Счет 95782287258966264115") == "Счет **4115"
    assert change_number("Счет 11492155674319392427") == "Счет **2427"
    assert change_number("Счет 59986621134048778289") == "Счет **8289"
#Операции разделены пустой строкой
def test_change_number():
    assert change_number("МИР 1582474475547301") == "МИР 1582 24** **** 7301"
    assert change_number("Maestro 1913883747791351") == "Maestro 1913 88** **** 1351"
    assert change_number("MasterCard 8826230888662405") == "MasterCard 8826 23** **** 2405"
    assert change_number("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"
#Операции разделены пустой строкой
def test_load_5operation():
    file_list = [
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
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961"
        }
    ]
    assert load_5operation(FILE) == file_list