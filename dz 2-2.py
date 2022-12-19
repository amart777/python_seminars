# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

print("Введите чиcло n")
n = int(input())
ran = range(1,n+1)

s1 = int
s1 = 1
result = []
for i in ran:
    s1 *= i
    res = s1
    result.append(res)

print(f"пусть n = {n} тогда : {result}")