# 1 Подсчитать сумму цифр в вещественном числе.

print("Введите чиcло сумму цифр которого нужно посчитать")
n = list(input())
for t in n:
    if t =='.': n.remove('.')
    
sumr = 0
sumr = int(sumr)
for i in n:
    res = i
    res = int(res)
    
    sumr = sumr+res
print(sumr)
