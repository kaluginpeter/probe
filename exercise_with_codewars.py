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
from statistics import mean
def better_than_average(class_points, your_points):
    class_points.insert(0, your_points)
    avr = mean(class_points)
    if your_points > avr:
        return True
    else:
        return False

# You're writing code to control your town's traffic lights.
# You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current
# state of the light and returns a string representing the state the light should change to.
def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'

# Write a function named setAlarm which receives two parameters. The first parameter, employed,
# is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.
# The function should return true if you are employed and not on vacation
# (because these are the circumstances under which you need to set an alarm). It should return false otherwise.
def set_alarm(employed, vacation):
    if (bool(employed) == True) and (bool(vacation) == False):
        return True
    else:
        return False

# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
def quarter_of(month):
    first = [1, 2, 3]
    second = [4, 5, 6]
    third = [7, 8, 9]
    fourth = [10, 11, 12]
    if month in first:
        return 1
    elif month in second:
        return 2
    elif month in third:
        return 3
    elif month in fourth:
        return 4

# It's pretty straightforward.
#  Your goal is to create a function that removes the first and last characters of a string.
#  You're given one parameter, the original string.
#  You don't have to worry with strings with less than two characters.
def remove_char(s):
    return s[1:-1]

# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
def remove_exclamation_marks(s):
    return ''.join(word for word in s if word not in '!')

# Very simple, given an integer or a floating-point number, find its opposite.
def opposite(number):
    return number * -1

# You will be given an array a and a value x.
# All you need to do is check whether the provided array contains the value
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.
def check(seq, elem):
    return elem in seq

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
def are_you_playing_banjo(name):
    n_lst = ['r', 'R']
    if name[0] in n_lst:
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

# Count the number of divisors of a positive integer n.
def divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count+=1
    return count

# Create a function that accepts 2 string arguments
# and returns an integer of the count of occurrences the 2nd argument is found in the first one.
def str_count(strng, letter):
    return strng.count(letter)

# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.
def is_pangram(s):
    s = s.lower()
    count = 0
    list = 'abcdefghijklmnopqrstuvwxyz'
    pangram = set(s) & set(list)
    return len(pangram) == len(list)

# Complete the function so that it finds the average of the three scores passed to it
# and returns the letter value associated with that grade.
def get_grade(s1, s2, s3):
    avr = (s1 + s2 +s3) / 3
    if 90 <= avr <= 100:
        return 'A'
    elif 80 <= avr < 90:
        return 'B'
    elif 70 <= avr < 80:
        return 'C'
    elif 60 <= avr < 70:
        return 'D'
    else:
        return 'F'

# You are going to be given a word.
# Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.
def get_middle(s):
    if len(s) % 2:
        index = int(len(s) / 2)
        return s[index]
    elif len(s) % 2 == 0:
        x = len(s) // 2
        y = len(s) // 2 - 1
        return (f'{s[y]}{s[x]}')

# Your classmates asked you to copy some paperwork for them.
# You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n * m

# Think of a way to store the languages as a database (eg an object).
# The languages are listed below so you can copy and paste!
# Write a 'welcome' function that takes a parameter 'language' (always a string),
# and returns a greeting - if you have it in your database.
# It should default to English if the language is not in the database, or in the event of an invalid input.
def greet(language):
    base = {'english': 'Welcome',
    'czech': 'Vitejte',
    'danish': 'Velkomst',
    'dutch': 'Welkom',
    'estonian': 'Tere tulemast',
    'finnish': 'Tervetuloa',
    'flemish': 'Welgekomen',
    'french': 'Bienvenue',
    'german': 'Willkommen',
    'irish': 'Failte',
    'italian': 'Benvenuto',
    'latvian': 'Gaidits',
    'lithuanian': 'Laukiamas',
    'polish': 'Witamy',
    'spanish': 'Bienvenido',
    'swedish': 'Valkommen',
    'welsh': 'Croeso'}
    if language in base:
        return base[language]
    else:
        return 'Welcome'

# When provided with a number between 0-9, return it in words.
def switch_it_up(number):
    numbers = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }
    return numbers[number]

# Simple, remove the spaces from the string, then return the resultant string.
def no_space(x):
    return x.replace(' ' ,'')

# There is an array with some numbers. All numbers are equal except for one. Try to find it!
def find_uniq(arr):
    found = set()
    found_again = set()

    for a in arr:
        if a in found_again:
            continue
        if a in found:
            found.remove(a)
            found_again.add(a)
        else:
            found.add(a)
    res = list(found)
    return (res[0])

# In this simple exercise, you will create a program that will take two lists of integers, a and b.
# Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b.
# You must find the difference of the cuboids' volumes regardless of which is bigger.
def find_difference(a, b):
    q_a = (a[0] * a[1]) * a[2]
    q_b = (b[0] * b[1]) * b[2]
    return abs(q_a - q_b)

# Given a year, return the century it is in.
import math
def century(year):
    return (math.ceil(year / 100))

# Complete the square sum function so that it squares each number passed into it and then sums the results together.
def square_sum(numbers):
    return sum([integer*integer for integer in numbers])

# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
# Otherwise, you can be sure he's not...
def friend(x):
    true_friends = []
    for name in x:
        if len(name) == 4 and name.isalpha():
            true_friends.append(name)
        else:
            pass
    return true_friends

# Create a method to see whether the string is ALL CAPS. UPD: isupper() not worked with special simbols
def is_uppercase(inp):
    special = ['$%&', '+%@']
    if inp.isupper():
        return True
    elif inp in special:
        return True
    else:
        return False

# Write a function which calculates the average of the numbers in a given list.
def find_average(numbers):
    return sum(numbers) / len(numbers)

# You have to write a function that accepts three parameters:
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
def enough(cap, on, wait):
    if on + wait < cap:
        return 0
    else:
        return abs(cap - (on + wait))

# I got them at the same time as kitten/puppy. That was humanYears years ago.
# Return their respective ages now as [humanYears,catYears,dogYears]
def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    if human_years == 1:
        return [human_years, cat_years + 15, dog_years + 15]
    elif human_years == 2:
        return [human_years, cat_years + 15 + 9, dog_years + 15 + 9]
    elif human_years > 2:
        cat_years = 24
        dog_years = 24
        for i in range(human_years-2):
            cat_years+=4
            dog_years+=5
        return [human_years, cat_years, dog_years]

# Implement the function unique_in_order which takes as argument a sequence
# and returns a list of items without any elements with the same value next to each other
# and preserving the original order of elements.
def unique_in_order(iterable):
    new = []
    if not iterable:
        return []
    for i in range(len(iterable)-1):
        if iterable[i] != iterable[i + 1]:
            new.append(iterable[i])
    new.append(iterable[-1])
    return new

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned.
# You may assume the parameter is non-negative.
def find_next_square(sq):
    perfect_sq = sq ** .5
    if perfect_sq.is_integer():
        return (perfect_sq + 1) ** 2
    else:
        return -1

# Complete the function that takes a non-negative integer n as input,
# and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).
def powers_of_two(n):
    list = []
    for i in range(n+1):
        list.append(2**i)
    return list

# All of the animals are having a feast! Each animal is bringing one dish.
# There is just one rule: the dish must start and end with the same letters as the animal's name.
# For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.
# Write a function feast that takes the animal's name and dish as arguments
# and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.
# Assume that beast and dish are always lowercase strings, and that each has at least two letters.
# beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string.
# They will not contain numerals.
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
def array_diff(a, b):
    list =[]
    for i in a:
        if i not in b:
            list.append(i)
    return list

# Complete the function that takes two integers (a, b, where a < b)
# and return an array of all integers between the input parameters, including them.
def between(a,b):
    list = []
    for i in range(a, b+1):
        list.append(i)
    return list

# Define String.prototype.toAlternatingCase
# (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase
# in your selected language; see the initial solution for details)
# such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase.
def to_alternating_case(string):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# Write a function that takes an array of strings as an argument
# and returns a sorted array containing the same strings, ordered from shortest to longest.
def sort_by_length(arr):
    arr.sort(key=len)
    return sorted(arr, key=len)

# Given an array of integers, remove the smallest value.
# Do not mutate the original array/list. If there are multiple elements with the same value,
# remove the one with a lower index. If you get an empty array/list, return an empty array/list.
def remove_smallest(numbers):
    if numbers:
        new_list = numbers.copy()
        new_list.remove(min(new_list))
        return new_list
    else:
        return numbers

# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
def sum_str(a, b):
    if a and b:
        c = int(a) + int(b)
        return str(c)
    elif a == '' and b == '':
        return '0'
    else:
        if a:
            return a
        else:
            return b

# Сalculate how many years ago the father was twice as old as his son
# (or in how many years he will be twice as old). The answer is always greater or equal to 0,
# no matter if it was in the past or it is in the future.
def twice_as_old(dad_years_old, son_years_old):
    ages = son_years_old * 2
    return abs(ages - dad_years_old)

