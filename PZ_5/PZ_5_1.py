# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
# результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
# получится нуль?

number = input("Введите число: ")

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите число: ")

def summ(n):
    steps = 0
    while n > 0:
        digit_sum = sum(int(digit) for digit in str(n))
        n -= digit_sum
        steps += 1
    return steps

result = summ(number)
print(f"Для числа {number} потребуется действий: {result}")
