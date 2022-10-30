# Задайте натуральное число N. 
# Напишите программу, 
# которая составит список 
# простых множителей числа N.

def find_type_number(number):
    divider = 2
    while divider < number:
        if number % divider == 0:
            return False
        divider += 1
        return True

n = int(input('Введите число N: '))


# print(find_type_number(n))


def decomposition(n):
    div_final = 2
    second_factor = 0
    while div_final < n:
        if n % div_final == 0:
            if find_type_number(n / div_final) == True:   
                if find_type_number(div_final) == True:
                    second_factor = n / div_final
                    print(second_factor, div_final)
                    break
            else:
                find_type_number(n / div_final)
    div_final += 1


decomposition(n)









