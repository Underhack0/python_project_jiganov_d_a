a = int(input("a: "))

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число:")
    if len(a) != 2:
        print("Неправильно ввели!")
        a = input("Введите первое число:")

print(len(a))