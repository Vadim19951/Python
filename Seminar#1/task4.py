# Напишите программу, 
# которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).




import sys

x = int(input("Введите значение x: "))



if x == 1:
    print('Значение координат на данной плоскости №1 равно от 0 до  плюс бесконечности на оси X и от нуля до плюс бесконенчности на оси Y')
elif x == 2:
    print('Значение координат на данной плоскости №2 равно от 0 до бесконечности на оси X и от нуля до минус бесконенчности на оси Y')
elif x == 3:
    print('Значение координат на данной плоскости №3 равно от 0 до минус бесконечности на оси X и от нуля до минус бесконенчности на оси Y')
elif x == 4:
    print('Значение координат на данной плоскости №4 равно от 0 до минус бесконечности на оси X и от нуля до плюс бесконенчности на оси Y')
else:
    print('Четверти с таким номером не существует!')