# -*- coding: utf-8 -*-
# Привет это kaluginpeter
# Сегодня распишу тему цикла for
# for <переменная цикла> in <список>:
#     <блок кода>

# Цикл for ("для каждого элемента")
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
print('Выход из цикла')

# Можно рассчитать количество букв
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
letters_count = 0
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    letters_count += len(animal)
    pass
print('Всего букв', letters_count)

# Способ принудительный останов цикла - break
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
