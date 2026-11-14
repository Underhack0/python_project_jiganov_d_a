A = [1,2,3,4]
K = input("K: ")
counter = 0

while type(K) != int:
    try:
        K = int(K)
    except ValueError:
        print("Неправильно ввели!")
        K = input("Введите первое число:")

for i in range(K - 1, len(A), K):
    print(A[i])