# Build a pyramid-shaped tower, as an array/list of strings,
# given a positive integer number of floors. A tower block is represented with "*" character.
def tower_builder(n_floors):
    list = []
    for i in range(n_floors):
        first_elem=''
        second_elem=''
        for j in range(i,n_floors-1):
            first_elem+=' '
        for k in range(2*i+1):
            second_elem+='*'
        list.append(first_elem + second_elem + first_elem)
    return list

# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.
def other_angle(a,b):
    return 180 - a - b

# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array
# or list of integers
def max_sequence(arr):
    local_max_sum = 0
    global_max = 0
    for elem in arr:
        local_max_sum = max(local_max_sum + elem, elem)
        global_max = max(local_max_sum, global_max)
    return global_max

# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
def accum(s):
    word = ''
    count = -1
    for i in s:
        count+=1
        char = i.lower() * count
        word = word + (i.upper() + char + '-')
    return word[:-1]

# You are given an array with positive numbers and a non-negative number N.
# You should find the N-th power of the element in the array with the index N.
# If N is outside of the array, then return -1.
def index(array, n):
    if n <= len(array) - 1:
        return array[n]**n
    else:
        return -1

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
def square_digits(num):
    elem = ''
    for i in str(num):
        square = int(i) ** 2
        elem += str(square)
    return int(elem)

# The goal of this exercise is to convert a string to a new string where each character
# in the new string is "(" if that character appears only once in the original string, or ")"
# if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.
def duplicate_encode(word):
    new_word = ''
    word = word[0].lower() + word[1:].lower()
    for char in word:
        if word.count(char) > 1:
            new_word += ')'
        else:
            new_word += '('
    return new_word

# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.
def area_or_perimeter(l , w):
    return ((l + w) * 2 if l != w else l * w)

# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
def increment_string(strng):
    stripped = strng.rstrip('1234567890')
    ints = strng[len(stripped):]
    if len(ints) == 0:
        return strng + '1'
    else:
        length_word = len(ints)
        new_ints = int(ints) + 1
        new_ints = str(new_ints).zfill(length_word)
        return stripped + new_ints

# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language )
# that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
def correct(s):
    s = s.replace('5', 'S')
    s = s.replace('0', 'O')
    s = s.replace('1', 'I')
    return s

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
# seven(times(five())) # must return 35
def zero(integer = None):
    return 0 if integer is None else int(integer(0))
def one(integer = None):
    return 1 if integer is None else int(integer(1))
def two(integer = None):
    return 2 if integer is None else int(integer(2))
def three(integer = None):
    return 3 if integer is None else int(integer(3))
def four(integer = None):
    return 4 if integer is None else int(integer(4))
def five(integer = None):
    return 5 if integer is None else int(integer(5))
def six(integer = None):
    return 6 if integer is None else int(integer(6))
def seven(integer = None):
    return 7 if integer is None else int(integer(7))
def eight(integer = None):
    return 8 if integer is None else int(integer(8))
def nine(integer = None):
    return 9 if integer is None else int(integer(9))

def plus(second_integer):
    return lambda integer: integer + second_integer
def minus(second_integer):
    return lambda integer: integer - second_integer
def times(second_integer):
    return lambda integer: integer * second_integer
def divided_by(second_integer):
    return lambda integer: integer / second_integer

# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.
def is_isogram(string):
    some_string = ''
    for word in string.lower():
        if word not in some_string:
            some_string += word
    print(some_string)
    if len(some_string) == len(string):
        return True
    else:
        return False

# You will be given a number and you will need to return it as a string in Expanded Form. For example:
# expanded_form(12) # Should return '10 + 2'
def expanded_form(num):
    list_of_numbers = []
    lenght = len(str(num)) - 1
    for char in str(num):
        if char != "0":
            list_of_numbers.append(char + "0" * lenght)
        lenght -= 1
    return " + ".join(list_of_numbers)

# Your task is to write a function that takes a string and return a new string with all vowels removed.
def disemvowel(string_):
    list = ['a','e','i','o','u', 'A','E','I','O','U']
    for char in string_:
        if char in list:
            string_ = string_.replace(char, '')
    return string_

# In DNA strings, symbols "A" and "T" are complements of each other,
# as "C" and "G". Your function receives one side of the DNA (string, except for Haskell);
# you need to return the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).
def DNA_strand(dna):
    dnk =''
    for char in dna:
        if char == 'A':
            dnk += 'T'
        elif char == 'T':
            dnk += 'A'
        elif char == 'G':
            dnk += 'C'
        elif char == 'C':
            dnk += 'G'
    return dnk

# Write a function that takes a list of strings as an argument
# and returns a filtered list containing the same elements but with the 'geese' removed.
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [elem for elem in birds if elem not in geese]

# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
def remove_url_anchor(url):
    if url.count('#'):
        index = url.index('#')
        return url[:index]
    return url

# You will be given a list of strings. You must sort it alphabetically (case-sensitive,
# and based on the ASCII values of the chars) and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
def two_sort(array):
    array.sort()
    return '***'.join(array[0])

# Bob needs a fast way to calculate the volume of a cuboid with three values:
# the length, width and height of the cuboid. Write a function to help Bob with this calculation.
def get_volume_of_cuboid(length, width, height):
    return length * width * height

# Create a function finalGrade, which calculates the final grade of a student depending on two parameters:
# a grade for the exam and a number of completed projects.
# This function should take two arguments:
# exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0

# Your task is to make a function that can take any non-negative integer as an argument
# and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.
def descending_order(num):
    order = []
    if num >= 0:
        for i in str(num):
            order.append(int(i))
    order.sort(reverse=True)
    return int(''.join(map(str, order)))

# Given an array (arr) as an argument
# complete the function countSmileys that should return the total number of smiling faces.
# Rules for a smiling face:
# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.
def count_smileys(arr):
    count = 0
    list = [':)', ':D', ';)', ';D', ':-)', ':~)', ';-)', ';~)', ':-D', ':~D', ';-D', ';~D']
    for elem in range(len(arr)):
        if arr[elem] in list:
            count += 1
    return count

# Given two numbers and an arithmetic operator (the name of it, as a string),
# return the result of the two numbers having that operator used on them.
# a and b will both be positive integers, and a will always be the first number in the operation,
# and b always the second.
# The four operators are "add", "subtract", "divide", "multiply".
def arithmetic(a, b, operator):
    if operator == 'add': return a + b
    elif operator == 'subtract': return a - b
    elif operator == 'multiply': return a * b
    elif operator == 'divide': return a / b

# You were camping with your friends far away from home,
# but when it's time to go back, you realize that your fuel is running out
# and the nearest pump is 50 miles away! You know that on average,
# your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple / list (depending on your language)
# like so: (index1, index2).
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]

# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
import re
def high_and_low(numbers):
    list = [int(s) for s in re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", numbers)]
    list.sort()
    integer = ''
    return integer + str(list[-1]) + ' ' + str(list[0])

# Given a non-empty array of integers, return the result of multiplying the values together in order.
def grow(arr):
    integer = 1
    for elem in arr:
        integer *= elem
    return integer

# Complete the solution so that it reverses the string passed into it.
def solution(string):
    return string[::-1]

# Finish the solution so that it sorts the passed in array of numbers.
# If the function passes in an empty array or null/nil value then it should return an empty array.
def solution(nums):
    if not nums:
        return []
    nums.sort()
    return nums

# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negatives, and the negatives become positives.
def invert(lst):
    return [i * -1 for i in lst]

# Use variables to find the sum of the goals Messi scored in 3 competitions
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard.
# It is your job to fix the code and get the program working again!
def say_hello(name):
    return 'Hello, ' + name

# Your task is to make function, which returns the sum of a sequence of integers.
# The sequence is defined by 3 non-negative values: begin, end, step (inclusive).
# If begin value is greater than the end, function should returns 0
def sequence_sum(begin_number, end_number, step):
    sum = 0
    for i in range(begin_number, end_number + 1, step):
        sum += i
    return sum

# Write a function that takes an array of words and smashes them together into a sentence
# and returns the sentence. You can ignore any need to sanitize words or add punctuation,
# but you should add spaces between each word.
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
def smash(words):
    return " ".join(words)

# However, sometimes, you can't arrange them into a square.
# Instead, you end up with an ordinary rectangle! Those blasted things!
# If you just had a way to know, whether you're currently working in vain…
# Wait! That's it! You just have to check if your number of building blocks is a perfect square.
import math

def is_square(n):
    if n < 0:
        return False
    return n == math.isqrt(n) ** 2

# Write a function that always returns 5
# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/
def unusual_five():
    return len('     ')

# This function should test if the factor is a factor of base.
# Return true if it is a factor or false if it is not.
def check_for_factor(base, factor):
    return base % factor == 0

# Given two integers a and b,
# which can be positive or negative, find the sum of all the integers between
# and including them and return it. If the two numbers are equal return a or b.
def get_sum(a,b):
    if a == b:
        return a
    list = []
    step = 1 if a < b else -1
    for i in range(a, b + step, step):
        list.append(i)
    return sum(list)

# In a factory a printer prints labels for boxes.
# For one kind of boxes the printer has to use colors which, for the sake of simplicity,
# are named with letters from a to m.
# The colors used by the printer are recorded in a control string.
# For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a,
# four times color b, one time color h then one time color a...
# Sometimes there are problems: lack of colors,
# technical malfunction and a "bad" control string is produced
# e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
def printer_error(s):
    return f"{len([n for n in s if n in 'nopqrstuvwxyz'])}/{len(s)}"

# Take 2 strings s1 and s2 including only letters from a to z.
# Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

# Americans are odd people: in their buildings, the first floor is actually the ground floor
# and there is no 13th floor (due to superstition).
# Write a function that given a floor in the american system returns the floor in the european system.
# With the 1st floor being replaced by the ground floor and the 13th floor being removed,
# the numbers move down to take their place. In case of above 13,
# they move down by two because there are two omitted numbers below them.
def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2

# In this simple exercise, you will build a program that takes a value, integer ,
# and returns a list of its multiples up to another value, limit .
# If limit is a multiple of integer, it should be included as well.
# There will only ever be positive integers passed into the function, not consisting of 0.
# The limit will always be higher than the base.
# For example, if the parameters passed are (2, 6),
# the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
# If you can, try writing it in only one line of code.
def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]

# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.
def count(string):
    dict = {}
    count = 0
    for char in string:
        count = string.count(char)
        dict[f"{char}"] = count
    return dict

# In mathematics, the factorial of a non-negative integer n, denoted by n!,
# is the product of all positive integers less than or equal to n.
# For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.
# Write a function to calculate factorial for a given input.
# If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#)
# or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript)
# or ValueError (Python) or return -1 (C).
import math
def factorial(n):
    if n > 12:
        raise ValueError
    return math.factorial(n)

# Messi is a soccer player with goals in three leagues:
# LaLiga
# Copa del Rey
# Champions
# Complete the function to return his total number of goals in all three leagues.
# Note: the input will always be valid.
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# Return the name of the winner. If there is no winner, return null (in Java and JavaScript),
# None (in Python), nil (in Ruby), or * in C.
# Task Description
# There are no given candidates. An elector can vote for anyone.
# Each ballot contains only one name and represents one vote for this name.
# A name is an arbitrary string, e.g. "A", "B", or "XJDHD".
# There are no spoiled ballots.
# The ballot-box is represented by an unsorted list of names.
# Each entry in the list corresponds to one vote for this name.
# You do not know the names in advance (because there are no candidates).
# A name wins the election if it gets more than n/2 votes
# (n = number of all votes, i.e. n is equal to the size of the given list).
def get_winner(ballots):
    list = []
    for elem in ballots:
        list.append(elem)
    elite = set(list)
    for char in elite:
        if list.count(char) > len(ballots) / 2 or list.count(char) == len(ballots):
            return char

# Sum all the numbers of a given array ( cq. list ),
# except the highest and the lowest element ( by value, not by index! ).
# The highest or lowest element respectively is a single element at each edge,
# even if there are more than one with the same value.
# Mind the input validation.
def sum_array(arr):
    if arr == [] or arr is None or len(arr) == 1:
        return 0
    integer = sum(arr)
    return integer - max(arr) - min(arr)

# You will be given an array and a limit value.
# You must check that all values in the array are below or equal to the limit value.
# If they are, return true. Else, return false.
# You can assume all values in the array are numbers.
def small_enough(array, limit):
    for elem in array:
        if elem > limit:
            return False
    return True

# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array or list ( depending on language ).
def count_by(x, n):
    list = []
    for i in range(x, x * n + 1, x):
        list.append(i)
    return list

# I created this function to add five to any number that was passed in to it
# and return the new value. It doesn't throw any errors but it returns the wrong number.
def add_five(num):
    return num + 5

# Your task is to sort a given string.
# Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.
def order(sentence):
    list = sentence.split()
    new_list = []
    for i in range(1, len(list) + 1):
        for elem in list:
            for char in elem:
                if char == str(i):
                    new_list.append(elem)
    return ' '.join(new_list)

# There is a queue for the self-checkout tills at the supermarket.
# Your task is write a function to calculate the total time required for all the customers to check out!
def queue_time(customers, n):
    time=[0]*n
    for custom in customers: time[time.index(min(time))]+=custom
    return max(time)

# You are given two arrays a1 and a2 of strings.
# Each string is composed with letters from a to z.
# Let x be any string in the first array and y be any string in the second array.
# Find max(abs(length(x) − length(y)))
# If a1 and/or a2 are empty return -1 in each language
# except in Haskell (F#) where you will return Nothing (None).
def mxdiflg(a1, a2):
    if a1 and a2: return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1

# Wolves have been reintroduced to Great Britain. You are a sheep farmer,
# and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue which is at the end of the array:
def warn_the_sheep(queue):
    if queue.index('wolf') == len(queue)-1:
        return 'Pls go away and stop eating my sheep'
    else:
        ind = len(queue) - queue.index('wolf') - 1
        return (f"Oi! Sheep number {ind}! You are about to be eaten by a wolf!")

# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other;
# return false otherwise.
def is_anagram(test, original):
    return set(test.lower()) == set(original.lower()) and len(test) == len(original)

# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.
def rps(p1, p2):
    if p1 == p2: return 'Draw!'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'Player 1 won!'
    elif p1 == 'scissors' and p2 == 'rock':
        return 'Player 2 won!'
    elif p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    elif p1 == 'rock' and p2 == 'paper':
        return 'Player 2 won!'
    elif p1 == 'paper' and p2 == 'scissors':
        return 'Player 2 won!'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'

# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World!
# if name is not given (or passed as an empty String).
# Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).
def hello(name=None):
    return ('Hello, World!' if not name else f"Hello, {name.title()}!")

# Timmy & Sarah think they are in love, but around where they live,
# they will only know once they pick a flower each.
# If one of the flowers has an even number of petals
# and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower
# and return true if they are in love and false if they aren't.
def lovefunc( flower1, flower2 ):
    return (flower1 % 2 != 0 and flower2 % 2 == 0) or (flower2 % 2 != 0 and flower1 % 2 == 0)

# A perfect number is a number in which the sum of its divisors (excluding itself) are equal to itself.
# Write a function that can verify if the given integer n is a perfect number,
# and return True if it is, or return False if not.
def isPerfect(n):
    return n in [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]

# Rules:
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
def people_with_age_drink(age):
    if age < 14: return 'drink toddy'
    elif age < 18: return 'drink coke'
    elif age < 21: return 'drink beer'
    elif age >= 21: return 'drink whisky'

# In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
# You will be passed a string
# and you must return that string in an array where an uppercase letter is a person standing up.
def wave(people):
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i].isalpha()]

# A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
# His mother looks out of a window 1.5 meters from the ground.
# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and h > window:
        count = 0
        while h > window:
            count += 1
            h = h * bounce
            if h > window:
                count += 1
        return count
    return -1

# Given a two-dimensional array of integers,
# return the flattened version of the array with all the integers in the sorted (ascending) order.
# Example:
def flatten_and_sort(array):
    new_list = [elem for sublist in array for elem in sublist]
    return sorted(new_list)

# Implement a pseudo-encryption algorithm which given a string S
# and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S,
# this process should be repeated N times.
def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


def decrypt_one_rep(encrypted_text):
    word1 = ""
    word2 = ""
    lenght = int(len(encrypted_text) / 2)
    word1 += encrypted_text[0:lenght]
    word2 += encrypted_text[lenght:]
    final_word = ""
    for i in range(0, lenght):
        final_word += word2[i] + word1[i]

    if len(encrypted_text) % 2 != 0:
        final_word += word2[lenght]
    return final_word


def decrypt(encrypted_text, n):
    if n < 0:
        return encrypted_text
    list = [encrypted_text]
    for i in range(1, n + 1):
        list.append(decrypt_one_rep(list[i - 1]))
    return list[n]

# You are given two sorted arrays that both only contain integers.
# Your task is to find a way to merge them into a single one, sorted in asc order.
# Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

# A string is considered to be in title case if each word in the string is either (a) capitalised
# (that is, only the first letter of the word is in upper case)
# or (b) considered to be an exception and put entirely into
# lower case unless it is the first word, which is always capitalised.
# Write a function that will convert a string into title case,
# given an optional list of exceptions (minor words).
# The list of minor words will be given as a string with each word separated by a space.
# Your function should ignore the case of the minor words string --
# it should behave in the same way even if the case of the minor word string is changed.
def title_case(title, minor_words=''):
    list2 = []
    list = [x.title() for x in title.split()]
    exam = [x.title() for x in minor_words.split()]
    if not list:
        return ''
    list2.append(list[0])
    list.pop(0)
    for elem in list:
        for i in range(len(exam)):
            if elem.lower() == exam[i].lower():
                list2.append(elem.lower())
                continue
        if elem not in exam:
            list2.append(elem.title())
    return ' '.join(list2)

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
def number(lines):
    list = []
    i = 1
    for elem in lines:
        list.append(f"{i}: {elem}")
        i += 1
    return list

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
def find_short(s):
    # your code here
    return len(list(i for i in sorted(s.split(), key=len))[0])

