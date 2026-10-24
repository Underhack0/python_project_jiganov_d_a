A = input("A: ")

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите первое число:")
    if A < 1 or A > 12:
        print("Неправильно ввели!")
        A = input("Введите первое число:")

if A == 1:
    print("31 день")
if A == 2:
    print("28 дней")
if A == 3:
    print("31 день")
if A == 4:
    print("30 дней")
if A == 5:
    print("31 день")
if A == 6:
    print("30 дней")
if A == 7:
    print("31 день")
if A == 8:
    print("30 дней")
if A == 9:
    print("31 день")
if A == 10:
    print("30 дней")
if A == 11:
    print("31 дней")
if A == 12:
    print("30 дней")








