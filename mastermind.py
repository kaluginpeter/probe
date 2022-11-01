# -*- coding: utf-8 -*-
# Логика игры Быки и Коровы будет описана в этом файле. Приступим!
from mastermind_engine import make_a_number, check_num, final
print('Привет! Давай сыграем в Быка и Коровы')
make_a_number()
print('Я загадал четырехзначное число, попробуй отгадать')
while True:
    guest_number = input('Назовите вариант четырехзначного числа: ')
    while True:
        if len(guest_number) == 4:
            break
        else:
            print('Не четырехзначное число!')
            guest_number = input('Попробуй еще раз назвать вариант числа: ')
    check_num(answer=guest_number)
    if final():
        break
print('Ты победил! Правильное число оказалось:', guest_number)