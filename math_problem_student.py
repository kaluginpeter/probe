# -*- coding: utf-8 -*-
# Привет это kaluginpeter, сегодня решим задачу циклом while
# (цикл while)

# Допустим ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составим программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
counter = 0
expenses1 = 12000
while counter < 9:
    percent = expenses * 0.03
    expenses = expenses + percent
    expenses1 += expenses
    counter += 1
request_grant = expenses1 - educational_grant * 10
print('Студенту надо попросить', request_grant.__round__(2), 'рублей')