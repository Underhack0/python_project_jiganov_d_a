# 1. Дано целое число N (> 0). Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + … + (2N)^2

N = input("N: ")

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите первое число:")
    if N <= 0:
        print("Неправильно ввели!")
        N = input("Введите первое число:")

answer = N ** 2
summand = 1

while N != summand:
    answer += (N + 1) ** 2
    summand += 1

else:
    answer += (2 * N) ** 2
    print(answer)
