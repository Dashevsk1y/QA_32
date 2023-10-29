class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def setDay(self, d):
        self.day = d

    def getDay(self):
        return self.day

    def setMonth(self, m):
        self.month = m

    def getMonth(self):
        return self.month

    def setYear(self, y):
        self.year = y

    def getYear(self):
        return self.year

    def __str__(self):
        return "'" + str(self.day) + '.' + str(self.month) + '.' + str(self.year) + "'"


class Human:
    def __init__(self, day, month, year):
        self.name = ''
        self.by_name = ''
        self.surname = ''
        self.birth_date = Date(day, month, year)
        self.contact_phone = '+38...'
        self.country = ''
        self.city = ''
        self.address_street = ''
        self.address_house = ''
        self.address_apartment = ''

    def set_name(self, name):
        self.name = name

    def set_by_name(self, by_name):
        self.by_name = by_name

    def set_surname(self, surname):
        self.surname = surname

    def set_birth_date(self, day, month, year):
        self.birth_date.setDay(day)
        self.birth_date.setMonth(month)
        self.birth_date.setYear(year)

    def set_contact_phone(self, contact_phone):
        self.contact_phone = contact_phone

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_address_street(self, street):
        self.address_street = street

    def set_address_house(self, house):
        self.address_house = house

    def set_address_apartment(self, apartment):
        self.address_apartment = apartment

    def get_name(self):
        return self.name

    def get_by_name(self):
        return self.by_name

    def get_surname(self):
        return self.surname

    def get_contact_phone(self):
        return self.contact_phone

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_address_street(self):
        return self.address_street

    def get_address_house(self):
        return self.address_house

    def get_address_apartment(self):
        return self.address_apartment

    def show_data(self):
        print('Прізвище, імя, по-батькові:' + self.name + ' ' + self.by_name + ' ' + self.surname)
        print('Дата народження:', self.birth_date)
        print('Контактний телефон:', self.contact_phone)
        print('Країна:', self.country)
        print('Місто:', self.city)
        print('Домашня адреса: вул. ' + self.address_street + ', д. ' + self.address_house + ', кв. ' + self.address_apartment)

    def input_data_of_person(self):
        print('Вводимо повную інформацію про персону:')
        name = input('Введіть імя: ')
        self.set_name(name)
        by_name = input('Введіть по-батькові: ')
        self.set_by_name(by_name)
        surname = input('Введіть прізвище: ')
        self.set_surname(surname)
        birth_date_day = input('Введіть дату дня народження: ')
        birth_date_month = input('Введіть місяць народження: ')
        birth_date_year = input('Введіть рік народження: ')
        self.set_birth_date(birth_date_day, birth_date_month, birth_date_year)
        contact_phone = input('Введіть номер телефона у форматі +38...: ')
        self.set_contact_phone(contact_phone)
        country = input('Введіть страну: ')
        self.set_country(country)
        city = input('Введіть місто: ')
        self.set_city(city)
        address_street = input('Введіть назву вулиці: ')
        self.set_address_street(address_street)
        address_house = input('Введіть номер будинку: ')
        self.set_address_house(address_house)
        address_apartment = input('Введіть номер квартири: ')
        self.set_address_apartment(address_apartment)

person1 = Human(0, 0, 0)  # Изначально задаем дату рождения с нулевыми значениями
person1.input_data_of_person()
person1.show_data()
