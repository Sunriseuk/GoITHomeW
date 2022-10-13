from core import AddressBook


def main():
    book = AddressBook()

    commands = {
        'exit': quit,
        'quit': quit,
        'end': quit,
        'add': book.add_record,
        'find': book.find_contact

    }

    while True:
        var = input('Enter command: ')
        if var not in commands:
            print('Wrong command')
            continue
        commands[var]()


if __name__ == '__main__':
    main()
