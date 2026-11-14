# Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из
# значений X и Y, а в переменную Y — максимальное из этих значений (X и Y —
# вещественные параметры, являющиеся одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное и максимальное из
# данных чисел A, B, C, D.

def minmax(x, y):
    if x > y:
        return y, x
    return x, y


a, b, c, d = map(float, input("Введите A, B, C, D через пробел: ").split())

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
while type(c) != int:
    try:
        c = int(a)
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите первое число:")
while type(d) != int:
    try:
        d = int(d)
    except ValueError:
        print("Неправильно ввели!")
        d = input("Введите первое число:")

a, b = minmax(a, b)
c, d = minmax(c, d)
a, c = minmax(a, c)
b, d = minmax(b, d)

print("Минимум:", a)
print("Максимум:", d)
