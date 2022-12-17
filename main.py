# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
import random

n = int(input("Введите кол-во позиций списка: "))
k = n
list1 = []
for i in range(n):
    list1.append(input(f"Введите {i + 1} элемент: "))
print(list1)
print("Перемешиваем . . .")
result_list = []
for i in range(n):
    p = random.uniform(0, k)
    result_list.append(list1[int(p)])
    del list1[int(p)]
    k-=1
print(result_list)