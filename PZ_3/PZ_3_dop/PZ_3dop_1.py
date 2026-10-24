a, b = int(input("a: ")), int(input("b: "))

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число:")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите первое число:")

sum = a + b

if sum < 0:
    sum *= 8
else:
    sum *= 1.5

print(sum)
