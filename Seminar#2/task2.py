# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input("Введите значение "))
min = 1
multiply = 1
print('\nНабор произведений чисел равен: ')
while min <= n:
     multiply *= min
     print(multiply, end = ", ")
     min += 1






# multiply *= min


# print(multiply)
# min += 1

# multiply *= min


# print(multiply)


