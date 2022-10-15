from core import *

CONTACTS = AddressBook()


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
        except (ValueError, IndexError, UnboundLocalError):
            print("\nError. Give me correct name and phone, please")
        except KeyError:
            print("\nError. Enter user name, please")
    return wrapper


@input_error
def hello_func():
    return 'How can I help you?'


@input_error
def exit_func():
    return 'good bye'


@input_error
def changefun(var):
    name = var.split()[1]
    phone_for_change = var.split()[2]
    new_phone = var.split()[3]
    if phone_for_change.isdigit() and new_phone.isdigit():
        record = CONTACTS.data[name]
        record.change_phone(phone_for_change, new_phone)
        return "\nContact was changed"


@input_error
def showallfun():
    for name, record in CONTACTS.items():
        return f"\n{name}: {[phone.value for phone in record.phones]}"


@input_error
def addfun(var):
    if (var.split()[1]).isalpha():
        name = var.split()[1]
    if (var.split()[2]).isdigit():
        phone = var.split()[2]
    if name in CONTACTS:
        record = CONTACTS.data[name]
        record.add_phone(phone)
    else:
        record = Record(name, phone)
        CONTACTS.add_record(record)
    return f"\nNew contact was added"


@input_error
def findfun(var):
    for name, record in CONTACTS.items():
        if name == var.split()[1]:
            return f"{name}: {[phone.value for phone in record.phones]}"


@input_error
def delfun(var):
    name = var.split()[1]
    phone_for_delete = var.split()[2]
    record = CONTACTS.data[name]
    record.delete_phone(phone_for_delete)
    print("\nContact's phone was deleted")


COMMANDS_DICT = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': addfun,
    'change': changefun,
    'show all': showallfun,
    'phone': findfun
}


def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()


def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_func)


def create_data(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError('Wrong name.')
    if not phone.isnumeric():
        raise ValueError('Wrong phone.')
    return name, phone


def break_func():
    return 'Wrong enter.'


def main():

    while True:
        user_input = input('Enter command for bot: ')
        result = change_input(user_input)
        print(result)
        if result == 'good bye':
            break


if __name__ == "__main__":
    main()
