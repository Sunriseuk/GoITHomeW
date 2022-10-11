import time
import re

from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []

    def addfun(self, phone):
        self.phones.append(Phone(phone))

    def changefun(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    # def remove_contacts(self, name, phone):
    #     if name == Name(name):
    #         Name(name)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


CONTACTS = AddressBook


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("You entered an incorrect command format")
        except TypeError:
            print("You entered an incorrect command format")
        except IndexError:
            print('You entered an incorrect command format')
        except ValueError as e:
            print(e.args[0])
        except Exception as e:
            print(e.args)
    return wrapper


@input_error
def addfun(add):  # Функция, которая добавляет контакт
    contact = add.split(' ')
    num = '380\d{9}'
    if contact[1].isalpha() and len(contact[2]) == 12 and re.match(num, contact[2]) is not None:
        name = contact[1]
        phone = contact[2]
        CONTACTS.update({name: phone})
        print(f"New contact added.")
    else:
        print('\nError! Enter: "add name 380XXXXXXXXX"')


@input_error
def changefun(change):  # Функция, которая заменяет контакт
    contact = change.split(' ')
    num = '380\d{9}'
    if contact[1] in phone_book.keys() and contact[1].isalpha() and len(contact[2]) == 12 and re.match(num, contact[2]) is not None:
        name = contact[1]
        phone = contact[2]
        CONTACTS[name] = phone
        print(f'\nYour new Phone Book is: \n {phone_book}')

    else:
        print('\nError! Enter: "change name 380XXXXXXXXX"')


@input_error
def phonefun(phone):  # Функция, которая вывод номер выбранного контакта
    contact = phone.split(' ')
    if contact[1] in phone_book:
        phone = CONTACTS[phone.strip()]
        print(phone)
    else:
        print('\nContact not found. Enter: "phone name"')


def show_allfun():  # Функция, которая выводит все контакты
    print(CONTACTS.items())


def reply(answer):
    aloop = True
    if "good bye" in answer or "close" in answer or "exit" in answer:
        print("\nGood bye!\n")
        aloop = False
    elif " hello " in (" " + answer + " "):
        print("\nHow can I help you?")
    elif answer.startswith("add "):
        addfun(answer)
    elif answer.startswith("change "):
        changefun(answer)
    elif answer.startswith("phone "):
        phonefun(answer)
    elif " show all " in (" " + answer + " "):
        show_allfun()

    else:
        print('Input Error')

    time.sleep(0.5)
    return aloop


def main():
    loop = True
    while loop:
        print("\nEnter something: \n")
        rep = input().lower()
        loop = reply(rep)


if __name__ == '__main__':
    main()
