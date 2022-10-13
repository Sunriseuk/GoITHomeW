from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class AddressBook(UserDict):

    def get_name(self):
        self.name = Name(input('enter name: '))

    def find_contact(self):
        self.get_name()
        if self.name.value in self.data:
            record = self.data[self.name.value]
            print(record, record.name.value, record.phones)
        else:
            print('Contact is not find')

    def add_record(self):
        self.get_name()
        phone = Phone(input('enter phone: '))
        record = Record(name=self.name)
        if phone.value:
            record.add(phone)
        self.data[record.name.value] = record
        print('New contact added:')


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add(self, phone):
        self.phones.append(phone)

    def remove(self, phone):
        self.phones.remove(phone)

    def update(self, i, old_phone, new_phone):
        self.remove(old_phone)
        self.add(new_phone)


# CONTACTS = {}


# @corrector
# def add_contact_handler():


# @corrector
# def find_contact_handler():
#     name = input('enter name: ')
#     print(name, CONTACTS[name])
