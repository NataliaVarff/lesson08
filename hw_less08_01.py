# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import date

class Data:
    date = str

    def __init__(self, date):
        self.date = date.split("-")

    @classmethod
    def method_1(cls, date):
        try:
             day, month, year = [int(i) for i in date.split("-")]
             return f"{type(day), day}, {type(month), month}, {type(year), year}"
        except ValueError:
            return f"Неверный формат даты!"

    @staticmethod
    def valid(date):
        try:
            day, month, year = date.split("-")
            date(int(year), int(month), int(day))
            return f"Ok.date"
        except ValueError:
            return f"Ошибка даты!"

Data.method_1("05-01-2022")
print(Data.method_1("05-01-2022"))
Data.valid("05-01-")
print(Data.valid("05-01-"))

