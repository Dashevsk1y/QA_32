# 1
# print("5, \' 'd', k")
# print(min(3, 5, 6, 7, 9, 0, 1, 8))
while True:
    user_input = input("Enter a number: ")

    if user_input.isdigit():  # Проверяем, является ли введенное значение числом
        if user_input == "1":
            print("You win!")
        elif user_input == "5":
            print("You lose(")
            break
        else:
            print("Try again")
    else:
        print("Please enter a valid number.")



