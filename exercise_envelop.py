# -*- coding: utf-8 -*-

# (if/elif/else)
# Привет Друг сегодня поработаем с операторами
# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки выводим на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (можно просто раскоментировать нужную строку и проверить свой код)
# Хочу по экспериментировать и решить через булевы значения
value_x = envelop_x > paper_x
value_y = envelop_y > paper_y
if value_x and value_y:
    print('Бумага подходит')
else:
    print('Размер бумаги слишком большой')