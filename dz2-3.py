# 3 Задать список из n чисел последовательности ((1+1/n)в степени n) и вывести на экран их сумму.

print("введите число n")
n = int(input())
result = []
sum = 0
for i in range(1,n+1):
    res = (1+1/i)**i
    result.append(res)
    sum += res
print (f"для {n}:{result}")
print ("сумма чисел =",sum)
