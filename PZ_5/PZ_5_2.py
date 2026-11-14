def minmax(x, y):
    if x > y:
        return y, x
    return x, y


a, b, c, d = map(float, input("Введите A, B, C, D через пробел: ").split())

a, b = minmax(a, b)
c, d = minmax(c, d)
a, c = minmax(a, c)
b, d = minmax(b, d)

print("Минимум:", a)
print("Максимум:", d)