# Given a string str, reverse it and omit all non-alphabetic characters.
def reverse_letter(string):
    return ''.join(reversed(list(i for i in string if i in 'qwertyuiopasdfghjklzxcvbnm')))

# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
def find_it(seq):
    return min([i for i in seq if seq.count(i) % 2 != 0])

# Define a function that takes an integer argument and returns a logical value true
# or false depending on if the integer is a prime.
# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.
from math import sqrt
def is_prime(num):
    flag = True
    prime_flag = 0
    if(num > 1):
	    for i in range(2, int(sqrt(num)) + 1):
		    if (num % i == 0):
			    prime_flag = 1
			    break
	    if prime_flag == 0:
		    flag = True
	    else:
		    flag = False
    else:
	    flag = False
    return flag

# So this function should return the first pair of two prime numbers spaced
# with a gap of g between the limits m, n if these numbers exist otherwise `nil
# or null or None or Nothing (or ... depending on the language).
def gap(g, m, n):
    first_int = 0
    second_int = 0
    for i in range(m,n+1):
        if int_is_prime(i):
            if first_int == 0:
                first_int = i
            elif second_int == 0:
                second_int = i
            else:
                first_int = second_int
                second_int = i
        if second_int - first_int == g:
            return [first_int, second_int]
    return None

def int_is_prime(n):
    if n <= 0 or n == 1:
        return False
    i = 2
    while (i <= n ** 0.5 ):
        if n % i == 0:
            return False
        i += 1
    return True\

# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"].
# The second one contains a student's submitted answers.
# The two arrays are not empty and are the same length. Return the score for this array of answers,
# giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer,
# represented as an empty string (in C the space character is used).
def check_exam(arr1,arr2):
    count = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            count += 4
            continue
        elif arr2[i] == '':
            count += 0
            continue
        count -= 1
    return (count if count > 0 else 0)

# Given a 2D ( nested ) list ( array, vector, .. ) of size m * n,
# your task is to find the sum of the minimum values in each row.
def sum_of_minimums(numbers):
    return sum(min(i) for i in numbers)

# Complete the method which accepts an array of integers, and returns one of the following:
# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise
def is_sorted_and_how(arr):
    if sorted(arr, key = int) == arr:
        return 'yes, ascending'
    elif sorted(arr, key = int, reverse = True) == arr:
        return 'yes, descending'
    return 'no'

# Given a list of digits, return the smallest number that could be formed from these digits,
# using the digits only once (ignore duplicates).
def min_value(digits):
    list = sorted(set(digits))
    integer = ''
    for elem in list:
        integer += str(elem)
    return int(integer)

# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# The binary number returned should be a string.
def add_binary(a,b):
    sum = bin(int(a) + int(b))
    return ''.join(list(sum)[2:])

# The function chooseBestSum (or choose_best_sum or ... depending on the language)
# will take as parameters t (maximum sum of distances, integer >= 0),
# k (number of towns to visit, k >= 1) and ls (list of distances,
# all distances are positive or zero integers and this list has at least one element).
# The function returns the "best" sum ie the biggest possible sum of k distances less than
# or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing,
# depending on the language. In that case with C, C++, D, Dart, Fortran, F#, Go, Julia, Kotlin,
# Nim, OCaml, Pascal, Perl, PowerShell, Reason, Rust, Scala, Shell, Swift return -1.
import itertools
def choose_best_sum(t, k, ls):
    combinations = list(itertools.combinations(ls, k))
    condition = [sum(distance) for distance in combinations]
    condition2 = [distance for distance in condition if distance <= t]
    if condition2 == []:
        largest_distance = None
    else:
        largest_distance = max([distance for distance in condition if distance <= t])
    return largest_distance

# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
# after it in the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string,
# they should be returned as they are. Only letters from the latin/english alphabet should be shifted,
# like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.
def rot13(message):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    transform = dict(zip(key, val))
    return ''.join(transform.get(char, char) for char in message)

# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
def round_to_next5(n):
    if n == 0:
        pass
    elif abs(n)%5 == 0:
        pass
    else:
        n =  n - n%5 + 5
    return n

# You need to write a function that reverses the words in a given string.
# A word can also fit an empty string. If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
def reverse(st):
    return ' '.join(list(st.split())[::-1])

# Write a function named sumDigits which takes a number as input
# and returns the sum of the absolute value of each of the number's decimal digits.
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))

# As a part of this Kata, you need to create a function that when provided with a triplet,
# returns the index of the numerical element that lies between the other two elements.
# The input to the function will be an array of three distinct numbers (Haskell: a tuple).
def gimme(input_array):
    return [input_array.index(i) for i in input_array if min(input_array) < i < max(input_array)][0]

# The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
# They would like your help with an application form that will tell prospective members
# which category they will be placed.
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
def open_or_senior(data):
    return ['Senior' if elem[0] >= 55 and elem[1] > 7 else 'Open' for elem in data]

# Alice and Bob were on a holiday. Both of them took many pictures of the places they've been,
# and now they want to show Charlie their entire collection.
# However, Charlie doesn't like these sessions, since the motif usually repeats.
# He isn't fond of seeing the Eiffel tower 40 times.
# He tells them that he will only sit for the session if they show the same motif at most N times.
# Luckily, Alice and Bob are able to encode the motif as a number.
# Can you help them to remove numbers such that their list contains each number only up to N times,
# without changing the order?
def delete_nth(order,max_e):
    sort_list = []
    for elem in order:
        if sort_list.count(elem) >= max_e:
            continue
        sort_list.append(elem)
    return sort_list

# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
# Your function product Fib takes an integer(prod) and returns an array
# depending on the language if F(n) * F(n+1) = prod.
def productFib(prod):
    First_val = 0
    Second_val = 1
    next = 0
    while First_val * Second_val < prod:
            next = First_val + Second_val
            First_val = Second_val
            Second_val = next
    return [First_val, Second_val, True if First_val * Second_val == prod else False]

# Given a sequence of numbers, find the largest pair sum in the sequence.
def largest_pair_sum(numbers):
    return sorted(numbers)[-1] + sorted(numbers)[-2]

# Your task is to write a function which calculates the value
# of a word based off the sum of the alphabet positions of its characters.
# The input will always be made of only lowercase letters and will never be empty.
def words_to_marks(s):
    return sum(ord(char) - 96 for char in s)

# We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day (evap_per_day)
# and the threshold (threshold) in percentage beyond which the evaporator is no longer useful.
# All numbers are strictly positive.
def evaporator(content, evap_per_day, threshold):
    result = 0;
    percentage = 100;
    while percentage > threshold:
        percentage = percentage - percentage * (evap_per_day / 100)
        result += 1
    return result

# You will be given an array of numbers. You have to sort the odd numbers
# in ascending order while leaving the even numbers at their original positions.
def sort_array(source_array):
    odds = iter(sorted(elem for elem in source_array if elem % 2))
    return [next(odds) if elem % 2 else elem for elem in source_array]

# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).
def solution(string, ending):
    return string[::-1][:len(ending)] == ending[::-1]

# Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does,
# he wants to know how many years 'Y' this sum 'P' has to be kept in the bank
# in order for it to amount to a desired sum of money 'D'.
# The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly.
# After paying taxes 'T' for the year the new sum is re-invested.
# Note to Tax: not the invested principal is taxed, but only the year's accrued interest
def calculate_years(principal, interest, tax, desired):
    count = 0
    if principal == desired:
            return count
    while principal < desired:
        count += 1
        percent = principal * interest - (principal * interest * tax)
        principal += percent
    return count

# A stream of data is received and needs to be reversed.
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
def data_reverse(data):
    return [elem for i in range(len(data), -1, -8) for elem in data[i: i + 8]]

# Implement a function that accepts 3 integer values a, b, c.
# The function should return true if a triangle can be built with
# the sides of given length and false in any other case.
def is_triangle(a, b, c):
    return max(a, b ,c) < a + b + c - max(a, b ,c)

# Your task is to write function factorial.
import math
def factorial(n):
    return math.factorial(n)

# Given an array of numbers, return a new array of length number containing the last even numbers
# from the original array (in the same order). The original array will be not empty
# and will contain at least "number" even numbers.
def even_numbers(arr,n):
    return [i for i in arr[::-1] if i % 2 == 0][:n][::-1]

# My grandfather always predicted how old people would get,
# and right before he passed away he revealed his secret!
# In honor of my grandfather's memory we will write a function using his formula!
# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself.
# Add them all together.
# Take the square root of the result.
# Divide by two.
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    return sum([age_1**2, age_2**2, age_3**2, age_4**2, age_5**2, age_6**2, age_7**2, age_8**2])**0.5 // 2

