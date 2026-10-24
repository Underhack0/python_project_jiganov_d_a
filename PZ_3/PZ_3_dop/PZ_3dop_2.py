a = int(input("a: "))

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число:")

if a % 2 == 0:
    a /= 4
else:
    a *= 5

print(a)