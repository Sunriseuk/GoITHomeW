import sys

result = ""
a = []
for arg in sys.argv:
    a.append(arg)
for i in a[1:-1]:
    result += i + ' '
result = result + a[-1]
print(result)
