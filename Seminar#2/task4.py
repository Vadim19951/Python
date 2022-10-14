# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# n = int(input("Введите значение n: "))
# lst = []
# index = 0
# while n != -n:
#    lst[index] = n
#    index += 1
#    n -= 1
# print(n)
  
# with open('Seminar#2/test03.txt', 'r') as my_file:
#    my_file.readline()
#    data = my_file.read()
# lst = data.split()
# print(lst)
# int(lst[0])

# N = int(input("Введите размер списка: "))
# spam = list(range(1, N+1))
# print(spam)

with open('Seminar#2/test03.txt', 'r') as my_file:
   data = my_file.read()
index = 0
n = int(input("Введите значение n: "))
lst = []
for i in range(-n, n + 1):
   lst.append(i)
print(lst)

while index < len(lst):
   lst[index] *= 5
print(lst)
