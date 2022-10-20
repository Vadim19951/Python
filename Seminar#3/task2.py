# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

lst = []
lst_result = []
for i in range(1, 7):
    lst.append(randint(1, 5))

count = 0
count_two = len(lst) - 1
for i in range(len(lst)):
    if i == count:
            if len(lst) % 2 != 0:
                while count != count_two:
                    result = lst[count] * lst[count_two]
                    lst_result.append(result)
                    count += 1
                    count_two -= 1 
                result = lst[count] * lst[count_two]
                lst_result.append(result)
            else:
                while count != len(lst) / 2:
                    result = lst[count] * lst[count_two]
                    lst_result.append(result)
                    count += 1
                    count_two -= 1

if len(lst) % 2 != 0:
    lst_result.pop()
    print(f'{lst} => {lst_result}')
else:
    print(f'{lst} => {lst_result}')
