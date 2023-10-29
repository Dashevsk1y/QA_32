import os

class Student:
    def __init__(self, first_name, last_name, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.average_grade = average_grade

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Середній бал: {self.average_grade}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, last_name):
        self.students = [s for s in self.students if s.last_name != last_name]

    def update_student(self, last_name, new_average_grade):
        for student in self.students:
            if student.last_name == last_name:
                student.average_grade = new_average_grade

    def get_all_students(self):
        return self.students

    def get_students_by_name(self, last_name):
        return [s for s in self.students if s.last_name == last_name]

    def sort_students_by_name(self):
        return sorted(self.students, key=lambda s: s.last_name)

    def get_excellent_students(self):
        return [s for s in self.students if s.average_grade >= 10]

    def save_students_to_file(self):
        with open("students.txt", "w") as file:
            for student in self.students:
                file.write(f"{student.first_name},{student.last_name},{student.average_grade}\n")

    def load_students_from_file(self):
        try:
            with open("students.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    if len(data) == 3:
                        first_name, last_name, average_grade = data
                        student = Student(first_name, last_name, float(average_grade))
                        self.students.append(student)
        except FileNotFoundError:
            print("Файл не знайдено. Почніть з створення файлу.")

def create_new_file():
    if os.path.isfile("students.txt"):
        print("Файл вже існує.")
        choice = input("Відкрити файл (так/ні)? ").strip().lower()
        if choice == "так" or choice == "yes":
            student_manager = open_existing_file()
            return student_manager
        else:
            return None
    else:
        open("students.txt", "w")
        print("Файл створено.")
        return StudentManager()

def open_existing_file():
    if os.path.isfile("students.txt"):
        student_manager = StudentManager()
        student_manager.load_students_from_file()
        return student_manager
    else:
        print("Файл не знайдено. Почніть з створення файлу.")
        return None

def main_menu(student_manager):
    while True:
        print("\n1. Додати студента")
        print("2. Видалити студента")
        print("3. Змінити інформацію про студента")
        print("4. Показати на екрані ВСІХ студентів")
        print("5. Вивести на екран інформацію про студента за прізвищем")
        print("6. Вивести студентів в алфавітному порядку за прізвищем")
        print("7. Вивести 'відмінників' (з середнім балом 10+)")
        print("8. Завершити роботу")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            first_name = input("Ім'я студента: ")
            last_name = input("Прізвище студента: ")
            average_grade = float(input("Середній бал: "))
            student_manager.add_student(Student(first_name, last_name, average_grade))
        elif choice == "2":
            last_name = input("Введіть прізвище студента для видалення: ")
            student_manager.remove_student(last_name)
        elif choice == "3":
            last_name = input("Введіть прізвище студента для зміни середнього балу: ")
            new_average_grade = float(input("Новий середній бал: "))
            student_manager.update_student(last_name, new_average_grade)
        elif choice == "4":
            print("Всі студенти:")
            for student in student_manager.get_all_students():
                print(student)
        elif choice == "5":
            last_name = input("Введіть прізвище для пошуку: ")
            students_found = student_manager.get_students_by_name(last_name)
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
            if student_manager is not None:
                student_manager.save_students_to_file()
            return False

student_manager = None

while True:
    choice = main_menu(student_manager)

    if choice == "1":
        if student_manager is None:
            student_manager = create_new_file()
    elif choice == "2":
        if student_manager is None:
            student_manager = open_existing_file()
    elif choice == "8":
        if student_manager is not None:
            student_manager.save_students_to_file()
        break
    else:
        if student_manager is not None:
            student_manager.save_students_to_file()
        print("Завершення роботи.")
        break

print("Програма завершена.")
