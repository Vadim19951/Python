# Напишите программу,
# которая будет преобразовывать десятичное число
# в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


n = int(input("Введите десятичное число n: "))
original_n = n
buff_string = ''
result = ''
index = 0
while n / 2 != 0:
    buff_string += str(n % 2)
    n = n // 2
index = len(buff_string)
while index > 0:
    result += buff_string[index - 1]
    index -= 1

print(f'десятичное число {original_n} равно двоичному {result}')
