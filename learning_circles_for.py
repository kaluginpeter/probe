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

# Использование опции else для цикла
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет...')
print('Выход из цикла')

# Можно пропустить остаток цикла через - continue
zoo_pets = ['lion', 'skunk', 'elephant', 'monkey', 'horse']
for animal in zoo_pets:
    if animal == 'skunk':
        continue
    print('У нас в руках', animal)
print('Выход из цикла')

# Для подкрепления информации прикрепляю полный пример

zoo_pets = [
    'lion', 'monkey', 'skunk',
    'elephant', 'horse',
]
for animal in zoo_pets:
    if animal == 'skunk':
        print('Фууу...')
        continue
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет...')
print('Выход из цикла')

# автоматическая распаковка содержимого списка/тьюпла(он же кортеж) происходит так

a, b = 1, 2
(a, b) = (1, 2)

for element in [(1, 2), (3, 4)]:
    a, b = element[0], element[1]
    print(a + b)

for (a, b) in [(1, 2), (3, 4)]:
    print(a+b)

pair_list = [(1, 2), (3, 4), (5, 6)]

for a, b in pair_list:
    print(a+b)

triple_list = [(1, 2, 3), (4, 5, 6)]
for a, b, c in triple_list:
    print(a, b, c)

# Так же разберем пример цикла по словарям
zoo_pet_mass = {
    'lion': 300,
    'skunk': 5,
    'elephant': 5000,
    'horse': 400,
}
total_mass = 0
for animal in zoo_pet_mass:
    print(animal, zoo_pet_mass[animal])
    total_mass += zoo_pet_mass[animal]
print('Общая масса животных', total_mass)

total_mass = 0
for animal, mass in zoo_pet_mass.items():
    print(animal, mass)
    total_mass += mass
print('Общая масса животных', total_mass)

total_mass = 0
for mass in zoo_pet_mass.values():
    print(mass)
    total_mass += mass
print('Общая масса животных', total_mass)