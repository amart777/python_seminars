# 4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

from random import randint

def f1(n):
    f1 = []
    for i in range(n):
        f1.append(randint(-n,n))
    return f1
n = int(input("Введите число "))
chisla = f1(n)
print(chisla)
positions = [1, 3, 6]
res = 1
for i in positions:
    if i <= len(chisla):
        chisla[i-1]
        res *= chisla[i-1]
print(res)