# We want to know the index of the vowels in a given word,
# for example, there are two vowels in the word super (the second and fourth letters).
# So given a string "super", we should return a list of [2, 4].
def vowel_indices(word):
    return [index + 1 for index, elem in enumerate(word) if elem.lower() in 'aeoiuy']

# Introduction
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters.
# The tension between left side letters and right side letters was too high and the war began.
# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight.
# When the left side wins return Left side wins!, when the right side wins return Right side wins!,
# in other case return Let's fight again!.
def alphabet_war(fight):
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_count = 0
    right_count = 0
    for char in fight:
        if char in left_side:
            left_count += left_side[char]
        elif char in right_side:
            right_count += right_side[char]
    if left_count > right_count:
        return 'Left side wins!'
    elif right_count > left_count:
        return 'Right side wins!'
    return "Let's fight again!"

# Several people are standing in a row divided into two teams.
# The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.
# Task
# Given an array of positive integers (the weights of the people),
# return a new array/tuple of two integers, where the first one is the total weight of team 1,
# and the second one is the total weight of team 2.
def row_weights(array):
    return sum(i for i in array[::2]), sum(i for i in array[1::2])

# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters
# and your task is to convert that string to either lowercase only or uppercase only based on:
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
def solve(s):
    count_lower: int = 0
    count_upper: int = 0
    for i in s:
        if i.islower():
            count_lower += 1
            continue
        count_upper += 1
    if count_lower >= count_upper:
        return s.lower()
    return s.upper()

# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year and moreover 50 new inhabitants
# per year come to live in the town. How many years does the town need
# to see its population greater or equal to p = 1200 inhabitants?
def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        p0 += int(p0 * (percent / 100) + aug)
        count += 1
    return count

# Find the total sum of internal angles (in degrees) in an n-sided simple polygon. N will be greater than 2.
def angle(n):
    return 180 * (n - 2)

# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
def binary_array_to_number(arr):
    return int("".join([str(i) for i in arr]), 2)

# Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.
# Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.)
# obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."
def sum_triangular_numbers(n):
    if n < 0:
        return 0
    sum = sum_triangular_numbers(n-1)
    return sum + (n * (n + 1)) / 2

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken
# to the successive powers of p is equal to k * n.
def dig_pow(n, p):
    count = 0
    for char in str(n):
        count += int(char) ** p
        p += 1
    return count // n if count % n == 0 else -1

# You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.
def longest_consec(strarr, k):
    return max(["".join(strarr[i:i+k]) for i in range(len(strarr)-k+1)], key=len)\
        if strarr and 0 < k <= len(strarr) else ""

# Let us begin with an example:
# A man has a rather old car being worth $2000.
# He saw a secondhand car being worth $8000.
# He wants to keep his old car until he can buy the secondhand one.
# He thinks he can save $1000 each month but the prices of his old car
# and of the new one decrease of 1.5 percent per month.
# Furthermore this percent of loss increases of 0.5 percent at the end of every two months.
# Our man finds it difficult to make all these calculations.
def nbMonths(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    months = 0
    savings = 0
    while start_price_old + savings < start_price_new:
        months += 1
        savings += saving_per_month
        if months % 2 == 0:
            percent_loss_by_month += 0.5
        start_price_old *= ((100 - percent_loss_by_month) / 100)
        start_price_new *= ((100 - percent_loss_by_month) / 100)
    return [months, round(start_price_old + savings - start_price_new)]

# Your car is old, it breaks easily. The shock absorbers are gone
# and you think it can handle about 15 more bumps before it dies totally.
# Unfortunately for you, your drive is very bumpy! Given a string showing either flat road (_) or bumps (n).
# If you are able to reach home safely by encountering 15 bumps or less, return Woohoo!, otherwise return Car Dead
def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"

# Find the number with the most digits.
# If two numbers in the argument array have the same number of digits, return the first one in the array.
def find_longest(arr):
    arr_len = [len(str(n)) for n in arr]
    return arr[arr_len.index(max(arr_len))]

# There are pillars near the road. The distance between the pillars is the same
# and the width of the pillars is the same. Your function accepts three arguments:
# number of pillars (≥ 1);
# distance between pillars (10 - 30 meters);
# width of the pillar (10 - 50 centimeters).
# Calculate the distance between the first and the last pillar in centimeters
# (without the width of the first and last pillar).
def pillars(num_pill, dist, width):
    return (num_pill - 2) * width + (100 * dist) * (num_pill - 1) if num_pill > 1 else 0

# What if we need the length of the words separated by a space
# to be added at the end of that same word and have it returned as an array?
def add_length(str_):
    return [f"{i} {len(i)}" for i in str_.split()]

# You're re-designing a blog and the blog's posts have the following format
# for showing the date and time a post was made:
# Weekday Month Day, time e.g., Friday May 2, 7pm
# You're running out of screen real estate, and on some pages you want
# to display a shorter format, Weekday Month Day that omits the time.
# Write a function, shortenToDate, that takes the Website date/time
# in its original string format, and returns the shortened format.
# Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm".
# Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".
def shorten_to_date(long_date):
    return long_date.split(',')[0]

# A student was working on a function and made some syntax mistakes while coding.
# Help them find their mistakes and fix them.
def main(verb, noun):
    return verb + noun

# Code as fast as you can! You need to double the integer and return it.
def doubleInteger(i):
    return i * 2

# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accept 1 parameters:
# n, n is the number of customers to buy hotdogs, different numbers have different
# prices (refer to the following table), return a number that the customer need to pay how much money.
def sale_hotdogs(n):
    if n < 5: return n * 100
    elif 5 <= n < 10: return n * 95
    return n * 90

# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
def replace_exclamation(s):
    for char in s:
        if char.lower() in 'aeiou':
            s = s.replace(char, '!')
    return s

# I will give you an integer. Give me back a shape that is as long
# and wide as the integer. The integer will be a whole number between 1 and 50.
def generate_shape(n: int) -> str:
    return '\n'.join(['+' * n] * n)

# Create a function called _if which takes 3 arguments:
# a boolean value bool and 2 functions (which do not take any parameters): func1 and func2
# When bool is truth-ish, func1 should be called, otherwise call the func2.
def _if(bool, func1, func2):
    return func1() if bool == True else func2()

# Your task is to write a function which returns the sum of following series upto nth term(parameter).
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

# Define a function that removes duplicates from an array of numbers and returns it as a result.
# The order of the sequence has to stay the same.
def distinct(seq):
    new_list = []
    for elem in seq:
        if elem not in new_list:
            new_list.append(elem)
    return new_list

# Given an array of numbers, check if any of the numbers are the character codes
# for lower case vowels (a, e, i, o, u).
# If they are, change the array value to a string of that vowel.
# Return the resulting array.
def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(elem, elem) for elem in s]

# In Python, there is a built-in filter function that operates similarly to JS's filter.
# For more information on how to use this function, visit https://docs.python.org/3/library/functions.html#filter
def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
def alphabet_position(text):
    return ' '.join([str(ord(char) - 96) for char in text.lower() if char >= 'a' and char<= 'z'])

# Complete the method which returns the number which is most frequent in the given input array.
# If there is a tie for most frequent number, return the largest number among them.
# Note: no empty arrays will be given.
from collections import Counter
def highest_rank(arr):
    c = Counter(arr)
    m = max(c.values())
    return max(k for k, v in c.items() if v == m)

# We want to generate a function that computes the series starting from 0 and ending until the given number.
def show_sequence(n):
    sum=0
    s=''
    if n==0:
        return "0=0"
    elif n<0:
        return str(n)+"<0"
    else:
        for i in range(0,n+1):
            sum += i
            s+=str(i)+'+'
        s = s.strip('+')
        s = s +" = "+str(sum)
        return s

# Remove all exclamation marks from the end of sentence.
def remove(s):
    while s.endswith('!'):
        s = s[:-1]
    return s

# Write a function that will check if two given characters are the same case.
# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
def same_case(a: str, b: str) -> int:
    if not a.isalpha() or not b.isalpha():
        return -1
    return 1 if a.islower() and b.islower() or a.isupper() and b.isupper() else 0

# Write a function that returns a string in which firstname is swapped with last name.
def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])

# To find the volume (centimeters cubed) of a cuboid you use the formula:
# volume = Length * Width * Height
# But someone forgot to use proper record keeping,
# so we only have the volume, and the length of a single side!
# It's up to you to find out whether the cuboid has equal sides (= is a cube).
def cube_checker(volume, side):
    return volume == side ** 3 if volume > 0 and side > 0 else False

# You've just moved into a perfectly straight street with exactly n identical houses
# on either side of the road. Naturally, you would like to find out the house number
# of the people on the other side of the street.
def over_the_road(address, n):
    return (n * 2) - address + 1

# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b))
# that checks whether the two arrays have the "same" elements, with the same multiplicities
# (the multiplicity of a member is the number of times it appears). "Same" means,
# here, that the elements in b are the elements in a squared, regardless of the order.
def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    return sorted(number ** 2 for number in array1) == sorted(array2)

# Output: String with comma delimited elements of the array in th same order.
def print_array(arr):
    return ','.join(str(i) for i in arr)

