# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и
#  выведите на экран их сумму.

# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# Данный пример для данного значения не понятия не подходит абсолютно!


n = int(input("Введите значение n: "))
count = 1
while count < n:
    res = (1 + (1 / count)) ** count
    print(res)
    count += 1
print(res)
