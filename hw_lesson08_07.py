# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.  Проверьте корректность полученного результата.

# комплексное число – это двумерное число.
# Оно имеет вид a + bi, где a и  b – действительные числа, i – так называемая мнимая единица

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"{self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i"

num1 = ComplexNum(4,5)
num2 = ComplexNum (2,3)
res_add = num1 + num2
res_mul = num1 * num2
print(res_add)
print(res_mul)