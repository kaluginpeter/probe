# -*- coding: utf-8 -*-
# Привет это kaluginpeter, сегодня порешаем задачи на Python
# Задача 1
# Есть список
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые меньше 5
for elem in a:
    if elem < 5:
        print(elem)
    else:
        continue