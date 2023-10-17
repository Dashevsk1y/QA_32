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
b = Number(3)

sum = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print("Сума:", sum)
print("Різниця:", subtraction)
print("Множення:", multiplication)
print("Ділення:", division)