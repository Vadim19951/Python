n = 1234 
result = 0

while n > 0:
   print(n % 10)
   result += n % 10
   n = n // 10
   
print(f'Результатом сложения цифр числа является: {result}')