# An AI has infected a text with a character!!
# This text is now fully mutated to this character.
# If the text or the character are empty, return an empty string.
# There will never be a case when both are empty as nothing is going on!!
# Note: The character is a string of length 1 or an empty string.
def contamination(text, char):
    return char * len(text) if text and char != '' else ''

# Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum.
# Assume that the input n will always be a positive integer.
def sum_cubes(n):
    return sum(i**3 for i in range(n + 1))

# We need a simple function that determines if a plural is needed or not.
# It should take a number, and return true if a plural should
# be used with that number or false if not. This would be useful when printing
# out a string such as 5 minutes, 14 apples, or 1 sun.
# You only need to worry about english grammar rules for this kata,
# where anything that isn't singular (one of something), it is plural (not one of something).
def plural(n):
    return n != 1

# You will be given an array a and a value x. All you need to do
# is check whether the provided array contains the value, without using a loop.
# Array can contain numbers or strings. x can be either. Return true
# if the array contains the value, false if not. With strings you will need to account for case.
def check(a, x):
    return x in a

# Given a variable n,
# If n is an integer, Return a string with dash'-'marks before and after each odd integer,
# but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.
# If n is not an integer, return the string "None".
def dashatize(num):
    num_str = str(num)
    for i in ['1','3','5','7','9']:
        num_str = num_str.replace(i,'-' + i + '-')
    return num_str.strip('-').replace('--','-')

# Fix the variables assigments so that this code stores the string 'devLab' in the variable name.
a, b, name = 'dev', 'Lab', 'devLab'

# Determine the total number of digits in the integer (n>=0) given
# as input to the function. For example, 9 is a single digit,
# 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.
def digits(n):
    return len(str(n))

# Christmas is coming and many people dreamed of having a ride with Santa's sleigh.
# But, of course, only Santa himself is allowed to use this wonderful transportation.
# And in order to make sure, that only he can board the sleigh, there's an authentication mechanism.
# Your task is to implement the authenticate() method of the sleigh, which takes the name of the person,
# who wants to board the sleigh and a secret password. If, and only if,
# the name equals "Santa Claus" and the password is "Ho Ho Ho!"
# (yes, even Santa has a secret password with uppercase and lowercase letters
# and special characters :D), the return value must be true. Otherwise it should return false.
class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'

# Your mission:
# Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
# A coupon is no more valid on the day AFTER the expiration date.
# All dates will be passed as strings in this format: "MONTH DATE, YEAR".
from datetime import date
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    month = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
            'November': 11, 'December': 12}
    if entered_code is correct_code:
        current_date = current_date.replace(',', '')
        expiration_date = expiration_date.replace(',', '')
        formatted_current = [month.get(i) if i in month.keys() else int(i) for i in current_date.split()]
        formatted_expiration = [month.get(i) if i in month.keys() else int(i) for i in expiration_date.split()]
        to_date_current = date(formatted_current[2], formatted_current[0], formatted_current[1])
        to_date_formatted_expiration = date(formatted_expiration[2], formatted_expiration[0], formatted_expiration[1])
        if to_date_current <= to_date_formatted_expiration:
            return True
        return False
    return False

# Complete the function, which calculates how much you need to
# tip based on the total amount of the bill and the service.
import math
def calculate_tip(amount, rating):
    rating_dict = {'poor': 5, 'good': 10, 'great': 15, 'excellent': 20, 'terrible': 0}
    if rating.lower() in rating_dict:
        return math.ceil(rating_dict[rating.lower()] * amount / 100)
    return 'Rating not recognised'

# You get any card as an argument. Your task is to return the suit of this card (in lowercase).
def define_suit(card):
    return 'clubs' if 'C' in card else 'spades' if 'S' in card\
        else 'diamonds' if 'D' in card else 'hearts' if 'H' in card else None

# Create a method that accepts a list and an item,
# and returns true if the item belongs to the list, otherwise false.
def include(arr,item):
    return item in arr

# You have to write a function that describe Leo:
# def leo(oscar):
#   pass
# if oscar was (integer) 88, you have to return "Leo finally won the oscar! Leo is happy".
# if oscar was 86, you have to return "Not even for Wolf of wallstreet?!"
# if it was not 88 or 86 (and below 88) you should return "When will you give Leo an Oscar?"
# if it was over 88 you should return "Leo got one already!"
def leo(oscar):
    if oscar == 88: return 'Leo finally won the oscar! Leo is happy'
    elif oscar == 86: return 'Not even for Wolf of wallstreet?!'
    elif oscar != 88 and oscar != 86 and oscar < 88: return 'When will you give Leo an Oscar?'
    elif oscar > 88: return 'Leo got one already!'

# Given a string s, write a method (function) that will return true if
# its a valid single integer or floating number or false if its not.
def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False

# The objective of Duck, duck, goose is to walk in a circle, tapping on each player's head until one is chosen.
def duck_duck_goose(players, goose):
    while len(players) < goose:
        goose -= len(players)
    return players[goose - 1].name

# Make a function that will return a greeting statement that uses an input;
# your program should return, "Hello, <name> how are you doing today?".
def greet(name):
    return f'Hello, {name} how are you doing today?'

# Write a function that returns the total surface area and volume of a box as an array: [area, volume]
def get_size(w,h,d):
    return [((w * h) + (w * d) + (h * d)) * 2, w * h * d]

# Write a function which removes from string all non-digit characters
# and parse the remaining to number. E.g: "hell5o wor6ld" -> 56
def get_number_from_string(string):
    return int(''.join(list(i for i in string if i in '0123456789')))\

# Your task is to sum the differences between consecutive pairs in the array in descending order.
def sum_of_differences(arr):
    arr = sorted(arr, reverse = True)
    list = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            list.append(arr[i] - arr[j])
    return max(list) if len(arr) > 1 else 0

# Basic regex tasks. Write a function that takes in a numeric code of any length.
# The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.
def validate_code(code):
    return str(code)[0] in '123'

# Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .
def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))

# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
#  the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.
def up_array(arr):
    integer = ''
    list = []
    print(arr)
    if len(arr) < 1 :
        return None
    elif len(arr) == 1 and arr[0] <=9:
        return [1]
    for i in arr:
        if len(str(i)) > 1 or i < 0:
            return None
    else:
        for elem in arr:
            if str(elem) in '1234567890':
                integer += str(elem)
    if integer[0] == '0' and integer[1] != '0':
        integer = int(integer[1:]) + 1
        integer = '0' + str(integer)
    elif integer[0] == '0' and integer[1] == '0':
        integer = int(integer[2:]) + 1
        integer = '00' + str(integer)
    elif integer[0] != '0':
        integer = str(int(integer) + 1)
    for char in integer:
        list.append(int(char))
    return list

# We want an array, but not just any old array, an array with contents!
# Write a function that produces an array with the numbers 0 to N-1 in it.
# For example, the following code will result in an array containing the numbers 0 to 4
def arr(n=0):
    return list(range(n))

# Time to test your basic knowledge in functions! Return the odds from a list:
# [1, 2, 3, 4, 5]  -->  [1, 3, 5]
# [2, 4, 6]        -->  []
odds = lambda list: [i for i in list if i % 2 !=0]

# Create a function close_compare that accepts 3 parameters: a, b, and an optional margin.
# The function should return whether a is lower than, close to, or higher than b.
# a is considered "close to" b if margin is greater than or equal to the distance between a and b.
def close_compare(a, b, margin=0):
    if a < b and b - a > margin: return -1
    elif a - b > margin and a > b: return 1
    elif a - b <= margin: return 0

# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
# Square all numbers k (0 <= k <= n) between 0 and n.
# Count the numbers of digits d used in the writing of all the k**2.
# Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.
def nb_dig(n, d):
    values_list = list(range(0, n+1))
    list_squared = list(map(lambda x: str(x**2), values_list))
    str_list_squared = ''.join(list_squared)
    print(str(d))
    return str_list_squared.count(str(d))

# Due to another of his misbehaved, the primary school's teacher of the young Gauß,
# Herr J.G. Büttner, to keep the bored and unruly young schoolboy Karl Friedrich Gauss
# busy for a good long time, while he teaching arithmetic to his mates,
# assigned him the problem of adding up all the whole numbers from 1 through a given number n.
def f(n):
    return sum(range(1, n + 1)) if type(n) is int and n > 0 else None

# Your friend invites you out to a cool floating pontoon around 1km off the beach.
# Among other things, the pontoon has a huge slide that drops you out right into the ocean,
# a small way from a set of stairs used to climb out.
# As you plunge out of the slide into the water, you see a shark hovering
# in the darkness under the pontoon... Crap!
# You need to work out if the shark will get to you before you can get to the pontoon.
# To make it easier... as you do the mental calculations in the water you either freeze
# when you realise you are dead, or swim when you realise you can make it!
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        if pontoon_distance / you_speed < shark_distance / (shark_speed / 2):
            return 'Alive!'
        else:
            return 'Shark Bait!'
    elif pontoon_distance / you_speed > shark_distance / shark_speed:
        return 'Shark Bait!'
    elif pontoon_distance / you_speed < shark_distance / shark_speed:
        return 'Alive!'

