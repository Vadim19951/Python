# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

with open('Seminar#2/test03.txt', 'r') as my_file:
   data = my_file.read()
index = 0
n = int(input("Введите значение n: "))
lst = []
for i in range(-n, n + 1):
   lst.append(i)
print(lst)

while index < len(lst):
   lst[index] *= int(data)
print(lst)
