# задача 1

def stiv_quote():
    quote = """\
    "Don't let the noise of others' opinions
     drown out your own inner voice."
                               - Steve Jobs"""
    print(quote)

stiv_quote()

# Задача 2

def numbers():
    start = int(input("Введите первое число: "))
    end = int(input("Введите второе число: "))
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number)
numbers()

# Задача 4
def find_max_of_four():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))
    num4 = float(input("Введите четвертое число: "))

    max_number = max(num1, num2, num3, num4)
    return max_number
result = find_max_of_four()
print("Максимальное число:", result)

    