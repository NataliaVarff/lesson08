#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class NotNumError(Exception):
    def __init__(self, txt):
        self.txt = txt

new_input = ""   # input("Введите любые данные: - число или строку. Для остановки наберите stop: ")
alist = []

while new_input != "stop":
    try:
        new_input = input("Введите любые данные: - число или строку. Для остановки наберите stop: ")
        if new_input.isdigit():
            alist.append(new_input)
        if not new_input.isdigit():
            raise NotNumError(f"введено не число {new_input}")
        else:
            None
    except NotNumError as nn:
        print(f"{nn}")

print(alist)

