# Завдання 1

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            raise ValueError("Непідтриманий операнд")

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        else:
            raise ValueError("Непідтриманий операнд")

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        else:
            raise ValueError("Непідтриманий операнд")

    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                raise ZeroDivisionError("Ділення на нуль заборонено")
            return Number(self.value / other.value)
        else:
            raise ValueError("Непідтриманий операнд")

    def __str__(self):
        return str(self.value)

# Приклад використання:
a = Number(4)
b = Number(2)

сума = a + b
різниця = a - b
продукт = a * b
частка = a / b

print("Сума:", сума)
print("Різниця:", різниця)
print("Множення:", продукт)
print("Ділення:", частка)