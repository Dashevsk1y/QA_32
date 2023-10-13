# Задание 1
class Human:
    def __init__(self):
        self.full_name = ""
        self.birthdate = ""
        self.contact_phone = ""
        self.city = ""
        self.country = ""
        self.home_address = ""

    def input_data(self):
        self.full_name = input("Enter full name: ")
        self.birthdate = input("Enter date of birth: ")
        self.contact_phone = input("Enter contact phone: ")
        self.city = input("Enter city: ")
        self.country = input("Enter country: ")
        self.home_address = input("Enter home address: ")

    def display_data(self):
        print("Full Name:", self.full_name)
        print("Date of Birth:", self.birthdate)
        print("Contact Phone:", self.contact_phone)
        print("City:", self.city)
        print("Country:", self.country)
        print("Home Address:", self.home_address)

    def get_full_name(self):
        return self.full_name

    def get_birthdate(self):
        return self.birthdate

    def get_contact_phone(self):
        return self.contact_phone

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_home_address(self):
        return self.home_address

    def set_full_name(self, new_name):
        self.full_name = new_name

    def set_birthdate(self, new_birthdate):
        self.birthdate = new_birthdate

    def set_contact_phone(self, new_phone):
        self.contact_phone = new_phone

    def set_city(self, new_city):
        self.city = new_city

    def set_country(self, new_country):
        self.country = new_country

    def set_home_address(self, new_address):
        self.home_address = new_address



person1 = Human()
person1.input_data()

print("\nEnter date:")
person1.display_data()

new_name = input("\nEnter new full name: ")
person1.set_full_name(new_name)

print("\nChange date:")
person1.display_data()

# Задание 2