# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



from random import randint


number = int(input('Введите число элементов списка '))
spisok1 = []
spisok2 = []

for i in range(number):
    spisok1.append(randint(0, 9))

for i in range(len(spisok1)):
    while i < len(spisok1)/2 and number > len(spisok1)/2:
        number = number - 1
        a = spisok1[i] * spisok1[number]
        spisok2.append(a)
        i += 1

print(spisok1)
print(spisok2)