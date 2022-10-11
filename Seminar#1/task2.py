# Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from pickle import TRUE
import sys

print('Введите значение истинности следующих высказываний, только 0 или 1:')
x = int(input("Введите значение x: "))
if x == 0:
    x = False
elif x == 1:
    x = True
else:
    sys.exit('Неверное значение X')

y = int(input("Введите значение y: "))
if y == 0:
    y = False
elif y == 1:
    y = True
else:
    sys.exit('Неверное значение Y') 

z = int(input("Введите значение z: "))
if z == 0:
    z = False
elif z == 1:
    z = True
else:
    sys.exit('Неверное значение Z')

leftSide = not(x or y or z )
rightSide = not x and not y and not z

if leftSide == rightSide:
    print('Выражение ИСТИННО!')
else:
    print('Выражение ЛОЖНО!')