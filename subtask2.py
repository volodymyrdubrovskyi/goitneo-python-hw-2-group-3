from collections import UserDict

# обработка ошибки количества символов в номере телефона
class LenPhoneError(Exception):
    pass

# обработка ошибки не нахождения телефона
class PhoneNotFindError(Exception):
    pass

# обработка ошибки не нахождения записи
class RecordNotFindError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    MAX_PHONE_LEN = 10

    def __init__(self, value):
        self.value = value
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # добавление обїекта телефон в запись
    def add_phone(self, phone):
        if len(phone) == Phone.MAX_PHONE_LEN:
            self.phones.append(Phone(phone))
        else:
            raise LenPhoneError

    # удаление телефона из списка телефонов
    def remove_phone(self, phone):
        find_phone = False
        for p in self.phones:
            if p.value == phone:
                find_phone = True
                phone_to_remove = p
        if find_phone:
            self.phones.remove(phone_to_remove)
        else:
            raise PhoneNotFindError


    # изменение обїекта телефон в записи
    def edit_phone(self, phone_old, phone_new):
        if len(phone_new) != Phone.MAX_PHONE_LEN:
            raise LenPhoneError
        else:
            for phone in self.phones:
                if phone.value == phone_old:
                    phone.value = phone_new

    # поиск номера телефона в текущей записи
    def find_phone(self, phone):
        res = None
        for p in self.phones:
            if p.value == phone:
                res = phone
        return res

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = UserDict()
    
    # добавление записи в словарь адресной книги
    def add_record(self, record):
        self.data[record.name.value] = record

    # поиск записи в словаре адресной книги
    def find(self, name):
        rec = self.data.get(name)
        if rec == None:
            raise RecordNotFindError
        else:
            return rec

    # удаление записи в словаре адресной книги
    def delete(self, name):
        if self.data.get(name) == None:
            raise RecordNotFindError
        else:
            self.data.pop(name)




# ниже код для проверки и отладки работы методов

# # Створення нової адресної книги
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Виведення всіх записів у книзі
# print('\nAll Records (1):')
# for name, record in book.data.items():
#     print(record)

# # Видалення запису Jane
# book.delete("Jane")

# # Виведення всіх записів у книзі
# print('\nAll Records (2):')
# for name, record in book.data.items():
#     print(record)

# john.add_phone("1234567890")

# # Виведення всіх записів у книзі
# print('\nAll Records (3):')
# for name, record in book.data.items():
#     print(record)

# john.remove_phone('5555555555')

# # Виведення всіх записів у книзі
# print('\nAll Records (4):')
# for name, record in book.data.items():
#     print(record)