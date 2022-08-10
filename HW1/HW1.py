result = None
operand = None
operator = None
wait_for_number = True
while True:
    operand = (input('Enter a number: '))
    if not operand.isdigit():
        print(f'{operand} is not a number')
    else:
        result = int(operand)
        break

while wait_for_number:
    operator = (input('Enter an operator: '))
    if operator == '=':
        break
    elif operator in '-+*/':
        wait_for_number = False
    else:
        print(f'{operator} is not an operator')

    while not wait_for_number:
        operand = (input('Enter a number: '))
        if not operand.isdigit():
            print(f'{operand} is not a number')
        else:
            if operator == '+':
                result += int(operand)
            elif operator == '-':
                result -= int(operand)
            elif operator == '/':
                try:
                    result /= int(operand)
                except ZeroDivisionError:
                    print('Деление на ноль!')
            elif operator == '*':
                result *= int(operand)
            wait_for_number = True
print(result)
