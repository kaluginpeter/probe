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

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
def double_char(s):
    double = 2
    return ''.join([char*double for char in s])

# Upd: Hello it's again kaluginpeter. Today we make some tasks on Codewars
# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    double_a = [i*2 for i in a]
    return double_a

# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2
# Input: []
# Output: 0
def sum_array(a):
    return sum(a)
# Хотя задачи носят решение короткого характера, думал я над ними довольно долго

# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# Write a function which converts the input string to uppercase.
def make_upper_case(s):
    return s.upper()

# Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]
def reverse_seq(n):
    numbers = list(range(n, 0, -1))
    return numbers

# Upd: Hello its kaluginpeter, continue make tasks on codewars
# Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.
# Examples:
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
def reverse_words(text):
    return ' '.join([x[::-1] for x in text.split(' ')])

# We need a function that can transform a string into a number. What ways of achieving this do you know?
def string_to_number(s):
    return (int(s))

# In this simple assignment you are given a number and have to make it negative.
# But maybe the number is already negative?
# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
def make_negative( number ):
    return -abs(number)

# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.
def past(h, m, s):
    hour = h * 60 *60 *1000
    min = m * 60 * 1000
    sec = s * 1000
    all = hour + min + sec
    return all

# Write function bmi that calculates body mass index.
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
def bmi(weight, height):
    bmi_m = weight / height ** 2
    if bmi_m <= 18.5:
        return "Underweight"
    elif bmi_m <= 25.0:
        return "Normal"
    elif bmi_m <= 30.0:
        return "Overweight"
    elif bmi_m > 30:
        return "Obese"

# You get an array of numbers, return the sum of all of the positives ones.
def positive_sum(arr):
    # Your code here
    count = 0
    for i in arr:
        if i > 0:
            count += i
    return count

# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.
def get_count(sentence):
    gl = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for x in sentence:
        if x in gl:
             count += 1
    return count

# Given an array of integers.
# Return an array, where the first element is the count of positives numbers
# and the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
def count_positives_sum_negatives(arr):
    count = 0
    count1 = 0
    if not arr:
        return arr
    else:
        for i in arr:
            if i > 0:
                count += 1
            elif i < 0:
                count1+= i
        return [count, count1]

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
def abbrev_name(name):
    return ('.'.join([e[0] for e in name.split()]).upper())

# Нужно написать каждое слово с большой буквы, но проблема здесь в апострофах
def to_jaden_case(string):
    return " ".join(w.capitalize() for w in string.split())

# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
def digitize(n):
    sec_a = [int(a) for a in str(n)]
    return list(reversed(sec_a))

# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.
def repeat_str(repeat, string):
    return string * repeat

# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink,
# rounded to the smallest value.
import math
def litres(time):
    count = time / 2
    return math.floor(count)

# Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).
def odd_or_even(arr):
    if arr == 0:
        return 'even'
    elif sum(arr) % 2 == 0:
        return 'even'
    elif sum(arr) % 2 != 0:
        return 'odd'

# Given an array of integers your solution should find the smallest integer.
# В этой задаче у меня получилось прибегнуть к хитрости
def find_smallest_int(arr):
    return min(arr)

# There is a bus moving in the city, and it takes and drop some people in each bus stop.
# You are provided with a list (or array) of integer pairs.
# Elements of each pair represent number of people get into bus (The first item)
# and number of people get off the bus (The second item) in a bus stop.
# Your task is to return number of people who are still in the bus after the last bus station (after the last array).
# Even though it is the last bus stop,
# the bus is not empty and some people are still in the bus, and they are probably sleeping there
def number(*bus_stops):
    count = 0
    for stations in bus_stops:
        for add, leave in stations:
            count += add - leave
    return count

# In this kata you will create a function that takes a list of non-negative integers
# and strings and returns a new list with the strings filtered out.
def filter_list(l):
    new_list = [elem for elem in l if isinstance(elem, (int))]
    return new_list

# You ask a small girl,"How old are you?" She always says, "x years old",
# where x is a random number between 0 and 9.
# Write a program that returns the girl's age (0-9) as an integer.
# Assume the test input string is always a valid string.
# For example, the test input may be "1 year old" or "5 years old".
# The first character in the string is always a number.
def get_age(age):
    return int(age[0])

# Create a function that returns the sum of the two lowest positive numbers
# given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
def sum_two_smallest_numbers(numbers):
    first = min(numbers)
    second = sorted(numbers)[1]
    all = first + second
    return all

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
def stray(arr):
    for i in arr:
        if arr.count(i)==1:
            elem = i
    return elem

# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
def first_non_consecutive(arr):
    for i, j in enumerate(arr, arr[0]):
        if i!=j:
            return j

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'

# Complete the solution so that the function will break up camel casing, using a space between words.
def solution(s):
    return ''.join(' ' + char if char.isupper() else char.strip() for char in s).strip()

# We need a function that can transform a number (integer) into a string.
def number_to_string(num):
    return str(num)

# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.
def xo(s):
    s = s.lower()
    word1 = s.count('x')
    word2 = s.count('o')
    if word1 == word2:
        return True
    else:
        return False

# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
def duplicate_count(text):
    text = text.lower()
    count = 0
    for x in set(text):
        if text.count(x) > 1:
            count += 1
    return count

# Write a function that returns both the minimum and maximum number of the given list/array.
def min_max(lst):
    return [min(lst), max(lst)]

# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle
def find_needle(haystack):
    if 'needle' in haystack: return(f"found the needle at position {haystack.index('needle')}")

# After a hard quarter in the office you decide to get some rest on a vacation.
# So you will book a flight for you and your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation.
# The manager of the car rental makes you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total.
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).
def rental_car_cost(d):
    cost = 40
    if d <4:
        return d * cost
    elif 4 <= d < 7:
        return d * cost - 20
    elif d >= 7:
        return d * cost - 50

# The cockroach is one of the fastest insects.
# Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer.
import math
def cockroach_speed(s):
    distance = (s * 1000 * 100) / 60 / 60
    return math.floor(distance)

# ATM machines allow 4 or 6 digit PIN codes
# and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    else:
        return False

# Take an array and remove every second element from the array.
# Always keep the first element and start removing with the next element.
def remove_every_other(my_list):
    del my_list[1::2]
    return my_list

# Write a program where Alex can input (n) how many times the hoop goes round
# and it will return him an encouraging message :)
# If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
# If he doesn't get 10 hoops, return the string "Keep at it until you get it".
def hoop_count(n):
    if n < 10:
        return "Keep at it until you get it"
    else:
        return "Great, now move on to tricks"

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!