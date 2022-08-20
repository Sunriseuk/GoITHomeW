def amount_payment(*args):
    sum = 0
    for pay in args:
        if pay > 0:
            sum += int(pay)
    return sum


amount_payment(100, 500, -200, 200)
