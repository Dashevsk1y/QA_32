import os

# Определите путь к файлу
file_path = os.path.join(os.path.dirname(__file__), "students.txt")

class Student:
    def __init__(self, first_name, last_name, student_id, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.average_grade = average_grade

    def __str__(self):
        return f"ID: {self.student_id}, {self.first_name} {self.last_name}, Середній бал: {self.average_grade}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def update_student(self, student_id, new_average_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.average_grade = new_average_grade

    def get_students(self):
        return self.students

    def get_student_by_name(self, last_name):
        return [s for s in self.students if s.last_name == last_name]

    def sort_students_by_name(self):
        return sorted(self.students, key=lambda s: s.last_name)

    def get_excellent_students(self):
        return [s for s in self.students if s.average_grade >= 10]

    def load_students_from_file(self):
        try:
            with open("students.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        first_name, last_name, student_id, average_grade = data
                        student = Student(first_name, last_name, int(student_id), float(average_grade))
                        self.students.append(student)
        except FileNotFoundError:
            print("Файл не знайдено. Почніть з створення файлу.")

    def save_students_to_file(self):
        with open("students.txt", "w") as file:
            for student in self.students:
                file.write(f"{student.first_name},{student.last_name},{student.student_id},{student.average_grade}\n")

def create_new_file():
    if os.path.isfile("students.txt"):
        print("Файл вже існує.")
        choice = input("Відкрити файл (так/ні)? ").strip().lower()
        if choice == "так" or choice == "yes":
            return True
        else:
            return False
    else:
        open("students.txt", "w")
        return True

def open_existing_file():
    if os.path.isfile("students.txt"):
        student_manager = StudentManager()
        student_manager.load_students_from_file()
        return student_manager
    else:
        print("Файл не знайдено. Почніть з створення файлу.")
        return None

def delete_file():
    if os.path.isfile("students.txt"):
        os.remove("students.txt")
        print("Файл видалено.")

def main_menu():
    print("1. Створити файл")
    print("2. Відкрити файл")
    choice = input("Оберіть опцію: ")
    return choice

student_manager = None

while True:
    choice = main_menu()

    if choice == "1":
        if create_new_file():
            student_manager = StudentManager()
    elif choice == "2":
        student_manager = open_existing_file()
    else:
        print("Невірний вибір. Завершення роботи.")
        break

    while student_manager is not None:
        print("\n1. Додати студента")
        print("2. Видалити студента")
        print("3. Змінити інформацію про студента")
        print("4. Показати на екрані ВСІХ студентів")
        print("5. Вивести на екран інформацію про студента за прізвищем")
        print("6. Вивести студентів в певному порядку (за алфавітом)")
        print("7. Вивести 'відмінників'")
        print("8. Вивести абсолютний шлях до файлу")
        print("9. Видалити файл і завершити роботу")
        print("10. Завершити роботу")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            first_name = input("Ім'я студента: ")
            last_name = input("Прізвище студента: ")
            id = int(input("ID студента: "))
            average_grade = float(input("Середній бал: "))
            student_manager.add_student(Student(first_name, last_name, id, average_grade))
        
        elif choice == "2":
            student_id = int(input("ID студента для видалення: "))
            student_manager.remove_student(student_id)
        
        elif choice == "3":
            student_id = int(input("ID студента для зміни середнього балу: "))
            new_average_grade = float(input("Новий середній бал: "))
            student_manager.update_student(student_id, new_average_grade)
        
        elif choice == "4":
            print("Всі студенти:")
            for student in student_manager.get_students():
                print(student)
        
        elif choice == "5":
            last_name = input("Введіть прізвище для пошуку: ")
            students_found = student_manager.get_student_by_name(last_name)
            if students_found:
                print(f"Результати пошуку за прізвищем '{last_name}':")
                for student in students_found:
                    print(student)
            else:
                print(f"Студентів з прізвищем '{last_name}' не знайдено.")
        
        elif choice == "6":
            students_sorted = student_manager.sort_students_by_name()
            print("Студенти, відсортовані за алфавітом:")
            for student in students_sorted:
                print(student)


        elif choice == "7":
            excellent_students = student_manager.get_excellent_students()
            print("Відмінники:")
            for student in excellent_students:
                print(student)

        elif choice == "8":
            print("Абсолютний шлях до файлу:", os.path.abspath("students.txt"))

        elif choice == "9":
            if student_manager is not None:
                student_manager.save_students_to_file()
            delete_file()
            print("Завершення роботи.")
            student_manager = None  # Устанавливаем student_manager в None, чтобы завершить внутренний цикл
            break
        
        
        elif choice == "10":  # Новый пункт
            if student_manager is not None:
                student_manager.save_students_to_file()
            print("Завершення роботи.")
            break
        else:
            print("Невірний вибір. Завершення роботи.")
            student_manager = None  # Устанавливаем student_manager в None, чтобы завершить внутренний цикл

print("Программа завершена.")