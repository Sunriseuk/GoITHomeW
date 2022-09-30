import time
import re

phone_book = {
    "коля": 380954504490,
    "оля": 380934432345,
    "таня": 380634562399,
    "наташа": 380671232349
}


def addfun(add):  # Функция, которая добавляет контакт
    contact = add.split(' ')
    num = '380\d{9}'
    if contact[1].isalpha() and len(contact[2]) == 12 and re.match(num, contact[2]) is not None:
        phone_book.update({contact[1]: int(contact[2])})
        print(f'\nYour new Phone Book is: \n {phone_book}')
    else:
        print('\nError! Enter: "add name 380XXXXXXXXX"')


def changefun(change):  # Функция, которая заменяет контакт
    contact = change.split(' ')
    num = '380\d{9}'
    if contact[1] in phone_book.keys() and contact[1].isalpha() and len(contact[2]) == 12 and re.match(num, contact[2]) is not None:
        phone_book[contact[1]] = int(contact[2])
        print(f'\nYour new Phone Book is: \n {phone_book}')

    else:
        print('\nError! Enter: "change name 380XXXXXXXXX"')


def phonefun(phone):  # Функция, которая вывод номер выбранного контакта
    contact = phone.split(' ')
    if contact[1] in phone_book.keys():
        print(f'\nNumber of contact is {phone_book[contact[1]]}')
    else:
        print('\nContact not found. Enter: "phone name"')


def show_allfun():  # Функция, которая выводит все контакты
    print(f'\nYour Phone Book is: \n {phone_book}')


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
