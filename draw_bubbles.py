# -*- coding: utf-8 -*-
# Привет с тобой kaluginpeter, сегодня попробуем порисовать с помощью библиотеки simple_draw
# Теперь в заданиях буду использовать тудушки
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius)
# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5)
# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step)
sd.pause()


