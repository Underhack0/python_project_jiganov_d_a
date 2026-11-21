# Дан список размера N. Найти количество его промежутков монотонности
# (то есть участков, на которых его элементы возрастают или убывают).

def monot(A):
    if not A:
        return 0

    count = 1
    dir = 0

    for i in range(len(A) - 1):
        if A[i + 1] > A[i]:
            cdir = 1
        elif A[i + 1] < A[i]:
            cdir = -1
        else:
            continue

        if dir != 0 and dir != cdir:
            count += 1
        dir = cdir

    return count

N = int(input("Введите размер списка: "))
lst = []
while len(lst) != N:
    lst.append(input("Введите следующий элемент списка: "))
print(monot(lst))
