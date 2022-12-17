# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].
import random

n1 = int(input("Введите число: "))
list1 = []
list2 = []
multiply = 1
n2 = int(input("Введите кол-во позиций: "))
for i in range(n2):
    list2.append(input("Введите позицию: "))
print(f'Ваши позиции: {list2}')
for i in range(n1):
    list1.append(random.randint(-n1, n1))
    while list1[i] == 0:
        list1[i] = random.randint(-n1, n1)
print(f"Список {list1}")
for i in list2:
    multiply *= list1[int(i)-1]
print(f'Произведение элементов на указанных позициях {multiply}')