# Get ASCII value of a character.
def get_ascii(c):
   return ord(c)

# Write a function that takes a single string (word) as argument.
# The function must return an ordered list containing the indexes of all capital letters in the string.
def capitals(word):
    return [value for value, i in enumerate(word) if i.isupper()]

# Complete the function which converts hex number (given as a string) to a decimal number.
def hex_to_dec(s):
    return int(s, 16)

# Create a combat function that takes the player's current health
# and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.
def combat(health, damage):
    return health - damage if health > damage else 0

# Find the sum of all multiples of n below m
# Keep in Mind
# n and m are natural numbers (positive integers)
# m is excluded from the multiples
def sum_mul(n, m):
    return sum(range(n, m, n)) if m > 0 and n > 0 else 'INVALID'

# Your job is simple, if x squared is more than 1000,
# return It's hotter than the sun!!, else, return Help yourself to a honeycomb Yorkie for the glovebox.
# Note: Input will either be a positive integer (or a string for untyped languages).
def apple(x):
  return "It's hotter than the sun!!" if int(x)**2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."

# You are required to create a simple calculator that returns
# the result of addition, subtraction, multiplication or division of two numbers.
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.
# if the variables are not numbers or the sign does not belong to the list above
# a message "unknown value" must be returned.
def calculator(x,y,op):
    if type(x) == int and type(y) == int:
        dict_op = {'+': x+y, '-': x-y, '*': x*y, '/': x/y}
        if op in dict_op and x !=0 and y !=0:
            return dict_op[op]
        else:
            return 'unknown value'
    return 'unknown value'

# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed
# of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells.
# RNA differs slightly from DNA its chemical structure and contains no Thymine.
# In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a function which translates a given DNA string into RNA.
def dna_to_rna(dna):
    dict = {'G': 'G', 'C': 'C', 'A': 'A', 'T': 'U'}
    return ''.join(list(dict[char] for char in dna))

# Find the sum of the odd numbers within an array, after cubing the initial integers.
# The function should return undefined/None/nil/NULL if any of the values aren't numbers.
# Note: Booleans should not be considered as numbers.
def cube_odd(arr):
    for elem in arr:
        if type(elem) != int:
            return None
    return sum([i**3 for i in arr if i % 2 != 0])

# You must implement a function that returns the difference between the largest
# and the smallest value in a given list / array (lst) received as the parameter.
# lst contains integers, that means it may contain some negative numbers
# if lst is empty or contains a single element, return 0
# lst is not sorted
def max_diff(lst):
    return max(lst) - min(lst) if lst else 0

# Your task is simply to count the total number of lowercase letters in a string.
def lowercase_count(strng):
    return len(list(i for i in strng if i.islower()))

# Return an array/list where Even numbers come first then odds
# Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .
# Array/list size is at least 4 .
# Array/list numbers could be a mixture of positives , negatives .
# Have no fear , It is guaranteed that no Zeroes will exists .
def men_from_boys(arr):
    return sorted(list(set(list(i for i in arr if i % 2 == 0)))) +\
           sorted(list(set(list(i for i in arr if i % 2 != 0))), reverse = True)

# Step 1: Create a function called encode() to replace all
# the lowercase vowels in a given string with numbers according to the following pattern:
# For example, encode("hello") would return "h2ll4".
# There is no need to worry about uppercase vowels in this kata.
# Step 2: Now create a function called decode() to turn the numbers
# back into vowels according to the same pattern shown above.
# For example, decode("h3 th2r2") would return "hi there".
# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
def encode(st):
    dict = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    return ''.join([dict[char] if char in dict else char for char in st])


def decode(st):
    dict = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    return ''.join([dict[char] if char in dict else char for char in st])

# You can print your name on a billboard ad. Find out how much it will cost you.
# Each character has a default price of £30, but that can be different if you are given 2 parameters instead of 1.
# You can not use multiplier "*" operator.
# If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a character).
def billboard(name, price=30):
    return sum(price for i in range(len(name)))

# Complete the function which converts a binary number (given as a string) to a decimal number.
def bin_to_decimal(inp):
    return int(inp, 2)

# Given an array/list of integers, find the Nth smallest element in the array.
# Notes
# Array/list size is at least 3.
# Array/list's numbers could be a mixture of positives , negatives and zeros.
# Repetition in array/list's numbers could occur, so don't remove duplications.
def nth_smallest(arr, pos):
    return sorted(arr)[pos-1]

# Implement String#digit? (in Java StringUtils.isDigit(String)),
# which should return true if given object is a digit (0-9), false otherwise.
def is_digit(n):
    return n in '0123456789' and n != ''

# Given a mixed array of number and string representations of integers, add up the non-string integers
# and subtract this from the total of the string integers.
# Return as a number.
def div_con(x):
    return sum(list(i if type(i) == int else 0 for i in x)) - sum(list(int(i) if type(i) == str else 0 for i in x ))

# A balanced number is a number where the sum of digits to the left of the middle digit(s)
# and the sum of digits to the right of the middle digit(s) are equal.
# If the number has an odd number of digits, then there is only one middle digit.
# (For example, 92645 has one middle digit, 6.) Otherwise, there are two middle digits.
# (For example, the middle digits of 1301 are 3 and 0.)
# The middle digit(s) should not be considered when determining whether a number is balanced or not,
# e.g. 413023 is a balanced number because the left sum and right sum are both 5.
# The task
# Given a number, find if it is balanced, and return the string "Balanced" or "Not Balanced" accordingly.
# The passed number will always be positive.
def balanced_num(number):
    s = str(number)
    l = (len(s)-1)//2
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"

# A number is called Automorphic number if and only if its square ends in the same digits as the number itself.
# Task
# Given a number determine if it Automorphic or not .
def automorphic(n):
    return 'Automorphic' if str(n**2).count(str(n)) else 'Not!!'

# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity
# to go for a short walk. The city provides its citizens with a Walk Generating App on
# their phones -- everytime you press the button it sends you an array of one-letter
# strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction)
# and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you
# will take you exactly ten minutes (you don't want to be early or late!) and will,
# of course, return you to your starting point. Return false otherwise.
def is_valid_walk(walk):
    list = []
    dict = {'n': 's', 's': 'n',
           'e': 'w', 'w': 'e'}
    if len(walk) == 10:
        for elem in walk:
            list.append(walk.count(elem) == walk.count(dict[elem]))
        print(list)
        return False not in list
    return False

# Write a function get_char() / getChar() which takes a number and returns the corresponding ASCII char for that value.
def get_char(c):
    return chr(c)

#Complete the function that takes two numbers as input,
# num and nth and return the nth digit of num (counting from right to left).
# Note
# If num is negative, ignore its sign and treat it as a positive value
# If nth is not positive, return -1
# Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0
def find_digit(num, nth):
    return int(str(num)[-nth]) if nth <= len(str(num)) and nth > 0 else -1 if nth <= 0 else 0

# Write function parse_float which takes a string/list and returns a number
# or 'none' if conversion is not possible.
def parse_float(string):
    try: return float(string)
    except Exception:
        return None

# Your task, is to create NxN multiplication table, of size provided in parameter.
def multiplication_table(size):
    return [[i * n for i in range(1, size + 1)] for n in range(1, size + 1)]

# Your task is to return the correct string using the Template String Feature.
def temple_strings(obj, feature):
    return f"{obj} are {feature}"

# Count the number of occurrences of each character
# and return it as a (list of tuples) in order of appearance. For empty output return (an empty list).
# Consult the solution set-up for the exact data structure implementation depending on your language.
import collections
def ordered_count(inp):
    return list(collections.Counter(inp).items())

# Modify the spacify function so that it returns the given string with spaces inserted between each character.
def spacify(string):
    return " ".join(string)

# Your boss decided to save money by purchasing some cut-rate optical character
# recognition software for scanning in the text of old novels to your database.
# At first it seems to capture words okay, but you quickly notice that it throws
# in a lot of numbers at random places in the text.
def string_clean(s):
    return ''.join('' if ch.isdigit() else ch for ch in s)

# iven an array/list [] of n integers , find maximum triplet sum in the array Without duplications .
# Notes :
# Array/list size is at least 3 .
# Array/list numbers could be a mixture of positives , negatives and zeros .
# Repetition of numbers in the array/list could occur , So (duplications are not included when summing).
def max_tri_sum(numbers):
    return sum(list(sorted(set(numbers), reverse = True))[:3])

