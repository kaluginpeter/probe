#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Привет это kaluginpeter, сегодня разберем пространство имен, параметры вызова функции по умолчанию и
# распаковку параметров.
# Бывают локальные и глобальные пространства имен,
# Глобальные задаются всему файлу, а локальные используются только в функциях
# For example:
a, b = 1, 2
print('global', a, b)
print('переменные "a" и "b" это глобальные переменные')

def local_space():
    a,b = 3,4
    print('local', a, b)
local_space()
print('''переменные "a" и "b" в функции local_space это локальные переменные,
они не имеют ничего общего с глобальными переменными "a" и "b", хотя и имеют общее название
и используются они только в функции local_space()''')
# Локальные переменные лучше зписать в виде _a и _b

# Приступим к параметрам вызова функции по умолчанию
# Вызов по умолчанию требуется для того, чтобы упростить работу в некоторых вычислениях и
# автоматического заполнения пропущенных значений переменных
# For example:
def calc(first=5, second=7):
    print('Сумма чисел', first, 'и ', second, '=', first+second)
calc(second=5)
print('В этом примере мы задали значение только переменной "b", а переменная "a" приняла значение по умолчанию')

def calc(first=5, second=7):
    print('Сумма чисел', first, 'и ', second, '=', first+second)
calc()
print('В этом примере мы использовали только значения по умолчанию')

def calc(first=5, second=7):
    print('Сумма чисел', first, 'и ', second, '=', first+second)
calc(first=10, second=10)
print('В этом примере мы задали именованные значения')

# Let's talk about unpacking parameters
# Распаковка значений требуется для "разложения по полочкам" принимаемых значений будь то от списка или же от словаря
# For example:
def scraping_some_list(*args):
    print('Result scraping list')
    print('Type', type(args))
    print('List is', args)
    for i, arg in enumerate(args):
        print('Позиционный элемент', i, '=', arg)
youtube = ['channels', 'videos', 'music', 'shorts']
scraping_some_list(*youtube)
# For example(for dictionaries):
def scraping_some_dict(**kwargs):
    print('Result scraping dictionaries')
    print('Type', type(kwargs))
    print('List is', kwargs)
    for key, value in kwargs.items():
        print('Именованный аргумент', key, '=', value)
youtube_dict = {'channel': 'video', 'shorts':'shorts_video', 'music':'musical_perfomance',}
scraping_some_dict(**youtube_dict)