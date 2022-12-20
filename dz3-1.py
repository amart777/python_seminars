
# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def f1(n):
    f1 = []
    for i in range(n):
        f1.append(randint(-n,n))
    return f1
n = int(input("Введите число элементов списка "))
chisla = f1(n)
print(chisla)

chisla.pop(0)
print(chisla[::2])

print(sum(chisla[::2]))
