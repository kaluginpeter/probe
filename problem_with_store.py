#!/usr/bin/env python
# -*- coding: utf-8 -*-
# И снова привет с тобой kaluginpeter
# Работаем со словарями
# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитываем на какую сумму лежит каждого товара на складе
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_code = goods['Стол']
table_items = store[table_code][0]
table_items2 = store[table_code][1]
table_quantity = table_items['quantity']
table_quantity2 = table_items2['quantity']
table_price = table_items['price']
table_price2 = table_items2['price']
table_cost = table_quantity * table_price + table_quantity2 * table_price2
print('Стол -', table_quantity + table_quantity2, 'шт, стоимость', table_cost, 'руб')

sofa_code = goods['Диван']
sofa_items = store[sofa_code][0]
sofa_items2 = store[sofa_code][1]
sofa_quantity = sofa_items['quantity']
sofa_quantity2 = sofa_items2['quantity']
sofa_price = sofa_items['price']
sofa_price2 = sofa_items2['price']
sofa_cost = sofa_quantity * sofa_price + sofa_quantity2 * sofa_price2
print('Диван -', sofa_quantity + sofa_quantity2, 'шт, стоимость', sofa_cost, 'руб')

chair_code = goods['Стул']
chair_items = store[chair_code][0]
chair_items2 = store[chair_code][1]
chair_items3 = store[chair_code][2]
chair_quantity = chair_items['quantity']
chair_quantity2 = chair_items2['quantity']
chair_quantity3 = chair_items3['quantity']
chair_price = chair_items['price']
chair_price2 = chair_items2['price']
chair_price3 = chair_items3['price']
chair_cost = chair_quantity * chair_price + chair_quantity2 * chair_price2 + chair_quantity3 * chair_price3
print('Стул -', chair_quantity + chair_quantity2 + chair_quantity3, 'шт, стоимость', chair_cost, 'руб')









# Выводим стоимость каждого товара на складе: один раз распечатать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб






