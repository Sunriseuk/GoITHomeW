def capital_text(s):
    a = 'hello world! awesome? yes'
    a = s.split('.')
    b = []
    c = ''
    for part in a:
        part = part.strip()
        part = part.capitalize()
        b.append(part + '. ')
    for part in b:
        c += part
    a = c.strip()
    a = a[:-1]

    a = a.split('!')
    b = []
    c = ''
    for part in a:
        part = part.strip()
        part = part.replace(part[0], part[0].upper())
        b.append(part + '! ')
    for part in b:
        c += part
    a = c.strip()
    a = a[:-1]

    a = a.split('?')
    b = []
    c = ''
    for part in a:
        part = part.strip()
        part = part.replace(part[0], part[0].upper())
        b.append(part + '? ')
    for part in b:
        c += part
    a = c.strip()
    a = a[:-1]

    return a
