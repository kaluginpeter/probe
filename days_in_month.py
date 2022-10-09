# -*- coding: utf-8 -*-

# (if/elif/else)
# Привет сегодня будет тема циклов
# Нужно по номеру месяца вывести кол-во дней в нем (без указания названия месяца, для справки(в феврале 28 дней))
# Результат проверки выводим на консоль
# Если номер месяца некорректен - сообщаем об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month == 1:
    print('31')
elif month == 2:
    print('28')
elif month == 3:
    print('31')
elif month == 4:
    print('30')
elif month == 5:
    print('31')
elif month == 6:
    print('30')
elif month == 7:
    print('31')
elif month == 8:
    print('31')
elif month == 9:
    print('30')
elif month == 10:
    print('31')
elif month == 11:
    print('30')
elif month == 12:
    print('31')
else:
    print('Такого месяца не существует')

# Это был простой перебор цифр, но можно поступить иначе
months_list = [1, 3, 5, 7, 8, 10, 12]
months_list1 = [4, 6, 9, 11]
month = int(input())
if month in months_list:
    print('В этом месяце - 31 день')
elif month in months_list1:
    print('В этом месяце - 30 дней')
elif month == 2:
    print('В этом месяце - 28 дней')
else:
    print('Такого месяца не существует')