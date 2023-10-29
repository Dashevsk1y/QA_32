import os
import re

def read_students():
    students = []
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            for line in file:
                student_data = line.strip().split(',')
                students.append(student_data)
    return students

def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(','.join(student) + '\n')

def is_valid_name(name):
    return re.match(r"^[A-Za-zА-Яа-яЁё]+$", name)

def is_valid_grade(grade):
    return re.match(r"^(10|11|12|[0-9](\.\d{1,2})?)$", grade)

def add_student(students):
    print()
    last_name = input("Прізвище студента: ")
    while not is_valid_name(last_name):
        print("Неправильний ввід. Прізвище повинно містити лише букви.")
        last_name = input("Прізвище студента: ")

    first_name = input("Ім'я студента: ")
    while not is_valid_name(first_name):
        print("Неправильний ввід. Ім'я повинно містити лише букви.")
        first_name = input("Ім'я студента: ")

    while True:
        average_grade = input("Середній бал (0-12): ")
        if is_valid_grade(average_grade):
            break
        else:
            print("Неправильний ввід. Бал повинен бути числом в межах від 0 до 12.")
    student_id = str(len(students) + 1)
    student_data = [student_id, last_name, first_name, average_grade]
    students.append(student_data)
    save_students(students)
    print("\nСтудента додано. ID студента:", student_id)

def remove_student(students):
    last_name = input("Введіть прізвище студента, якого бажаєте видалити: ")
    found = False
    for student in students:
        if student[1] == last_name:
            students.remove(student)
            save_students(students)
            found = True
            print("Студента видалено.")
            break
    if not found:
        print("Студента з прізвищем", last_name, "не знайдено.")

def change_student_info(students):
    last_name = input("Введіть прізвище студента, інформацію про якого ви бажаєте змінити: ")
    found = False
    for student in students:
        if student[1] == last_name:
            first_name = input("Нове ім'я студента: ")
            average_grade = input("Новий середній бал: ")
            student[2] = first_name
            student[3] = average_grade
            save_students(students)
            found = True
            print("Інформацію про студента оновлено.")
            break
    if not found:
        print("Студента з прізвищем", last_name, "не знайдено.")

def show_all_students(students):
    if len(students) > 0:
        print("Список студентів:")
        print(f"{'ID':<5}{'Прізвище':<15}{'Ім''я':<15}{'Середній бал':<5}")
        for student in students:
            print(f"{student[0]:<5}{student[1]:<15}{student[2]:<15}{student[3]:<5}")
        print()
    else:
        print("Немає жодного студента в базі даних.")

def search_student(students):
    search_parameter = input("Введіть параметр пошуку (прізвище, ім'я тощо): ")
    found = False
    for student in students:
        if search_parameter in student[1] or search_parameter in student[2]:
            print(f"ID: {student[0]}, Прізвище: {student[1]}, Ім'я: {student[2]}, Середній бал: {student[3]}")
            found = True
    if not found:
        print("Співпадінь не знайдено.")

def sort_students(students):
    sort_parameter = input("Введіть параметр сортування (прізвище, бал тощо): ")
    if sort_parameter == 'прізвище':
        students.sort(key=lambda student: student[1])
    elif sort_parameter == 'бал':
        students.sort(key=lambda student: float(student[3]), reverse=True)
    else:
        print("Неправильний параметр сортування.")
        return

    show_all_students(students)

def excellent_students(students):
    excellent = [student for student in students if float(student[3]) >= 10]
    if len(excellent) > 0:
        print("Список 'відмінників':")
        show_all_students(excellent)
    else:
        print("Відмінники відсутні.")

def is_excellent(average_grade):
    try:
        grade = float(average_grade)
        return grade >= 10
    except ValueError:
        return False

def validate_choice(options):
    while True:
        choice = input(f"Оберіть дію ({', '.join(options)}): ")
        if choice in options:
            return choice
        else:
            print("Неправильний вибір. Будь ласка, оберіть із доступних опцій.")

def exit_program(students):
    while True:
        choice = input("Виберіть, як завершити роботу:\n1. Завершити роботу та зберегти зміни в файлі\n2. Завершити роботу та видалити файл\n")
        if choice == '1':
            save_students(students)
            print("Файл змінено. Вихід з програми.")
            exit(0)
        elif choice == '2':
            if os.path.exists("students.txt"):
                os.remove("students.txt")
                print("Файл видалено. Вихід з програми.")
                exit(0)
            else:
                print("Файл не існує. Вихід з програми.")
                exit(0)
        else:
            print("Неправильний вибір. Будь ласка, оберіть 1 або 2.")

while True:
    print("1. Створити файл")
    print("2. Відкрити файл")
    print("3. Вийти")
    menu_choice = validate_choice(["1", "2", "3"])
    if menu_choice == '1':
        if os.path.exists("students.txt"):
            print("Файл вже існує. Оберіть 'Відкрити файл' або 'Вийти'.")
        else:
            with open("students.txt", "w") as file:
                print("Файл для студентів створено.")
                students = []
                while True:
                    print("1. Додати студента")
                    print("2. Видалити студента")
                    print("3. Змінити інформацію про студента")
                    print("4. Показати на екрані ВСІХ студентів")
                    print("5. Вивести на екран інформацію про студента, виконавши пошук за вказаним параметром")
                    print("6. Вивести студентів в певному порядку")
                    print("7. Вивести 'відмінників'")
                    print("8. Завершити роботу")
                    choice = validate_choice(["1", "2", "3", "4", "5", "6", "7", "8"])
                    if choice == '1':
                        add_student(students)
                    elif choice == '2':
                        remove_student(students)
                    elif choice == '3':
                        change_student_info(students)
                    elif choice == '4':
                        show_all_students(students)
                    elif choice == '5':
                        search_student(students)
                    elif choice == '6':
                        sort_students(students)
                    elif choice == '7':
                        excellent_students(students)
                    elif choice == '8':
                        exit_program(students)
                        break
    elif menu_choice == '2':
        if os.path.exists("students.txt"):
            students = read_students()
            while True:
                print("1. Додати студента")
                print("2. Видалити студента")
                print("3. Змінити інформацію про студента")
                print("4. Показати на екрані ВСІХ студентів")
                print("5. Вивести на екран інформацію про студента, виконавши пошук за вказаним параметром")
                print("6. Вивести студентів в певному порядку")
                print("7. Вивести 'відмінників'")
                print("8. Завершити роботу")
                choice = validate_choice(["1", "2", "3", "4", "5", "6", "7", "8"])
                if choice == '1':
                    add_student(students)
                elif choice == '2':
                    remove_student(students)
                elif choice == '3':
                    change_student_info(students)
                elif choice == '4':
                    show_all_students(students)
                elif choice == '5':
                    search_student(students)
                elif choice == '6':
                    sort_students(students)
                elif choice == '7':
                    excellent_students(students)
                elif choice == '8':
                    exit_program(students)
        else:
            print("Файл не існує. Спершу створіть файл ('Створити файл для студентів').")
    elif menu_choice == '3':
        print("Вихід з програми.")
        break