# The word i18n is a common abbreviation of internationalization
# in the developer community, used instead of typing the whole word
# and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.
# Write a function that takes a string and turns any and all "words"
# (see below) within that string of length 4 or greater into an abbreviation, following these rules:
# A "word" is a sequence of alphabetical characters. By this definition,
# any other character like a space or hyphen (eg. "elephant-ride")
# will split up a series of letters into two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter,
# then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").
def abbreviate(s):
    word = ""
    sentence = []
    result = []
    for i in s:
        if i.isalpha():
            word += i
        else:
            sentence.append(word)
            sentence.append(i)
            word = ""
            continue
    if word:
        sentence.append(word)
    for i in sentence:
        if len(i) >= 4:
            result += i[0] + str(len(i)-2) + i[-1]
        else:
            result += i
    return "".join(result)

# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
def shortcut( s ):
    return ''.join([i if i not in 'aeoiu' else '' for i in s])

# Philip's just turned four and he wants to know how old he will be
# in various years in the future such as 2090 or 3044.
# His parents can't keep up calculating this so they've begged
# you to help them out by writing a programme that can answer Philip's endless questions.
# Your task is to write a function that takes two parameters:
# the year of birth and the year to count years in relation to.
# As Philip is getting more curious every day he may soon want to know how many years
# it was until he would be born, so your function needs to work with both dates in the future and in the past.
# Provide output in this format: For dates in the future:
# "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)."
# If the year of birth equals the year requested return: "You were born this very year!"
# "..." are to be replaced by the number, followed and proceeded by a single space.
# Mind that you need to account for both "year" and "years", depending on the result.
def calculate_age(year_of_birth, current_year):
    return f"You are {current_year - year_of_birth} {'year' if current_year - year_of_birth == 1 else 'years'} old."\
        if year_of_birth < current_year else\
        f"You will be born in {year_of_birth - current_year}" \
        f" {'year' if year_of_birth - current_year == 1 else 'years'}." \
            if year_of_birth > current_year else 'You were born this very year!'

# Reverse every other word in a given string, then return the string.
# Throw away any leading or trailing whitespace, while ensuring there
# is exactly one space between each word. Punctuation marks should be
# treated as if they are a part of the word in this kata.
def reverse_alternate(s):
    list = s.split()
    for elem in list[1::2]:
        word = elem[::-1]
        list.insert(list.index(elem), word)
        list.remove(elem)
    return ' '.join(list)

# This is the first step to understanding FizzBuzz.
# Your inputs: a positive integer, n, greater than or equal to one.
# n is provided, you have NO CONTROL over its value.
# Your expected output is an array of positive integers from 1 to n (inclusive).
# Your job is to write an algorithm that gets you from the input to the output.
def pre_fizz(n):
    return [i for i in range(1, n + 1)]

# You'll be given a string, and have to return the sum of all characters as an int.
# The function should be able to handle all ASCII characters.
def uni_total(s):
    return sum(ord(i) for i in s)

# Complete the function that calculates the area of the red square,
# when the length of the circular arc A is given as the input. Return the result rounded to two decimals.
from math import pi

def square_area(A):
    return round((2 * A / pi) ** 2, 2)

# Write a function called sortGiftCode/sort_gift_code/SortGiftCode that accepts
# a string containing up to 26 unique alphabetical characters, and returns
# a string containing the same characters in alphabetical order.
def sort_gift_code(code):
    return "".join(sorted(code))

# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method/Info getter which should return johns age is 34
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

# Given a string of words (x), you need to return an array of the words,
# sorted alphabetically by the final character in each.
# If two words have the same last letter, they returned array should show
# them in the order they appeared in the given string.
def last(s):
    return sorted(s.split(), key=lambda x: x[-1])

# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
def adjacent_element_product(array):
    return max(a * b for a, b in zip(array, array[1:]))

# Write a small function that returns the values of an array that are not odd.
# All values in the array will be integers. Return the good values in the order they are given.
def no_odds(values):
    return [i for i in values if i % 2 == 0]

# You are given a string containing a sequence of character sequences separated by commas.
# Write a function which returns a new string containing the same character sequences except
# the first and the last ones but this time separated by spaces.
# If the input string is empty or the removal of the first
# and last items would cause the resulting string to be empty,
# return an empty value (represented as a generic value NULL in the examples below).
def array(string):
    return ' '.join(string.split(',')[1:-1]) or None

# Complete the function which returns the weekday according to the input number:
# Otherwise returns "Wrong, please enter a number between 1 and 7"
def whatday(num):
    dict = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday',
            4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    return dict[num] if num in dict else 'Wrong, please enter a number between 1 and 7'

# Write a function, persistence, that takes in a positive parameter num
# and returns its multiplicative persistence, which is the numbe
# r of times you must multiply the digits in num until you reach a single digit.
def persistence(n):
    count = 0
    integer = 1
    while len(str(n)) > 1:
        count += 1
        for elem in str(n):
            integer *= int(elem)
        n = integer
        integer = 1
    return count

# Create a function named (combine_names) that accepts two parameters
# (first and last name). The function should return the full name.
def combine_names(first, last):
    return first + ' ' + last

# Don Drumphet lives in a nice neighborhood,
# but one of his neighbors has started to let his house go.
# Don Drumphet wants to build a wall between his house and his neighbor’s,
# and is trying to get the neighborhood association to pay for it.
# He begins to solicit his neighbors to petition to get the association to build the wall.
# Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span,
# and can only remember two letters from each of his neighbors’ names. As he collects signatures,
# he insists that his neighbors keep truncating their names until two letters remain, and he can finally read them.
# Your code will show Full name of the neighbor and the truncated version of the name as an array.
# If the number of the characters in name is less than or equal to two,
# it will return an array containing only the name as is"
def who_is_paying(name):
    return [name,name[:2]] if len(name) > 2 else [name]

# A Tidy number is a number whose digits are in non-decreasing order.
# Task
# Given a number, Find if it is Tidy or not .
def tidyNumber(n):
    return sorted([int(i) for i in str(n)]) == [int(i) for i in str(n)]

# In John's car the GPS records every s seconds the distance travelled from an origin
# (distances are measured in an arbitrary but consistent unit). For example, below is part of a record with s = 15:
# x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
# The sections are:
# 0.0-0.19, 0.19-0.5, 0.5-0.75, 0.75-1.0, 1.0-1.25, 1.25-1.50, 1.5-1.75, 1.75-2.0, 2.0-2.25
# We can calculate John's average hourly speed on every section and we get:
# [45.6, 74.4, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0]
# Given s and x the task is to return as an integer the *floor* of the maximum average
# speed per hour obtained on the sections of x. If x length is less than
# or equal to 1 return 0 since the car didn't move.
# Example:
# with the above data your function gps(s, x)should return 74
def gps(s, x):
    speed = []
    lenght = 0
    for elem in x:
        speed.append(3600 * (elem - lenght) / s)
        lenght = elem
    return max(speed) if len(x) > 0 else 0

# In this Kata your task will be to return the count of pairs that have consecutive numbers as follows:
def pairs(ar):
    counter = 0
    for i in range(0, len(ar)-1,2):
        if i+1 > len(ar):
            break
        elif abs(ar[i] - ar[i+1]) == 1:
            counter += 1
    return counte

# Create a function that finds the integral of the expression passed.
# In order to find the integral all you need to do is add one to the exponent (the second argument),
# and divide the coefficient (the first argument) by that new number.
# For example for 3x^2, the integral would be 1x^3: we added 1 to the exponent,
# and divided the coefficient by that new number).
def integrate(coefficient, exponent):
    return f"{int(coefficient / (exponent+1))}x^{exponent+1}"

# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".
# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
import string
def solve(s):
    streakCounter = 0
    tempCounter = 0
    streakList = []
    alphDict = dict(zip(string.ascii_lowercase, [num for num in range(1, 27, 1)]))
    for i in list(alphDict):
        if i in list('aeiou'):
            alphDict.pop(i)
        else:
            pass
    for sym in s:
        if sym in list(alphDict):
            streakCounter += 1
            tempCounter += alphDict[sym]
        else:
            if streakCounter > 0:
                streakList.append(tempCounter)
                tempCounter = 0
                streakCounter = 0
            else:
                pass
    return max(streakList)

# Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.
def to_binary(n):
    return int(bin(n)[2:])

# Strong number is the number that the sum of the factorial of its digits is equal to number itself.
# For example, 145 is strong, since 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Task
# Given a number, Find if it is Strong or not and return either "STRONG!!!!" or "Not Strong !!".
from math import factorial
def strong_num(number):
    return 'STRONG!!!!' if sum(factorial(int(i)) for i in str(number)) == number else 'Not Strong !!'

# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type

# For this problem you must create a program that says who ate the last cookie.
# If the input is a string then "Zach" ate the cookie.
# If the input is a float or an int then "Monica" ate the cookie.
# If the input is anything else "the dog" ate the cookie.
# The way to return the statement is: "Who ate the last cookie? It was (name)!"
# Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach!
# (The reason you return Zach is because the input is a string)
# Note: Make sure you return the correct message with correct spaces and punctuation.
# Please leave feedback for this kata. Cheers!
def cookie(x):
    if type(x) is str: return "Who ate the last cookie? It was Zach!"
    if type(x) is int or type(x) is float: return "Who ate the last cookie? It was Monica!"
    return "Who ate the last cookie? It was the dog!"
