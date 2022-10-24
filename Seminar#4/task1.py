# Вычислить число c 
# заданной точностью d
# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

n = int(input("Введите величину точности n: "))
koefficient = 1
result = 0
for i in range(10000000):
    if i % 2 == 0:
        result += 4/koefficient
    else:
        result -= 4/koefficient
    koefficient += 2  

result = round(result, n)

print(result)

