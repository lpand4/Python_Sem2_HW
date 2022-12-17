# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} - ПРИМЕР ВИДИМО НЕ ИЗ ЭТОЙ ЗАДАЧИ -_-

n = int(input("Введите число: "))
result_list = []
sum = 0
for i in range(1,n+1):
    result_list.append((1+1/i)**i)
    sum += result_list[i-1]
print(result_list)
print(sum)