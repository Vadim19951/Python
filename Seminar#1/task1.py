# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


lst = ['Понедельник рабочий','Вторник рабочий','Среда тоже работай','Четверг это маленькая пятница','Потерпи до вечера, это пятница',
'В суботу можешь поспать до обеда','Бегом в церковь на службу,сегодня воскресенье!','Такого дня недели не существует']

day = int(input('Введите день недели: '))

if day == 1:
    print(lst[0])
elif day == 2:
    print(lst[1])
elif day == 3:
    print(lst[2])
elif day == 4:
    print(lst[3])
elif day == 5:
    print(lst[4])
elif day == 6:
    print(lst[5])
elif day == 7:
    print(lst[6])
else:
    print(lst[7])    

