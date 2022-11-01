# -*- coding: utf-8 -*-
# Движок игры Быки и Коровы
from random import randint
computer_number = None
guest_number = None
bulls = None
def make_a_number():
    global computer_number
    computer_number = randint(1023, 9876)
    if len(str(computer_number)) == len(set(str(computer_number))) and str(computer_number)[0] != '0':
        return True
    else:
        return False

def check_num(answer):
    global guest_number, computer_number, bulls
    computer_number = str(computer_number)
    guest_number = str(answer)
    bulls = 0
    cows = 0
    for i in range(4):
        if guest_number[i] == computer_number[i]:
            bulls += 1
        elif guest_number[i] in computer_number:
            cows += 1
    print({'Быки': str(bulls), 'Коровы': str(cows)})

def final():
    if bulls == 4:
        return True
    return False
