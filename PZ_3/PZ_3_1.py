# 1. Даны два целых числа: А, В. Проверить истинность высказывания: «Ровно одно и чисел А и В нечетное».

A, B = input("A:"), input("B:")

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите первое число:")

while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Неправильно ввели!")
        B = input("Введите первое число:")

if A % 2 == 0:
    if B % 2 != 0:
        print("Высказывание верно.")

    else:
        print("Высказывание не верно.")

elif B % 2 == 0:
    if A % 2 != 0:
        print("Высказывание верно.")

    else:
        print("Высказывание не верно.")

elif B % 2 != 0 and A % 2 != 0:
    print("Высказывание не верно.")
