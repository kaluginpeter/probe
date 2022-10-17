# -*- coding: utf-8 -*-
# Привет это kaluginpeter, сегодня порешаем задачи с Codewars. Let's do it

# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
# Use conditionals to return the proper message:
# case	             return
# name equals owner	 'Hello boss'
# otherwise	         'Hello guest'
def greet(name, owner):
    # Add code here
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
# A hero is on his way to the castle to complete his mission.
# However, he's been told that the castle is surrounded with a couple of powerful dragons!
# Each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry..
# Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific
# given number of dragons, will he survive?
# Return True if yes, False otherwise :)
def hero(bullets, dragons):
    if bullets // dragons == 2:
        return True
    elif bullets and dragons == 0:
            return True
    else:
        return False

# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.
# For example:
# summation(2) -> 3
# 1 + 2
# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
def summation(num):
    count = 0
    for i in range(num+1):
        count += i
    return count