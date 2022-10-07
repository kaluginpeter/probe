#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Hello everyone Did you get bored? Its again kaluginpeter
# В который раз("Если хочешь что-то хорошо выучить повторяй это 1000 раз" или что-то вроде того)
# продолжая тему со списками, поступила идея на новое задание
# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Нужно распечатать общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Можно делать много вычислений внутри print() - но это плохой стиль(The Zen of Python спасибо не скажет).
# Лучше заранее вычислить необходимое, а затем в print(выводить)
world = violator_songs_list[0][1]
enjoy = violator_songs_list[5][1]
clean = violator_songs_list[8][1]
all_time_songs1 = world + enjoy + clean
print('''Общее время звучания: 'Halo', 'Enjoy the Silence', 'Clean' составляет''', all_time_songs1)
# Повторяем со вторым словарем песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# печатаем общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут


