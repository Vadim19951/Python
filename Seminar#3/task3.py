# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.23, 4.34, 5.232, 2.98, 3.9, 4.1]
min = lst[0]
max = lst[0] 
min_int = min
max_int = max
min_float_remain = 0
max_float_remain = 0
result = 0
for i in range(len(lst)):
        if min > lst[i]:
            min = lst[i]
        elif max < lst[i]:
            max = lst[i]
print(f'{min} and {max}')

min_int = int(min)
max_int = int(max)
min_float_remain = min - min_int
max_float_remain = max - max_int
result = max_float_remain - min_float_remain

print(f'Разница дробных частей минимального и макисмального элемента {max} and {min} равна {result} ')









