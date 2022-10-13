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


def hellofun():
    print("\nHow can I help you?")


def quitfun():
    print("\nGood bye!")
    quit()


@input_error
def changefun(var):
    name = var.split()[1]
    phone_for_change = var.split()[2]
    new_phone = var.split()[3]
    if phone_for_change.isdigit() and new_phone.isdigit():
        record = CONTACTS.data[name]
        record.change_phone(phone_for_change, new_phone)
        print("\nContact was changed")


def showallfun():
    for name, record in CONTACTS.items():
        print(f"\n{name}: {[phone.value for phone in record.phones]}")


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
    print(f"\nNew contact was added")


@input_error
def findfun(var):
    for name, record in CONTACTS.items():
        if name == var.split()[1]:
            print(f"{name}: {[phone.value for phone in record.phones]}")


@input_error
def delfun(var):
    name = var.split()[1]
    phone_for_delete = var.split()[2]
    record = CONTACTS.data[name]
    record.delete_phone(phone_for_delete)
    print("\nContact's phone was deleted")


COMMANDS = {
    "hello": hellofun,
    "show all": showallfun,
    "exit": quitfun,
    "close": quitfun,
    "good bye": quitfun
}


def main():
    while True:
        var = (input("\nEnter command: ")).lower()
        if var.startswith('add'):
            addfun(var)
        elif var.startswith('change'):
            changefun(var)
        elif var.startswith('phone'):
            findfun(var)
        elif var.startswith('delete'):
            delfun(var)
        elif var not in COMMANDS:
            print("Wrong command!")
            continue
        else:
            COMMANDS[var]()


if __name__ == "__main__":
    main()
