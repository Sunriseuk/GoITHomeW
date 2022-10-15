from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __repr__(self):
        rep = ", ".join([phone.value for phone in self.phones])

        return rep

    def add_contact(self, phone):
        self.phones.append(Phone(phone))

    def replace_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def remove_contact(self, new_phone):
        for phone in self.phones:
            if phone.value == new_phone:
                self.phones.remove(phone)
                return True


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
