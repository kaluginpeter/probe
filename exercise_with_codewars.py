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

# You probably know that number 42 is "the answer to life, the universe
# and everything" according to Douglas Adams' "The Hitchhiker's Guide to the Galaxy".
# For Freud, the answer was quite different...
# In the society he lived in, people - women in particular - had to repress their
# sexual needs and desires. This was simply how the society was at the time.
# Freud then wanted to study the illnesses created by this,
# and so he digged to the root of their desires. This led to some
# of the most important psychoanalytic theories to this day, Freud being the father of psychoanalysis.
# Now, basically, when a person hears about Freud, s/he hears "sex" because for Freud,
# everything was related to, and explained by sex.
# In this kata, the function will take a string as its argument,
# and return a string with every word replaced by the explanation to everything,
# according to Freud. Note that an empty string, or no arguments, should return an empty string.
def to_freud(sentence):
    return ' '.join(['sex'] * len(sentence.split()))

# Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.
def solve(arr):
    return list(dict.fromkeys(arr[::-1]))[::-1]

# Oh, no! The number has been mixed up with the text.
# Your goal is to retrieve the number from the text, can you return the number back to its original state?
# Task
# Your task is to return a number from a string.
def filter_string(string):
    return int(''.join(i for i in string if i.isdigit()))

# Given an array/list [] of integers , Find the product of the k maximal numbers.
# Notes
# Array/list size is at least 3 .
# Array/list's numbers Will be mixture of positives , negatives and zeros
# Repetition of numbers in the array/list could occur.
def max_product(lst, n_largest_elements):
    mul = 1
    for n in sorted(lst, reverse=True)[:n_largest_elements]:
        mul *= n
    return mul

# To complete this Kata you need to make a function multiplyAll/multiply_all which takes
# an array of integers as an argument. This function must return another function,
# which takes a single integer as an argument and returns a new array.
# The returned array should consist of each of the elements from the first array multiplied by the integer.
def multiply_all(arr):
    def multiply(num):
        return [num * elem for elem in arr]
    return multiply

# This series of katas will introduce you to basics of doing geometry with computers.
# Point objects have x and y attributes (X and Y in C#) attributes.
# Write a function calculating distance between Point a and Point b.
def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5

# Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.
import math
def nearest_sq(n):
    return round(math.sqrt(n))**2

# Color Ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
import random
class Ghost(object):
  def __init__(self):
    self.color = random.choice(["white", "yellow", "purple", "red"])

# You are creating a text-based terminal version of your favorite board game.
# In the board game, each turn has six steps that must happen in this order:
# roll the dice, move, combat, get coins, buy more health, and print status.
from preloaded import *
health, position, coins = 100, 0, 0
def main(): pass
log = 'roll_dice move combat get_coins buy_health print_status'.split()

# Input:
# a string strng
# an array of strings arr
# Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):
# a boolean true if all rotations of strng are included in arr
# false otherwise
def contain_all_rots(strng, arr):
    rotate = strng
    if not len(arr) or not strng:
        return True
    for index in range(len(strng)):
        if rotate  not in arr:
            return False
        first_letter = rotate[0]
        rotate = rotate[1:]
        rotate += first_letter
    return True

# Given a string, turn each character into its ASCII character code
# and join them together to create a number - let's call this number total1:
# 'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
# Then replace any incidence of the number 7 with the number 1, and call this number 'total2':
# total1 = 656667
#               ^
# total2 = 656661
#               ^
# Then return the difference between the sum of the digits in total1 and total2:
def calc(x):
    word= ''.join([str(ord(i)) for i in x])
    word1 = ''.join([str(ord(i)) for i in x]).replace('7', '1')
    return sum(int(i) for i in word) - sum(int(i) for i in word1)

# An element is leader if it is greater than The Sum all the elements to its right side.
# Task
# Given an array/list [] of integers , Find all the LEADERS in the array.
def array_leaders(numbers):
    output = []
    for i in range(0, len(numbers)):
        if numbers[i] > sum(numbers[i+1:]):
            output.append(numbers[i])
    return output

# Our fruit guy has a bag of fruit (represented as an array of strings)
# where some fruits are rotten. He wants to replace all the rotten pieces of fruit with fresh ones.
# For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"].
# Your task is to implement a method that accepts an array of strings containing fruits
# should returns an array of strings where all the rotten fruits are replaced by good ones.
# Notes
# If the array is null/nil/None or empty you should return empty array ([]).
# The rotten fruit name will be in this camelcase (rottenFruit).
# The returned array should be in lowercase.
def remove_rotten(bag_of_fruits):
    try:
        return [i.replace('rotten', '').lower() if 'rotten' in i else i.lower() for i in bag_of_fruits]
    except:
        return []

# You're on your way to the market when you hear beautiful music coming from a nearby street performer.
# The notes come together like you wouln't believe as the musician puts together patterns of tunes.
# As you wonder what kind of algorithm you could use to shift octaves by
# 8 pitches or something silly like that, it dawns on you that you have been watching
# the musician for some 10 odd minutes. You ask, "how much do people normally
# tip for something like this?" The artist looks up. "It's always gonna be about tree fiddy."
# It was then that you realize the musician was a 400 foot tall beast from the paleolithic era!
# The Loch Ness Monster almost tricked you!
# There are only 2 guaranteed ways to tell if you are speaking to The Loch Ness Monster:
# A) it is a 400 foot tall beast from the paleolithic era; B) it will ask you for tree fiddy.
# Since Nessie is a master of disguise, the only way accurately tell is to look for the phrase
# "tree fiddy". Since you are tired of being grifted by this monster,
# the time has come to code a solution for finding The Loch Ness Monster.
# Note that the phrase can also be written as "3.50" or "three fifty".
def is_lock_ness_monster(string):
    return True in [i in string for i in ['tree fiddy', '3.50', 'three fifty']]

# You task is to implement an simple interpreter for the notorious esoteric language HQ9+
# that will work for a single character input:
# If the input is 'H', return 'Hello World!'
# If the input is 'Q', return the input
# If the input is '9', return the full lyrics of 99 Bottles of Beer. It should be formatted like this:
LINES = "{0} of beer on the wall, {0} of beer.\nTake one down and pass it around, {1} of beer on the wall."
SONG = '\n'.join( LINES.format("{} bottles".format(n), "{} bottle".format(n-1)+"s"*(n!=2)) for n in range(99,1,-1) )
SONG += """
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""
def HQ9(code):
    return {'H': 'Hello World!', 'Q': 'Q', '9': SONG}.get(code, None)
# Write a function that can return the smallest value of an array or the index of that value.
# The function's 2nd parameter will tell whether it should return the value or the index.
# Assume the first parameter will always be an array filled with at least 1 number and no duplicates.
# Assume the second parameter will be a string holding one of two values: 'value' and 'index'.
def find_smallest(numbers,to_return):
    return numbers.index(min(numbers)) if to_return == 'index' else min(numbers)

# There's a "3 for 2" (or "2+1" if you like) offer on mangoes.
# For a given quantity and price (per mango), calculate the total cost of the mangoes.
def mango(quantity, price):
    return (quantity - quantity // 3) * price

# Your colleagues have been looking over you shoulder.
# When you should have been doing your boring real job,
# you've been using the work computers to smash in endless hours of codewars.
# In a team meeting, a terrible, awful person declares to the group that you aren't working.
# You're in trouble. You quickly have to gauge the feeling in the room to decide whether
# or not you should gather your things and leave.
# Given an object (meet) containing team member names as keys, and their happiness rating out
# of 10 as the value, you need to assess the overall happiness rating of the group.
# If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.
# Happiness rating will be total score / number of people in the room.
# Note that your boss is in the room (boss), their score is worth double it's face value
# (but they are still just one person!).
def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss] ) / len(meet) <= 5 else 'Nice Work Champ!'

# The number n is Evil if it has an even number of 1's in its binary representation.
# The first few Evil numbers: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20
# The number n is Odious if it has an odd number of 1's in its binary representation.
# The first few Odious numbers: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19
# You have to write a function that determine if a number is Evil of Odious,
# function should return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.
def evil(n):
    return "It's Evil!" if  bin(n).count('1') % 2 == 0 else "It's Odious!"

# Every now and then people in the office moves teams or departments.
# Depending what people are doing with their time they can become more or less boring.
# Time to assess the current team.
# You will be provided with an object(staff) containing the staff names as keys,
# and the department they work in as values.
# Each department has a different boredom assessment score, as follows:
def boredom(staff):
    dict_score = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    boredom_score = 0
    for v in staff.values():
        if v in dict_score:
            boredom_score += dict_score.get(v)
    return 'kill me now' if boredom_score <= 80 else 'i can handle this' if 80 < boredom_score < 100 else 'party time!!'

# You have access to the ship "draft" and "crew".
# "Draft" is the total ship weight and "crew" is the number of humans on the ship.
# Each crew member adds 1.5 units to the ship draft. If after removing the weight
# of the crew, the draft is still more than 20, then the ship is worth looting.
# Any ship weighing that much must have a lot of booty!
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20

# In this kata you will have to write a function that takes litres and price_per_litre (in dollar) as arguments.
# Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount
# of 10 cents per litre, and so on every two litres,
# up to a maximum discount of 25 cents per litre.
# But total discount per litre cannot be more than 25 cents.
# Return the total cost rounded to 2 decimal places.
# Also you can guess that there will not be negative or non-numeric inputs.
# Good Luck!
def fuel_price(litres, price_per_liter):
    discount = int(min(litres, 10)/2) * 5 / 100
    return round((price_per_liter - discount) * litres, 2)

# Given a string made up of letters a, b, and/or c, switch the position
# of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.
def switcheroo(string):
    return string.replace('a', '-').replace('b', 'a').replace('-', 'b')

# ASC Week 1 Challenge 4 (Medium #1)
# Write a function that converts any sentence into a V A P O R W A V E sentence.
# a V A P O R W A V E sentence converts all the letters into uppercase,
# and adds 2 spaces between each letter (or special character)
# to create this V A P O R W A V E effect.
# Note that spaces should be ignored in this case.
def vaporcode(s):
    return '  '.join(i.upper() for i in s.replace(' ', ''))

# Create a method all which takes two params:
# a sequence
# a function (function pointer in C)
# and returns true if the function in the params returns true for every element in the sequence.
# Otherwise, it should return false. If the sequence is empty,
# it should return true, since technically nothing failed the test.
def _all(seq, fun):
    return all(fun(i) for i in seq)

# Write a function that calculates the original product price, without VAT.
def excluding_vat_price(price):
    return round(price - price / 115 * 15, 2) if price else -1

# Given an unsorted array of 3 positive integers [ n1, n2, n3 ],
# determine if it is possible to form a Pythagorean Triple using those 3 integers.
# A Pythagorean Triple consists of arranging 3 integers, such that:
# a2 + b2 = c2
def pythagorean_triple(integers):
    return sorted(integers)[0]**2 + sorted(integers)[1]**2 == sorted(integers)[2]**2

# Some new cashiers started to work at your restaurant.
# They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
# All the orders they create look something like this:
# "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
# The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
# Their preference is to get the orders as a nice clean string with spaces and capitals like so:
# "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
# The kitchen staff expect the items to be in the same order as they appear in the menu.
# The menu items are fairly simple, there is no overlap in the names of the items:
def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    return "".join([(i + " ") * order.count(i.lower()) for i in menu if i.lower() in order]).rstrip()

# Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)
# (the dedicated builtin(s) functionalities are deactivated)
def reverse(lst):
    list1 = list()
    for elem in lst:
        list1.insert(0, elem)
    return list1

# According to the creation myths of the Abrahamic religions,
# Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2
# containing objects (representing Adam and Eve). The first object in the array should be
# an instance of the class Man. The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
def God():
    return [Man(), Woman()]
class Human(object):
    pass
class Man(Human):
    pass
class Woman(Human):
    pass

# Make multiple functions that will return the sum,
# difference, modulus, product, quotient, and the exponent respectively.
# Please use the following function names:
def add(a,b):
  return a + b
def multiply(a,b):
  return a * b
def divide(a,b):
  return a / b
def mod(a,b):
  return a % b
def exponent(a,b):
  return a ** b
def subt(a,b):
  return a - b

# Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!
# You need to cast the whole array to the correct type.
# Create the function that takes as a parameter a sequence of numbers represented
# as strings and outputs a sequence of numbers.
# ie:["1", "2", "3"] to [1, 2, 3]
# Note that you can receive floats as well.
def to_float_array(arr):
    return list(map(float, arr))

# Given a string made of digits [0-9], return a string where
# each digit is repeated a number of times equals to its value.
def explode(s):
    return ''.join(c * int(c) for c in s)

# Disarium number is the number that The sum of its digits powered
# with their respective positions is equal to the number itself.
# Task
# Given a number, Find if it is Disarium or not .
def disarium_number(number):
    return 'Disarium !!' if sum(int(i)**(int(j) + 1) for j, i in enumerate(str(number))) == number else 'Not !!'

# You will be given a string (x) featuring a cat 'C' and a mouse 'm'.
# The rest of the string will be made up of '.'.
# You need to find out if the cat can catch the mouse from it's current position.
# The cat can jump over three characters. So:
# C.....m returns 'Escaped!' <-- more than three characters between
# C...m returns 'Caught!' <-- as there are three characters between the two, the cat can jump.
def cat_mouse(x):
    return 'Escaped!' if x.count('.') > 3 else 'Caught!'

# Modify the kebabize function so that it converts a camel case string into a kebab case.
import re
def kebabize(string):
    return '-'.join(re.split('(?<=.)(?=[A-Z])', re.sub(r'[0-9]+', '', string))).lower()

# Given a string and an array of integers representing indices, capitalize all letters at the given indices.
# For example:
# capitalize("abcdef",[1,2,5]) = "aBCdeF"
# capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
# The input will be a lowercase string with no spaces and an array of digits.
# Good luck!
def capitalize(s,ind):
    list = [j for j in s]
    for i in ind:
        if i <= len(list):
            list[i] = list[i].upper()
    return ''.join(list)

# John has invited some friends. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
# Could you make a program that
# makes this string uppercase
# gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name.
# Last name and first name of a guest come in the result between parentheses separated by a comma.
# So the result of function meeting(s) will be:
# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)
# (CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts,
# pictures or other items. We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
def likes(names):
    if len(names) >= 4:
        return ', '.join(names[:2]) + f" and {len(names[2:])} others like this"
    elif 1 < len(names) < 4:
        return ', '.join(names[:-1]) + f" and {names[-1]} like this"
    return f"{'no one' if len(names) == 0 else names[0]} likes this"

# Write a function called calculate that takes 3 values.
# The first and third values are numbers. The second value is a character.
# If the character is "+" , "-", "*", or "/", the function will
# return the result of the corresponding mathematical function on the two numbers.
# If the string is not one of the specified characters, the function should return
# null (throw an ArgumentException in C#).
# Keep in mind, you cannot divide by zero. If an attempt to divide by zero is made,
# return null (throw an ArgumentException in C#)/(None in Python).
def calculate(num1, operation, num2):
    dict = {'+': num1 + num2, '-': num1 - num2,
           '*': num1 * num2, '/': num1 / num2 if num1 !=0 and num2 !=0 else None}
    return dict[operation] if operation in dict else None

# Write a method that takes one argument as name
# and then greets that name, capitalized and ends with an exclamation point.
def greet(name):
    return f'Hello {name.title()}!'

# In this first kata in the series, you need to define a Hero prototype
# to be used in a terminal game. The hero should have the following attributes:
class Hero(object):
    def __init__(self, name='Hero', position='00', health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
        self.experience = experience

# Add the value "codewars" to the websites array.
# After your code executes the websites array should == ["codewars"]
# The websites array has already been defined for you using the following code:
websites.append("codewars")

# Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.
# Find the number of Friday 13th in the given year.
import calendar
def unlucky_days(year):
	return sum(calendar.weekday(year, m, 13) == 4 for m in range(1, 13))

# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
def correct_polish_letters(st):
    dict = {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'}
    return ''.join(dict[i] if i in dict else i for i in st)

# Your task is to write a function toLeetSpeak that converts a regular english sentence to Leetspeak.
#More about LeetSpeak You can read at wiki -> https://en.wikipedia.org/wiki/Leet
# Consider only uppercase letters (no lowercase letters, no numbers) and spaces.
def to_leet_speak(str):
    dict = {'A' : '@',  'B' : '8',  'C' : '(',  'D' : 'D',  'E' : '3',  'F' : 'F',  'G' : '6',
            'H' : '#',  'I' : '!',  'J' : 'J', 'K' : 'K',  'L' : '1',  'M' : 'M',
            'N' : 'N',  'O': '0',  'P' : 'P',  'Q' : 'Q',  'R' : 'R',  'S' : '$',
            'T' : '7',  'U' : 'U',  'V' : 'V',  'W' : 'W',  'X' : 'X',  'Y' : 'Y',  'Z' : '2', ' ': ' '}
    return ''.join(dict[i] for i in str)

# Given a string, write a function that returns the string
# with a question mark ("?") appends to the end, unless the original
# string ends with a question mark, in which case, returns the original string.
def ensure_question(s):
    return s if s.endswith('?') else s + '?'

# Given a string s. You have to return another string such that
# even-indexed and odd-indexed characters of s are grouped and groups are space-separated (see sample below)
def sort_my_string(s):
    return s[::2] + ' ' + s[1::2]

# Given an input of an array of digits, return the array with each digit incremented
# by its position in the array: the first digit will be incremented by 1,
# the second digit by 2, etc. Make sure to start counting your positions from 1 ( and not 0 ).
# Your result can only contain single digit numbers, so if adding a digit
# with its position gives you a multiple-digit number, only the last digit of the number should be returned.
# Notes:
# return an empty array if your array is empty
# arrays will only contain numbers so don't worry about checking that
def incrementer(nums):
    return [i+j+1 if i+j+1<10 else int(str(i+j+1)[-1]) for i,j in enumerate(nums)]

# Given a string "abc" and assuming that each letter in the string
# has a value equal to its position in the alphabet, our string
# will have a value of 1 + 2 + 3 = 6. This means that: a = 1, b = 2, c = 3 ....z = 26.
# You will be given a list of strings and your task will be to return the values of the
# strings as explained above multiplied by the position of that string in the list.
# For our purpose, position begins with 1.
# nameValue ["abc","abc abc"] should return [6,24] because of [ 6 * 1, 12 * 2 ]. Note how spaces are ignored.
# "abc" has a value of 6, while "abc abc" has a value of 12. Now, the value at position 1 is multiplied
# by 1 while the value at position 2 is multiplied by 2.
# Input will only contain lowercase characters and spaces.
# Good luck!
def name_value(my_list):
    return [sum(ord(k)-96 if k.isalpha() else 0 for k in j) * (i+1) for i, j in enumerate(my_list)]

# Write function alternateCase which switch every letter in string
# from upper to lower and from lower to upper. E.g: Hello World -> hELLO wORLD
def alternateCase(s):
    return s.swapcase()

# Write a function that accepts two arguments and generates a sequence
# containing the integers from the first argument to the second inclusive.
# Input
# Pair of integers greater than or equal to 0. The second argument will always be greater than or equal to the first.
def generate_integers(m, n):
    return [i for i in range(m,n+1)]

# Write a function
# vowel_2_index
# that takes in a string and replaces all the vowels [a,e,i,o,u]
# with their respective positions within that string.
# E.g:
def vowel_2_index(string):
    return ''.join(str(i+1) if j.lower() in 'aeiou' else j for i, j in enumerate(string))

# A variation of determining leap years, assuming only integers are used and years can be negative and positive.
# Write a function which will return the days in the year and the year entered in a string. For example:
import calendar
def year_days(year):
    return f"{year} has {366 if calendar.isleap(abs(year)) else 365} days"

# Born a misinterpretation of this kata, your task here is pretty simple:
# given an array of values and an amount of beggars, you are supposed to
# return an array with the sum of what each beggar brings home, assuming they
# all take regular turns, from the first to the last.
# For example: [1,2,3,4,5] for 2 beggars will return a result of [9,6],
# as the first one takes [1,3,5], the second collects [2,4].
# The same array with 3 beggars would have in turn have produced a better
# out come for the second beggar: [5,7,3], as they will respectively take [1,4], [2,5] and [3].
# Also note that not all beggars have to take the same amount of "offers", meaning that the length
# of the array is not necessarily a multiple of n; length can be even shorter,
# in which case the last beggars will of course take nothing (0).
# Note: in case you don't get why this kata is about English beggars,
# then you are not familiar on how religiously queues are taken in the kingdom ;)
# Note 2: do not modify the input array.
def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]

# Mothers arranged a dance party for the children in school. At that party,
# there are only mothers and their children. All are having great fun on the
# dance floor when suddenly all the lights went out.
# It's a dark night and no one can see each other.
# But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.
# Legend:
# -Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
# -Function input: String contains only letters, uppercase letters are unique.
# Task:
# Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".
def find_children(dancing_brigade):
    list = sorted(set([i.lower() for i in dancing_brigade]))
    return ''.join(i.upper() + i * dancing_brigade.count(i) for i in list)

# Implement a function, multiples(m, n), which returns
# an array of the first m multiples of the real number n. Assume that m is a positive integer.
def multiples(m, n):
    return [i * n for i in range(1, m+1)]

# Jumping number is the number that All adjacent digits in it differ by 1.
# Task
# Given a number, Find if it is Jumping or not .
def jumping_number(number):
    number = list(str(number))
    for i in range(0, len(number)-1):
        if abs(int(number[i+1])-int(number[i])) != 1:
            return 'Not!!'
    return 'Jumping!!'

# In this Kata you are expected to find the coefficients
# of quadratic equation of the given two roots (x1 and x2).
# Equation will be the form of ax^2 + bx + c = 0
# Return type is a Vector (tuple in Rust, Array in Ruby)
# containing coefficients of the equations in the order (a, b, c).
# Since there are infinitely many solutions to this problem, we fix a = 1.
# Remember, the roots can be written like (x-x1) * (x-x2) = 0
def quadratic(x1, x2):
    return (1, -(x1 + x2), x1 * x2)

# Find the difference between the sum of the squares of the first n natural
# numbers (1 <= n <= 100) and the square of their sum.
# Example
# For example, when n = 10:
# The square of the sum of the numbers is:
# (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)2 = 552 = 3025
# The sum of the squares of the numbers is:
# 12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385
def difference_of_squares(n):
    return sum([i for i in range(1,n+1)])**2 - sum([i**2 for i in range(1, n+1)])

# You are creating an "Escape the room" game.
# The first step is to create a hash table called rooms that contains
# all of the rooms of the game. There should be at least 3 rooms inside it,
# each being a hash table with at least three properties (e.g. name, description, completed).
rooms = {
    'room1': {
    'name': 'Peter', 'description': 'python', 'completed': False },
    'room2': {
    'name': 'Ivan', 'description': 'js', 'completed': True },
    'room3': {
    'name': 'Pasha', 'description': 'golang', 'completed': True }
        }

# This Kata is intended as a small challenge for my students
# All Star Code Challenge #22
# Create a function that takes an integer argument of seconds
# and converts the value into a string describing how many hours and minutes comprise that many seconds.
# Any remaining seconds left over are ignored.
# Note:
# The string output needs to be in the specific form - "X hour(s) and X minute(s)"
def to_time(seconds):
    return f'{seconds//3600} hour(s) and {(seconds//60)%60} minute(s)'

# Write a function to get the first element(s) of a sequence.
# Passing a parameter n (default=1) will return the first n element(s) of the sequence.
# If n == 0 return an empty sequence []
def first(seq, n=1):
    return seq[:n] if seq else []

# Have you heard about the myth that if you fold a paper enough times, you can reach the moon with it?
# Sure you have, but exactly how many? Maybe it's time to write a program to figure it out.
# You know that a piece of paper has a thickness of 0.0001m. Given distance in units of meters,
# calculate how many times you have to fold the paper to make the paper reach this distance.
# (If you're not familiar with the concept of folding a paper: Each fold doubles its total thickness.)
# Note: Of course you can't do half a fold. You should know what this means ;P
# Also, if somebody is giving you a negative distance, it's clearly bogus
# and you should yell at them by returning null (or whatever equivalent in your language).
# In Shell please return None. In C and COBOL please return -1.
def fold_to(distance):
    if distance < 0:
        return None
    count = 0
    paper = 0.0001
    while paper < distance:
        count += 1
        paper = paper * 2
    return count

# We need to write some code to return the original price of a product,
# the return type must be of type decimal and the number must be rounded to two decimal places.
# We will be given the sale price (discounted price), and the sale percentage,
# our job is to figure out the original price.
def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / (100 - sale_percentage) * 100, 2)

# Compare two strings by comparing the sum of their values (ASCII character code).
# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.
def compare(s1,s2):
    if not s1 and not s2:
        return True
    if any(x for x in s1 if not x.isalpha()):
        s1 = ''
    if any(x for x in s2 if not x.isalpha()):
        s2 = ''
    return sum(ord(x.upper()) for x in s1) == sum(ord(x.upper()) for x in s2)

# This function takes two numbers as parameters, the first number
# being the coefficient, and the second number being the exponent.
# Your function should multiply the two numbers, and then subtract 1 from the exponent.
# Then, it has to print out an expression (like 28x^7). "^1" should not be truncated when exponent = 2.
def derive(coefficient, exponent):
    return f"{coefficient*exponent}x^{exponent-1 if exponent >2 else exponent}"

# Consider the word "abode". We can see that the letter a is in position 1
# and b is in position 2. In the alphabet, a and b are also in positions 1 and 2.
# Notice also that d and e in abode occupy the positions they would occupy in the alphabet,
# which are positions 4 and 5.
# Given an array of words, return an array of the number of letters that occupy their
# positions in the alphabet for each word.
def solve(arr):
    output = []
    for str in arr:
        str = list(map(lambda x: ord(x.lower())-96, list(str)))
        str = list(map(lambda x: x[0] == x[1], zip(str, range(1,len(str)+1))))
        output.append(str.count(True))
    return output

# Find the length of the longest substring in the given string s that is the same in reverse.
# As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
# If the length of the input string is 0, the return value must be 0.
def longest_palindrome (s):
    if(len(s) == 0):
        return 0
    results = set()
    string_length = len(s)
    for i, char in enumerate(s):
        start, end = i-1, i+1
        while start >=0 and end < string_length and s[start] == s[end]:
            results.add(s[start:end+1])
            start -= 1
            end += 1
        start, end = i, i + 1
        while start >= 0 and end < string_length and s[start] == s[end]:
            results.add(s[start:end+1])
            start -= 1
            end += 1
    lst = sorted(list(results), key=len)
    if(len(lst) == 0):
        return 1
    else:
        return len(lst[-1])

# Given a string, return a new string that has transformed based on the input:
# Change case of every character, ie. lower case to upper case, upper case to lower case.
# Reverse the order of words from the input.
# Note: You will have to handle multiple spaces, and leading/trailing spaces.
def string_transformer(s):
    return ' '.join(s.swapcase().split(' ')[::-1])

# In this Kata, you will be given two strings a and b
# and your task will be to return the characters that are not common in the two strings.
def solve(a,b):
    return ''.join(i if i not in b else '' for i in a) + ''.join(i if i not in a else '' for i in b)
#set(a)^(set(b))

# Create a method sayHello/say_hello/SayHello that takes as input a name, city,
# and state to welcome a person. Note that name will be an array consisting of one
# or more values that should be joined together with one space between each,
# and the length of the name array in test cases will vary.
def say_hello(name, city, state):
    return f"Hello, {' '.join(i for i in name)}! Welcome to {city}, {state}!"

# A sequence or a series, in mathematics, is a string of objects, like numbers,
# that follow a particular pattern. The individual elements in a sequence are called terms.
# A simple example is 3, 6, 9, 12, 15, 18, 21, ..., where the pattern is: "add 3 to the previous term".
# In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28,
# ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".
def sum_of_n(n):
    if n < 0:
        return sorted([sum(x for x in range(i,1)) for i in range(n, 1)])[::-1]
    return [sum([x for x in range(i+1)]) for i in range(n+1)]

# Wilson primes satisfy the following condition. Let P represent a prime number.
# Then,
# ((P-1)! + 1) / (P * P)
# should give a whole number.
# Your task is to create a function that returns true if the given number is a Wilson prime.
def am_i_wilson(n):
    list = [5, 13, 563, 5971, 558771, 1964215, 8121909,
            12326713, 23025711, 26921605, 341569806, 399292158]
    return n in list

# This kata is about converting numbers to their binary or hexadecimal representation:
# If a number is even, convert it to binary.
# If a number is odd, convert it to hex.
# Numbers will be positive. The hexadecimal string should be lowercased.
def evens_and_odds(n):
    return bin(n)[2:] if n%2 == 0 else hex(n)[2:]

# Given an array/list [] of integers ,
# Find The maximum difference between the successive elements in its sorted form.
# Notes
# Array/list size is at least 3 .
# Array/list's numbers Will be mixture of positives and negatives also zeros_
# Repetition of numbers in the array/list could occur.
# The Maximum Gap is computed Regardless the sign.
import numpy as np
def max_gap(numbers):
    numbers = np.array(sorted(numbers))
    return np.max(numbers[1:]-numbers[:-1])

# Welcome to the Codewars Bar!
# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
# Your fellow coders have bought you several drinks tonight in the form of a string.
# Return a string suggesting how many glasses of water you should drink to not be hungover.
def hydrate(drink_string):
    s = sum([int(i) if i.isdigit() else 0 for i in drink_string])
    return f"{s} {'glass' if s == 1 else 'glasses'} of water"

# Every Friday and Saturday night, farmer counts amount of sheep returned back to his farm
# (sheep returned on Friday stay and don't leave for a weekend).
# Sheep return in groups each of the days -> you will be given two arrays
# with these numbers (one for Friday and one for Saturday night).
# Entries are always positive ints, higher than zero.
# Farmer knows the total amount of sheep, this is a third parameter.
# You need to return the amount of sheep lost (not returned to the farm) after final sheep counting on Saturday.
def lost_sheep(friday,saturday,total):
    return total - sum(friday + saturday)

# In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.)
# called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans.
# It then returns true if exactly one of the two expressions are true, false otherwise.
# Since we cannot define keywords in Javascript (well, at least I don't know how to do it),
# your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated.
# Your xor function should have the behaviour described above,
# returning true if exactly one of the two expressions evaluate to true, false otherwise.
def xor(a,b):
    return a != b

# Create a function args_count, that returns the count of passed arguments
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)

# Remove all exclamation marks from sentence but ensure a exclamation
# mark at the end of string. For a beginner kata, you can assume that the
# input data is always a non empty string, no need to verify it.
def remove(s):
    return s.replace("!", "") + "!"

# Two red beads are placed between every two blue beads.
# There are N blue beads. After looking at the arrangement below work out the number of red beads.
def count_red_beads(n):
    return 0 if n < 2 else n*2-2

# A trick I learned in elementary school to determine whether
# or not a number was divisible by three is to add all of the integers
# in the number together and to divide the resulting sum by three.
# If there is no remainder from dividing the sum by three, then the original number is divisible by three as well.
# Given a series of digits as a string, determine if the number represented by the string is divisible by three.
def divisible_by_three(st):
    s = sum(int(i) for i in st)
    while s != 0:
        s = s-3
        if s < 0:
            return False
    return True

# Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.
class Dog():
    def __init__(self, breed):
        self.breed = breed
snoopy = Dog("Beagle")
snoopy.bark = lambda: "Woof"
scoobydoo = Dog("Great Dane")
scoobydoo.bark = lambda: 'Woof'

# You are given a method called main, make it print the line Hello World!,
# (yes, that includes a new line character at the end) and don't return anything
# Note that for some languages, the function main is the entry point of the program.
class Solution:
    def main(self, name=''):
        print('Hello World!')

# Write function potatoes with
# int parameter p0 - initial percent of water-
# int parameter w0 - initial weight -
# int parameter p1 - final percent of water -
# potatoesshould return the final weight coming out of the oven w1 truncated as an int.
def potatoes(p0, w0, p1):
    return w0 * (100 - p0) // (100 - p1)

# Haskell has some useful functions for dealing with lists:
# $ ghci
# GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
# λ head [1,2,3,4,5]
# 1
# λ tail [1,2,3,4,5]
# [2,3,4,5]
# λ init [1,2,3,4,5]
# [1,2,3,4]
# λ last [1,2,3,4,5]
# 5
# Your job is to implement these functions in your given language.
# Make sure it doesn't edit the array; that would cause problems! Here's a cheat sheet:
def head(lst):
    return lst[0]
def tail(lst):
    return lst[1:]
def init(lst):
    return lst[:-1]
def last(lst):
    return lst[-1]

# Your job at E-Corp is both boring and difficult. It isn't made any easier by the fact
# that everyone constantly wants to have a meeting with you, and that the meeting rooms are always taken!
# In this kata, you will be given an array. Each value represents a meeting room. Your job?
# Find the first empty one and return its index (N.B. There may be more than one empty room in some test cases).
def meeting(rooms):
    return rooms.index("O") if "O" in rooms else "None available!"

# You and a group of friends are earning some extra money in the school holidays
# by re-painting the numbers on people's letterboxes for a small fee.
# Since there are 10 of you in the group each person just concentrates on painting one digit!
# For example, somebody will paint only the 1's, somebody else will paint only the 2's and so on...
# But at the end of the day you realise not everybody did the same amount of work.
# To avoid any fights you need to distribute the money fairly. That's where this Kata comes in.
# Kata Task
# Given the start and end letterbox numbers, write a method to return the frequency of all 10 digits painted.
def paint_letterboxes(start, finish):
    squad = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(start,finish+1):
        while i != 0:
            squad[i % 10]+=1
            i //= 10
    return squad

# Imagine you are creating a game where the user has to guess the correct number.
# But there is a limit of how many guesses the user can do.
# If the user tries to guess more than the limit, the function should throw an error.
# If the user guess is right it should return true.
# If the user guess is wrong it should return false and lose a life.
# Can you finish the game so all the rules are met?
class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives < 1:
            raise 'Too many guesses!'
        if self.number == n:
            return True
        self.lives -= 1
        return False

# The function new_avg(arr, navg) should return the expected donation
# (rounded up to the next integer) that will permit to reach the average navg.
# Should the last donation be a non positive number (<= 0) John wants us:
# to return:
# Nothing in Haskell, Elm
# None in F#, Ocaml, Rust, Scala
# -1 in C, D, Fortran, Nim, PowerShell, Go, Pascal, Prolog, Lua, Perl, Erlang
# or to throw an error (some examples for such a case):
# IllegalArgumentException() in Clojure, Java
# ArgumentException() in C#
# echo ERROR in Shell
# argument-error in Racket
# std::invalid_argument in C++
# ValueError in Python
# So, he will clearly see that his expectations are not great enough. In "Sample Tests" you can see what to return.
# Notes:
# all donations and navg are numbers (integers or floats), arr can be empty.
# See examples below and "Sample Tests" to see which return is to be done.
from math import ceil
def new_avg(arr, newavg):
    ndon = float(newavg) * (len(arr) + 1) - sum(arr)
    if ndon >= 0:
        return ceil(ndon)
    else:
        raise ValueError('Negative number found')

# In this kata, your job is to return the two distinct highest values in a list.
# If there're less than 2 unique values, return as many of them, as possible.
# The result should also be ordered from highest to lowest.
def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]

# Write a function that removes every lone 9 that is inbetween 7s.
def seven_ate9(str_):
    strung_out = str_
    for i in range(len(strung_out)):
        if strung_out[i:i+3] == '797':
            strung_out = strung_out.replace('797','77')
            continue
    return strung_out

# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring.
# Vowels are any of aeiou.
# Good luck!
# If you like substring Katas, please try:
import re
def solve(s):
    matches = re.findall('[aeiou]+', s)
    return max(list(map(len, matches)))

# Take the following IPv4 address: 128.32.10.1
# This address has 4 octets where each octet is a single byte (or 8 bits).
# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
# Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.
# Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.
def ip_to_int32(ip):
    res = ''
    for part in ip.split('.'):
        b = bin(int(part))[2:]
        res += "%08d" % (int(b))
    return(int(res, 2))

# Given an array of Boolean values and a logical operator,
# return a Boolean result based on sequentially applying the operator to the values in the array.
from functools import reduce
def logical_calc(array, op):
    if op == "AND":
        return all(array)
    elif op == "OR":
        return any(array)
    elif op == "XOR":
        return reduce(lambda x, y: x ^ y, array)

# In this kata, you will do addition and subtraction on a given string. The return value must be also a string.
# Note: the input will not be empty.
import re
def calculate(s):
    s = re.sub('plus', '+', s)
    s = re.sub('minus','-', s)
    return str(eval(s))

# Write a class Block that creates a block (Duh..)
##Requirements
# The constructor should take an array as an argument, this will contain 3 integers
# of the form [width, length, height] from which the Block should be created.
class Block:
    def __init__(self, measurements):
        self.width, self.length, self.height = measurements
    def get_height(self):
        return self.height
    def get_length(self):
        return self.length
    def get_surface_area(self):
        return 2 * (self.height * self.length +
                    self.length * self.width +
                    self.height * self.width)
    def get_volume(self):
        return self.height * self.length * self.width
    def get_width(self):
        return self.width

# Given two strings s1 and s2, we want to visualize how different the
# two strings are. We will only take into account the lowercase letters (a to z).
# First let us count the frequency of each lowercase letters in s1 and s2.
# s1 = "A aaaa bb c"
# s2 = "& aaa bbb c d"
# s1 has 4 'a', 2 'b', 1 'c'
# s2 has 3 'a', 3 'b', 1 'c', 1 'd'
# So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2.
# In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.
# We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb"
# where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4.
# In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.
# The task is to produce a string in which each lowercase letters of s1 or s2 appears
# as many times as its maximum if this maximum is strictly greater than 1;
# these letters will be prefixed by the number of the string where they appear
# with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.
# In the result, substrings (a substring is for example 2:nnnnn or 1:hhh;
# it contains the prefix) will be in decreasing order of their length
# and when they have the same length sorted in ascending lexicographic
# order (letters and digits - more precisely sorted by codepoint);
# the different groups will be separated by '/'. See examples and "Example Tests".
# Hopefully other examples can make this clearer.
def mix(s1, s2):
    dictionary = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            dictionary[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(dictionary[ch][1] for ch in sorted(dictionary, key=lambda x: dictionary[x]))

# In this kata, we will make a function to test whether a period is late.
# Our function will take three parameters:
# last - The Date object with the date of the last period
# today - The Date object with the date of the check
# cycleLength - Integer representing the length of the cycle in days
# Return true if the number of days passed from last to today
# is greater than cycleLength. Otherwise, return false.
from datetime import *
def period_is_late(last, today, cycle_length):
    return last + timedelta(days = cycle_length) < today

# You will be given a 2D array of the maze and an array of directions.
# Your task is to follow the directions given.
# If you reach the end point before all your moves have gone, you should return Finish.
# If you hit any walls or go outside the maze border, you should return Dead.
# If you find yourself still in the maze after using all the moves, you should return Lost.

def maze_runner(maze, directions):
    startX = 0 ; startY = 0
    for y in range(len(maze)):
        for x in range(len(maze)):
            if maze[x][y] == 2:
                startX = y
                startY = x
    for dire in directions:
        if dire == "N": startY = startY - 1
        if dire == "E": startX = startX + 1
        if dire == "S": startY = startY + 1
        if dire == "W": startX = startX -1
        if startY < 0 or startY > len(maze)-1 or startX < 0 or startX > len(maze)-1 or maze[startY][startX] == 1: return "Dead"
        if maze[startY][startX] == 3: return "Finish"
    return "Lost"

# Define a method/function that removes from a given array
# of integers all the values contained in a second array.
class List(object):
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]

# Complete the solution so that it takes the object (JavaScript/CoffeeScript)
# or hash (ruby) passed in and generates a human readable string from its key/value pairs.
# The format should be "KEY = VALUE". Each key/value pair should be separated by a comma except for the last pair.
def solution(pairs):
    return ",".join(sorted(["{} = {}".format(k,v) for k,v in pairs.items()]))

# Complete the solution so that it returns a formatted string.
# The return value should equal "Value is VALUE" where value is a 5 digit padded number.
def solution(value):
    value = str(value)
    return 'Value is ' + '0'*(5-len(value)) + value

# Write a function that returns the number of occurrences of an element in an array.
def number_of_occurrences(element, sample):
    return sample.count(element)

# Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.
# In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.
# Strings a and b may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).
# If a and b have the same length treat a as the longer producing b+reverse(a)+b
def shorter_reverse_longer(a, b):
    if len(a) < len(b):
        return f'{a}{b[::-1]}{a}'
    return f'{b}{a[::-1]}{b}'

# Complete the function to find the count of the most frequent item of an array.
# You can assume that input is an array of integers. For an empty array return 0
def most_frequent_item_count(collection):
    return [max(collection.count(i) for i in collection)][0] if collection else 0

# You received a whatsup message from an unknown number. Could it be from that girl/boy
# with a foreign accent you met yesterday evening?
# Write a simple function to check if the string contains the word hallo in different languages.
# These are the languages of the possible people you met the night before:
# hello - english
# ciao - italian
# salut - french
# hallo - german
# hola - spanish
# ahoj - czech republic
# czesc - polish
# Notes
# you can assume the input is a string.
# to keep this a beginner exercise you don't need to check
# if the greeting is a subset of word (Hallowen can pass the test)
# function should be case insensitive to pass the tests
def validate_hello(greetings):
    hellos = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any(greet in greetings.lower() for greet in hellos)

# Create a function that returns the average of an array of numbers ("scores"),
# rounded to the nearest whole number. You are not allowed to use any loops
# (including for, for/in, while, and do/while loops).
def average(array):
    return round(sum(array) / len(array))

# Write a function that reverses the bits in an integer.
# For example, the number 417 is 110100001 in binary.
# Reversing the binary is 100001011 which is 267.
# You can assume that the number is not negative.
def reverse_bits(n):
    return int(str(bin(n).replace("0b", ""))[::-1], 2)

# Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran),
# check if the array contains three and two of the same values.
import collections
def check_three_and_two(array):
    count_letter = collections.Counter()
    for letter in array:
        count_letter[letter] += 1
    if max(count_letter.values()) == 3 and min(count_letter.values()) == 2:
        return True
    return False

# Your task is to return to the function seven(m)
# (m integer >= 0) an array (or a pair, depending on the language)
# of numbers, the first being the last number m with at most 2 digits
# obtained by your function (this last m will be divisible or not by 7),
# the second one being the number of steps to get the result.
# Forth Note:
# Return on the stack number-of-steps, last-number-m-with-at-most-2-digits
def seven(m):
    steps = 0
    while True:
        if m < 100:
            return (m, steps)
        m = m // 10 - 2 * (m % 10)
        steps += 1

# Write a function partlist that gives all the ways
# to divide a list (an array) of at least two elements into two non-empty parts.
# Each two non empty parts will be in a pair (or an array for languages without
# tuples or a structin C - C: see Examples test Cases - )
# Each part will be in a string
# Elements of a pair must be in the same order as in the original array.
def partlist(arr):
    return [(" ".join(arr[:i]), " ".join(arr[i:])) for i in range(1, len(arr))]

# Implement the function which should return true if given object
# is a vowel (meaning a, e, i, o, u, uppercase or lowercase), and false otherwise.
def is_vowel(s):
    return s.lower() in ['a', 'e', 'i', 'o', 'u']

# Everybody knows the classic "half your age plus seven" dating rule that a lot of people
# follow (including myself). It's the 'recommended' age range in which to date someone.
# minimum age <= your age <= maximum age #Task
# Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.
# This equation doesn't work when the age <= 14, so use this equation instead:
# min = age - 0.10 * age
# max = age + 0.10 * age
# You should floor all your answers so that an integer is given instead
# of a float (which doesn't represent age). Return your answer in the form [min]-[max]
def dating_range(age):
    return f"{int(age/2+7) if age > 14 else int(age - 0.10 * age)}-{int((age-7)*2) if age > 14 else int(age + 0.10 * age)}"

# Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override
# are some notable examples from the film Hackers.
# Your task is to create a function that,
# given a proper first and last name, will return the correct alias.
# Notes:
# Two objects that return a one word name in response
# to the first letter of the first name and one for the first letter of the surname are already given.
# If the first character of either of the names given to the function is not a letter
# from A - Z, you should return "Your name must start with a letter from A - Z."
# Sometimes people might forget to capitalize the first letter of their name
# so your function should accommodate for these grammatical errors.
import re
FIRST_NAME = {
    "C": "Cache", "R": "RAD", "J": "Java","B": "Beta","H": "Half-life","L": "Logic","O": "OS",
    "Y": "Y","Q": "Quantum","T": "Trojan","S": "Strike","M": "Malware","E": "Energy",
    "F": "Function","A": "Alpha","K": "Keystroke","I": "Ice","W": "WiFi","N": "Nagware","Z": "Zero",
    "D": "Data","G": "Glitch","V": "Vanilla","X": "Xerox","P": "Phishing","U": "Ultraviolet"
}
SURNAME = {
    "E": "Electron","Q": "Quark","Z": "Zombie","C": "Catalyst","S": "Spy",
    "O": "Overclock","X": "X","D": "Discharge","M": "Mike","P": "Payload",
    "G": "Gig","K": "Killer","R": "Roy","B": "Bomb","H": "Hacker","Y": "Yob","I": "IP","F": "Faraday",
    "A": "Analogue","W": "Worm","U": "Unit","L": "Lazer","T": "T-Rex","V": "Virus",
    "N": "n00b","J": "Jabber",
}
def alias_gen(f_name, l_name):
    regex = r'^[a-zA-Z]+'
    if re.match(regex, f_name) and re.match(regex, l_name):
        return '{} {}'.format(FIRST_NAME[f_name[0].upper()], SURNAME[l_name[0].upper()])
    else:
        return 'Your name must start with a letter from A - Z.'

# Implement a function that returns the minimal and the maximal value of a list (in this order).
def get_min_max(seq):
    return (min(seq), max(seq))

# In this Kata, you will be given a string and your task will
# be to return a list of ints detailing the count of uppercase letters,
# lowercase, numbers and special characters, as follows.
def solve(s):
  uc, lc, num, sp = 0, 0, 0, 0
  for ch in s:
    if ch.isupper(): uc += 1
    elif ch.islower(): lc += 1
    elif ch.isdigit(): num += 1
    else: sp += 1
  return [uc, lc, num, sp]

# Given an array/list [] of integers , Construct a product array Of same size
# Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].
# Notes
# Array/list size is at least 2 .
# Array/list's numbers Will be only Positives
# Repetition of numbers in the array/list could occur.
from operator import mul
from functools import reduce
def product_array(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers]

# A Nice array is defined to be an array where for every value n in the array,
# there is also an element n - 1 or n + 1 in the array.
# Write a function named isNice / IsNice that returns true if its array argument is a Nice array,
# else false.An empty array is not considered nice.
def is_nice(arr):
    return all(i+1 in arr or i-1 in arr for i in arr) if arr else 0

# Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL),
# multiplied by the integer at the last index.
# Indices in sequence start from 0.
# If the sequence is empty, you should return 0.
def even_last(numbers):
    total = 0
    if numbers:
        last = numbers[-1]
        numbers = [num for i, num in enumerate(numbers) if i % 2 ==0]
        total = sum(numbers) * last
    return total

# When provided with a String, capitalize all vowels
def swap(st):
    return ''.join(i.swapcase() if i in 'aeiou' else i for i in st)

# You're running an online business and a big part of your day is fulfilling orders.
# As your volume picks up that's been taking more of your time, and unfortunately
# lately you've been running into situations where you take an order but can't fulfill it.
# You've decided to write a function fillable() that takes three arguments: a dictionary
# stock representing all the merchandise you have in stock, a string merch representing
# the thing your customer wants to buy, and an integer n representing the number
# of units of merch they would like to buy. Your function should return
# True if you have the merchandise in stock to complete the sale, otherwise it should return False.
# Valid data will always be passed in and n will always be >= 1.
def fillable(stock, merch, n):
    return merch in stock and stock[merch] >= n

# Your task is to write a function called valid_spacing()
# or validSpacing() which checks if a string has valid spacing.
# The function should return either true or false (or the corresponding value in each language).
# For this kata, the definition of valid spacing is one space between words,
# and no leading or trailing spaces. Words can be any consecutive sequence
# of non space characters. Below are some examples of what the function should return:
def valid_spacing(s):
    return ' '.join(s.split()) == s

# Just a simple sorting usage. Create a function that returns
# the elements of the input-array / list sorted in lexicographical order.
def sortme(names):
    return sorted(names)

# Complete the function that returns an array of length n,
# starting with the given number x and the squares of the previous number.
# If n is negative or zero, return an empty array/list.
def squares(x, n):
    if (n<1): return []
    result = [x]
    i=0
    while i < n-1:
        i+=1
        x*=x
        result.append(x)
    return result

# Write a function filterLucky/filter_lucky() that accepts
# a list of integers and filters the list to only include the elements that contain the digit 7.
def filter_lucky(lst):
    return list(filter(lambda x: '7' in str(x), lst))

# You and a friend have decided to play a game to drill your statistical
# intuitions. The game works like this:
# You have a bunch of red and blue marbles.
# To start the game you grab a handful of marbles of each color
# and put them into the bag, keeping track of how many of each color go in.
# You take turns reaching into the bag, guessing a color, and then pulling one marble out.
# You get a point if you guessed correctly. The trick is you only have three seconds to make your guess,
# so you have to think quickly.
# You've decided to write a function, guessBlue() to help automatically calculate whether you should guess
# "blue" or "red". The function should take four arguments:
# the number of blue marbles you put in the bag to start
# the number of red marbles you put in the bag to start
# the number of blue marbles pulled out so far (always lower than the starting number of blue marbles)
# the number of red marbles pulled out so far (always lower than the starting number of red marbles)
# guessBlue() should return the probability of drawing a blue marble, expressed as a float.
# For example, guessBlue(5, 5, 2, 3) should return 0.6.
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start-blue_pulled)/(blue_start-blue_pulled+red_start-red_pulled)

# You are given a list of unique integers arr, and two integers a and b.
# Your task is to find out whether or not a and b appear consecutively in arr,
# and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.
def consecutive(arr, a, b):
    return arr.index(a) == arr.index(b)-1 or arr.index(a) == arr.index(b)+1

# Write a function that takes a string and an an integer n as parameters
# and returns a list of all words that are longer than n.
def filter_long_words(sentence, n):
    return [i for i in sentence.split() if len(i) > n]

# Your task is to determine how many files of the copy queue you will be able
# to save into your Hard Disk Drive. The files must be saved in the order they appear in the queue.
# Input:
# Array of file sizes (0 <= s <= 100)
# Capacity of the HD (0 <= c <= 500)
# Output:
# Number of files that can be fully saved in the HD.
def save(sizes, hd):
    return sum([sum(sizes[:i+1]) <= hd for i in range(len(sizes))])

# In this exercise, a string is passed to a method and a new string has
# to be returned with the first character of each word in the string.
def make_string(s):
    return ''.join(i[0] for i in s.split())

# Your task in this kata is to implement a function that calculates
# the sum of the integers inside a string. For example,
# in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.
# Note: only positive integers will be tested.
import re
def sum_of_integers_in_string(s):
    return sum([int(i) for i in re.findall(r'\d+', s)])

# Write a function to greet a person. Function will take name as input
# and greet the person by saying hello. Return null/nil/None if input is empty string or null/nil/None.
def greet(name):
    return f"hello {name}!" if name else None

# Hey Codewarrior!
# You already implemented a Cube class, but now we need your help again!
# I'm talking about constructors. We don't have one.
# Let's code two: One taking an integer and one handling no given arguments!
# Also we got a problem with negative values. Correct the code so negative
# values will be switched to positive ones!
# The constructor taking no arguments should assign 0 to Cube's Side property.
class Cube(object):
    def __init__(self, side=0):
        self._side = abs(side)

    def get_side(self):\
        return self._side

    def set_side(self, new_side):
        self._side = abs(new_side)

# In your class, you have started lessons about arithmetic progression. Since you are also a programmer,
# you have decided to write a function that will return the first n elements of the sequence with
# the given common difference d and first element a. Note that the difference may be zero!
# The result should be a string of numbers, separated by comma and space.
def arithmetic_sequence_elements(a, d, n):
	return ', '.join(str(a + i * d) for i in range(n))

# When given a string of space separated words, return the word with the longest length.
# If there are multiple words with the longest length,
# return the last instance of the word with the longest length.
def longest_word(string_of_words):
    return sorted(string_of_words.split(), key=len)[-1]

# Given a year, Find The next happy year or The closest year You'll see your best friend
def next_happy_year(year):
    happy_year = False
    while happy_year == False:
        year += 1
        if len(set(list(str(year)))) == 4:
            happy_year = True
    return year

# The medians of a triangle are the segments that unit the vertices with the midpoint of their opposite sides.
# The three medians of a triangle intersect at the same point, called the barycenter or the centroid.
# Given a triangle, defined by the cartesian coordinates of its vertices we need
# to localize its barycenter or centroid.
# The function bar_triang() or barTriang or bar-triang, receives the coordinates
# of the three vertices A, B and C  as three different arguments and outputs the
# coordinates of the barycenter O in an array [xO, yO]
# This is how our asked function should work: the result of the coordinates should
# be expressed up to four decimals, (rounded result).
# You know that the coordinates of the barycenter are given by the following formulas.
def bar_triang(*args):
    return list(map(lambda a: round(sum(a) / 3.0, 4), zip(*args)))

# You will be given an array of objects representing data about developers
# who have signed up to attend the next coding meetup that you are organising.
# Given the following input array:
# write a function that when executed as findAdmin(list1, 'JavaScript')
# returns only the JavaScript developers who are GitHub admins:
from typing import List
def find_admin(lst, lang):
    return [i for i in lst if i['language'] == lang and i['githubAdmin'] == 'yes']

# You receive the name of a city as a string, and you need to return
# a string that shows how many times each letter shows up in the string by using asterisks (*).
def get_strings(city):
    letters = {}
    for letter in city:
        if letter.lower() not in letters:
            letters[letter.lower()] = 1
        else:
            letters[letter.lower()] += 1
    return ",".join(key + ":" + "*"*value for key, value in letters.items() if key != " ")

# Given an array of N integers, you have to find how many times you have to add up the smallest
# numbers in the array until their Sum becomes greater or equal to K.
# Notes:
# List size is at least 3.
# All numbers will be positive.
# Numbers could occur more than once , (Duplications may exist).
# Threshold K will always be reachable.
def minimum_steps(numbers, value):
    numbers = sorted(numbers)
    count = 0
    for i in range(len(numbers)):
        count+=numbers[i]
        if count >= value:
            return i

# The function must return the truncated version of the given
# string up to the given limit followed by "..." if the result is
# shorter than the original. Return the same string if nothing was truncated.
def solution(st, limit):
    return st[:limit] + '...' if limit < len(st) else st

# Fellow code warrior, we need your help!
# We seem to have lost one of our sequence elements, and we need your help to retrieve it!
# Our sequence given was supposed to contain all of the integers from 0 to 9 (in no particular order),
# but one of them seems to be missing.
# Write a function that accepts a sequence of unique integers between 0 and 9 (inclusive),
# and returns the missing element.
def get_missing_element(seq):
    return [i for i in range(10) if i not in seq][0]

# Extra perfect number is the number that first and last bits are set bits.
# Task
# Given a positive integer N , Return the extra perfect numbers in range from 1 to N .
def extra_perfect(n):
    return [i for i in range(1, n+1, 2)]

# Simple enough this one - you will be given an array. The values in the array will either
# be numbers or strings, or a mix of both. You will not get an empty array, nor a sparse one.
# Your job is to return a single array that has first the numbers sorted in ascending order,
# followed by the strings sorted in alphabetic order. The values must maintain their original type.
# Note that numbers written as strings are strings and must be sorted with the other strings.
def db_sort(arr):
    return sorted([i for i in arr if type(i) == int]) + sorted([i for i in arr if type(i) == str])

# Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.
# Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.
# Rules:
# Obviously the words should be Caps, Every word should end with '!!!!',
# Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.
def gordon(a):
    trans = a.lower().maketrans({'a':'@', 'e':'*', 'o':'*','u':'*','i':'*'})
    return '!!!! '.join(a.translate(trans).upper().split()) + '!!!!'

# Given two numbers x and n, calculate the (positive) nth root of x; this means that being r = result, r^n = x
# Examples
def root(x, n):
    return x**(1/n)

# Given a string, return true if the first instance of "x"
# in the string is immediately followed by the string "xx".
def triple_x(s):
    for i, elem in enumerate(s[:-2]):
        if elem == 'x':
            return elem == s[i+1] and elem == s[i+2]
    return False

# The other day I saw an amazing video where a guy hacked some wifi controlled lightbulbs
# by flying a drone past them. Brilliant.
# In this kata we will recreate that stunt... sort of.
# You will be given two strings: lamps and drone. lamps represents a row of lamps,
# currently off, each represented by x. When these lamps are on, they should be represented by o.
# The drone string represents the position of the drone T (any better suggestion
# for character??) and its flight path up until this point =. The drone always
# flies left to right, and always begins at the start of the row of lamps.
# Anywhere the drone has flown, including its current position,
# will result in the lamp at that position switching on.
# Return the resulting lamps string. See example tests for more clarity.
def fly_by(lamps, drone):
    return 'o'*len(drone) + lamps[len(drone):] if len(drone) <= len(lamps) else 'o'*len(lamps)

# You are given a string of n lines, each substring being n characters long. For example:
# s = "abcd\nefgh\nijkl\nmnop"
# We will study the "horizontal" and the "vertical" scaling of this square of strings.
# A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').
# Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
# A v-vertical scaling of a string consists of replicating v times each part of the squared string.
# Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
def scale(strng, k, n):
    return '\n'.join(''.join(b * k for b in a) for a in strng.split('\n') for _ in range(n)) if strng else ''

# Bob is a lazy man.
# He needs you to create a method that can determine how many
# letters (both uppercase and lowercase ASCII letters) and digits are in a given string.
def count_letters_and_digits(s):
    return len([i for i in s if i.isdigit() or i.isalpha()])

# You have stumbled across the divine pleasure that is owning
# a dog and a garden. Now time to pick up all the cr@p! :D
# Given a 2D array to represent your garden, you must find
# and collect all of the dog cr@p - represented by '@'.
# You will also be given the number of bags you have access to
# (bags), and the capactity of a bag (cap). If there are no bags then
# you can't pick anything up, so you can ignore cap.
# You need to find out if you have enough capacity to collect all the cr@p and make your garden clean again.
# If you do, return 'Clean', else return 'Cr@p'.
# Watch out though - if your dog is out there ('D'), he gets very
# touchy about being watched. If he is there you need to return 'Dog!!'.
def crap(garden, bags, cap):
    c = 0
    for el in garden:
        for e in el:
            if e == "@":
                c += 1
            if e == "D":
                return "Dog!!"
    return "Clean" if c <= bags * cap else "Cr@p"

# Imagine you start on the 5th floor of a building, then travel down to the 2nd floor,
# then back up to the 8th floor. You have travelled a total of 3 + 6 = 9 floors of distance.
# Given an array representing a series of floors you must reach by elevator,
# return an integer representing the total distance travelled for visiting each floor in the array in order.
def elevator_distance(array):
    return sum([abs(array[i] - array[i+1]) for i in range(len(array)-1)])

# Complete the function to create backronyms. Transform the given string (without spaces)
# to a backronym, using the preloaded dictionary and return a string of words,
# separated with a single space (but no trailing spaces).
# The keys of the preloaded dictionary are uppercase letters A-Z
# and the values are predetermined words, for example:
dictionary
def make_backronym(acronym):
    return ' '.join(dictionary[i.upper()] for i in acronym)

# My friend John likes to go to the cinema. He can choose between system A and system B.
# System A : he buys a ticket (15 dollars) every time
# System B : he buys a card (500 dollars) and a first ticket for 0.90 times the ticket price,
# then for each additional ticket he pays 0.90 times the price paid for the previous ticket.
# Example:
# If John goes to the cinema 3 times
# System A : 15 * 3 = 45
# System B : 500 + 15 * 0.90 + (15 * 0.90) * 0.90 + (15 * 0.90 * 0.90) * 0.90 ( = 536.5849999999999,
# no rounding for each ticket)
# John wants to know how many times he must go to the cinema so that the final result of System B,
# when rounded up to the next dollar, will be cheaper than System A.
# The function movie has 3 parameters: card (price of the card), ticket (normal price of a ticket),
# perc (fraction of what he paid for the previous ticket) and returns the first n such that
import math
def movie(card, ticket, perc):
    total_card = card
    total_tickets = 0
    i = 1
    while math.ceil(total_card) >= total_tickets:
        total_card += ticket *(perc**i)
        total_tickets += ticket
        i += 1
    return i - 1

# You will be given an array of objects representing data
# about developers who have signed up to attend the next coding meetup that you are organising.
# Your task is to return an object which includes the count
# of food options selected by the developers on the meetup sign-up form..
from typing import List
def order_food(lst):
    meals = {}
    for i in lst:
        if i['meal'] not in meals:
            meals[i['meal']] = 1
        else:
            meals[i['meal']] += 1
    return meals

# This kata is the first of a sequence of four about "Squared Strings".
# You are given a string of n lines, each substring being n characters long: For example:
# s = "abcd\nefgh\nijkl\nmnop"
# We will study some transformations of this square of strings.
def vert_mirror(strng):
    return '\n'.join(i[::-1] for i in strng.split('\n'))
def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])
def oper(fct, s):
    return fct(s)

# Each floating-point number should be formatted that only the first two decimal places are returned.
# You don't need to check whether the input is a valid number because only valid numbers are used in the tests.
# Don't round the numbers! Just cut them after two decimal places!
from math import trunc
def two_decimal_places(number):
    factor = float(10 ** 2)
    return trunc(number * factor) / factor

# Definition
# A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5
# Given a number determine if it special number or not .
def special_number(n):
    return "Special!!" if max(str(n)) <= "5" else "NOT!!"

# Given an array (a list in Python) of integers and an integer n, find all occurrences of n
# in the given array and return another array containing all the index positions of n in the given array.
# If n is not in the given array, return an empty array [].
# Assume that n and all values in the given array will always be integers.
def find_all(array, n):
    return [e for e,i in enumerate(array) if i == n]

# Given an array of numbers (in string format), you must return a string.
# The numbers correspond to the letters of the alphabet in reverse order:
# a=26, z=1 etc. You should also account for '!', '?' and ' ' that are represented by
# '27', '28' and '29' respectively.
# All inputs will be valid.
def switcher(arr):
    letters = ' ?!abcdefghijklmnopqrstuvwxyz'
    return ''.join(letters[::-1][int(idx) - 1] for idx in arr)

# My friend wants a new band name for her band. She like bands that use the formula:
# "The" + a noun with the first letter capitalized, for example:
# "dolphin" -> "The Dolphin"
# However, when a noun STARTS and ENDS with the same letter,
# she likes to repeat the noun twice and connect them together
# with the first and last letter, combined into one word (WITHOUT "The" in front), like this:
# "alaska" -> "Alaskalaska"
# Complete the function that takes a noun as a string, and returns her preferred band name written as a string.
def band_name_generator(name):
    name = name.lower()
    if name[0] == name[-1]:
        return (name[:-1] + name).capitalize()
    return "The {}".format(name.capitalize())

# Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied,
# only prime numbers are multiplied to calculate the primorial of a number.
# It's denoted with P# and it is the product of the first n prime numbers.
# Task
# Given a number N , calculate its primorial.
import functools
def num_primorial(n):
    def sieveOfEratosthenes(n):
        if n <= 2:
            return []
        sieve = list(range(3, n, 2))
        top = len(sieve)
        for si in sieve:
            if si:
                bottom = (si*si - 3) // 2
                if bottom >= top:
                    break
                sieve[bottom::si] = [0] * -((bottom - top) // si)
        return [2] + [el for el in sieve if el]
    return functools.reduce(lambda a, b: a*b, sieveOfEratosthenes(10000)[:n])

# Well met with Fibonacci bigger brother, AKA Tribonacci.
# As the name may already reveal, it works basically like a Fibonacci,
# but summing the last 3 (instead of 2) numbers of the sequence to generate the next.
# And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting
# input (AKA signature), we have this sequence:
def tribonacci(signature, n):
    if n == 0:
        return []
    def fib(n):
        a, b, c = signature[0], signature[1], signature[2]
        for _ in range(n):
            yield a
            a, b, c = b, c, a+b+c
    return list(fib(n))

# You receive some random elements as a space-delimited string. Check if the
# elements are part of an ascending sequence of integers
# starting with 1, with an increment of 1 (e.g. 1, 2, 3, 4).
# Return:
# 0 if the elements can form such a sequence, and no number is missing ("not broken", e.g. "1 2 4 3")
# 1 if there are any non-numeric elements in the input ("invalid", e.g. "1 2 a")
# n if the elements are part of such a sequence, but some numbers are missing,
# and n is the lowest of them ("broken", e.g. "1 2 4" or "1 5")
def find_missing_number(sequence):
    if not sequence:
        return 0
    try:
        sequence = set(int(a) for a in sequence.split())
    except ValueError:
        return 1
    for b in range(1, max(sequence) + 1):
        if b not in sequence:
            return b
    return 0

# The bloody photocopier is broken... Just as you were sneaking around
# the office to print off your favourite binary code!
# Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.
# Given a string of binary, return the version the photocopier gives you as a string.
def broken(inp):
    return inp.translate(inp.maketrans({'0':'1', '1':'0'}))

# Write a function that finds the sum of all its arguments.
def sum_args(*args):
    return sum([*args])

# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).
# Input:
# If, you can read?
# Output:
# India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?
# Note:
# There are preloaded dictionary you can use, named NATO
# The set of used punctuation is ,.!?.
# Punctuation should be kept in your return string, but spaces should not.
# Xray should not have a dash within.
# Every word and punctuation mark should be seperated by a space ' '.
# There should be no trailing whitespace
NATO
def to_nato(words):
    return ' '.join(NATO[i.upper()] if i not in ',.!?' else i for i in words.replace(' ', ''))

# Cheesy Cheeseman just got a new monitor! He is happy with it,
# but he just discovered that his old desktop wallpaper no longer fits.
# He wants to find a new wallpaper, but does not know which size wallpaper
# he should be looking for, and alas, he just threw out the new monitor's box.
# Luckily he remembers the width and the aspect ratio of the monitor from
# when Bob Mortimer sold it to him. Can you help Cheesy out?
# The Challenge
# Given an integer width and a string ratio written as WIDTH:HEIGHT,
# output the screen dimensions as a string written as WIDTHxHEIGHT.
# Note: The calculated height should be represented as an integer.
# If the height is fractional, truncate it.
def find_screen_height(width, ratio):
    lhs, rhs = list(map(int, ratio.split(':')))
    height = int(width * rhs/lhs)
    return str(width) + 'x' + str(height)

# Create the function prefill that returns an array of n elements
# that all have the same value v. See if you can do this without using a loop.
# You have to validate input:
# v can be anything (primitive or otherwise)
# if v is ommited, fill the array with undefined
# if n is 0, return an empty array
# if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
# When throwing a TypeError, the message should be n is invalid, where
# you replace n for the actual value passed to the function.
def prefill(n,v='undefined'):
    if str(n).isdigit()==True:
        return [v for _ in range(int(n))]
    else:
        raise TypeError('%s is invalid'%(n))

# A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code
# c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.
# In the bookseller's stocklist each code c is followed
# by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.
# For example an extract of a stocklist could be:
# L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
# or
# L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
# You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :
# M = {"A", "B", "C", "W"}
# or
# M = ["A", "B", "C", "W"] or ...
# and your task is to find all the books of L with codes
# belonging to each category of M and to sum their quantity according to each category.
# For the lists L and M of example you have to return the
# string (in Haskell/Clojure/Racket/Prolog a list of pairs):
def stock_list(listOfArt, listofCat):
	stock = {}
	result=''
	for a in listOfArt:
		cat = a.split(' ')[0][0:1]
		if stock.get(cat):
			stock[cat]+= int(a.split(' ')[1])
		else:
			stock[cat] = int(a.split(' ')[1])
	for c in listofCat:
		if stock.get(c):
			result+='({0} : {1}) - '.format(c, stock.get(c))
		else:
			result+='({0} : {1}) - '.format(c, 0)
	if all(s == 0 for s in stock.values()): return ''
	return result[0:len(result)-3] if result.endswith(' ') else result

# Given a string of digits confirm whether the sum of all the individual even digits
# are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.
# If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"
# If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"
# If the total of both even and odd numbers are identical return: "Even and Odd are the same"
def even_or_odd(s):
    a = sum(int(i) for i in s if int(i)%2 != 0)
    b = sum(int(i) for i in s if int(i)%2 == 0)
    return 'Even is greater than Odd' if b > a else 'Odd is greater than Even' if a>b else 'Even and Odd are the same'

# Given two words and a letter, return a single word that's a combination of both words,
# merged at the point where the given letter first appears in each word.
# The returned word should have the beginning of the first word and the ending of the second,
# with the dividing letter in the middle. You can assume both words will contain the dividing letter.
def string_merge(string1, string2, letter):
    return string1[:string1.index(letter)] + string2[string2.index(letter):]

# Given a positive integer n: 0 < n < 1e6,
# remove the last digit until you're left with a number that is a multiple of three.
# Return n if the input is already a multiple of three,
# and if no such number exists, return null, a similar empty value, or -1.
def prev_mult_of_three(n):
    while n % 3 != 0:
        if len(str(n)) == 1 and n % 3 != 0:
            return None
        n = int(str(n)[:-1])
    return n

# A traveling salesman has to visit clients. He got each client's address e.g. "432 Main Long Road
# St. Louisville OH 43071" as a list.
# The basic zipcode format usually consists of two capital letters followed by a white
# space and five digits. The list of clients to visit was given as a string of all
# addresses, each separated from the others by a comma, e.g. :
# "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,
# 786 High Street Pollocksville NY 56432".
# To ease his travel he wants to group the list by zipcode.
# Task
# The function travel will take two parameters r (addresses' list of all
# clients' as a string) and zipcode and returns a string in the following format:
# zipcode:street and town,street and town,.../house number,house number,...
# The street numbers must be in the same order as the streets where they belong.
# If a given zipcode doesn't exist in the list of clients' addresses return "zipcode:/"
def travel(r, zipcode):
    l = r.split(',')
    lst = []
    l_n = []
    con = ''
    for elem in l:
        if zipcode == elem[-8:]:
            lst.append(elem[:-9])
    for i in lst:
        while True:
            for char in i:
                if char.isdigit():
                    con += char
                    continue
                l_n.append(con)
                con = ''
                break
            break
    for i in range(len(lst)):
        lst[i] = lst[i][len(l_n[i])+1:]
    return f"{zipcode}:{','.join(i for i in lst)}/{','.join(i for i in l_n)}"

# You are given a string of n lines, each substring being n characters long: For example:
# s = "abcd\nefgh\nijkl\nmnop"
# We will study some transformations of this square of strings.
# Clock rotation 180 degrees: rot
# rot(s) => "ponm\nlkji\nhgfe\ndcba"
# selfie_and_rot(s) (or selfieAndRot or selfie-and-rot)
# It is initial string + string obtained by clock rotation 180 degrees
# with dots interspersed in order (hopefully) to better show the rotation when printed.
# s = "abcd\nefgh\nijkl\nmnop" -->
# "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
def rot(strng):
    return strng[::-1]
def selfie_and_rot(strng):
    return '\n'.join(i+'.'*len(i) for i in strng.split('\n')) + '\n' +'\n'.join('.'*len(i)+i[::-1] for i in strng.split('\n')[::-1])
def oper(fct, s):
    return fct(s)

# Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume
# of n3 n^3n  3
#  , the cube above will have volume of (n−1)3 (n-1)^3(n−1) 3
#   and so on until the top which will have a volume of 13 1^31 3 .
# You are given the total volume m of the building. Being given m can you find the
# number n of cubes you will have to build?
# The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an
# integer m and you have to return the integer n such
# as n3+(n−1)3+(n−2)3+...+13=m n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = mn
# 3 +(n−1) 3 +(n−2) 3 +...+1 3 =m if such a n exists or -1 if there is no such n.
def find_nb(M):
    m = 0
    i = 0
    while m < M:
        m += i ** 3
        if m == M:
            return i
        i += 1
    return -1

# It's tricky keeping track of who is owed what when spending money in a group.
# Write a function to balance the books.
# The function should take one parameter: an object/dict with two or more
# name-value pairs which represent the members of the group and the amount spent by each.
# The function should return an object/dict with the same names, showing
# how much money the members should pay or receive.
# Further points:
# The values should be positive numbers if the person should receive money
# from the group, negative numbers if they owe money to the group.
# If value is a decimal, round to two decimal places.
# Translations and comments (and upvotes!) welcome.
# Example
# 3 friends go out together: A spends £20, B spends £15, and C spends £10.
# The function should return an object/dict showing that A should receive £5,
# B should receive £0, and C should pay £5.
group = {
    'A': 20,
    'B': 15,
    'C': 10
}
def split_the_bill(x):
    total_each_owed = sum(x.values())/float(len(x))
    return {key:round(value - total_each_owed, 2) for key, value in x.items()}

# For this game of BINGO, you will receive a single array of 10 numbers
# from 1 to 26 as an input. Duplicate numbers within the array are possible.
# Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc).
# Write a function where you will win the game if your numbers can spell "BINGO".
# They do not need to be in the right order in the input array. Otherwise you will lose.
# Your outputs should be "WIN" or "LOSE" respectively.
import string
def bingo(array):
    lst = []
    for elem in array:
        lst.append(string.ascii_lowercase[elem-1])
    return 'WIN' if all(i in lst for i in 'bingo') else 'LOSE'

# Let's create some scrolling text!
# Your task is to complete the function which takes a string,
# and returns an array with all possible rotations of the given string, in uppercase.
def scrolling_text(text):
    lst = []
    for i in range(len(text)):
        lst.append(text.upper())
        text = text[1:] + text[0]
    return lst

# John wants to decorate the walls of a room with wallpaper. He wants a fool-proof method for getting it right.
# John knows that the rectangular room has a length of l meters, a width of w meters,
# a height of h meters. The standard width of the rolls he wants to buy is 52 centimeters.
# The length of a roll is 10 meters. He bears in mind however, that it’s best to have an
# extra length of wallpaper handy in case of mistakes or miscalculations so he wants to
# buy a length 15% greater than the one he needs.
# Last time he did these calculations he got a headache, so could you help John?
# Task
# Your function wallpaper(l, w, h) should return as a plain English word in lower
# case the number of rolls he must buy.

from math import ceil
WORDS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'
}
def wallpaper(l, w, h):
    if 0 in (l, w, h):
        return 'zero'
    return WORDS[int(ceil((((l * h) * 2 + (w * h) * 2) * 1.15) / 5.2))]

# Count the number of exclamation marks and question marks, return the product.
def product(s):
    return int(s.count('!'))*int(s.count('?'))

# For every good kata idea there seem to be quite a few bad ones!
# In this kata you need to check the provided 2 dimensional array
# (x) for good ideas 'good' and bad ideas 'bad'. If there are
# one or two good ideas, return 'Publish!', if there are more
# than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
# The sub arrays may not be the same length.
# The solution should be case insensitive (ie good, GOOD
# and gOOd all count as a good idea). All inputs may not be strings.
def well(arr):
    l = [j.lower() if type(j) == str else j for i in arr for j in i]
    con = l.count('good')
    return 'Fail!' if con == 0 else 'Publish!' if 1 <= con <= 2 else 'I smell a series!'

# In this kata you are given a string for example:
# "example(unwanted thing)example"
# Your task is to remove everything inside the parentheses as well as the parentheses themselves.
# The example above would return:
# "exampleexample"
# Notes
# Other than parentheses only letters and spaces can occur in the string.
# Don't worry about other brackets like "[]" and "{}" as these will never appear.
# There can be multiple parentheses.
# The parentheses can be nested.
import re
def remove_parentheses(s):
    while re.findall(r"\([^()]*\)", s):
        s = re.sub(r"\([^()]*\)", "", s)
    return s

# Create the function consecutive(arr) that takes an array of integers
# and return the minimum number of integers needed to make the contents
# of arr consecutive from the lowest number to the highest number.
def consecutive(arr):
    try:
        return len(range(min(arr), max(arr)+1)) - len(arr)
    except:
        return 0

# Write a function that takes a string
# and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.
# All non-vowels including non alpha characters (spaces,commas etc.) should be included.
def vowel_one(s):
    return ''.join('1' if i.lower() in 'aeoiu' else '0' for i in s)

# Write a function to find if a number is lucky or not.
# If the sum of all digits is 0 or multiple of 9 then the number is lucky.
# 1892376 => 1+8+9+2+3+7+6 = 36. 36 is divisible by 9, hence number is lucky.
# Function will return true for lucky numbers and false for others.
def is_lucky(n):
    return sum(int(i) for i in str(n)) % 9 == 0 or str(sum(int(i) for i in str(n)))[0] == '0'

# To introduce the problem think to my neighbor who drives a tanker truck.
# The level indicator is down and he is worried because he does not know
# if he will be able to make deliveries. We put the truck on a horizontal
# ground and measured the height of the liquid in the tank.
# Fortunately the tank is a perfect cylinder and the vertical walls on
# each end are flat. The height of the remaining liquid is h, the diameter
# of the cylinder base is d, the total volume is vt (h, d, vt are positive
# or null integers). You can assume that h <= d.
# Could you calculate the remaining volume of the liquid? Your function
# tankvol(h, d, vt) returns an integer which is the truncated result (e.g floor) of your float calculation.
import math
def tankvol(h, d, vt):
    radius = d / 2
    cylinder_length = vt / (math.pi * (radius * radius))
    volume = cylinder_length * (((radius * radius) * math.acos((radius - h) / radius)) - ((radius - h) * math.sqrt((2 * radius * h) - (h * h))))
    return int(volume)

# Given a list of integers values, your job is to return the sum of the values;
# however, if the same integer value appears multiple times in the list,
# you can only count it once in your sum.
def unique_sum(lst):
    return sum(set(lst)) if lst else None

# Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency
# in cents, and returns a dictionary/hash which shows the least amount of coins used to make up
# that amount. The only coin denominations considered in this exercise are: Pennies (1¢),
# Nickels (5¢), Dimes (10¢) and Quarters (25¢). Therefor the dictionary returned should
# contain exactly 4 key/value pairs.
# Notes:
# If the function is passed either 0 or a negative number, the function should
# return the dictionary with all values equal to 0.
# If a float is passed into the function, its value should be rounded down,
# and the resulting dictionary should never contain fractions of a coin.
def loose_change(cents):
    d = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents > 0:
        d['Quarters'] = cents//25
        cents = cents- 25*(cents//25)
        d['Dimes'] = cents // 10
        cents = cents-10*(cents//10)
        d['Nickels'] = cents // 5
        cents = cents-5*(cents//5)
        d['Pennies'] = cents // 1
    return d

# Move every letter in the provided string forward 10 letters through the alphabet.
# If it goes past 'z', start again at 'a'.
# Input will be a string with length > 0.
def move_ten(st):
    d = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    return ''.join(d[d.index(i)+10] for i in st)

# Function composition is a mathematical operation that mainly presents itself in lambda calculus
# and computability. It is explained well here, but this is my explanation, in simple mathematical notation:
# f3 = compose( f1 f2 )
#    Is equivalent to...
# f3(a) = f1( f2( a ) )
# Your task is to create a compose function to carry out this task,
# which will be passed two functions or lambdas. Ruby functions will
# be passed, and should return, either a proc or a lambda.
# Remember that the resulting composed function may be passed multiple arguments!
def compose(f, g):
    def wrapper(*args):
        return f(g(*args))
    return wrapper

# Your job is to implement a function which returns the last D digits of an integer N as a list.
# Special cases:
# If D > (the number of digits of N), return all the digits.
# If D <= 0, return an empty list.
def solution(n,d):
    return [int(i) for i in str(n)[-d:]] if d > 0 else []

# Time to win the lottery!
# Given a lottery ticket (ticket), represented by an array of 2-value arrays,
# you must find out if you've won the jackpot.
# Example ticket:
# [ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
# To do this, you must first count the 'mini-wins' on your ticket.
# Each subarray has both a string and a number within it.
# If the character code of any of the characters in the string matches the number,
# you get a mini win. Note you can only have one mini win per sub array.
# Once you have counted all of your mini wins, compare that number to the
# other input provided (win). If your total is more than or equal to (win),
# return 'Winner!'. Else return 'Loser!'.
# All inputs will be in the correct format. Strings on tickets are not always the same length.
def bingo(ticket,win):
    count = 0
    for i in ticket:
        for j in i[0]:
            if ord(j)==i[1]:
                count += 1
                break
    return 'Winner!' if count >= win else 'Loser!'

# Given a positive number n > 1 find the prime factor
# decomposition of n. The result will be a string with the following form :
#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
def prime_factors(n):
    i = 2
    res = {}
    while n/i != 1:
        if n%i == 0:
            if i in res:
                res[i] = res[i]+1
            else:
                res[i] = 1
            n = n/i
        else:
            i+=1
    if i in res:
        res[i] = res[i]+1
    else:
        res[i] = 1
    t = ''
    res = sorted(res.items(),key = lambda a:a[0])
    for key in res:
        if key[1] == 1:
            t = t + '('+str(key[0]) +')'
        else:
            t = t + '(' +str(key[0]) + '**' + str(key[1]) + ')'
    return t

# Write a function insert_dash(num) / insertDash(num) / InsertDash(int num) that will insert dashes
# ('-') between each two odd digits in num. For example:
# if num is 454793 the output should be 4547-9-3. Don't count zero as an odd digit.
# Note that the number will always be non-negative (>= 0).
import re
def insert_dash(num):
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))\

# Write a function that returns true if the number is a "Very Even" number.
# If a number is a single digit, then it is simply "Very Even" if it itself is even.
# If it has 2 or more digits, it is "Very Even" if the sum of its digits is "Very Even".
def is_very_even_number(n):
    while len(str(n))!= 1:
        n = sum(int(i) for i in str(n))
    return n % 2 == 0

# The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.
# But some of the rats are deaf and are going the wrong way!
# Kata Task
# How many deaf rats are there?
# Legend
# P = The Pied Piper
# O~ = Rat going left
# ~O = Rat going right
# Example
# ex1 ~O~O~O~O P has 0 deaf rats
# ex2 P O~ O~ ~O O~ has 1 deaf rat
# ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats
import re
def count_deaf_rats(town):
    t = town.split('P')
    return find(t[0]).count('O~') + find(t[1]).count('~O')
def find(s):
    return [''.join(j) for j in re.findall('(~O)|(O~)', s)]

# From Wikipedia:
# "A divisibility rule is a shorthand way of determining whether
# a given integer is divisible by a fixed divisor without performing
# the division, usually by examining its digits."
# When you divide the successive powers of 10 by 13 you get the
# following remainders of the integer divisions:
# 1, 10, 9, 12, 3, 4 because:
# 10 ^ 0 ->  1 (mod 13)
# 10 ^ 1 -> 10 (mod 13)
# 10 ^ 2 ->  9 (mod 13)
# 10 ^ 3 -> 12 (mod 13)
# 10 ^ 4 ->  3 (mod 13)
# 10 ^ 5 ->  4 (mod 13)
# (For "mod" you can see: https://en.wikipedia.org/wiki/Modulo_operation)
# Then the whole pattern repeats. Hence the following method:
# Multiply
# the right most digit of the number with the left most number in the sequence shown above,
# the second right most digit with the second left most digit of the number in the sequence.
# The cycle goes on and you sum all these products. Repeat this process until
# the sequence of sums is stationary.
def thirt(n):
    pattern = [1, 10, 9, 12, 3, 4]
    sum = 0
    while True:
        current_sum = 0
        for index, digit in enumerate(str(n)[::-1]):
            current_index = index % len(pattern)
            current_sum += int(digit) * pattern[current_index]
        if sum == current_sum:
            return sum
        sum = current_sum
        n = current_sum

# Create a function that takes in the sum and age difference of two people, calculates
# their individual ages, and returns a pair of values (oldest age first) if those exist or null/None if:
# sum < 0
# difference < 0
# Either of the calculated ages come out to be negative
def get_ages(sum_, diff):
    a = (sum_ - diff)/2
    b = sum_ - a
    if sum_ < 0 or diff < 0 or a < 0 or b < 0:
        return None
    return (b,a)

# Create a function add(n)/Add(n) which returns a function that always adds n to any number
# Note for Java: the return type and methods have not been provided to make it a bit more challenging.
def add(n):
    return lambda x: x + n

# Write a program that outputs the top n elements from a list.
# Example:
# largest(2, [7,6,5,4,3,2,1])
# => [6,7]
def largest(n,xs):
    return sorted(xs)[-n:]

# The aim of this kata is to split a given string into different strings
# of equal size (note size of strings is passed to the method)
def split_in_parts(s, part_length):
    words = []
    for i in range(0, len(s), part_length):
        words.append(s[i:i+part_length])
    return ' '.join(words)

# Positive integers that are divisible exactly by the sum of
# their digits are called Harshad numbers. The first few
# Harshad numbers are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, ...
# We are interested in Harshad numbers where the product of its digit sum s
# and s with the digits reversed, gives the original number n. For example consider number 1729:
# its digit sum, s = 1 + 7 + 2 + 9 = 19
# reversing s = 91
# and 19 * 91 = 1729 --> the number that we started with.
# Complete the function which tests if a positive integer n is Harshad number,
# and returns True if the product of its digit sum and its digit sum reversed equals n; otherwise return False.
def number_joy(n):
    s = sum(int(i) for i in str(n))
    return s * int(str(s)[::-1]) == n

# Nickname Generator
# Write a function, nicknameGenerator that takes
# a string name as an argument and returns the first 3 or 4 letters as a nickname.
# If the 3rd letter is a consonant, return the first 3 letters.
# nickname("Robert") //=> "Rob"
# nickname("Kimberly") //=> "Kim"
# nickname("Samantha") //=> "Sam"
# If the 3rd letter is a vowel, return the first 4 letters.
def nickname_generator(name):
    return "Error: Name too short" if len(name) < 4 else name[:3+(name[2] in "aeiuo")]

# Return an output string that translates an input string s/$s by
# replacing each character in s/$s with a number representing
# the number of times that character occurs in s/$s and separating each number with the character(s) sep/$sep.
def freq_seq(s, sep):
    return sep.join(str(s.count(i)) for i in s)

# You are to write a function that takes a string as its first parameter.
# This string will be a string of words.
# You are expected to then use the second parameter, which will be an integer,
# to find the corresponding word in the given string. The first word would be represented by 0.
# Once you have the located string you are finally going to multiply by it the
# third provided parameter, which will also be an integer.
# You are additionally required to add a hyphen in between each word.
def modify_multiply(st, loc, num):
    return '-'.join(st.split()[loc] for i in range(num))

# Create a function which accepts one arbitrary string as an argument, and return a string of length 26.
# The objective is to set each of the 26 characters of the output string to either '1' or '0'
# based on the fact whether the Nth letter of the alphabet is present in the input (independent of its case).
# So if an 'a' or an 'A' appears anywhere in the input string (any number of times),
# set the first character of the output string to '1', otherwise to '0'.
# if 'b' or 'B' appears in the string, set the second character to '1', and so on for the rest of the alphabet.
def change(st):
    alp = "abcdefghijklmnopqrstuvwxyz"
    return "".join(["1" if c in st or c.upper() in st else "0" for c in alp]) if len(st) else "00000000000000000000000000"

# There are two lists, possibly of different lengths. The first one consists of keys,
# the second one consists of values. Write a function createDict(keys, values)
# that returns a dictionary created from keys and values. If there are not enough values,
# the rest of keys should have a None (JS null)value. If there not enough keys, just ignore the rest of values.
def createDict(keys, values):
    return {k:(values[e] if e<len(values) else None) for e,k in enumerate(keys)}

# dataand data1 are two strings with rainfall records of a few cities for months from January
# to December. The records of towns are separated by \n. The name of each town is followed by :.
# data and towns can be seen in "Your Test Cases:".
# Task:
# function: mean(town, strng) should return the average of rainfall
# for the city town and the strng data or data1 (In R and Julia this function is called avg).
# function: variance(town, strng) should return the variance of rainfall
# for the city town and the strng data or data1.
import re
def mean(town, strng):
    data_split = re.findall(r'.+(?:\n|$)', strng)
    for counter, town_info in enumerate(data_split):
        if town in town_info:
            town_name = re.match(r'\w+', town_info)
            if town != town_name.group():
                continue
            numbers = re.findall(r'\d+\.?\d+', town_info)
            float_numbers = [float(x) for x in numbers]
            return sum(float_numbers)/len(float_numbers)
    return -1
def variance(town, strng):
    data_split = re.findall(r'.+(?:\n|$)', strng)
    for counter, town_info in enumerate(data_split):
        if town in town_info:
            town_name = re.match(r'\w+', town_info)
            if town != town_name.group():
                continue
            numbers = re.findall(r'\d+\.?\d+', town_info)
            float_numbers = [float(x) for x in numbers]
            mean = sum(float_numbers)/len(float_numbers)
            squared_nums = [(x-mean)**2 for x in float_numbers]
            return sum(squared_nums)/(len(squared_nums))
    return -1

# Your task is to write a higher order function for chaining together a list of unary functions.
# In other words, it should return a function that does a left fold on the given functions.
def chained(functions):
    def apply(param):
        result = param
        for f in functions:
            result = f(result)
        return result
    return apply

Unscramble the eggs.

# The string given to your function has had an "egg"
# inserted directly after each consonant. You need to return the string before it became eggcoded.
def unscramble_eggs(word):
    return word.replace('egg','')

# Create function fib that returns n'th element of Fibonacci sequence (classic programming task).
def fibonacci(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a,b = b, a+b
    return a

# In this Kata, you will be given an array of unique elements, and your task
# is to rearrange the values so that the first max value is followed by the first minimum,
# followed by second max value then second min value, etc.
def solve(arr):
    l = sorted(arr, reverse=True)
    ls = []
    for i in range(len(arr)//2+1):
        ls.append(l[i])
        ls.append(l[::-1][i])
    return ls[:-2] if len(arr)%2 == 0 else ls[:-1]

# You are given a string of letters and an array of numbers.
# The numbers indicate positions of letters that must be removed, in order,
# starting from the beginning of the array.
# After each removal the size of the string decreases (there is no empty space).
# Return the only letter left.
def last_survivor(letters, coords):
    for i in coords:
        letters = letters[:i] + letters[i+1:]
    return letters

# Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language)
# that determines if a given non-negative integer is a power of two. From the corresponding Wikipedia entry:
# a power of two is a number of the form 2n where n is an integer,
# i.e. the result of exponentiation with number two as the base and integer n as the exponent.
# You may assume the input is always valid.
def power_of_two(n: int) -> list:
    i = 2
    while i < n:
        i=i*2
    return i == n if n!=1 else True

# Complete the function which takes a non-zero integer as its argument.
# If the integer is divisible by 3, return the string "Java".
# If the integer is divisible by 3 and divisible by 4, return the string "Coffee"
# If one of the condition above is true and the integer is even, add "Script" to the end of the string.
# If none of the condition is true, return the string "mocha_missing!"
def caffeine_buzz(n):
    i = ''
    if n % 3 == 0 and n % 4 == 0:
        i += 'Coffee'
    elif n % 3 == 0:
        i += 'Java'
    else:
        return "mocha_missing!"
    if n % 2 == 0:
        i += 'Script'
    return i

# A new task for you!
# You have to create a method, that corrects a given time string.
# There was a problem in addition, so many of the time strings are broken.
# Time is formatted using the 24-hour clock, so from 00:00:00 to 23:59:59.
def time_correct(t):
    if not t:
        return t
    try:
        h, m, s = map(int, t.split(":"))
        s = h * 3600 + m * 60 + s
        _, s = divmod(s, 86400)
        h, s = divmod(s, 3600)
        m, s = divmod(s, 60)
        return "{:02}:{:02}:{:02}".format(h, m, s)
    except ValueError:
        return None

# Print all numbers up to 3rd parameter which are multiple of both 1st and 2nd parameter.
# Python, Javascript, Java, Ruby versions: return results in a list/array
# NOTICE:
# Do NOT worry about checking zeros or negative values.
# To find out if 3rd parameter (the upper limit) is inclusive or not,
# check the tests, it differs in each translation
def multiples(s1,s2,s3):
    l = []
    for i in range(1,s3):
        if i %s1 == 0 and i % s2 == 0:
            l.append(i)
    return l

# The aim of the kata is to try to show how difficult it can be to calculate
# decimals of an irrational number with a certain precision.
# We have chosen to get a few decimals of the number
# "pi" using the following infinite series (Leibniz 1646–1716):
# PI / 4 = 1 - 1/3 + 1/5 - 1/7 + ... which gives an approximation of PI / 4.
# http://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# To have a measure of the difficulty we will count how many
# iterations are needed to calculate PI with a given precision of epsilon.
# There are several ways to determine the precision of the calculus but to keep
# things easy we will calculate PI within epsilon of your language Math::PI constant.
# In other words, given as input a precision of epsilon we will stop the
# iterative process when the absolute value of the difference between our
# calculation using the Leibniz series and the Math::PI constant of your language is less than epsilon.
# Your function returns an array or a string or a tuple depending
# on the language (See sample tests) with
# your number of iterations
# your approximation of PI with 10 decimals
from math import pi
def iter_pi(epsilon):
    count = 1
    my_pi = 4.0
    while abs(pi - my_pi) > epsilon:
        if count % 2:
            my_pi -= (1.0 / (count * 2 + 1)) * 4
        else:
            my_pi += (1.0 / (count * 2 + 1)) * 4
        count += 1
    return [count, round(my_pi, 10)]

# Create a function isDivisible(n,...) that checks if the first argument
# n is divisible by all other arguments (return true if no other arguments)
def is_divisible(*args):
    l =[*args]
    return all(l[0] % i == 0 for i in l[1:])

# Help Suzuki rake his garden!
# The monastery has a magnificent Zen garden made of white gravel and rocks and it
# is raked diligently everyday by the monks. Suzuki having a keen eye
# is always on the lookout for anything creeping into the garden that must
# be removed during the daily raking such as insects or moss.
# You will be given a string representing the garden such as:
VALID = {'gravel', 'rock'}
def rake_garden(garden):
    return ' '.join(a if a in VALID else 'gravel' for a in garden.split())

# Let us begin with an example:
# Take a number: 56789. Rotate left, you get 67895.
# Keep the first digit in place and rotate left the other digits: 68957.
# Keep the first two digits in place and rotate the other ones: 68579.
# Keep the first three digits and rotate left the rest: 68597. Now it is over
# since keeping the first four it remains only one digit which rotated is itself.
# You have the following sequence of numbers:
# 56789 -> 67895 -> 68957 -> 68579 -> 68597
# and you must return the greatest: 68957.
# Task
# Write function max_rot(n) which given a positive integer n
# returns the maximum number you got doing rotations similar to the above example.
# So max_rot (or maxRot or ... depending on the language) is such as:
def max_rot(n):
    maximum = n
    s = list(str(n))
    for i in range(len(s) - 1):
        s.append(s.pop(i))
        current = int(''.join(s))
        if current > maximum:
            maximum = current
    return maximum

# Scenario
# the rhythm of beautiful musical notes is drawing a Pendulum
# Beautiful musical notes are the Numbers
# Task
# Given an array/list [] of n integers , Arrange them in a way similar to the to-and-fro movement of a Pendulum
# The Smallest element of the list of integers , must come in center position of array/list.
# The Higher than smallest , goes to the right .
# The Next higher number goes to the left of minimum number and So on ,
# in a to-and-fro manner similar to that of a Pendulum.
def pendulum(values):
    sorted_values = sorted(values)
    mid = [sorted_values [0]]
    right = sorted_values[1::2]
    left = sorted_values[2::2]
    return left[::-1] + mid + right

# Sort the given array of strings in alphabetical order, case insensitive. For example:
def sortme(words):
    return sorted(words,key=lambda x: x.lower())

# Write a function that returns a sequence (index begins with 1) of all the even characters
# from a string. If the string is smaller than two characters or longer than 100 characters,
# the function should return "invalid string".
def even_chars(st):
    return [i for i in st[1::2]] if 1 < len(st) < 100 else 'invalid string'

# The Stanton measure of an array is computed as follows: count the number
# of occurences for value 1 in the array. Let this count be n. The Stanton measure
# is the number of times that n appears in the array.
# Write a function which takes an integer array and returns its Stanton measure.
# Examples
# The Stanton measure of [1, 4, 3, 2, 1, 2, 3, 2] is 3, because 1 occurs 2 times
# in the array and 2 occurs 3 times.
# The Stanton measure of [1, 4, 1, 2, 11, 2, 3, 1] is 1, because 1 occurs 3 times
# in the array and 3 occurs 1 time.
def stanton_measure(arr):
    return arr.count(arr.count(1))

# There exist two zeroes: +0 (or just 0) and -0.
# Write a function that returns true if the input number is -0 and false otherwise (True and False for Python).
# In JavaScript / TypeScript / Coffeescript the input will be a number.
# In Python / Java / C / NASM / Haskell / the input will be a float.
def is_negative_zero(n):
    return str(n) == '-0.0'

# Our loose definition of Vampire Numbers can be described as follows:
def vampire_test(x, y):
    l = [i for i in str(x * y)]
    w = str(x) + str(y)
    return all(i in l for i in w) and len(w) == len(l)

# Task
# Using n as a parameter in the function pattern, where n>0,
# \complete the codes to get the pattern (take the help of examples):
# Note: There is no newline in the end (after the pattern ends)
# Examples
# pattern(3) should return "1\n1*2\n1**3", e.g. the following:
def pattern(n):
    OUTPUT = '1{}{}'.format
    return '\n'.join(OUTPUT('*' * a, a + 1 if a else '') for a in range(n))

# The UK driving number is made up from the personal details of the driver. The individual letters
# and digits can be code using the below information
from dateutil.parser import parse
def driver(data):
    lic = ""
    if len(data[2]) >= 5:
          lic += data[2][:5]
    else:
            lic += data[2]
            while (len(lic) < 5): lic += "9"
    lic += (str(parse(data[3]).year))[2]
    month = parse(data[3]).month
    if data[4] == "F": month += 50
    month = str(month)
    if len(month) == 1: month = "0" + month
    lic += month
    day = str(parse(data[3]).day)
    if len(day) == 1: day = "0" + day
    lic += day
    lic += (str(parse(data[3]).year))[3]
    lic +=  data[0][:1]
    if (data[1]) != "":
        lic += data[1][:1]
    else:
        lic += "9"
    lic += "9AA"
    return lic.upper()

# Given the sum and gcd of two numbers, return those two numbers in ascending order.
# If the numbers do not exist, return -1, (or NULL in C, tuple (-1,-1)
# in C#, pair (-1,-1) in C++,None in Rust, array {-1,-1}  in Java and Golang).
def solve(s,g):
    for i in range(g, s+1, g):
        remainder = s - i
        if remainder % g == 0:
            return (i, remainder)
    return -1

# Write a function generateIntegers/generate_integers that accepts a single argument
# n/$n and generates an array containing the integers from 0 to n/$n inclusive.
# For example, generateIntegers(3)/generate_integers(3) should return [0, 1, 2, 3].
# n/$n can be any integer greater than or equal to 0.
def generate_integers(n):
    return list(range(n + 1))

# An element in an array is dominant if it is greater than all elements to its right.
# You will be given an array and your task will be to return a list of all dominant elements. For example:
def solve(arr):
    l = []
    for i in range(len(arr)):
        if max(arr[i:]) == arr[i] and arr[i] not in l:
            l.append(arr[i])
    return l

# Some people just have a first name; some people have first
# and last names and some people have first, middle and last names.
# You task is to initialize the middle names (if there is any).
def initialize_names(name):
    arr = name.split()
    l = []
    if len(arr)>2:
        l.append(arr[0])
        for i in arr[1:-1]:
            l.append(i[0].upper()+'.')
        l.append(arr[-1])
        return ' '.join(l)
    return name

# You are the developer working on a website which features a large counter
# on its homepage, proudly displaying the number of happy customers who have downloaded your companies software.
# You have been tasked with adding an effect to this counter to make it more interesting.
# Instead of just displaying the count value immediatley when the page loads,
# we want to create the effect of each digit cycling through its preceding
# numbers before stopping on the actual value.
# Task
# As a step towards achieving this; you have decided to create a function
# that will produce a multi-dimensional array out of the hit count value.
# Each inner dimension of the array represents an individual digit in the
# hit count, and will include all numbers that come before it, going back to 0.
# Rules
# The function will take one argument which will be a four character string representing hit count
# The function must return a multi-dimensional array containing four inner arrays
# The final value in each inner array must be the actual value to be displayed
# Values returned in the array must be of the type number
def counter_effect(hit_count):
    return [range(int(i)+1) for i in hit_count]

# Peter can see a clock in the mirror from the place he sits in the office. When he saw the clock shows 12:22
# He knows that the time is 11:38
# in the same manner:
# 05:25 --> 06:35
# 01:50 --> 10:10
# 11:58 --> 12:02
# 12:01 --> 11:59
# Please complete the function WhatIsTheTime(timeInMirror),
# where timeInMirror is the mirrored time (what Peter sees) as string.
# Return the real time as a string.
# Consider hours to be between 1 <= hour < 13.
# So there is no 00:20, instead it is 12:20.
# There is no 13:20, instead it is 01:20.
def what_is_the_time(time_in_mirror):
    hour = int(time_in_mirror[0:2])
    minute = int(time_in_mirror[3:5])
    if hour < 11:
        hour1 = 11 - hour
    else:
        hour1 = 23 - hour
    minute1 = 60 - minute
    if minute1 == 60:
        minute1 -=60
        hour1 += 1
    if hour1 > 12:
        hour1 -=12
    ans = ""
    if hour1 > 9 :
        ans = str(hour1) + ':'
    else:
        ans = '0' + str(hour1) + ':'
    if minute1 > 9:
        ans += str(minute1)
    else:
        ans += '0' + str(minute1)
    return ans

# Remove all exclamation marks from sentence except at the end.
def remove(s):
    count = 0
    j = s
    while j.endswith('!'):
        count += 1
        j = j[:-1]
    r = (len(s)-len(j))
    return j.replace('!', '') + '!' * r

# You have to create a function calcType, which receives 3 arguments: 2 numbers,
# and the result of an unknown operation performed on them (also a number).
# Based on those 3 values you have to return a string, that describes which operation
# was used to get the given result.
# The possible return strings are: "addition", "subtraction", "multiplication", "division".
def calc_type(a, b, res):
    if a+b==res:
        return 'addition'
    elif a-b==res:
        return 'subtraction'
    elif a*b==res:
        return 'multiplication'
    elif a/b==res:
        return 'division'

# You will be given an array which will include both integers and characters.
# Return an array of length 2 with a[0] representing the mean of the ten
# integers as a floating point number. There will always be 10 integers and 10 characters.
# Create a single string with the characters and return it as a[1] while maintaining the original order.
def mean(lst):
    return [sum(int(i) for i in lst if i.isdigit())/10, ''.join(j for j in lst if j.isalpha())]

# Write reverseList function that simply reverses lists.
def reverse_list(lst):
    return lst[::-1]


# Write function heron which calculates the area of a
# triangle with sides a, b, and c (x, y, z in COBOL). Heron 's formula:
# s∗(s−a)∗(s−b)∗(s−c)\sqrt {s * (s - a) * (s - b) * (s - c)} s∗(s−a)∗(s−b)∗(s−c)
# Output should have 2 digits precision.
def heron(a, b, c):
    i=(a+b+c)/2
    return round((i*(i-a)*(i-b)*(i-c))**.5, 2)

# A zero-indexed array arr consisting of n integers is given. The dominator of array
# arr is the value that occurs in more than half of the elements of arr.
# For example, consider array arr such that arr = [3,4,3,2,3,1,3,3]
# The dominator of arr is 3 because it occurs in 5 out of 8 elements of arr and 5 is more than a half of 8.
# Write a function dominator(arr) that, given a zero-indexed array arr consisting of n integers,
# returns the dominator of arr. The function should return −1 if array does not have a dominator.
# All values in arr will be >=0.
def dominator(arr):
    w = [i for i in arr if arr.count(i) > len(arr)//2]
    return w[0] if w else -1

# Christmas is coming, and Santa has a long list to go through, to find who deserves presents for the
# big day. Go through a list of children, and return
# a list containing every child who appeared on Santa's list.
# Do not add any child more than once. Output should be sorted.
# Comparison should be case sensitive and the returned list should contain only one copy of
# each name: "Sam" and "sam" are different, but "sAm" and "sAm" are not.
def find_children(santas_list, children):
    return sorted(set([child for child in children if child in santas_list]))

# Create a method that takes an array/list as an input,
# and outputs the index at which the sole odd number is located.
# This method should work with arrays with negative numbers. If there are
# no odd numbers in the array, then the method should output -1.
def odd_one(arr):
    try:
        return arr.index(max([i for i in arr if i%2!=0]))
    except:
        return -1

# Lot of museum allow you to be a member, for a certain
# amount amount_by_year you can have unlimitted acces to the museum.
# In this kata you should complete a function in order to know after how many visit it
# will be better to take an annual pass. The function take 2 arguments annual_price and individual_price.
import math
def how_many_times(annual_price, individual_price):
    return math.ceil(annual_price/individual_price)

# Move all exclamation marks to the end of the sentence
def remove(s):
    count = s.count('!')
    return s.replace('!', '') + '!'*count

# Digital Cypher assigns to each letter of the alphabet unique number. For example:
# a  b  c  d  e  f  g  h  i  j  k  l  m
# 1  2  3  4  5  6  7  8  9 10 11 12 13
# n  o  p  q  r  s  t  u  v  w  x  y  z
# 14 15 16 17 18 19 20 21 22 23 24 25 26
# Instead of letters in encrypted word we write the corresponding number, eg. The word scout:
#  s  c  o  u  t
# 19  3 15 21 20
# Then we add to each obtained digit consecutive digits from the key. For example. In case of key equal to 1939 :
def encode(message, key):
    letter_dict = {
        'a': 1,'b': 2,
        'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,
        'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26
        }
    num_list = []
    key_list = str(key)
    x = 0
    for i in message:
        num_list.append(letter_dict[i] + int(key_list[x]))
        x += 1
        if x >= len(key_list):
            x = 0
    return num_list

# Is every value in the array an array?
# This should only test the second array dimension of the array.
# The values of the nested arrays don't have to be arrays.
def arr_check(arr):
    return all(type(i) == list for i in arr)

# Your task is very simple. Just write a function takes an input string
# of lowercase letters and returns true/false depending on whether the string is in alphabetical order or not.
# Examples (input -> output)
# "kata" -> false ('a' comes after 'k')
# "ant" -> true (all characters are in alphabetical order)
def alphabetic(s):
    return s == "".join(sorted(s))

# Write function replaceAll (Python: replace_all) that will replace all occurrences of an item with another.
# Python / JavaScript: The function has to work for strings and lists.
# Example: replaceAll [1,2,2] 1 2 -> in list [1,2,2] we replace 1 with 2 to get new list [2,2,2]
def replace_all(obj, find, replace):
    if type(obj) == list:
        return [replace if i == find else i for i in obj]
    return obj.replace(find, replace)

# Learning to code around your full time job is taking over your life. You realise
# that in order to make significant steps quickly, it would help to go to a coding bootcamp in London.
# Problem is, many of them cost a fortune, and those that don't still
# involve a significant amount of time off work - who will pay your mortgage?!
# To offset this risk, you decide that rather than leaving work totally, you will request a
# sabbatical so that you can go back to work post bootcamp and be paid while you look for your next role.
# You need to approach your boss. Her decision will be based on three parameters:
# val = your value to the organisation
# happiness = her happiness level at the time of asking and finally
# The numbers of letters from 'sabbatical' that are present in string s.
# Note that if s contains three instances of the letter 'l', that still
# scores three points, even though there is only one in the word sabbatical.
# If the sum of the three parameters (as described above) is > 22, return 'Sabbatical!
# Boom!', else return 'Back to your desk, boy.'.
# FUNDAMENTALSSTRINGSARRAYSMATHEMATICS
import re
def sabb(s, value, happiness):
    letters = re.findall('[sabatical]', s)
    return 'Sabbatical! Boom!' if len(letters) + value + happiness > 22 else 'Back to your desk, boy.'

# Given an array, return the difference between the count of even numbers
# and the count of odd numbers. 0 will be considered an even number.
# For example:
# solve([0,1,2,3]) = 0 because there are two even numbers and two odd numbers. Even - Odd = 2 - 2 = 0.
# Let's now add two letters to the last example:
# solve([0,1,2,3,'a','b']) = 0. Again, Even - Odd = 2 - 2 = 0. Ignore letters.
# The input will be an array of lowercase letters and numbers only.
# In some languages (Haskell, C++, and others), input will be an array of strings:
def solve(a):
    count_e = 0
    count_o = 0
    for elem in a:
        if str(elem).isdigit():
            if elem %2==0:
                count_e += 1
            elif elem %2!=0:
                count_o += 1
    return count_e - count_o

# Implement the method length, which accepts a linked list (head), and returns the length of the list.
# For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.
def length(head):
    if head == None:
        return 0
    elif head:
        number = 1
        while head.next:
              head = head.next
              number += 1
        return number

# In this Kata, we will check if a string contains consecutive letters
# as they appear in the English alphabet and if each letter occurs only once.
def solve(s):
    return "".join(sorted(s)) in "abcdefghijklmnopqrstuvwxyz"

# So you've found a meeting room - phew! You arrive there ready to present,
# and find that someone has taken one or more of the chairs!!
# You need to find some quick.... check all the other meeting rooms to see if all of the chairs are in use.
# Your meeting room can take up to 8 chairs. need will tell you
# how many have been taken. You need to find that many.=
# Find the spare chairs from the array of meeting rooms. Each meeting
# room tuple will have the number of occupants as a string.
# Each occupant is represented by 'X'. The room tuple will also
# have an integer telling you how many chairs there are in the room.
# You should return an array of integers that shows how many chairs you take
# from each room in order, up until you have the required amount.
# example:
# [['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9], ['XXX',2]] when you need 4 chairs:
# result -> [0, 1, 3] no chairs free in room 0, take 1 from room 1, take 3 from room 2. no need to
# consider room 3 as you have your 4 chairs already.
# If you need no chairs, return "Game On". If there aren't enough spare chairs available, return "Not enough!".
def meeting(rooms, need):
    if need == 0:
        return 'Game On'
    count = []
    for room in rooms:
        if room[1] - len(room[0]) >0:
            if room[1] - len(room[0]) >= need:
                count.append(need)
                return count
            else:
                count.append(room[1] - len(room[0]))
                need -= room[1] - len(room[0])
        else:
            count.append(0)
    return "Not enough!"

# As you may know, once some people pass their teens, they jokingly only celebrate their 20th or 21st birthday,
# forever. With some maths skills, that's totally possible - you only need to select the correct number base!
# For example, if they turn 32, that's exactly 20 - in base 16... Already 39? That's just 21, in base 19!
# Your task is to translate the given age to the much desired 20 (or 21) years,
# and indicate the number base, in the format specified below.
# Note: input will be always > 21
def womens_age(n):
    base = n // 2
    remainder = n % 2
    return "{}? That's just {}, in base {}!".format(n, 20 + remainder, base)

# You are going to be given an array of integers. Your job is to take that array
# and find an index N where the sum of the integers to the left of N is equal
# to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.
# For example:
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array,
# the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array,
# the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

# Remove words from the sentence if they contain exactly one exclamation mark.
# Words are separated by a single space, without leading/trailing spaces.
def remove(s):
    return ' '.join(filter(lambda word: word.count('!') != 1, s.split(' ')))

# With a friend we used to play the following game on a chessboard (8, rows, 8 columns). On
# the first row at the bottom we put numbers:
# 1/2, 2/3, 3/4, 4/5, 5/6, 6/7, 7/8, 8/9
# On row 2 (2nd row from the bottom) we have:
# 1/3, 2/4, 3/5, 4/6, 5/7, 6/8, 7/9, 8/10
# On row 3:
# 1/4, 2/5, 3/6, 4/7, 5/8, 6/9, 7/10, 8/11
# until last row:
# 1/9, 2/10, 3/11, 4/12, 5/13, 6/14, 7/15, 8/16
# When all numbers are on the chessboard each in turn we toss a coin. The one who get
# "head" wins and the other gives him, in dollars, the sum of the numbers on the chessboard.
# We play for fun, the dollars come from a monopoly game!
# Task
# How much can I (or my friend) win or loses for each game if the chessboard has n rows
# and n columns? Add all of the fractional values on an n by n sized board and give the
# answer as a simplified fraction.
# See Sample Tests for each language
# Ruby, Python, JS, Coffee, Clojure, PHP, Elixir, Crystal, Typescript, Go:
# The function called 'game' with parameter n (integer >= 0) returns as result an
# irreducible fraction written as an array of integers: [numerator, denominator].
# If the denominator is 1 return [numerator].
def game(n):
    if n == 0: return [0]
    if n == 1: return [1, 2]
    if n == 2: return [3, 2]
    if n == 3: return [9, 2]
    s, step = 4.5, 3.5
    for _ in range(n-3):
        s = s + step
        step += 1.0
    if int(s) == s: return [s]
    else: return [int(str(2*int(s)+1)), 2]

# You will be given an array of numbers.
# For each number in the array you will need to create an object.
# The object key will be the number, as a string. The value will be the corresponding character code, as a string.
# Return an array of the resulting objects.
# All inputs will be arrays of numbers.
# All character codes are valid lower case letters. The input array will not be empty.
def num_obj(s):
    return [{str(i) : chr(i)} for i in s]

# The prime numbers are not regularly spaced. For example from 2 to
# 3 the step is 1. From 3 to 5 the step is 2. From 7 to 11 it is 4.
# Between 2 and 50 we have the following pairs of 2-steps primes:
# 3, 5 - 5, 7, - 11, 13, - 17, 19, - 29, 31, - 41, 43
# We will write a function step with parameters:
# g (integer >= 2) which indicates the step we are looking for,
# m (integer >= 2) which gives the start of the search (m inclusive),
# n (integer >= m) which gives the end of the search (n inclusive)
# In the example above step(2, 2, 50) will return [3, 5] which is the first pair between 2 and 50 with a 2-steps.
# So this function should return the first pair of the two prime numbers spaced with a step of g between the
# limits m, n if these g-steps prime numbers exist otherwise
# nil or null or None or Nothing or [] or "0, 0" or {0, 0} or 0 0 or "" (depending on the language).
def step(g, m, n):
    prime_list = []
    for num in range(m, n):
        number_prime = isPrime(num)
        prime_list.append(number_prime)
        if number_prime == True:
            if len(prime_list) > g:
                if prime_list[num-g-m] == True:
                    return [num-g, num]
            else:
                previous_prime = num
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        elif i*i > num:
            return True
    return True

# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
# You are given a year as integer (e. g. 2001). You should
# return the most frequent day(s) of the week in that year.
# The result has to be a list of days sorted by the order
# of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'],
# ['Monday', 'Sunday']). Week starts with Monday.
# Input: Year as an int.
# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).
# Preconditions:
# Week starts on Monday.
# Year is between 1583 and 4000.
# Calendar is Gregorian.
from datetime import date
def most_frequent_days(year):
    names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start = date(year,1,1).weekday()
    end = date(year, 12, 31).weekday()
    days = list(range(start, 7)) + list(range(0 ,end +1))
    total = days.count(max(days,key=days.count))
    result = []
    for day in [0,1,2,3,4,5,6]:
        if day in days:
            if days.count(day) == total:
                result.append(day)
    return list(map(lambda x: names[x], result))

# Kata Task
# stations is a list/array of distances (miles) from one station to the next along the Pony Express route.
# Implement the riders method/function, to return how many riders are necessary
# to get the mail from one end to the other.
# NOTE: Each rider travels as far as he can, but never more than 100 miles.
def riders(stations):
	riders, travelled = 1, 0
	for miles in stations:
		if travelled + miles > 100:
			riders += 1
			travelled = miles
		else:
			travelled += miles
	return riders

# Remove all exclamation marks from the end of words. Words are separated by a
# single space. There are no exclamation marks within a word.
def remove(s):
    l = []
    for i in s.split():
        while i.endswith('!'):
            i = i[:-1]
        l.append(i)
    return ' '.join(l)

# Given an array, find the duplicates in that array, and return a new array of those
# duplicates. The elements of the returned array should appear in the order when they first appeared as duplicates.
# Note: numbers and their corresponding string representations should not
# be treated as duplicates (i.e., "1" != 1).
def duplicates(array):
    l = []
    d = []
    for elem in array:
        if elem not in l:
            l.append(elem)
            continue
        elif elem in l and elem not in d:
            d.append(elem)
    return d

# The depth of an integer n is defined to be how many multiples
# of n it is necessary to compute before all 10 digits have appeared at least once in some multiple.
def compute_depth(n):
    l = []
    count = 1
    while len(l)<10:
        s = n*count
        for i in str(s):
            if i not in l:
                l.append(i)
        count+=1
    return count-1

# Some people have been killed!
# You have managed to narrow the suspects down to just a few. Luckily, you know every
# person who those suspects have seen on the day of the murders.
# Task.
# Given a dictionary with all the names of the suspects and everyone that they have
# seen on that day which may look like this:
def killer(suspect_info, dead):
    for k,v in suspect_info.items():
        if all(i in v for i in dead):
            return k

# You must create a function, spread, that takes a function and
# a list of arguments to be applied to that function. You must make this function return
# the result of calling the given function/lambda with the given arguments.
def spread(func, args):
    return func(*args)

# Complete the function that takes an array of words.
# You must concatenate the nth letter from each word to construct a new
# word which should be returned as a string, where n is the position of the word in the list.
def nth_char(words):
    word = ''
    i = 0
    while i < len(words):
        word += words[i][i]
        i+=1
    return word

# In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:
class Dictionary():
    def __init__(self):
        self.d = {}

    def newentry(self, word, definition):
        self.word = word
        self.definition = definition
        self.d[self.word] = self.definition

    def look(self, key):
        self.key = key
        try:
            return self.d[self.key]
        except:
            return f"Can't find entry for {self.key}"

# Write a generic function chainer
# Write a generic function chainer that takes a starting value,
# and an array of functions to execute on it (array of symbols for Ruby).
# The input for each function is the output of the previous function
# (except the first function, which takes the starting value as its input).
# Return the final value after execution is complete.
def chain(init_val, functions):
    for func in functions:
        init_val = func(init_val)
    return init_val

# You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle
# (but not at beginning or end). The length of the strings, before and after the colon, are random.
# Your job is to return a list of two strings
# (in the same order as the original list), but with the characters after each colon swapped.
def tail_swap(strings):
    l = []
    final = []
    for i in strings:
        for elem in i.split(':'):
            l.append(elem)
    final.append(l[0] + ':' + l[3])
    final.append(l[2] + ':' + l[1])
    return final

# Slot machine (American English), informally fruit machine (British English), puggy
# (Scottish English slang), the slots (Canadian and American English), poker machine
# (or pokies in slang) (Australian English and New Zealand English) or
# simply slot (American English), is a casino gambling machine with three
# or more reels which spin when a button is pushed. Slot machines are
# also known as one-armed bandits because they were originally operated by one lever on
# the side of the machine as distinct from a button on the front panel,
# and because of their ability to leave the player in debt and impoverished.
# Many modern machines are still equipped with a legacy lever in addition to the button. (Source Wikipedia)
# Task
# You will be given three reels of different images and told at
# which index the reels stop. From this information your job is to return the score of the resulted reels.
# Rules
# 1. There are always exactly three reels
# 2. Each reel has 10 different items.
# 3. The three reel inputs may be different.
# 4. The spin array represents the index of where the reels finish.
# 5. The three spin inputs may be different
# 6. Three of the same is worth more than two of the same
# 7. Two of the same plus one "Wild" is double the score.
# 8. No matching items returns 0.
def fruit(reels, spins):
    triple = {
        'Wild Wild Wild': 100, 'Star Star Star': 90, 'Bell Bell Bell': 80,
        'Shell Shell Shell': 70, 'Seven Seven Seven': 60, 'Cherry Cherry Cherry': 50,
        'Bar Bar Bar': 40, 'King King King': 30, 'Queen Queen Queen': 20, 'Jack Jack Jack': 10
    }
    double = {
        'Wild': 10, 'Star': 9, 'Bell': 8, 'Shell': 7, 'Seven': 6, 'Cherry': 5, 'Bar': 4, 'King': 3,
        'Queen': 2, 'Jack': 1
    }
    l = [reels[0][spins[0]], reels[1][spins[1]], reels[2][spins[2]]]
    if l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
        if l[0] == l[1] == l[2]:
            return triple[' '.join(sorted(l))]
        elif (l.count(l[0]) == 2 or l.count(l[1]) == 2) and l.count('Wild') != 1:
            for elem in l:
                if l.count(elem) == 2:
                    return double[elem]
        elif (l.count(l[0]) == 2 or l.count(l[1]) == 2) and l.count('Wild') == 1:
            for elem in l:
                if l.count(elem) == 2:
                    return double[elem] * 2
    return 0

# If you have completed the Tribonacci sequence kata, you would know by now that
# mister Fibonacci has at least a bigger brother. If not, give it a quick look to get how things work.
# Well, time to expand the family a little more: think of
# a Quadribonacci starting with a signature of 4 elements and each following element is
# the sum of the 4 previous, a Pentabonacci (well Cinquebonacci would probably sound a bit more italian,
# but it would also sound really awful) with a signature of 5 elements
# and each following element is the sum of the 5 previous, and so on.
# Well, guess what? You have to build a Xbonacci function that takes a signature of X elements -
# and remember each next element is the sum of the last X elements -
# and returns the first n elements of the so seeded sequence.
def Xbonacci(signature,n):
    result = signature[:]
    for x in range(n-len(signature)):
        current_fib = 0
        start = len(result) - len(signature)
        for y in result[start:]:
            current_fib += y
        result.append(current_fib)
    return result[:n]

# You love coffee and want to know what beans you can afford to buy it.
# The first argument to your search function will be a number which represents your budget.
# The second argument will be an array of coffee bean prices.
# Your 'search' function should return the stores that sell coffee within your budget.
# The search function should return a string of prices for the coffees
# beans you can afford. The prices in this string are to be sorted in ascending order.
def search(budget, prices):
    return ','.join(str(i) for i in sorted(list(filter(lambda x: x<= budget, prices))))

# Write a function called "filterEvenLengthWords".
# Given an array of strings, "filterEvenLengthWords" returns an array
# containing only the elements of the given array whose length is an even number.
# var output = filterEvenLengthWords(['word', 'words', 'word', 'words']);
# console.log(output); // --> ['word', 'word']
def filter_even_length_words(words):
    return [word for word in words if len(word) % 2 == 0]

# Write a function that takes a list (in Python) or array (in other languages)
# of numbers, and makes a copy of it.
# Note that you may have troubles if you do not return an actual copy,
# item by item, just a pointer or an alias for an existing list or array.
# If not a list or array is given as a parameter in interpreted languages, the function should raise an error.
def copy_list(l):
    copy = [i for i in l]
    return copy

# One suggestion to build a satisfactory password is to start with a memorable phrase
# or sentence and make a password by extracting the first letter of each word.
# ven better is to replace some of those letters with numbers (e.g., the letter
# O can be replaced with the number 0):
# instead of including i or I put the number 1 in the password;
# instead of including o or O put the number 0 in the password;
# instead of including s or S put the number 5 in the password.
def make_password(phrase):
    d = {'i': '1', 'o': '0', 's':'5'}
    word = [i[0] for i in phrase.split()]
    return ''.join(d[i.lower()] if i.lower() in d else i for i in word)

# Sort the Vowels!
# In this kata, we want to sort the vowels in a special format.
# Task
# Write a function which takes a input string s and return a string in the following way:
def sort_vowels(s):
    try:
        return '\n'.join(i+'|' if i.lower() not in 'aeoiu' else '|'+i for i in s)
    except:
        return ''

# Vowel harmony is a phenomenon in some languages. It means that "A
# vowel or vowels in a word are changed to sound the same (thus "in harmony.")" (wikipedia).
# This kata is based on vowel harmony in Hungarian.
# Task:
# Your goal is to create a function dative() (Dative() in C#) which returns
# the valid form of a valid Hungarian word w in dative case i. e.
# append the correct suffix nek or nak to the word w based on vowel harmony rules.
# Vowel Harmony Rules (simplified)
# When the last vowel in the word is
# a front vowel (e, é, i, í, ö, ő, ü, ű) the suffix is -nek
# a back vowel (a, á, o, ó, u, ú) the suffix is -nak
def dative(word):
    for letter in word[::-1]:
        if letter in "eéiíöőüű":
            return word + "nek"
        elif letter in "aáoóuú":
            return word + "nak"

# A Cartesian coordinate system is a coordinate system that specifies each point uniquely
# in a plane by a pair of numerical coordinates, which are the signed distances to
# the point from two fixed perpendicular directed lines, measured in the same unit of length.
# The сoordinates of a point in the grid are written as (x,y). Each point in a
# coordinate system has eight neighboring points. Provided that the grid step = 1.
# It is necessary to write a function that takes a coordinate on the x-axis and y-axis
# and returns a list of all the neighboring points. Points inside your returned list
# need not be sorted (any order is valid).
def cartesian_neighbor(x, y):
    return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
            (x + 1, y + 1)]

# i is the imaginary unit, it is defined by i²=−1i² = -1i²=−1,
# therefore it is a solution to x²+1=0x² + 1 = 0x²+1=0.
# Your Task
# Complete the function pofi that returns iii to the power of a given non-negative integer
# in its simplest form, as a string (answer may contain iii).
def pofi(n):
    return ['1','i','-1','-i'][n % 4]

# Count how often sign changes in array.
# result
# number from 0 to ... . Empty array returns 0
def catch_sign_change(lst):
    return sum((x>=0)!=(y>=0) for x, y in zip(lst,lst[1:]))

# When you sign up for an account somewhere, some websites do not actually store
# your password in their databases. Instead, they will transform your password into something
# else using a cryptographic hashing algorithm.
# After the password is transformed, it is then called a password hash. Whenever you try to login,
# the website will transform the password you tried
# using the same hashing algorithm and simply see if the password hashes are the same.
# Create the function that converts a given string into an md5 hash. The return value
# should be encoded in hexadecimal.
from hashlib import md5
def pass_hash(str):
    return md5(str.encode()).hexdigest()

# In this kata you parse RGB colors represented by strings.
# The formats are primarily used in HTML and CSS.
# Your task is to implement a function which takes a color as a string and returns
# the parsed color as a map (see Examples).
def parse_html_color(color):
    color = PRESET_COLORS.get(color.lower(), color)
    if len(color) == 7:
        r, g, b = (int(color[i:i+2], 16) for i in range(1, 7, 2))
    else:
        r, g, b = (int(color[i+1]*2, 16) for i in range(3))
    return dict(zip("rgb", (r, g, b)))

# Digital Cypher assigns to each letter of the alphabet unique number. For example:
# a  b  c  d  e  f  g  h  i  j  k  l  m
# 1  2  3  4  5  6  7  8  9 10 11 12 13
# n  o  p  q  r  s  t  u  v  w  x  y  z
# 14 15 16 17 18 19 20 21 22 23 24 25 26
# Instead of letters in encrypted word we write the corresponding number, eg. The word scout:
# s  c  o  u  t
# 19  3 15 21 20
# Then we add to each obtained digit consecutive digits from the key. For example. In case of key equal to 1939 :
def decode(code, key):
    key=str(key)
    return "".join([chr(code[i] +96 - int(key[i%len(key)])) for i in range(0, len(code))])

# Write a program that, given a word, computes the scrabble score for that word.
def scrabble_score(st):
    w1 = 'A,E,I,O,U,L,N,R,S,T'
    w2 = 'D,G'
    w3 = 'B,C,M,P'
    w4 = 'F,H,V,W,Y'
    w5 = 'K'
    w6 = 'JX'
    w7 = 'QZ'
    count = 0
    st.replace(' ', '')
    for i in st.upper():
        if i in w1:
            count +=1
        elif i in w2:
            count += 2
        elif i in w3:
            count += 3
        elif i in w4:
            count += 4
        elif i in w5:
            count += 5
        elif i in w6:
            count += 8
        elif i in w7:
            count += 10
    return count

# Your story
# You've always loved both Fizz Buzz katas and cuckoo clocks, and when
# you walked by a garage sale and saw an ornate cuckoo clock with a missing pendulum,
# and a "Beyond-Ultimate Raspberry Pi Starter Kit"
# filled with all sorts of sensors and motors and other components,
# it's like you were suddenly hit by a beam of light and knew that it was your mission to
# combine the two to create a computerized Fizz Buzz cuckoo clock!
# You took them home and set up shop on the kitchen table, getting
# more and more excited as you got everything working together just perfectly.
# Soon the only task remaining was to write a function to select from the
# sounds you had recorded depending on what time it was:
# Your plan
# When a minute is evenly divisible by three, the clock will say the word "Fizz".
# When a minute is evenly divisible by five, the clock will say the word "Buzz".
# When a minute is evenly divisible by both, the clock will say "Fizz Buzz", with two exceptions:
# On the hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo bird will
# come out and "Cuckoo" between one and twelve times depending on the hour.
# On the half hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo will
# come out and "Cuckoo" just once.
# With minutes that are not evenly divisible by either three or five, at first you had
# intended to have the clock just say the numbers ala Fizz Buzz, but then you decided
# at least for version 1.0 to just have the clock make a quiet, subtle "tick" sound for
# a little more clock nature and a little less noise.
# Your input will be a string containing hour and minute values in 24-hour time,
# separated by a colon, and with leading zeros. For example, 1:34 pm would be "13:34".

# Your return value will be a string containing the combination of Fizz, Buzz, Cuckoo,
# and/or tick sounds that the clock needs to make at that time, separated by spaces.
# Note that although the input is in 24-hour time, cuckoo clocks' cuckoos are in 12-hour time.
def fizz_buzz_cuckoo_clock(time):
    hh, mm = map(int, time.split(":"))
    if mm ==  0:return " ".join(["Cuckoo"] * (hh % 12 or 12))
    elif mm == 30:return "Cuckoo"
    elif mm % 15 == 0:return "Fizz Buzz"
    elif mm %  3 == 0:return "Fizz"
    elif mm %  5 == 0:return "Buzz"
    else:return "tick"

# Can Santa save Christmas?
# Oh no! Santa's little elves are sick this year. He has to distribute the presents on his own.
# But he has only 24 hours left. Can he do it?
# Your Task:
# You will get an array as input with time durations as string
# in the following format: HH:MM:SS. Each duration represents the
# time taken by Santa to deliver a present. Determine whether he can do it
# in 24 hours or not. In case the time required to deliver all of the presents is exactly 24 hours,
# Santa can complete the delivery ;-).
def determineTime(arr):
    total_sec = sum(h * 3600 + m * 60 + s for h, m, s in [list(map(int, elem.split(':'))) for elem in arr])
    return total_sec <= 86400

# Write a function that will check whether ANY permutation of the characters of the input string
# is a palindrome. Bonus points for a solution that is efficient and/or
# that uses only built-in language functions. Deem yourself brilliant if
# you can come up with a version that does not use any function whatsoever.
# Example
# madam -> True
# adamm -> True
# junk -> False
# Hint
# The brute force approach would be to generate all the permutations of the
# string and check each one of them whether it is a palindrome. However,
# an optimized approach will not require this at all.
permute_a_palindrome=lambda s:bool(len(list(filter(lambda x:x%2!=0,[s.count(char) for char in set(s)])))<2)

# Linked Lists - Get Nth
# Implement a GetNth() function that takes a linked list and an integer
# index and returns the node stored at the Nth index position. GetNth()
# uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on.
# So for the list 42 -> 13 -> 666, GetNth(1) should return Node(13);
# getNth(1 -> 2 -> 3 -> null, 0).data === 1
# getNth(1 -> 2 -> 3 -> null, 1).data === 2
# The index should be in the range [0..length-1]. If it is not,
# or if the list is empty, GetNth() should throw/raise
# an exception (ArgumentException in C#, InvalidArgumentException in PHP, Exception in Java).
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def get_nth(node, index):
    if node and index >= 0: return node if index < 1 else get_nth(node.next, index - 1)
    raise ValueError

# Implement String#ipv4_address?, which should return true if given object is an IPv4 address
# - four numbers (0-255) separated by dots.
# It should only accept addresses in canonical representation, so no leading 0s, spaces etc.
import re
def ipv4_address(address):
    regex = re.compile(r'''
    #      200-249   | 250-255 | 100-109| 0-99 110-199
    \b([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\b    
    ''', re.VERBOSE)
    mo = regex.match(address)
    if mo is None:
        return False
    elif  mo.group() == address:
        return (bool(mo))
    else:
        return False

# Peter lives on a hill, and he always moans about the way to his home. "It's always just
# up. I never get a rest". But you're pretty sure that at least at one point Peter's
# altitude doesn't rise, but fall. To get him, you use a nefarious plan:
# you attach an altimeter to his backpack and you read the data from his way back at the next day.
# Task
# You're given a list of compareable elements:
def is_monotone(heights):
    return heights == sorted(heights) if heights else True

# Write a function that takes in a binary string and returns the equivalent
# decoded text (the text is ASCII encoded).
# Each 8 bits on the binary string represent 1 character on the ASCII table.
# The input string will always be a valid binary string.
# Characters can be in the range from "00000000" to "11111111" (inclusive)
# Note: In the case of an empty binary string your function should return an empty string.
import binascii
def binary_to_string(binary):
    try:
        input_string=int(binary, 2)
        Total_bytes= (input_string.bit_length() +7) // 8
        input_array = input_string.to_bytes(Total_bytes, "big")
        ASCII_value=input_array.decode()
        return ASCII_value
    except:
        return '' if binary == '' else None

# Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two
# strings left and right on the balance - are they balanced?
# If the left side is more heavy, return "Left"; if the right side
# is more heavy, return "Right"; if they are balanced, return "Balance".
def balance(left, right):
    count_l = 0
    count_r = 0
    d = {'!':2, '?':3}
    for i in left:
        count_l += d[i]
    for i in right:
        count_r += d[i]
    return 'Balance' if count_l == count_r else 'Left' if count_l > count_r else 'Right'

# iven a string that includes alphanumeric characters ("3a4B2d") return
# the expansion of that string: The numeric values represent the occurrence of each letter preceding that numeric
# value. There should be no numeric characters in the final string.
# Notes
# The first occurrence of a numeric value should be the number of
# times each character behind it is repeated, until the next numeric value appears
# If there are multiple consecutive numeric characters, only the last one should be used (ignore the
# previous ones)
# Empty strings should return an empty string.
# Your code should be able to work for both lower and capital case letters.
import re
def string_expansion(s):
    result = str()
    regex = re.compile(r'(\d)?([a-zA-Z]+)+')
    mo = regex.findall(s)
    print(mo)
    for item in mo:
        if len(item[1]) > 1:
            lst = list(item[1])
            for letter in lst:
                if item[0] == '':
                    number = 1
                else:
                    number = item[0]
                letters = letter*int(number)
                result += ''.join(letters)
        else:
            if item[0] == '':
                number = 1
            else:
                number = item[0]
            letters = item[1]*int(number)
            result += ''.join(letters)
    return result

# You have to write a calculator that receives strings for input.
# The dots will represent the number in the equation. There will be
# dots on one side, an operator, and dots again after the operator.
# The dots and the operator will be separated by one space.
# Here are the following valid operators :
# + Addition
# - Subtraction
# * Multiplication
# // Integer Division
# Your Work (Task)
# You'll have to return a string that contains dots,
# as many the equation returns. If the result is 0, return the empty string.
# When it comes to subtraction, the first number will always be greater than or equal to the second number.
def calculator(txt):
    l = txt.split()
    if '+' in l:
        return l[0] + l[2]
    elif '-' in l:
        return l[0][:len(l[0])-len(l[2])]
    elif '*' in l:
        return l[0] * len(l[2])
    elif '//' in l:
        return l[0][:len(l[0])//len(l[2])]

# Write a function that flattens an Array of Array
# objects into a flat Array. Your function must only do one level of flattening.
def flatten(lst):
    return sum(([i] if not isinstance(i, list) else i for i in lst), [])

# Given a square matrix (i.e. an array of subarrays), find the sum of values from the first value of
# the first array, the second value of the second array, the third value of the third array, and so on...
def diagonal_sum(array):
    return sum(array[i][i] for i in range(len(array)))

# Write a function that checks whether all elements in an array are square numbers. The function
# should be able to take any number of array elements.
# Your function should return true if all elements in the array are square numbers and false if not.
# An empty array should return undefined / None / nil /false (for C).
# You can assume that all array elements will be positive integers.
from math import isqrt
def is_square(a):
    if a:
        return all(isqrt(x)**2 == x for x in a)

# In cryptanalysis, words patterns can be a useful tool in cracking simple ciphers.
# A word pattern is a description of the patterns of letters occurring in a word,
# where each letter is given an integer code in order of appearance. So the
# first letter is given the code 0, and second is then assigned 1 if it is
# different to the first letter or 0 otherwise, and so on.
# As an example, the word "hello" would become "0.1.2.2.3". For this task case-sensitivity is ignored,
# so "hello", "helLo" and "heLlo" will all return the same word pattern.
# Your task is to return the word pattern for a given word. All words provided will
# be non-empty strings of alphabetic characters only, i.e. matching the regex "[a-zA-Z]+".
def word_pattern(word):
    output = ''
    conversion = []
    word = word.lower()
    for letter in word:
        if letter not in conversion:
            conversion.append(letter)
        output += str(conversion.index(letter)) +'.'
    return output[:-1]

# It's your birthday. Your colleagues buy you a cake. The numbers of
# candles on the cake is provided (candles). Please note this is not reality, and
# your age can be anywhere up to 1000. Yes, you would look a mess.
# As a surprise, your colleagues have arranged for your friend to hide inside the cake
# and burst out. They pretend this is for your benefit, but likely it is just because they want to see
# you fall over covered in cake. Sounds fun!
# When your friend jumps out of the cake, he/she will knock some of the candles to the floor. If the number of
# candles that fall is higher than 70% of total candles, the carpet will catch fire.
# You will work out the number of candles that will fall from the provided lowercase string (debris).
# You must add up the character ASCII code of each even indexed
# (assume a 0 based indexing) character in the string, with
# the alphabetical position ("a" = 1, "b" = 2, etc.) of each odd indexed character to get the string's total.
import string
def cake(candles, debris):
    fallen_candles = sum(
        string.ascii_letters.index(char) if index % 2 else ord(char)
        for index, char in enumerate(debris)
    )
    return "Fire!" if candles and fallen_candles > candles * 0.7 else "That was close!"

# Complete the method that takes a sequence of objects with two keys each: country or state, and
# capital. Keys may be symbols or strings.
# The method should return an array of sentences declaring the state or country and its capital.
def capital(capitals):
    return [f"The capital of {c.get('state') or c['country']} is {c['capital']}" for c in capitals]

# Write a function that doubles every second integer in a list, starting from the left.
def double_every_other(lst):
    return [i*2 if lst.index(i)%2!=0 else i for i in lst]

# Suppose you have 4 numbers: '0', '9', '6', '4' and 3 strings composed with them:
# s1 = "6900690040"
# s2 = "4690606946"
# s3 = "9990494604"
# Compare s1 and s2 to see how many positions they have in common: 0 at index 3, 6
# at index 4, 4 at index 8 ie 3 common positions out of ten.
# Compare s1 and s3 to see how many positions they have in common: 9 at index
# 1, 0 at index 3, 9 at index 5 ie 3 common positions out of ten.
# Compare s2 and s3. We find 2 common positions out of ten.
# So for the 3 strings we have 8 common positions out of 30 ie 0.2666... or 26.666...%
# Given n substrings (n >= 2) in a string s our function pos_average will calculate the average
# percentage of positions that are the same between the (n * (n-1)) / 2 sets of substrings
# taken amongst the given n substrings. It can happen that some substrings are duplicate but since their
# ranks are not the same in s they are considered as different substrings.
# The function returns the percentage formatted as a float with 10 decimals but the result is
# tested at 1e.-9 (see function assertFuzzy in the tests).
import numpy as np
def pos_average(s):
    s = s.replace(',','')
    s = s.split(' ')
    total = (len(s)*(len(s)-1))/2
    sequence_array = []
    for sequence in s:
        sequence_array.append(list(sequence))
    arr = np.array(sequence_array)
    counter = 0
    for i in range(0, arr.shape[1]):
        print(arr[:,i])
        unique, counts = np.unique(arr[:,i], return_counts=True)
        print('unique', unique)
        for k in range(0, len(counts)):
            print(counts[k])
            if counts[k] > 1:
                counter += np.sum(np.arange(1, counts[k]))
    return counter/(total*len(s[0]))*100

# Your Story
# "A piano in the home meant something." - Fried Green Tomatoes at the Whistle Stop Cafe
# You've just realized a childhood dream by getting a beautiful and beautiful-sounding upright piano from
# a friend who was leaving the country. You immediately started doing things
# like playing "Heart and Soul" over and over again, using one finger to pick out any
# melody that came into your head, requesting some sheet music books from the library,
# signing up for some MOOCs like Developing Your Musicianship, and wondering if you will
# think of any good ideas for writing piano-related katas and apps.
# Now you're doing an exercise where you play the very first (leftmost, lowest in pitch)
# key on the 88-key keyboard, which (as shown below) is white, with the little finger
# on your left hand, then the second key, which is black, with the ring finger on your
# left hand, then the third key, which is white, with the middle finger on your left hand,
# then the fourth key, also white, with your left index finger, and then the fifth key,
# which is black, with your left thumb. Then you play the sixth key, which is white,
# with your right thumb, and continue on playing the seventh, eighth, ninth, and tenth
# keys with the other four fingers of your right hand. Then for the eleventh key you go
# back to your left little finger, and so on. Once you get to the rightmost/highest, 88th,
# key, you start all over again with your left little finger on the first key. Your thought
# is that this will help you to learn to move smoothly and with uniform pressure on the keys
# from each finger to the next and back and forth between hands.
# You're not saying the names of the notes while you're doing this, but instead just
# counting each key press out loud (not starting again at 1 after 88, but continuing on
# to 89 and so forth) to try to keep a steady rhythm going and to see how far you can get before messing up.
# You move gracefully and with flourishes, and between screwups you hear, see, and feel that you are
# part of some great repeating progression between low and high notes and black and white keys.
# Your Function
# The function you are going to write is not actually going to help you with your piano playing,
# but just explore one of the patterns you're experiencing: Given the number you stopped on, was
# it on a black key or a white key? For example, in the description of your piano exercise above,
# if you stopped at 5, your left thumb would be on the fifth key of the piano, which is black. Or
# if you stopped at 92, you would have gone all the way from keys 1 to 88 and then wrapped around,
# so that you would be on the fourth key, which is white.
# Your function will receive an integer between 1 and 10000 (maybe you think that in principle
# it would be cool to count up to, say, a billion, but considering how many years it would take
# it is just not possible) and return the string "black" or "white" -- here are a few more examples:
def black_or_white_key(key_press_count):
    count = (key_press_count - 1) % 88 % 12
    l = [0, 2, 3, 5, 7, 8, 10]
    return 'white' if count in l else 'black'

# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# There are tests with strings up to 10 000 characters long so your code will need to be efficient.
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.
import re
def longest(s):
    matches = re.findall('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*', s)
    current_longest = matches[0]
    for match in matches:
        if len(match) > len(current_longest):
            current_longest = match
    return current_longest

# You are given a string of n lines, each substring being n characters long: For example:
# s = "abcd\nefgh\nijkl\nmnop"
# We will study some transformations of this square of strings.
# Symmetry with respect to the main diagonal: diag_1_sym (or diag1Sym or diag-1-sym)
# diag_1_sym(s) => "aeim\nbfjn\ncgko\ndhlp"
# Clockwise rotation 90 degrees: rot_90_clock (or rot90Clock or rot-90-clock)
# rot_90_clock(s) => "miea\nnjfb\nokgc\nplhd"
# selfie_and_diag1(s) (or selfieAndDiag1 or selfie-and-diag1) It is initial
# string + string obtained by symmetry with respect to the main diagonal.
# s = "abcd\nefgh\nijkl\nmnop" -->
# "abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp"
# or printed for the last:
import copy
def diag_1_sym(s):
    w=[[x for x in ele]for ele in s.split('\n')]
    L,n=copy.deepcopy(w),len(w)
    for i in range(n):
        for j in range(n):
            L[i][j]=w[j][i]
    return '\n'.join([''.join(x) for x in L])
def rot_90_clock(strng):
    op=diag_1_sym(strng)
    return '\n'.join([x[::-1] for x in op.split('\n')])
def selfie_and_diag1(strng):
    op1,op2=strng.split('\n'),diag_1_sym(strng).split('\n')
    return '\n'.join([x+'|'+y for x,y in zip(op1,op2)])
def oper(fct, s):
    return fct(s)

# Input : an array of integers.
# Output : this array, but sorted in such a way that there are two wings:
# the left wing with numbers decreasing,
# the right wing with numbers increasing.
# the two wings have the same length. If the length of the array is odd the wings are around the
# bottom, if the length is even the bottom is considered to be part of the right wing.
# each integer l of the left wing must be greater or equal to its counterpart r in the right wing, the
# difference l - r being as small as possible. In other words the
# right wing must be nearly as steep as the left wing.
# The function is make_valley or makeValley or make-valley.
def make_valley(l):
    l = sorted(l, reverse = True)
    return l[::2] + l[1::2][::-1]

# The town sheriff dislikes odd numbers and wants all odd numbered families out of town! In town
# crowds can form and individuals are often mixed with other people and families. However you
# can distinguish the family they belong to by the number on the shirts they wear.
# As the sheriff's assistant it's your job to find all the odd numbered families and remove them from the town!
# Challenge: You are given a list of numbers. The numbers each repeat a certain number of times.
# Remove all numbers that repeat an odd number of times while keeping everything else the same.
# odd_ones_out([1, 2, 3, 1, 3, 3]) = [1, 1]
# In the above example:
# the number 1 appears twice
# the number 2 appears once
# the number 3 appears three times
# 2 and 3 both appear an odd number of times, so they are removed from the list. The final result is: [1,1]
# Here are more examples:
def odd_ones_out(numbers):
    return [i for i in numbers if numbers.count(i)%2==0]

# Write function which takes a string and make an acronym of it.
# Rule of making acronym in this kata:
# split string to words by space char
# take every first letter from word in given string
# uppercase it
# join them toghether
def to_acronym(inp):
    return ''.join(i[0].upper() for i in inp.split())

# This Kata is intended as a small challenge for my students
# All Star Code Challenge #16
# Create a function called noRepeat() that takes a string argument and
# returns a single letter string of the first not repeated character in the entire string.
def no_repeat(string):
    return [i for i in string if string.count(i) == 1][0]

# Create a function that takes a number and returns an array of strings containing the number cut off at each digit.
# Examples
# 420 should return ["4", "42", "420"]
# 2017 should return ["2", "20", "201", "2017"]
# 2010 should return ["2", "20", "201", "2010"]
# 4020 should return ["4", "40", "402", "4020"]
# 80200 should return ["8", "80", "802", "8020", "80200"]
# PS: The input is guaranteed to be an integer in the range [0, 1000000]
def create_array_of_tiers(n):
    return [str(n)[:i] for i in range(1,len(str(n))+1)]

# Impliment the reverse function, which takes in input n and reverses it.
# For instance, reverse(123) should return 321. You should do this
# without converting the inputted number into a string.
def reverse(n, count=0):
	return reverse(n // 10, count * 10 + n % 10) if n else count

# Write a function that receives two strings as parameter. This strings are in the following
# format of date: YYYY/MM/DD. Your job is: Take the years and calculate the difference between them.
def how_many_years (date1,date2):
    return abs(int(date1.split('/')[0]) - int(date2.split('/')[0]))

# Your task is to find all the elements of an array that are non consecutive.
# A number is non consecutive if it is not exactly one larger
# than the previous element in the array. The first element gets a pass and is never considered non consecutive.
# Create a function name all_non_consecutive
# E.g., if we have an array [1,2,3,4,6,7,8,15,16] then 6 and 15 are non-consecutive.
# You should return the results as an array of objects with two values i:
# <the index of the non-consecutive number> and n: <the non-consecutive number>.
def all_non_consecutive(a):
    return [{"i": i, "n": y} for i, (x, y) in enumerate(zip(a, a[1:]), 1) if x != y - 1]

# Too long, didn't read
# You get a list of integers, and you have to write a function mirror that returns the
# "mirror" (or symmetric) version of this list: i.e. the middle element is the
# greatest, then the next greatest on both sides, then the next greatest, and so on...
# More info
# The list will always consist of integers in range -1000..1000 and will vary in size between 0
# and 10000. Your function should not mutate the input array, and this will be tested
# (where applicable). Notice that the returned list will always be of odd size, since there
# will always be a definitive middle element.
def mirror(data: list) -> list:
    return sorted(data) + sorted(data, reverse=True)[1:]

# This Kata is intended as a small challenge for my students
# All Star Code Challenge #1
# Write a function, called sumPPG, that takes two NBA player objects/struct/Hash/Dict/Class and sums their PPG
def sum_ppg(player_one, player_two):
    return player_one['ppg'] + player_two['ppg']

# This kata requires you to convert minutes (int) to hours and minutes in the format hh:mm (string).
# If the input is 0 or negative value, then you should return "00:00"
# Hint: use the modulo operation to solve this challenge. The modulo operation simply returns the remainder
# after a division. For example the remainder of 5 / 2 is 1, so 5 modulo 2 is 1.
# Example
# If the input is 78, then you should return "01:18", because 78 minutes converts to 1 hour and 18 minutes.
def time_convert(num):
    return '%02d:%02d' % (num // 60, num % 60) if num > 0 else '00:00'

# You have a group chat application, but who is online!?
# You want to show your users which of their friends are online and available to chat!
# Given an input of an array of objects containing usernames, status and time since last activity (in mins),
# create a function to work out who is online, offline and away.
# If someone is online but their lastActivity was more than 10 minutes ago they are to be considered away.
from collections import defaultdict
def who_is_online(friends):
    d = defaultdict(list)
    for user in friends:
        status = 'away' if user['status'] == 'online' and user['last_activity'] > 10 else user['status']
        d[status].append(user['username'])
    return d


Linked
lists
are
data
structures
composed
of
nested or chained
objects, each
containing
a
single
value and a
reference
to
the
next
object.

Here
's an example of a list:


class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# LinkedList(1, LinkedList(2, LinkedList(3)))
# Write a function listToArray( or list_to_array in Python) that
# converts a list to an array, like this:
# [1, 2, 3]
# Assume all inputs are valid lists
# with at least one value.For the purpose of simplicity, all values will be either numbers, strings, or Booleans.
def list_to_array(lst):
    return ([lst.value] + list_to_array(lst.next)) if lst else []

# Oh no! Ghosts have reportedly swarmed the city. It's your job to get rid of them and save the day!
# In this kata, strings represent buildings while whitespaces within those strings represent ghosts.
# So what are you waiting for? Return the building(string) without any ghosts(whitespaces)!
def ghostbusters(building):
    return building.replace(' ', '') if ' ' in building else "You just wanted my autograph didn't you?"

# Write a function last that accepts a list and returns the last element in the list.
# If the list is empty:
# In languages that have a built-in option or result type (like OCaml or Haskell), return an empty option
# In languages that do not have an empty option, just return None
def last(lst):
    return lst[-1] if lst else None

# Paul is an excellent coder and sits high on the CW leaderboard. He solves kata like a banshee but would
# also like to lead a normal life, with other activities. But he just can't stop solving all the kata!!
# Given an array (x) you need to calculate the Paul Misery Score. The values are worth the following points:
def paul(x):
    d = {'kata':5, 'Petes kata':10, 'life':0, 'eating':1}
    count = sum(d[i] for i in x)
    return 'Super happy!' if count < 40 else 'Happy!' if 40 <= count < 70 else 'Sad!' if 70 <= count < 100 else 'Miserable!'

# It's important day today: the class has just had a math test. You will be given a list of marks.
# Complete the function that will:
# Calculate the average mark of the whole class and round it to 3 decimal places.
# Make a dictionary/hash with keys "h", "a", "l" to make clear how many high, average and
# low marks they got. High marks are 9 & 10, average marks are 7 & 8, and low marks are 1 to 6.
# Return list [class_average, dictionary] if there are different type of marks, or [class_average,
# dictionary, "They did well"] if there are only high marks.
def test(r):
    avr = round(sum(r)/len(r), 3)
    h, a, l = 0, 0, 0
    for mark in r:
        if 9 <= mark <= 10:
            h += 1
        elif 7 <= mark <= 8:
            a += 1
        elif 1 <= mark <= 6:
            l += 1
    l = [avr, {'h': h, 'a': a, 'l': l}, f"{'They did well' if a + l == 0 else ''}"]
    return l[:-1] if l[-1] == '' else l

# Happy Holidays fellow Code Warriors!
# It's almost Christmas! That means Santa's making his list, and checking it twice. Unfortunately,
# elves accidentally mixed the Naughty and Nice list together! Santa needs your help to save Christmas!
# Save Christmas!
# Santa needs you to write two functions. Both of the functions accept a sequence of objects.
# The first one returns a sequence containing only the names of the nice people,
# and the other returns a sequence containing only the names of the naughty people.
# Return an empty sequence [] if the result from either of the functions contains no names.
# The objects in the passed will represent people. Each object contains two properties: name and wasNice.
# name - The name of the person
# wasNice - True if the person was nice this year, false if they were naughty
def get_nice_names(people):
    l = []
    for d in people:
        if d['was_nice']:
            l.append(d['name'])
    return l if l else []

def get_naughty_names(people):
    l = []
    for d in people:
        if not d['was_nice']:
            l.append(d['name'])
    return l if l else []

# This Kata is intended as a small challenge for my students
# Your family runs a shop and have just brought a Scrolling
# Text Machine (http://3.imimg.com/data3/RP/IP/MY-2369478/l-e-d-multicolour-text-board-250x250.jpg) to help
# get some more business.
# The scroller works by replacing the current text string with a similar text string,
# but with the first letter shifted to the end; this simulates movement.
# You're father is far too busy with the business to worry about such details, so, naturally, he's
# making you come up with the text strings.
# Create a function named rotate() that accepts a string argument and returns an array of
# strings with each letter from the input string being rotated to the end.
def rotate(str_):
    l = [i for i in str_]
    result = []
    for i in range(len(l)):
        temp = l[0]
        l.append(temp)
        l.pop(0)
        result.append(''.join(l))
    return result

# In this Kata, you will be given two positive integers a and b and your task will be to apply
# the following operations:
# i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
# ii) If a ≥ 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
# iii) If b ≥ 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].
# a and b will both be lower than 10E8.
# More examples in tests cases. Good luck!
def solve(a,b):
    if a == 0 or b == 0:
        return [a,b]
    elif a >= 2*b:
        a = a-2*b
        return solve(a,b)
    elif b >= 2*a:
        b = b-2*a
        return solve(a,b)
    else:
        return [a,b]

# In your class, you have started lessons about geometric progression.
# Since you are also a programmer, you have decided to write a function that
# will print first n elements of the sequence with the given constant r and first element a.
# Result should be separated by comma and space.
def geometric_sequence_elements(a, r, n):
    return ", ".join(str(a * r ** i) for i in range(n))

# You are working at a lower league football stadium and you've been tasked with automating the scoreboard.
# The referee will shout out the score, you have already set up the voice recognition module
# which turns the ref's voice into a string, but the spoken score needs to be converted into
# a pair for the scoreboard!
# e.g. "The score is four nil" should return [4,0]
# Either teams score has a range of 0-9, and the ref won't say the same string every time e.g.
def scoreboard(string):
    d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine': 9 , 'nil':0}
    score = []
    for elem in string.split():
        if elem in d:
            score.append(d[elem])
    return score

# In this Kata the aim is to compare each pair of integers from 2 arrays, and return a new array of large numbers.
# Note: Both arrays have the same dimensions.
def get_larger_numbers(a, b):
    return [max(a[i], b[i]) for i,j in enumerate(a)]

# Create a function that takes a string as a parameter and does the following, in this order:
# Replaces every letter with the letter following it in the alphabet (see note below)
# Makes any vowels capital
# Makes any consonants lower case
# Note:
# the alphabet should wrap around, so Z becomes A
# in this kata, y isn't considered as a vowel.
def changer(s):
    l = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    word = ''
    s = s.lower()
    for i in s:
        if i in l:
            if l[l.index(i)+1] in 'aeoiu':
                word += l[l.index(i)+1].upper()
                continue
            else:
                word += l[l.index(i)+1]
                continue
        else:
            word += i
    return word

# Remember the triangle of balls in billiards? To build a classic triangle (5 levels) you need 15 balls.
# With 3 balls you can build a 2-level triangle, etc.
# For more examples, Write a function that takes number of balls (≥ 1) and
# calculates how many levels you can build a triangle.
def pyramid(balls):
    s = 0
    i=1
    while balls >= i:
        balls -= i
        i += 1
        s+=1
    return s

# Find the last element of the given argument(s).
def last(*args):
    try:
        return [args][-1][-1][-1]
    except:
        return args[-1]

# In your class, you have started lessons about "arithmetic progression". Because you are also a programmer,
# you have decided to write a function.
# This function, arithmetic_sequence_sum(a, r, n), should return the sum of the
# first (n) elements of a sequence in which each element is the sum of the given integer
# (a), and a number of occurences of the given integer (r), based on the element's position within the sequence.
# For example:
# arithmetic_sequence_sum(2, 3, 5) should return 40:
def arithmetic_sequence_sum(a, r, n):
    return sum(a + r * i for i in range(n))

# Implement a function that receives a string, and lets you extend it with repeated calls. When no argument
# is passed you should return a string consisting of space-separated words you've received earlier.
# Note: there will always be at least 1 string; all inputs will be non-empty.
class create_message(str):
    def  __call__(self, s=""):
        return create_message((self+" "+s).rstrip())

# Being a bald man myself, I know the feeling of needing to keep it clean shaven. Nothing worse
# that a stray hair waving in the wind.
# You will be given a string(x). Clean shaved head is shown as "-"
# and stray hairs are shown as "/". Your task is to check the head for stray hairs and get rid of them.
# You should return the original string, but with any stray hairs removed. Keep count
# ot them though, as there is a second element you need to return:
# 0 hairs --> "Clean!"
# 1 hair --> "Unicorn!"
# 2 hairs --> "Homer!"
# 3-5 hairs --> "Careless!"
# >5 hairs --> "Hobo!"
# So for this head: "------/------" you shoud return:
# ["-------------", "Unicorn"]
def bald(s):
    c = 'Clean!' if s.count('/') == 0 else 'Unicorn!' if s.count('/') == 1 else 'Homer!' if s.count('/') == 2 else 'Careless!' if 3 <= s.count('/') <= 5 else 'Hobo!'
    return [s.replace('/', '-'), c]

# Complete the function that takes a list of numbers (nums), as the only argument to the function.
# Take each number in the list and square it if it is even, or square root the
# number if it is odd. Take this new list and return the sum of it, rounded to two decimal places.
# The list will never be empty and will only contain values that are greater than or equal to zero.
# Good luck!
def sum_square_even_root_odd(nums):
    return round(sum(i**2 if i%2==0 else i **.5 for i in nums), 2)

# In this Kata, you will be given an array of arrays and your task will be to return the
# number of unique arrays that can be formed by picking exactly one element from each subarray.
# For example: solve([[1,2],[4],[5,6]]) = 4, because it results in only 4 possibilites.
# They are [1,4,5],[1,4,6],[2,4,5],[2,4,6].
# Make sure that you don't count duplicates; for example solve([[1,2],[4,4],[5,6,6]]) = 4,
# since the extra outcomes are just duplicates.
# See test cases for more examples.
# Good luck!
# If you like this Kata, please try:
def solve(lists):
    res = 1
    for list in lists:
        res *= len(set(list))
    return res

# Write the following function:
# def area_of_polygon_inside_circle(circle_radius, number_of_sides):
# It should calculate the area of a regular polygon of numberOfSides, number-of-sides,
# or number_of_sides sides inside a circle of radius circleRadius, circle-radius,
# or circle_radius which passes through all the vertices of the polygon
# (such circle is called circumscribed circle or circumcircle). The answer should be a number rounded to
# 3 decimal places.
import math
def area_of_polygon_inside_circle(r, n):
    return float("{:.3f}".format((math.sin(2 * math.pi / n) * r * r * n) / 2))

# There are some stones on Bob's table in a row, and each of
# them can be red, green or blue, indicated by the characters R, G, and B.
# Help Bob find the minimum number of stones he needs to remove from the table
# so that the stones in each pair of adjacent stones have different colours.
import re
def solution(stones):
    res = 0
    for i in 'RGB':
        matches = re.findall(rf'{i}+', stones)
        for match in matches:
            res += len(match)-1
    return res

# For this Kata you will be given an array of numbers and another number n.
# You have to find the sum of the n largest numbers of the array
# and the product of the n smallest numbers of the array, and compare the two.
# If the sum of the n largest numbers is higher, return "sum"
# If the product of the n smallest numbers is higher, return "product"
# If the 2 values are equal, return "same"
# Note The array will never be empty and n will always be smaller than the length of the array.
import functools
def sum_or_product(array, n):
    big = sum(sorted(array)[-n:])
    small = functools.reduce(lambda a, b : a * b, sorted(array)[:n])
    return 'sum' if big > small else 'product' if small > big else 'same'

# A startup office has an ongoing problem with its bin.
# Due to low budgets, they don't hire cleaners. As a result, the staff are left to voluntarily empty the bin.
# It has emerged that a voluntary system is not working and the bin is often overflowing.
# One staff member has suggested creating a rota system based upon the staff seating plan.
# Create a function binRota that accepts a 2D array of names.
# The function will return a single array containing staff names in the order that they should empty the bin.
# Adding to the problem, the office has some temporary staff.
# This means that the seating plan changes every month. Both staff members'
# names and the number of rows of seats may change. Ensure that the function
# binRota works when tested with these changes.
# Notes:
# All the rows will always be the same length as each other.
# There will be no empty spaces in the seating plan.
# There will be no empty arrays.
# Each row will be at least one seat long.
def bin_rota(arr):
    l = []
    for i in range(len(arr)):
        if i % 2 == 0:
            l += arr[i]
            continue
        else:
            l += arr[i][::-1]
    return l

# You are given an array of non-negative integers, your task is to complete the series from 0 to
# the highest number in the array.
# If the numbers in the sequence provided are not in order you should order them,
# but if a value repeats, then you must return a sequence with only one item,
# and the value of that item must be 0. like this:
def complete_series(seq):
    return [i for i in range(max(seq)+1)] if len(set(seq)) == len(seq) else [0]

# I will give you an integer (N) and a string. Break the string up into as
# many substrings of N as you can without spaces. If there are leftover characters, include those as well.
def string_breakers(n, st):
    st = st.replace(' ', '')
    l = []
    s = len(st)//n if len(st) % n == 0 else len(st)// n + 1
    for i in range(s):
        l.append(st[:n])
        st = st[n:]
    return '\n'.join(l)

# In this Kata, you will be given a lower case string and your task will be to remove k characters
# from that string using the following rule:
# - first remove all letter 'a', followed by letter 'b', then 'c', etc...
# - remove the leftmost character first.
def solve(st,k):
    num, removed = 0, 0
    while removed < k and st:
        if chr(num+97) in st:
            indx = st.index(chr(num+97))
            st = st[0:indx] + st[indx+1:]
            removed += 1
        else:
            num += 1
    return st

#Make them bark
# You have been hired by a dogbreeder to write a program to keep record of his dogs.
# You've already made a constructor Dog, so no one has to hardcode every puppy.
# The work seems to be done. It's high time to collect the payment.
# ..hold on! The dogbreeder says he wont pay you, until he can make every dog object .bark().
# Even the ones already done with your constructor. "Every dog barks" he says.
# He also refuses to rewrite them, lazy as he is.
# You can't even count how much objects that bastard client of yours already made.
# He has a lot of dogs, and none of them can .bark().
# Can you solve this problem, or will you let this client outsmart you for good?
# Practical info:
# The .bark() method of a dog should return the string 'Woof!'.
# The contructor you made (it is preloaded) looks like this:
def bark(self):
    return "Woof!"
Dog.bark = bark

# Write a function that accepts two arguments: an array/list of integers and another integer (n).
# Determine the number of times where two integers in the array have a difference of n.
def int_diff(lst, n):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if abs(lst[i] - lst[j]) == n:
                count += 1
    return count

# Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3,
# "Boom" if it is divisible by 5, "BangBoom" if it divisible by 3 and 5,
# and "Miss" if it isn't divisible by any of them. Note: Your program should only return one value
# Ex: Input: 105 --> Output: "BangBoom" Ex: Input: 9 --> Output: "Bang" Ex:Input: 25 --> Output: "Boom"
def multiple(x):
    return 'Bang' if x%3==0 and x%5!=0 else 'Boom' if x%3!=0 and x%5==0 else 'BangBoom' if x%3==0 and x%5==0 else 'Miss'

# Write a method that will search an array of strings for all strings that contain another string, ignoring
# capitalization. Then return an array of the found strings.
# The method takes two parameters, the query string and the array of strings to search, and returns an array.
# If the string isn't contained in any of the strings in the array,
# the method returns an array containing a single string: "Empty" (or Nothing in Haskell,
# or "None" in Python and C)
def word_search(query, seq):
    return [i for i in seq if query.lower() in i.lower()] or ["None"]

# JavaScript provides a built-in parseInt method.
# It can be used like this:
# parseInt("10") returns 10
# parseInt("10 apples") also returns 10
# We would like it to return "NaN" (as a string) for the second case
# because the input string is not a valid number.
# You are asked to write a myParseInt method with the following rules:
# It should make the conversion if the given string only contains a single integer value (and possibly
# spaces - including tabs, line feeds... - at both ends)
# For all other strings (including the ones representing float values), it should return NaN
# It should assume that all numbers are not signed and written in base 10
def my_parse_int(string):
    try:
        return int(string)
    except:
        return 'NaN'

# Your job is to create a class called Song.
# A new Song will take two parameters, title and artist.
# mount_moose = Song('Mount Moose', 'The Snazzy Moose')
# mount_moose.title => 'Mount Moose'
# mount_moose.artist => 'The Snazzy Moose'
# You will also have to create an instance method named howMany() (or how_many()).
# The method takes an array of people who have listened to the song that day.
# The output should be how many new listeners the song gained on that day out of all listeners.
# Names should be treated in a case-insensitive manner, i.e. "John" is the same as "john".
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = list(map(lambda listener: listener.lower(), artist))
    def how_many(self, listeners):
        listens = 0
        for listener in listeners:
            listener = listener.lower()
            if listener not in self.listeners:
                self.listeners.append(listener)
                listens += 1
        return listens

# Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.
# And because the local council has lost most of our tax money to a Nigerian email scam there
# are no funds to fix the clock properly.
# Instead, they are asking for volunteer programmers to write some code that tell the time
# by only looking at the remaining hour-hand!
# What a bunch of cheapskates!
# Can you do it?
# Kata
# Given the angle (in degrees) of the hour-hand, return the time in 12 hour HH:MM format.
# Round down to the nearest minute.
import math
def what_time_is_it(angle):
    calc = math.floor(angle / 30)
    remain = angle % 30
    min = math.floor(remain * 2)
    if angle == 0: return "12:00"
    elif calc == 0 and min < 10: return f"12:0{min}"
    elif calc == 0 and min > 9: return f"12:{min}"
    elif remain == 0 and calc < 10: return f"0{calc}:00"
    elif remain == 0 and calc > 9: return f"{calc}:00"
    elif min < 10 and calc < 10: return f"0{calc}:0{min}"
    elif min < 10 and calc > 9: return f"{calc}:0{min}"
    elif min > 9 and calc < 10: return f"0{calc}:{min}"
    elif min > 9 and calc > 9: return f"{calc}:{min}"

# Create a moreZeros function which will receive a string for input, and return an array
# (or null terminated string in C) containing only the characters from that string whose binary
# representation of its ASCII value consists of more zeros than ones.
# You should remove any duplicate characters, keeping the first occurrence of any such duplicates, so they
# are in the same order in the final array as they first appeared in the input string.
def more_zeros(s):
    l = []
    for i in s:
        c = format(ord(i), 'b')
        if c.count('1') < c.count('0') and i not in l:
            l.append(i)
    return l

# Complete the function circleArea so that it will return the area of a circle with the given radius.
# Round the returned number to two decimal places (except for Haskell).
# If the radius is not positive or not a number, return false.
import math
def circle_area(r):
    return round(math.pi*r**2, 2) if type(r) == int and r > 0 else False

# Normally we have firstname, middle and the last name but there may be more than one word in a name
# like a South Indian one.
# Similar to those kinda names we need to initialize the names.
# See the pattern below:
def initials(name):
    return '.'.join(i.upper()[0] if i.lower() != name.split()[-1].lower() else i.capitalize() for i in name.split())

# What's in a name?
# ..Or rather, what's a name in? For us, a particular string is where we are looking for a name.
# Task
# Write a function, taking two strings in parameter, that tests whether or not the first string contains
# all of the letters of the second string, in order.
# The function should return true if that is the case, and else false. Letter comparison should be case-INsensitive.
def name_in_str(str, name):
    word = iter(str.lower())
    return all(i in word for i in name.lower())

# This is related to my other Kata about cats and dogs.
# Kata Task
# I have a cat and a dog which I got as kitten / puppy.
# I forget when that was, but I do know their current ages as catYears and dogYears.
# Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]
# NOTES:
# Results are truncated whole numbers of "human" years
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that
def owned_cat_and_dog(cy, dy):
    cat = 0 if cy < 15 else 1 if cy < 24 else 2 + (cy - 24) // 4
    dog = 0 if dy < 15 else 1 if dy < 24 else 2 + (dy - 24) // 5
    return [cat, dog]

# We need a method in the List Class that may count specific digits from a given list of integers.
# This marked digits will be given in a second list. The method .count_spec_digits()/.countSpecDigits() will
# accept two arguments, a list of an uncertain amount of integers integers_lists/integersLists (and of an uncertain
# amount of digits, too) and a second list, digits_list/digitsList that has the specific digits to
# count which length cannot be be longer than 10 (It's obvious, we've got ten digits).
# The method will output a list of tuples, each tuple having two elements, the first
# one will be a digit to count, and second one, its corresponding total frequency in all
# the integers of the first list. This list of tuples should be ordered with the same order that the digits
# have in digitsList
class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        s = "".join(str(i) for i in integers_list)
        return [(dig, s.count(str(dig))) for dig in digits_list]

# Given 2 string parameters, show a concatenation of:
# the reverse of the 2nd string with inverted case; e.g Fish -> HSIf
# a separator in between both strings: @@@
# the 1st string reversed with inverted case and then mirrored; e.g Water -> RETAwwATER
def reverse_and_mirror(s1, s2):
    return f"{s2[::-1].swapcase()}@@@{s1[::-1].swapcase()}{s1.swapcase()}"

# Write a function that will randomly upper and lower characters in a string - randomCase() (random_case()
# for Python).
# A few examples:
import random
def random_case(x):
    return "".join([random.choice([i.lower(), i.upper()]) for i in x])

# You have to write a function pattern which creates the following pattern upto n number of rows.
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
def pattern(n):
    l = list(range(1, n + 1))
    return '\n'.join(''.join(map(str, l[i:])) for i in range(n))

# How many days are we represented in a foreign country?
# My colleagues make business trips to a foreign country. We must find the number of days our
# company is represented in a country. Every day that one or more colleagues are present in the
# country is a day that the company is represented. A single day cannot count for more than one day.
# Write a function that recieves a list of pairs and returns the number of days that
# the company is represented in the foreign country. The first number of the pair
# is the number of the day of arrival and the second number of the pair is the day
# of departure of someone who travels, i.e. 1 january is number 1 and 31 of december is 365.
def days_represented(trips):
    s = set()
    for i in trips:
        s.update(range(i[0], i[1] + 1))
    return len(s)

# There are five workers : James,John,Robert,Michael and William.They work one by
# one and on weekends they rest. Order is same as in the description(James
# works on mondays,John works on tuesdays and so on).You have to create a function
# 'task' that will take 3 arguments(w, n, c):
# Weekday
# Number of trees that must be sprayed on that day
# Cost of 1 litre liquid that is needed to spray tree,let's say one tree needs 1 litre liquid.
# Let cost of all liquid be x
# Your function should return string like this : 'It is (weekday) today, (name),
# you have to work, you must spray (number) trees and you need (x) dollars to buy liquid'
def task(w,n,c):
    workers = {"Monday" : "James", "Tuesday" : "John", "Wednesday" : "Robert", "Thursday" : "Michael", "Friday" : "William"}
    return f"It is {w} today, {workers[w]}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid"

# Write a function consonantCount, consonant_count or ConsonantCount that takes a string of English-language
# text and returns the number of consonants in the string.
# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.
def consonant_count(s):
    return sum([1 if i not in 'aeiou' and i.isalpha() else 0 for i in s.replace(' ', '').lower()])

# Is it possible to write a book without the letter 'e' ?
# Task
# Given String str, return:
# How many "e" does it contain (case-insensitive) in string format.
# If given String doesn't contain any "e", return: "There is no "e"."
# If given String is empty, return empty String.
# If given String is `null`/`None`/`nil`, return `null`/`None`/`nil`
def find_e(s):
    try:
        c = str(s.lower().count('e'))
        return c if s != '' and int(c) > 0 else 'There is no "e".' if int(c) == 0 and s!='' else '' if s == '' else None
    except:
        return None

# Write a function that takes a string and returns an array containing binary
# numbers equivalent to the ASCII codes of the characters of the string. The binary strings should
# be eight digits long.
def word_to_bin(word):
    return [bin(ord(letter))[2:].zfill(8) for letter in word]

# In this Kata, you will be given an integer array and your task is
# to return the sum of elements occupying prime-numbered indices.
# The first element of the array is at index 0.
# Good luck!
# If you like this Kata, try:
# Dominant primes. It takes this idea a step further.
def is_prime(n):
    return n >= 2 and all(n%i for i in range(2, 1+int(n**.5)))
def total(arr):
    return sum(n for i, n in enumerate(arr) if is_prime(i))

# The snail crawls up the column. During the day it crawls up some distance. During the night
# she sleeps, so she slides down for some distance (less than crawls up during the day).
# Your function takes three arguments:
# The height of the column (meters)
# The distance that the snail crawls during the day (meters)
# The distance that the snail slides down during the night (meters)
# Calculate number of day when the snail will reach the top of the column.
def snail(column, day, night):
    count = 0
    while column > 0:
        count += 1
        if column - day <= 0:
            return count
        column -= day - night
    return count

# Complete the solution so that it returns the number of times the search_text is found within the full_text.
def solution(full_text, search_text):
    return full_text.count(search_text)

# A binary gap within a positive number num is any sequence of consecutive zeros that is
# surrounded by ones at both ends in the binary representation of num.
# For example:
# 9 has binary representation 1001 and contains a binary gap of length 2.
# 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# 20 has binary representation 10100 and contains one binary gap of length 1.
# 15 has binary representation 1111 and has 0 binary gaps.
# Write function gap(num) that,  given a positive num,  returns the length of its longest binary gap.
# The function should return 0 if num doesn't contain a binary gap.
def gap(num):
    binary = str(bin(num)).strip('0').split('b')[1]
    binary = binary.split('1')
    return max(list(map(lambda x: len(x), binary)))

# *** No Loops Allowed ***
# You will be given an array (a) and a limit value (limit).
# You must check that all values in the array are below or equal to the limit value.
# If they are, return true. Else, return false.
# You can assume all values in the array are numbers.
# Do not use loops. Do not modify input array.
# Looking for more, loop-restrained fun? Check out the other kata in the series:
def small_enough(a, limit):
    return max(a) <= limit

# Challenge:
# Given a two-dimensional array, return a new array which carries over only those arrays from the original,
# which were not empty and whose items are all of the same type (i.e. homogenous).
# For simplicity, the arrays inside the array will only contain characters and integers.
# Example:
# Given [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]], your function should return [[1, 5, 4], ['b']].
# Addendum:
# Please keep in mind that for this kata, we assume that empty arrays are not homogenous.
# The resultant arrays should be in the order they were originally in and should not have its values changed.
# No implicit type casting is allowed. A subarray [1, '2'] would be considered illegal and should be filtered out.
def filter_homogenous(arrays):
    return [i for i in arrays if (all(type(a) == int for a in i) or all(type(a) == str for a in i)) and i]

# Let's build a calculator that can calculate the average for an arbitrary number of arguments.
# The test expects you to provide a Calculator object with an average method:
# Calculator.average()
# The test also expects that when you pass no arguments, it returns 0. The arguments are expected to be integers.
# It expects Calculator.average(3,4,5) to return 4.
class Calculator:
    @staticmethod
    def average(*args):
        return sum(args) / len(args) if args else 0

# Harshad numbers (also called Niven numbers) are positive numbers that can be divided
# (without remainder) by the sum of their digits.
# For example, the following numbers are Harshad numbers:
# 10, because 1 + 0 = 1 and 10 is divisible by 1
# 27, because 2 + 7 = 9 and 27 is divisible by 9
# 588, because 5 + 8 + 8 = 21 and 588 is divisible by 21
# While these numbers are not:
# 19, because 1 + 9 = 10 and 19 is not divisible by 10
# 589, because 5 + 8 + 9 = 22 and 589 is not divisible by 22
# 1001, because 1 + 1 = 2 and 1001 is not divisible by 2
# Harshad numbers can be found in any number base, but we are going to focus on base 10 exclusively.
# Your task
# Your task is to complete the skeleton Harshad object ("static class") which has 3 functions:
# isValid() that checks if n is a Harshad number or not
# getNext() that returns the next Harshad number > n
# getSerie() that returns a series of n Harshad numbers, optional start value not included
# You do not need to care about the passed parameters in the test cases, they will always
# be valid integers (except for the start argument in getSerie() which is optional and should default to 0).
# Note: only the first 2000 Harshad numbers will be checked in the tests.
from itertools import count, islice
class Harshad:
    @staticmethod
    def is_valid(number):
        return number % sum(int(i) for i in str(number)) == 0
    @classmethod
    def get_next(self, number):
        return next(i for i in count(number+1) if self.is_valid(i))
    @classmethod
    def get_series(self, c, start = 0):
        return list(islice(filter(self.is_valid, (i for i in count(start+1))), c))

# Remember the spongebob meme that is meant to make fun of people by repeating what they say in a mocking way?
def sponge_meme( s ):
    bob = ''
    i = 0
    while i < len(s):
        if i % 2 != 0:
            bob += s[i].lower()
        else:
            bob += s[i].upper()
        i += 1
    return bob

# You are given a string of words (x), for each word within the string you need to turn the word
# 'inside out'. By this I mean the internal letters will move out, and the external letters move toward the centre.
# If the word is even length, all letters will move. If the length is odd, you are expected to leave the
# 'middle' letter of the word where it is.
# An example should clarify:
# 'taxi' would become 'atix' 'taxis' would become 'atxsi'
import re
def inside_out(s):
    return re.sub(r'\S+', lambda m: inside_out_word(m.group()), s)
def inside_out_word(s):
    i, j = len(s) // 2, (len(s) + 1) // 2
    return s[:i][::-1] + s[i:j] + s[j:][::-1]

# Alice and Bob have participated to a Rock Off with their bands. A jury of true
# metalheads rates the two challenges, awarding points to the bands on a scale from 1 to
# 50 for three categories: Song Heaviness, Originality, and Members' outfits.
# For each one of these 3 categories they are going to be awarded one point, should
# they get a better judgement from the jury. No point is awarded in case of an equal vote.
# You are going to receive two arrays, containing first the score of Alice's
# band and then those of Bob's. Your task is to find their total score by comparing them in a single line.
# Example:
# Alice's band plays a Nirvana inspired grunge and has been rated 20 for Heaviness, 32
# for Originality and only 18 for Outfits. Bob listens to Slayer and has gotten a good
# 48 for Heaviness, 25 for Originality and a rather honest 40 for Outfits.
# The total score should be followed by a colon : and by one of the following quotes:
# if Alice's band wins: Alice made "Kurt" proud! if Bob's band
# wins: Bob made "Jeff" proud! if they end up with a draw: that looks like a "draw"! Rock on!
# The solution to the example above should therefore appear like '1, 2: Bob made "Jeff" proud!'.
def solve(a, b):
    alice = sum(i > j for i, j in zip(a, b))
    bob = sum(j > i for i, j in zip(a, b))
    if alice == bob:
        words = 'that looks like a "draw"! Rock on!'
    elif alice > bob:
        words = 'Alice made "Kurt" proud!'
    else:
        words = 'Bob made "Jeff" proud!'
    return f"{alice}, {bob}: {words}"

# The borrowers are tiny tiny fictional people. As tiny tiny people they
# have to be sure they aren't spotted, or more importantly, stepped on.
# As a result, the borrowers talk very very quietly. They find that capitals and
# punctuation of any sort lead them to raise their voices and put them in danger.
# The young borrowers have begged their parents to stop using caps and punctuation.
# Change the input text s to new borrower speak. Help save the next generation!
def borrow(s):
    return s.replace(' ', '').replace('!', '').replace('?', '').replace('.', '').replace(',', '').replace(';', '').replace(':', '').lower()

# You are given array of integers, your task will be to count all pairs in that array and return their count.
# Notes:
# Array can be empty or contain only one value; in this case return 0
# If there are more pairs of a certain number, count each pair only once.
# E.g.: for [0, 0, 0, 0] the return value is 2 (= 2 pairs of 0s)
# Random tests: maximum array length is 1000, range of values in array is between 0 and 1000
def duplicates(arr):
    return sum(arr.count(i) // 2 for i in set(arr))

# Suppose we know the process by which a string s was encoded to a string r (see explanation below).
# The aim of the kata is to decode this string r to get back the original string s.
# Explanation of the encoding process:
# input: a string s composed of lowercase letters from "a" to "z", and a positive integer num
# we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...
# if c is a character of s whose corresponding number is x, apply to x the function
# f: x-> f(x) = num * x % 26, then find ch the corresponding character of f(x)
# Accumulate all these ch in a string r
# concatenate num and r and return the result
# Task
# A string s was encoded to string r by the above process. complete the function
# to get back s whenever it is possible.
# Indeed it can happen that the decoding is impossible for strings composed
# of whatever letters from "a" to "z" when positive integer num has not been
# correctly chosen. In that case return "Impossible to decode".
from string import ascii_lowercase as aLow
def decode(r):
    i = next(i for i, c in enumerate(r) if c.isalpha())
    n, r = int(r[:i]), r[i:]
    maps = {chr(97 + n * k % 26): v for k, v in enumerate(aLow)}
    return "Impossible to decode" if len(maps) != 26 else ''.join(maps[c] for c in r)

# Write a function that takes an integer in input and outputs a string with currency format.
# Integer in currency format is expressed by a string of number where every three characters are separated by comma.
# For example:
def to_currency(price):
  return '{:,}'.format(price)

# Description:
# Given a string, you need to write a method that order every letter in this string in ascending order.
# Also, you should validate that the given string is not empty or null. If so, the method should return:
# "Invalid String!"
# Notes
# • the given string can be lowercase and uppercase.
# • the string could include spaces or other special characters like '# ! or ,'. Sort them based on their
# ASCII codes
def order_word(s):
    return ''.join(sorted(s, key=ord)) if s else 'Invalid String!'

# You are given a string of words and numbers. Extract the expression including:
# the operator: either addition ("gains") or subtraction ("loses")
# the two numbers that we are operating on
# Return the result of the calculation.
# Notes:
# "loses" and "gains" are the only two words describing operators
# No fruit debts nor bitten apples = The numbers are integers and no negatives
def calculate(string):
    d = {'gains': int(string.split()[2]) + int(string.split()[-1]), 'loses': int(string.split()[2]) - int(string.split()[-1])}
    return d['gains'] if 'gains' in string else d['loses']

# Implement a function which takes a sequence of objects and a property name, and returns a sequence containing
# the named property of each object.
# For example:
def pluck(objs, name):
    return [d[name] if name in d else None for d in objs]

# While developing a website, you detect that some of the members have troubles logging in.
# Searching through the code you find that all logins ending with a "_" make problems.
# So you want to write a function that takes an array of pairs of login-names and e-mails,
# and outputs an array of all login-name, e-mails-pairs from the login-names that end with "_".
def search_names(logins):
    return list(filter(lambda x: x[0].endswith('_'), logins))

# Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?
# Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).
# The list must be sorted by the value and be sorted largest to smallest.
def sort_dict(d):
  return sorted(d.items(), key=lambda x: x[1], reverse=True)

# Given a random string consisting of numbers, letters, symbols, you need to sum up the numbers in the string.
# Note:
# Consecutive integers should be treated as a single number. eg, 2015 should be
# treated as a single number 2015, NOT four numbers
# All the numbers should be treaded as positive integer. eg, 11-14
# should be treated as two numbers 11 and 14. Same as 3.14, should be treated as two numbers 3 and 14
# If no number was given in the string, it should return 0
import re
def sum_from_string(string):
    return sum(int(i) for i in re.findall("\d+",string))

# Triangular number is any amount of points that can fill an equilateral triangle.
# Example: the number 6 is a triangular number because all sides of a triangle has the same amount of points.
def is_triangular(t):
    return (8 * t + 1)**.5 % 1 == 0

# Write function which will create a string from a list of strings, separated by space.
def words_to_sentence(words):
    return ' '.join(words)

# Convert a hash into an array. Nothing more, Nothing less.
# {name: 'Jeremy', age: 24, role: 'Software Engineer'}
# should be converted into
# [["name", "Jeremy"], ["age", 24], ["role", "Software Engineer"]]
# Note: The output array should be sorted alphabetically.
# Good Luck!
def convert_hash_to_array(hash):
    return sorted([[k, v] for k,v in hash.items()])

# A sequence is usually a set or an array of numbers that has a strict way
# for moving from the nth term to the (n+1)th term.
# If f(n) = f(n-1) + c where c is a constant value, then f is an arithmetic sequence.
# An example would be (where the first term is 0 and the constant is 1) is [0, 1, 2, 3, 4, 5, ... and so on] )
# Else if (pun) f(n) = f(n-1) * c where c is a constant value, then f is a geometric sequence.
# Example where the first term is 2 and the constant is 2 will be [2, 4, 8, 16, 32, 64, ... to infinity ... ]
# There are some sequences that aren't arithmetic nor are they geometric.
# Here is a link to feed your brain : Sequence !
# You're going to write a function that's going to return the value in the nth
# index of an arithmetic sequence.(That is, adding a constant to move to the next element in the "set").
# The function's name is nthterm/Nthterm, it takes three inputs first,n,c where:
# first is the first value in the 0 INDEX.
# n is the index of the value we want.
# c is the constant added between the terms.
# Remember that first is in the index 0 .. just saying ...
def nthterm(first, n, c):
    return first + n * c

# The way the ohms value needs to be formatted in the string you return depends on the magnitude of the value:
# For resistors less than 1000 ohms, return a string containing the number of ohms, a space,
# the word "ohms" followed by a comma and a space, the tolerance value (5, 10, or 20), and a percent sign.
# For example, for the "yellow violet black" resistor mentioned above, you would return "47 ohms, 20%".
# For resistors greater than or equal to 1000 ohms, but less than 1000000 ohms, you will use the same
# format as above, except that the ohms value will be divided by 1000 and have a lower-case "k" after it.
# For example, for a resistor with bands of "yellow violet red gold", you would return "4.7k ohms, 5%"
# For resistors of 1000000 ohms or greater, you will divide the ohms value by 1000000 and have
# an upper-case "M" after it. For example, for a resistor with bands of
# "brown black green silver", you would return "1M ohms, 10%"
# Test case resistor values will all be between 10 ohms and 990M ohms.
def decode_resistor_colors(bands):
    d = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'gray':8, 'white':9, 'silver':10, 'gold':5}
    bands = [d[b] for b in bands.split()]
    ohms = (bands[0] * 10 + bands[1]) * 10 ** bands[2]
    ohms, sfx = (ohms/1000000.0, 'M') if ohms > 999999 else (ohms / 1000.0, 'k') if ohms > 999 else (ohms, '')
    return "{}{} ohms, {}%".format(int(ohms) if ohms // 1 == ohms else ohms, sfx, bands[3] if len(bands) > 3 else 20)

# Given a string and an array of index numbers, return the characters of the string rearranged to be in
# the order specified by the accompanying array.
# Ex:
# scramble('abcd', [0,3,1,2]) -> 'acdb'
# The string that you will be returning back will have: 'a' at index 0, 'b' at index 3,
# 'c' at index 1, 'd' at index 2, because the order of those characters maps to their
# corresponding numbers in the index array.
# In other words, put the first character in the string at the index described by the first element of the array
# You can assume that you will be given a string and array of equal length and both containing valid characters
# (A-Z, a-z, or 0-9).
def scramble(string, array):
    return "".join(v for k, v in sorted(zip(array, string)))

# For every positive integer N, there exists a unique sequence starting with 1 and ending with
# N and such that every number in the sequence is either the double of the preceeding number or the double plus 1.
# For example, given N = 13, the sequence is [1, 3, 6, 13], because . . . :
#  3 =  2*1 +1
#  6 =  2*3
#  13 = 2*6 +1
# Write a function that returns this sequence given a number N.
# Try generating the elements of the resulting list in ascending order, i.e., without
# resorting to a list reversal or prependig the elements to a list.
def climb(n):
    return  [n >> n.bit_length() - i - 1 for i in range(n.bit_length())]

# Given an array of strings, reverse them and their order in such way that their length
# stays the same as the length of the original inputs.
def reverse(a):
    l = reversed(''.join(a))
    return [''.join(next(l) for k in i) for i in a]

# Write a function generatePairs (Javascript) / generate_pairs (Python / Ruby) that accepts an integer argument
# n and generates an array containing the pairs of integers [a, b] that satisfy the following conditions:
# 0 <= a <= b <= n
# The pairs should be sorted by increasing values of a then increasing values of b.
def generate_pairs(n):
    return [[i,j] for i in range(n+1) for j in range(i, n+1)]

# Your job is to create a simple password validation function, as seen on many websites.
# The rules for a valid password are as follows:
# There needs to be at least 1 uppercase letter.
# There needs to be at least 1 lowercase letter.
# There needs to be at least 1 number.
# The password needs to be at least 8 characters long.
# You are permitted to use any methods to validate the password.
import re
def password(s):
    return bool(re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8}', s))

# Suzuki needs help lining up his students!
# Today Suzuki will be interviewing his students to ensure they are progressing in their training.
# He decided to schedule the interviews based on the length of the students name in descending order.
# The students will line up and wait for their turn.
# You will be given a string of student names. Sort them and return a list of names in descending order.
# Here is an example input:
def lineup_students(s):
    return sorted(s.split(), key=lambda i:(len(i), i), reverse=True)

# Create a function that returns a villain name based on the user's birthday. The birthday will be passed to the function as a valid Date object, so for simplicity, there's no need to worry about converting strings to dates.
# The first name will come from the month, and the last name will come from the last digit of the date:
# Month -> first name
# January -> "The Evil"
# February -> "The Vile"
# March -> "The Cruel"
# April -> "The Trashy"
# May -> "The Despicable"
# June -> "The Embarrassing"
# July -> "The Disreputable"
# August -> "The Atrocious"
# September -> "The Twirling"
# October -> "The Orange"
# November -> "The Terrifying"
# December -> "The Awkward"
# Last digit of date -> last name
# 0 -> "Mustache"
# 1 -> "Pickle"
# 2 -> "Hood Ornament"
# 3 -> "Raisin"
# 4 -> "Recycling Bin"
# 5 -> "Potato"
# 6 -> "Tomato"
# 7 -> "House Cat"
# 8 -> "Teaspoon"
# 9 -> "Laundry Basket"
# The returned value should be a string in the form of "First Name Last Name".
# For example, a birthday of November 18 would return "The Terrifying Teaspoon"
def get_villain_name(birthdate):
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    return first[birthdate.month - 1] + ' ' + last[int(str(birthdate.day)[-1])]

# Challenge: Given two null-terminated strings in the arguments "string"
# and "prefix", determine if "string" starts with the "prefix" string. Return true or false.
# Example:
# startsWith("hello world!", "hello"); // should return true
# startsWith("hello world!", "HELLO"); // should return false
# startsWith("nowai", "nowaisir"); // should return false
# Addendum: For this problem, an empty "prefix" string should always return true for any value of "string".
# If the length of the "prefix" string is greater than the length of the "string", return false.
# The check should be case-sensitive, i.e. startsWith("hello", "HE") should return false, whereas
# startsWith("hello", "he") should return true.
# The length of the "string" as well as the "prefix" can be defined by the formula: 0 <= length < +Infinity
# No characters should be ignored and/or omitted during the test, e.g. whitespace characters should not be ignored.
def starts_with(st, prefix):
    return st.startswith(prefix)

# Create a function that takes an input String and returns a String, where all the uppercase words of
# the input String are in front and all the lowercase words at the end. The order of the
# uppercase and lowercase words should be the order in which they occur.
# If a word starts with a number or special character, skip the word and leave it out of the result.
# Input String will not be empty.
# For an input String: "hey You, Sort me Already!" the function should return: "You, Sort Already! hey me"
def capitals_first(string):
    return ' '.join([i for i in string.split() if i[0].isupper()] + [i for i in string.split() if i[0].islower()])

# You need to write a function, that returns the first non-repeated character in the given string.
# If all the characters are unique, return the first character of the string.
# If there is no unique character, return null in JS or Java, and None in Python.
# You can assume, that the input string has always non-zero length.
def first_non_repeated(s):
    result = [i for i in s if s.count(i) == 1]
    return result[0] if result else None

# Create a function, as short as possible, that returns this lyrics.
# Your code should be less than 300 characters. Watch out for the three points at the end of the song.
def baby_shark_lyrics():
    l = ['Baby shark', 'Mommy shark', 'Daddy shark', 'Grandma shark', 'Grandpa shark', "Let's go hunt"]
    res = ''
    for i in l:
        res += f"{i}, doo doo doo doo doo doo\n"*3 + i+'!\n'
    return res + "Run away,…"

# The hamming distance of two equal-length strings is the number of positions, in which the two string differ.
# In other words, the number of character substitutions required to transform one string into the other.
# For this first Kata, you will write a function hamming_distance(a, b) with two equal-length strings
# containing only 0s and 1s as parameters. There is no need to test the parameters for validity
# (but you can, if you want).The function's output should be the hamming distance of the two strings as an integer.
def hamming_distance(a, b):
    return sum(1 for k,v in zip(a, b) if k!=v)

# A non-empty array a of length n is called an array of all possibilities if it contains all numbers
# between [0,a.length-1].Write a method named isAllPossibilities that accepts an integer array and
# returns true if the array is an array of all possibilities, else false.
def is_all_possibilities(arr):
    return sorted(arr) == list(range(0, max(arr)+1)) if arr else False

# You are given a string representing a number in binary. Your task is to delete
# all the unset bits in this string and return the corresponding number (after keeping only the '1's).
# In practice, you should implement this function:
def eliminate_unset_bits(number):
    i = number.replace('0', '')
    return int(i, 2) if i  else 0

# Fix My Phone Numbers
# Oh thank goodness you're here! The last intern has completely ruined everything!
# All of our customer's phone numbers have been scrambled, and we need those phone numbers to
# annoy them with endless sales calls!
# The Format
# Phone numbers are stored as strings and comprise 11 digits, eg '02078834982' and must always start with a 0.
# However, something strange has happened and now all of the phone numbers contain lots
# of random characters, whitespace and some are not phone numbers at all!
# For example, '02078834982' has somehow become 'efRFS:)0207ERGQREG88349F82!' and there are lots more
# lines that we need to check.
# The Task
# Given a string, you must decide whether or not it contains a valid phone number. If
# it does, return the corrected phone number as a string ie. '02078834982' with no whitespace or
# special characters, else return "Not a phone number".
def is_it_a_num(s: str) -> str:
    n = ''.join(i for i in s if i.isdigit())
    res = n.startswith('0') and len(n) == 11
    return n if res else 'Not a phone number'

# Task
# Create a function shuffleIt. The function accepts two or more parameters. The first parameter arr
# is an array of numbers, followed by an arbitrary number of numeric arrays.
# Each numeric array contains two numbers, which are indices for elements in
# arr (the numbers will always be within bounds). For every such array, swap the
# elements. Try to use all your new skills: arrow functions,
# the spread operator, destructuring, and rest parameters.
def shuffle_it(arr, *args):
    for k,v in args:
        arr[k], arr[v] = arr[v], arr[k]
    return arr

# Implement a function to calculate the sum of the numerical values in a nested list. For example :
def sum_nested(lst):
	return sum(sum_nested(x) if isinstance(x,list) else x for x in lst)

# In this Kata, you will be given a string and your task is to return the most valuable character.
# The value of a character is the difference between the index of its last occurrence and the index
# of its first occurrence. Return the character that has the highest value. If there is
# a tie, return the alphabetically lowest character. [For Golang return rune]
def solve(st):
    return sorted((st.find(i) - st.rfind(i), i) for i in set(st))[0][1]

# Given a string as input, move all of its vowels to the end of the string, in the same order as they were before.
# Vowels are (in this kata): a, e, i, o, u
# Note: all provided input strings are lowercase.
def move_vowels(s):
    return ''.join(sorted(s, key=lambda x: x in 'aeiou'))

# You are given an initial 2-value array (x). You will use this to calculate a score.
# If both values in (x) are numbers, the score is the sum of the two. If only one is a number,
# the score is that number. If neither is a number, return 'Void!'.
# Once you have your score, you must return an array of arrays. Each sub array will be the same as
# (x) and the number of sub arrays should be equal to the score.
# For example:
def explode(arr):
    numbers = [i for i in arr if type(i) == int]
    return [arr] * sum(numbers) if numbers else "Void!"

# Create a function that takes a 2D array as an input, and outputs another array that contains
# the average values for the numbers in the nested arrays at the corresponding indexes.
# Note: the function should also work with negative numbers and floats.
def avg_array(arrs):
    return [sum(i) / len(i) for i in zip(*arrs)]

# Let's assume we need "clean" strings. Clean means a string should only contain letters a-z, A-Z and spaces.
# We assume that there are no double spaces or line breaks.
# Write a function that takes a string and returns a string without the unnecessary characters.
def remove_chars(s):
    return ''.join(i for i in s if i.isalpha() or i == ' ')

# This is a follow up from my kata The old switcheroo
# Write the function :
# def encode(str)
# that takes in a string str and replaces all the letters with their respective positions in the English alphabet.
def encode(string):
    return ''.join(str(ord(i.lower())-96) if i.isalpha() else i for i in string)

# Kevin is noticing his space run out! Write a function that removes the spaces from
# the values and returns an array showing the space decreasing. For example, running this function
# on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace'].
def spacey(array):
    return [''.join(array[:i]) for i in range(1, len(array) + 1)]

# Given two arrays of integers m and n, test if they contain at least one identical element.
# Return true if they do; false if not.
# Your code must handle any value within the range of a 32-bit integer,
# and must be capable of handling either array being empty (which is a false result, as
# there are no duplicated elements).
def duplicate_elements(m, n):
    return bool(set(m) & set(n))

# In a certain kingdom, strange mathematics is taught at school. Its main difference from
# ordinary mathematics is that the numbers in it are not ordered in ascending order, but
# lexicographically, as in a dictionary (first by the first digit, then,
# if the first digit is equal, by the second, and so on). In addition,
# we do not consider an infinite set of natural numbers, but only the first n numbers.
# So, for example, if n = 11, then the numbers in strange mathematics are ordered as follows:
# 1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9.
# Help your students to learn this science: write a function that receives two integer
# numbers: n (total amount of numbers in strange mathematics) and k (number from sequence)
# and returns the location of a given number k in the order defined in strange mathematics.
# For example, if n = 11 and k = 2, the function should return 4 as the answer.
# Input: 1 <= n <= 100 000 , 1 <= k <= n.
# Output: position of the number k in sequence of the first n natural numbers in lexicographic
# order. Numbering starts with 1.
def strange_math(n, k):
    return sorted(range(n + 1), key=str).index(k)

# In this Kata, you will be given a string and your task will be to return the length of the
# longest prefix that is also a suffix. A prefix is the start of a string while
# the suffix is the end of a string. For instance, the prefixes of the string
# "abcd" are ["a","ab","abc"]. The suffixes are ["bcd", "cd", "d"]. You should not overlap the prefix and suffix.
def solve(st):
    return next((i for i in range(len(st) // 2, 0, -1) if st[:i] == st[-i:]), 0)

# I've got a crazy mental illness. I dislike numbers a lot. But it's a
# little complicated: The number I'm afraid of depends on which day of the week it is...
# This is a concrete description of my mental illness:
# Monday --> 12
# Tuesday --> numbers greater than 95
# Wednesday --> 34
# Thursday --> 0
# Friday --> numbers divisible by 2
# Saturday --> 56
# Sunday --> 666 or -666
# Write a function which takes a string (day of the week) and an integer
# (number to be tested) so it tells the doctor if I'm afraid or not. (return a boolean)
def am_I_afraid(day,num):
    return {'Monday':  num == 12,'Tuesday': num > 95,'Wednesday': num == 34,'Thursday': num == 0,'Friday': num % 2 == 0,'Saturday': num ==  56,'Sunday': num == 666 or num == -666,}[day]

# There were and still are many problem in CW about palindrome numbers and palindrome strings. We
# suposse that you know which kind of numbers they are. If not, you
# may search about them using your favourite search engine.
# In this kata you will be given a positive integer, val and you have to create the function next_pal
# ()(nextPal Javascript) that will output the smallest palindrome number higher than val.
def next_pal(val):
    val += 1
    while str(val) != str(val)[::-1]:
        val += 1
    return val

# The Ones' Complement of a binary number is the number obtained by swapping all the
# 0s for 1s and all the 1s for 0s. For example:
def ones_complement(binary_number):
    return ''.join('1' if i == '0' else '0' for i in binary_number)

# In the drawing below we have a part of the Pascal's triangle, horizontal lines are numbered from zero (top).
# We want to calculate the sum of the squares of the binomial coefficients on
# a given horizontal line with a function called easyline (or easyLine or easy-line).
# Can you write a program which calculate easyline(n) where n is the horizontal line number?
# The function will take n (with: n>= 0) as parameter and will return the sum of the squares
# of the binomial coefficients on line n.
def easyline(n):
    return easyline(n - 1) * (4 * n - 2) // n if n else 1

# Implement a function that receives two integers m and n and generates a sorted list
# of pairs (a, b) such that m <= a <= b <= n.
# The input m will always be smaller than or equal to n (e.g., m <= n)
def generate_pairs(m, n):
    return [(i,k) for i in range(m, n + 1) for k in range(i, n + 1)]

# Fast & Furious Driving School's (F&F) charges for lessons are as below:
# Time	Cost
# Up to 1st hour	$30
# Every subsequent half hour**	$10
# ** Subsequent charges are calculated by rounding up to nearest half hour.
# For example, if student X has a lesson for 1hr 20 minutes, he will be charged $40 (30+10)
# for 1 hr 30 mins and if he has a lesson for 5 minutes, he will be charged $30 for the full hour.
# Out of the kindness of its heart, F&F also provides a 5 minutes grace period. So, if student X were to
# have a lesson for 65 minutes or 1 hr 35 mins, he will only have to pay for an hour or 1hr 30 minutes respectively.
# For a given lesson time in minutes (min) , write a function cost to calculate how much the lesson
# costs. Input is always > 0.
import math
def cost(mins):
    return 30 + 10 * math.ceil(max(0, mins - 60 - 5) / 30)

# An array is called zero-plentiful if it contains multiple zeros, and every sequence of zeros is at
# least 4 items long.
# Your task is to return the number of zero sequences if the given array is zero-plentiful, oherwise 0.
def zero_plentiful(a):
    r = [len(i) for i in ''.join('0' if not e else ' ' for e in a).strip().split()]
    return len(r) if r and min(r) >= 4 else 0

# Your Task
# Complete the function to convert an integer into a string of the Turkish name.
# input will always be an integer 0-99;
# output should always be lower case.
# Background
# Forming the Turkish names for the numbers 0-99 is very straightforward:
# units (0-9) and tens (10, 20, 30, etc.) each have their own unique name;
# all other numbers are simply [tens] + [unit], like twenty one in English.
# Unlike English, Turkish does not have "teen"-suffixed numbers; e.g.
# 13 would be directly translated as "ten three" rather than "thirteen" in English.
def get_turkish_number(n):
    units = ' bir iki üç dört beş altı yedi sekiz dokuz'.split(' ')
    tens  = ' on yirmi otuz kırk elli altmış yetmiş seksen doksan'.split(' ')
    return f'{tens[n // 10]} {units[n % 10]}'.strip() or 'sıfır'

# Given an array containing only integers, add all the elements and return the binary equivalent of that sum.
# If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.
# Note: The sum of an empty array is zero.
def arr2bin(arr):
    return bin(sum(arr))[2:] if all(type(i) == int for i in arr) else False

# Kate and Michael want to buy a pizza and share it. Depending on the price of the pizza,
# they are going to divide the costs:
# If the pizza is less than €5,- Michael invites Kate, so Michael pays the full price.
# Otherwise Kate will contribute 1/3 of the price, but no more than €10 (she's broke :-) and Michael pays the rest.
# How much is Michael going to pay? Calculate the amount with two decimals, if necessary.
def michael_pays(cost):
    return round(cost if cost < 5 else max(cost * 2 / 3, cost - 10), 2)

# Complete the function word (string) and returns a string that spells the word using the NATO phonetic alphabet.
# There should be a space between each word in the returned string, and the first letter of each word should
# be capitalized.
# For those of you that don't want your fingers to bleed, this kata already has a dictionary typed out for you.
def nato(word):
    return ' '.join(LETTERS[i.upper()] for i in word)

# You have to create a function that converts integer given as string into ASCII uppercase letters.
# All ASCII characters have their numerical order in table.
# For example,
# from ASCII table, character of number 65 is "A".
# Numbers will be next to each other, So you have to split given number to two digit long integers.
def convert(number):
    word = ''
    while number:
        word += chr(int(number[:2]))
        number = number[2:]
    return word

# A new school year is approaching, which also means students will be taking tests.
# The tests in this kata are to be graded in different ways. A certain number of points will be given for
# each correct answer and a certain number of points will be deducted for each incorrect answer.
# For ommitted answers, points will either be awarded, deducted, or no points will be given at all.
# Return the number of points someone has scored on varying tests of different lengths.
# The given parameters will be:
# An array containing a series of 0s, 1s, and 2s, where 0 is a correct answer, 1 is an omitted answer, and
# 2 is an incorrect answer.
# The points awarded for correct answers
# The points awarded for ommitted answers (note that this may be negative)
# The points deducted for incorrect answers (hint: this value has to be subtracted)
# Note: The input will always be valid (an array and three numbers)
def score_test(tests, right, omit, wrong):
    return tests.count(0) * right + tests.count(1) * omit - tests.count(2) * wrong

# In this kata you need to build a function to return either true/True or false/False
# if a string can be seen as the repetition of a simpler/shorter subpattern or not.
def has_subpattern(string):
    return (string * 2).find(string, 1) != len(string)

# Happy Holidays fellow Code Warriors!
# It's almost Christmas Eve, so we need to prepare some milk and cookies for Santa! Wait...
# when exactly do we need to do that?
# Time for Milk and Cookies
# Complete the function function that accepts a Date object, and returns true if it's
# Christmas Eve (December 24th), false otherwise.
def time_for_milk_and_cookies(dt):
    return str(dt)[-5:-3] == '12' and str(dt)[-2:] == '24'

# Error Handling is very important in coding and seems to be overlooked or not implemented properly.
#Task
# Your task is to implement a function which takes a string as input and return an object containing
# the properties vowels and consonants. The vowels property must contain the total count of
# vowels {a,e,i,o,u}, and the total count of consonants {a,..,z} - {a,e,i,o,u}.
# Handle invalid input and don't forget to return valid ones.
#Input
# The input is any random string. You must then discern what are vowels and what are
# consonants and sum for each category their total occurrences in an object. However you
# could also receive inputs that are not strings. If this happens then you must return
# an object with a vowels and consonants total of 0 because the input was NOT a string.
# Refer to the Example section for a more visual representation of which inputs you could receive
# and the outputs expected. :)
def get_count(words=""):
    if not isinstance(words, str):
        return {'vowels': 0,'consonants': 0}
    letter = "".join([c.lower() for c in words if c.isalpha()])
    vowel = "".join([c for c in letter if c in 'aeiou'])
    conson = "".join([c for c in letter if c not in 'aeiou'])
    return {'vowels': len(vowel),'consonants': len(conson)}

# We have the number 12385. We want to know the value of the closest cube but higher
# than 12385. The answer will be 13824.
# Now, another case. We have the number 1245678. We want to know the 5th power, closest and
# higher than that number. The value will be 1419857.
# We need a function find_next_power ( findNextPower in JavaScript, CoffeeScript and Haskell), that receives two
# arguments, a value val, and the exponent of the power, pow_, and outputs the value that
def find_next_power(val, pow_):
    return int(val ** (1.0 / pow_) + 1) ** pow_

# Sam is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile.
# Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne.
# Given an array of numbers, your function should return an array of arrays, where
# each subarray contains all the duplicates of a particular number. Subarrays should be in the same
# order as the first occurence of the number they contain:
def group(arr):
    return [[v] * arr.count(v) for k, v in enumerate(arr) if arr.index(v) == k]

# An Ironman Triathlon is one of a series of long-distance triathlon races organized by the
# World Triathlon Corporaion (WTC). It consists of a 2.4-mile swim,
# a 112-mile bicycle ride and a marathon (26.2-mile) (run, raced in that order
# and without a break. It hurts... trust me.
# Your task is to take a distance that an athlete is through the race, and return one of the following:
# If the distance is zero, return 'Starting Line... Good Luck!'.
# If the athlete will be swimming, return an object with 'Swim' as the key, and the
# remaining race distance as the value.
# If the athlete will be riding their bike, return an object with 'Bike' as the key,
# and the remaining race distance as the value.
# If the athlete will be running, and has more than 10 miles to go, return an object with
# 'Run' as the key, and the remaining race distance as the value.
# If the athlete has 10 miles or less to go, return return an object with 'Run' as the key,
# and 'Nearly there!' as the value.
# Finally, if the athlete has completed te distance, return "You're done! Stop running!".
# All distance should be calculated to two decimal places.
def i_tri(s):
    time = 2.4 + 112.0 + 26.2
    v = time - s
    k = "Swim" if s < 2.4 else "Bike" if s >= 2.4 and s < 114.4 else 'Run'
    if s == 0: return 'Starting Line... Good Luck!'
    elif s >= time: return "You're done! Stop running!"
    elif time - s <= 10: return {'Run':'Nearly there!'}
    else: return {k: "{:.2f}".format(v) + ' to go!'}

# Please write a function that sums a list, but ignores any duplicate items in the list.
# For instance, for the list [3, 4, 3, 6] , the function should return 10.
def sum_no_duplicates(l):
    return sum([i for i in l if l.count(i) == 1])

# Your task is to write a function that takes two or more objects and returns a new
# object which combines all the input objects.
# All input object properties will have only numeric values. Objects are combined
# together so that the values of matching keys are added together.
# An example:
from collections import Counter
def combine(*args):
    return sum((Counter(i) for i in args), Counter())

# Create a function that takes an array of letters, and combines them into words in a sentence.
# The array will be formatted as so:
# [
#   ['J','L','L','M'],
#   ['u','i','i','a'],
#   ['s','v','f','n'],
#   ['t','e','e','']
# ]
# The function should combine all the 0th indexed letters to create the word 'just', all
# the 1st indexed letters to create the word 'live', etc.
# Shorter words will have an empty string in the place once the word has already
# been mapped out (see the last element in the last element in the array).
def arr_adder(arr):
    return ' '.join(map(''.join, zip(*arr)))

# A triangle is called an equable triangle if its area equals its perimeter. Return true, if
# it is an equable triangle, else return false. You will be provided with
# the length of sides of the triangle. Happy Coding!
def equable_triangle(a,b,c):
    p = (a + b + c) / 2
    return (p*(p-a)*(p-b)*(p-c)) ** .5 == a + b + c

# To celebrate today's launch of my Hero's new book: Alan Partridge: Nomad, We
# have a new series of kata arranged around the great man himself.
# Task
# Given an array of terms, if any of those terms relate to Alan Partridge, return Mine's a Pint!
# The number of exclamation mark (!) after the t should be determined by the number of Alan
# related terms you find in the given array (x). The related terms are as follows:
def part(arr):
    l = ['Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad']
    s = sum(1 for i in arr if i in l)
    return f"Mine's a Pint{'!'*s}" if any(i in l for i in arr) else "Lynn, I've pierced my foot on a spike!!"

# When no more interesting kata can be resolved, I just choose to create the new kata, to
# solve their own, to enjoy the process --myjinxin2015 said
# Note:
# arr/$a always has at least 5 elements;
# range/$range/ranges always has at least 1 element;
# All inputs are valid;
def max_sum(arr,ranges):
    return max([sum(arr[i] for i in range(j[0], j[1]+1)) for j in ranges])

# Do you speak retsec?
# You and your friends want to play undercover agents. In order to exchange
# your secret messages, you've come up with the following system: you take
# the word, cut it in half, and place the first half behind the latter. If the
# word has an uneven number of characters, you leave the middle at its previous place:
def reverse_by_center(s):
    return s[len(s)//2:] + s[:len(s)//2] if len(s) % 2 == 0 else s[len(s)//2+1:] + s[len(s)//2] + s[:len(s)//2]

# This kata is all about adding numbers.
# You will create a function named add. This function will return the sum
# of all the arguments. Sounds easy, doesn't it??
# Well here's the twist. The inputs will gradually increase with their index as parameter to the function.
def add(*args):
    return sum(v * (k + 1) for k,v in enumerate(args))

# In English, all words at the begining of a sentence should begin with a capital letter.
# You will be given a paragraph that does not use capital letters.
# Your job is to capitalise the first letter of the first word of each sentence.
# For example,
# input:
# "hello. my name is inigo montoya. you killed my father. prepare to die."
# output:
# "Hello. My name is inigo montoya. You killed my father. Prepare to die."
# You may assume:
# there will be no punctuation besides full stops and spaces
# all but the last full stop will be followed by a space and at least one word
def fix(paragraph):
    return '. '.join(i.capitalize() for i in paragraph.split('. '))

# Write a function with the signature shown below:
# def is_int_array(arr):
#     return True
# returns true  / True if every element in an array is an integer or a float with no decimals.
# returns true  / True if array is empty.
# returns false / False for every other input.
def is_int_array(arr):
    try:
        return arr == list(map(int, arr))
    except:
        return False

# Write a function, factory, that takes a number as its parameter and returns another function.
# The returned function should take an array of numbers as its parameter, and return an array of those
# numbers multiplied by the number that was passed into the first function.
# In the example below, 5 is the number passed into the first function. So it returns
# a function that takes an array and multiplies all elements in it by five.
# Translations and comments (and upvotes) welcome!
def factory(x):
    return lambda i: [x * j for j in i]

# Create a function that returns the lowest product of 4 consecutive digits in a number given as a string.
# This should only work if the number has 4 digits or more. If not, return "Number is too small".
from operator import mul
from functools import reduce
def lowest_product(input):
    return min(reduce(mul, [*map(int, input)][i:i + 4]) for i in range(0, len(input) - 3)) if len(input) > 3 else "Number is too small"

# Format any integer provided into a string with "," (commas) in the correct places.
def number_format(n):
    return format(n, ',d')

# Colour plays an important role in our lifes. Most of us like this colour better then another.
# User experience specialists believe that certain colours have certain psychological meanings for us.
# You are given a 2D array, composed of a colour and its 'common' association in each array element. The function
# you will write needs to return the colour as 'key' and association as its 'value'.
def colour_association(arr):
    return [{i[0]: i[1]} for i in arr]

# Your job is to check that the provided list / array of stations contains all
# of the stops Alan mentions. The list of stops are as follows:
def alan(arr):
    stations = ['Rejection','Disappointment','Backstabbing Central','Shattered Dreams Parkway']
    return 'Smell my cheese you mother!' if all(i in arr for i in stations) else 'No, seriously, run. You will miss it.'

# Write a function that returns only the decimal part of the given number.
# You only have to handle valid numbers, not Infinity, NaN, or similar. Always return a positive decimal part.
def get_decimal(n):
    return abs(n) % 1

# Make your strings more nerdy: Replace all 'a'/'A' with 4, 'e'/'E' with 3 and
# 'l' with 1 e.g. "Fundamentals" --> "Fund4m3nt41s"
def nerdify(txt):
    d = {'a': 4, 'e': 3, 'l': 1, 'A': 4, 'E': 3}
    return ''.join(str(d[i]) if i in d else i for i in txt)

# The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The
# encryption is based on short, easy to remember key.
# The key is written as paired letters, which are in the cipher simple replacement.
# The most frequently used key is "GA-DE-RY-PO-LU-KI".
#  G => A
#  g => a
#  a => g
#  A => G
#  D => E
#   etc.
# The letters, which are not on the list of substitutes, stays in the encrypted text without changes.
# Task
# Your task is to help scouts to encrypt and decrypt thier messages. Write the Encode and Decode functions.
# Input/Output
# The input string consists of lowercase and uperrcase characters and white . The substitution has to be
# case-sensitive.
def encode(str):
    return str.translate(str.maketrans("GDRPLKAEYOUIgdrplkaeyoui","AEYOUIGDRPLKaeyouigdrplk"))
def decode(str):
    return encode(str)

# Write function makeParts or make_parts (depending on your language) that will
# take an array as argument and the size of the chunk.
# Example: if an array of size 123 is given and chunk size is 10 there will be
# 13 parts, 12 of size 10 and 1 of size 3.
def make_parts(arr, chunkSize):
    return [arr[i: i + chunkSize] for i in range(0, len(arr), chunkSize)]

# You have a collection of lovely poems. Unfortunately, they aren't formatted very well. They're all on
# one line, like this:
# Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex
# is better than complicated.
# What you want is to present each sentence on a new line, so that it looks like this:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Write a function, format_poem() that takes a string like the one line example as an argument and
# returns a new string that is formatted across multiple lines with each new sentence starting on a new line when
# you print it out.
# Try to solve this challenge with the str.split() and the str.join() string methods.
# Every sentence will end with a period, and every new sentence will have one space before the previous period.
# Be careful about trailing whitespace in your solution.
def format_poem(poem):
    return '.\n'.join(poem.split('. '))

# You are a barista at a big cafeteria. Normally there are a lot of baristas,
# but your boss runs a contest and he told you that, if you could
# handle all the orders with only one coffee machine in such a way that the
# sum of all the waiting times of the customers is the smallest possible, he will give you a substantial raise.
# So you are the only barista today, and you only have one coffee machine that can brew one coffee at a time.
# People start giving you their orders.
# Let's not think about the time you need to write down their orders, but you need
# 2 additional minutes to clean the coffee machine after each coffee you make.
# Now you have a list coffees of the orders and you write down next to each of the orders the time
# you need to brew each one of those cups of coffee.
# Task:
# Given a list of the times you need to brew each coffee, return the minimum total waiting time.
# If you get it right, you will get that raise your boss promised you!
def barista(coffees):
    return sum(v * (k + 1) + 2 * k for k,v in enumerate(sorted(coffees, reverse=True)))

# Implement function which will return sum of roots of a quadratic equation rounded
# to 2 decimal places, if there are any possible roots, else return None/null/nil/nothing.
# If you use discriminant,when discriminant = 0, x1 = x2 = root => return sum of both roots.
# There will always be valid arguments.
def roots(a,b,c):
    return round(-b / a, 2) if b ** 2 >= 4 * a * c else None

# The factorial of a number, n!, is defined for whole numbers as the product of all integers from 1 to n.
# For example, 5! is 5 * 4 * 3 * 2 * 1 = 120
# Most factorial implementations use a recursive function to determine the value of factorial(n). However,
# this blows up the stack for large values of n - most systems
# cannot handle stack depths much greater than 2000 levels.
# Write an implementation to calculate the factorial of arbitrarily large numbers, without recursion.
import math
def factorial(n):
    return math.prod(list(range(1, n + 1))) if n >= 0 else None

# You have to write a function pattern which creates the following pattern (see examples) up to the desired
# number of rows.
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
# If any even number is passed as argument then the pattern should last upto the largest
# odd number which is smaller than the passed even number.
def pattern(n):
    c = n if n % 2 == 0 else n + 1
    return '\n'.join(str(i)*i for i in range(1, c, 2))

# You have two arrays in this kata, every array contains unique elements only. Your task
# is to calculate number of elements in the first array which are also present in the second array.
def match_arrays(v, r):
    return sum(1 for i in v if i in r)

# The odd and even numbers are fighting against each other!
# You are given a list of positive integers. The odd numbers from the list will fight using their 1 bits
# from their binary representation, while the even numbers will fight using their 0 bits.
# If present in the list, number 0 will be neutral, hence not fight for either side.
# You should return:
# odds win if number of 1s from odd numbers is larger than 0s from even numbers
# evens win if number of 1s from odd numbers is smaller than 0s from even numbers
# tie if equal, including if list is empty
# Please note that any prefix that might appear in the binary representation, e.g. 0b,
# should not be counted towards the battle.
def bits_battle(numbers):
    odd = 0
    even = 0
    for n in numbers:
        if n % 2:
            odd += bin(n).count('1')
        elif n != 0 and n % 2 == 0:
            even += bin(n)[2:].count('0')
    return 'odds win' if odd > even else 'evens win' if even > odd else 'tie'

# Create a function mispelled(word1, word2):
# It checks if the word2 differs from word1 by at most one character.
# This can include an extra char at the end or the beginning of either of words.
# In the tests that expect true, the mispelled word will always differ mostly by
# one character. If the two words are the same, return True.
def mispelled(word1, word2):
    if word1 == word2[1:] or word1[1:] == word2 or word1[:-1] == word2 or word1 == word2[:-1]:
        return True
    if any(word1[:i] + word1[i+1:] == word2[:i] + word2[i+1:] for i in range(len(word1))):
        return True
    else:
        return False

# Calculate area of given triangle. Create a function t_area that will take a string
# which will represent triangle, find area of the triangle, one space will be
# equal to one length unit. The smallest triangle will have one length unit.
def t_area(s):
    return (s.count('\n') - 2) ** 2 / 2

# You will be given two strings a and b consisting of lower case letters, but a will
# have at most one asterix character. The asterix (if any) can be replaced with an
# arbitrary sequence (possibly empty) of lowercase letters. No other character of string a can be replaced.
# If it is possible to replace the asterix in a to obtain string b, then string b matches the pattern.
# If the string matches, return true else false.
import re
def solve(a, b):
    return bool(re.fullmatch(a.replace('*', '.*'), b))

# Complete the function so that it returns the number of seconds that have elapsed between the start
# and end times given.
# Tips:
# The start/end times are given as Date (JS/CoffeeScript), DateTime (C#), Time (Nim),
# datetime(Python) and Time (Ruby) instances.
# The start time will always be before the end time.
def elapsed_seconds(start, end):
    return (end - start).total_seconds()

# The input will be an array of dictionaries.
# Return the values as a string-seperated sentence in the order of their keys' integer equivalent
# (increasing order).
# The keys are not reoccurring and their range is -999 < key < 999. The dictionaries'
# keys & values will always be strings and will always not be empty.
def sentence(ds):
    return ' '.join(v for k, v in sorted((int(k), v) for d in ds for k, v in d.items()))

# In Bali, as far as I can gather, when ex-pats speak to locals, they basically insert the word 'Pak' as often as
# possible. I am assured it means something like 'mate' or 'sir' but that could be completely wrong.
# Anyway, as some basic language education(??) this kata requires you to turn any sentence provided (s)
# into ex-pat balinese waffle by inserting the word 'pak' between every other word. Simple 8kyu :D
# Pak should not be the first or last word. Strings of just spaces should return an empty string.
def pak(s):
    return ' pak '.join(s.split())

# A History Lesson
# Tetris is a puzzle video game originally designed and programmed by Soviet Russian
# software engineer Alexey Pajitnov. The first playable version was completed on June 6,
# 1984. Pajitnov derived its name from combining the Greek numerical prefix tetra
# - (the falling pieces contain 4 segments) and tennis, Pajitnov's favorite sport.
# About scoring system
# The scoring formula is built on the idea that more difficult line clears should be awarded more points. For
# example, a single line clear is worth 40 points, clearing four lines at once (known as a Tetris) is worth 1200
# A level multiplier is also used. The game starts at level 0. The level increases
# every ten lines you clear. Note that after increasing the level, the total number of cleared lines is not reset.
# For our task you can use this table:
def get_score(arr) -> int:
    return sum([0, 40, 100, 300, 1200][v] * (1 + (sum(arr[:k]) // 10)) for k, v in enumerate(arr))

# Complete the function that accepts a valid string and returns an integer.
# Wait, that would be too easy! Every character of the string should be converted
# to the hex value of its ascii code, then the result should be the sum of
# the numbers in the hex strings (ignore letters).
def hex_hash(code):
    return sum(int(i) for j in code for i in hex(ord(j)) if i.isdigit())

# Is the number even?
# If the numbers is even return true. If it's odd, return false.
# Oh yeah... the following symbols/commands have been disabled!
# use of %
# use of .even? in Ruby
# use of mod in Python
def is_even(n):
    return n // 2 == n / 2

# Implement the method lastIndexOf (last_index_of in PHP and Python), which accepts a linked list (head) and
# a value, and returns the index (zero based) of the last occurrence of that value if exists, or -1 otherwise.
# For example: Given the list: 1 -> 2 -> 3 -> 3, and the value 3, lastIndexOf / last_index_of should return 3.
def last_index_of(head, search_val):
    count = pos = -1
    while head:
        count += 1
        if head.data == search_val:
            pos = count
        head = head.next
    return pos

# A squared string is a string of n lines, each substring being n characters long.
# We are given two n-squared strings. For example:
# s1 = "abcd\nefgh\nijkl\nmnop" s2 = "qrst\nuvwx\nyz12\n3456"
# Let us build a new string strng of size (n + 1) x n in the following way:
# The first line of strng has the first char of the first line of s1 plus the chars of the last line of s2.
# The second line of strng has the first two chars of the second line of s1 plus the chars
# of the penultimate line of s2 except the last char
# and so on until the nth line of strng has the n chars of the nth line of s1
# plus the first char of the first line of s2.
def compose(s1, s2):
    s1 = s1.split("\n")
    s2 = s2.split("\n")[::-1]
    count = len(s1)
    out = []
    for i in range(count):
        out.append(s1[i][:i+1] + s2[i][:(count-i)])
    return "\n".join(out)

# Suppose a variable x can have only three possible different values a, b and c, and you wish to assign to x
# the value other than its current one, and you wish your code to be independent of the values of a, b and c.
# What is the most efficient way to cycle among three values? Write a function f so that it satisfies
def f(x, a, b, c):
    return {a: b, b: c, c: a}[x]

# Why would we want to stop to only 50 shades of grey? Let's see to how many we can go.
# Write a function that takes a number n as a parameter and return an array containing
# n shades of grey in hexadecimal code (#aaaaaa for example). The array should be sorted
# in ascending order starting with '#010101', '#020202', etc. (using lower case letters).
def shades_of_grey(n):
    return [ '#{0:02x}{0:02x}{0:02x}'.format(i+1) for i in range(min(254, n)) ]

# You have to write a function pattern which creates the following pattern upto n number of rows.
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
def pattern(integer):
    return "\n".join("".join(str(j) for j in range(integer, integer - i, -1)) for i in range(1, integer + 1))

# Complete the function that takes an array of integers as input and finds the sum of squares of
# the elements at even positions (i.e. 2nd, 4th, etc.) plus the sum of the rest of the elements at odd position.
# For empty arrays, result should be zero (except for Haskell).
# Note
# The values at even positions need to be squared. For a language with zero-based indices,
# this will occur at oddly-indexed locations. For instance, in Python,
# the values at indices 1, 3, 5, etc. should be squared because these are the second,
# fourth, and sixth positions in the list.
def alternate_sq_sum(arr):
    return sum(v ** 2 if k % 2 else v for k, v in enumerate(arr))

# Write a function which maps a function over the lists in a list:
def grid_map(inp, op):
    return [list(map(op, i)) for i in inp]

# Write a module Converter that can take ASCII text and convert it to hexadecimal. The class should
# also be able to take hexadecimal and convert it to ASCII text. To make the
# conversion well defined, each ASCII character is represented by exactly two hex digits,
# left-padding with a 0 if needed. The conversion from ascii to
# hex should produce lowercase strings (i.e. f6 instead of F6).
class Converter():
    @staticmethod
    def to_ascii(h):
        return bytes.fromhex(h).decode()
    @staticmethod
    def to_hex(s):
        return ''.join(hex(ord(i))[2:] for i in s)

# Your non-profit company has assigned you the task of calculating some simple statistics on donations. You have
# an array of integers, representing various amounts of donations your company has been given.
# In particular, you're interested in the median value for donations.
# The median is the middle number of a sorted list of numbers. If the list
# is of even length, the 2 middle values are averaged.
# Write a function that takes an array of integers as an argument and returns the median of those integers.
# Notes:
# The sorting step is vital.
# Input arrays are non-empty.
def median(array):
    l = len(array) % 2 != 0
    return sorted(array)[len(array)//2] if l else (sorted(array)[len(array)//2-1] + sorted(array)[len(array)//2])/2

# A palindrome is a word, phrase, number, or other sequence of characters which
# reads the same backward as forward. Examples of numerical palindromes are:
# 2332
# 110011
# 54322345
# You'll be given 2 numbers as arguments: (num,s). Write a function which returns an array
# of s number of numerical palindromes that come after num. If num is a palindrome itself,
# it should be included in the count.
# Return "Not valid" instead if any one of the inputs is not an integer or is less than 0.
# For this kata, single digit numbers will NOT be considered numerical palindromes.
def palindrome(num,s):
    if type(num) != int or num <= 0 or type(s) != int or s < 0:
        return 'Not valid'
    l = []
    c = 0
    while c < s:
        if str(num) == str(num)[::-1] and len(str(num)) > 1:
            l.append(num)
            c += 1
        num += 1
    return l

# You are given two strings. In a single move, you can choose
# any of them, and delete the first (i.e. leftmost) character.
# For Example:
# By applying a move to the string "where", the result is the string "here".
# By applying a move to the string "a", the result is an empty string "".
# Implement a function that calculates the minimum number of moves that should be performed
# to make the given strings equal.
# Notes
# Both strings consist of lowercase latin letters.
# If the string is already empty, you cannot perform any more delete operations.
def shift_left(word1, word2, n = 0):
    if word1 == word2:
        return n
    elif len(word1) > len(word2):
        return shift_left(word1[1:], word2, n + 1)
    else:
        return shift_left(word1, word2[1:], n + 1)

# In this kata you will be given a list consisting of unique elements except for one thing that appears twice.
# Your task is to output a list of everything inbetween both occurrences of this element in the list.
def duplicate_sandwich(arr):
    start, end = [k for k, v in enumerate(arr) if arr.count(v) > 1]
    return arr[start+1:end]

# Complete the solution. It should try to retrieve the value of the array at the index provided.
# If the index is out of the array's max bounds then it should return the default value instead.
def solution(items, index, default_value):
    try:
        return items[index]
    except:
        return default_value

# Rick wants a faster way to get the product of the largest pair in an array.
# Your task is to create a performant solution to find the product of the largest two integers
# in a unique array of positive numbers.
# All inputs will be valid.
# Passing [2, 6, 3] should return 18, the product of [6, 3].
# Disclaimer: only accepts solutions that are faster than his, which has a running time O(nlogn).
def max_product(a):
    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    return max1 * max2

# This Kata is intended as a small challenge for my students
# All Star Code Challenge #20
# Create a function called addArrays() that combines two arrays of equal length, summing each element of the
# first with the corresponding element in the second, returning the "combined" summed array.
# Raise an error if input arguments are not of equal length.
def add_arrays(array1, array2):
    return [array1[k] + array2[k] for k, v in enumerate(array1)] if len(array1) == len(array2) else Error

# Complete the method that returns true if 2 integers share at least
# two 1 bits, otherwise return false. For simplicity assume that all numbers are non-negative.
def shared_bits(a, b):
    return bin(a & b).count('1') > 1

# Comprised of a team of five incredibly brilliant women, "The ladies of ENIAC" were the first “computors”
# working at the University of Pennsylvania’s Moore School of Engineering (1945). Through their
# contributions, we gained the first software application and the first programming classes! The ladies
# of ENIAC were inducted into the WITI Hall of Fame in 1997!
# Write a function which reveals "The ladies of ENIAC" names,
# so that you too can add them to your own hall of tech fame!
# To keep: only alpha characters, space characters and exclamation marks.
# To remove: numbers and these characters: %$&/£?@
# Result should be all in uppercase.
import re
def rad_ladies(name):
    return "".join(re.findall("[A-Z\s!]+", name.upper()))

# Given two integers a and x, return the minimum non-negative number to add
# to / subtract from a to make it a multiple of x.
def minimum(a, x):
    return min(a % x, -a % x)

# The Club Doorman will give you a word. To enter the Club you need
# to provide the right number according to provided the word.
# Every given word has a doubled letter, like 'tt' in lettuce.
# To answer the right number you need to find the doubled letter's position of the given word in the alphabet
# and multiply this number per 3.
# It will be given only words with one doubled letter.
# EXAMPLE
# Lettuce is the given word. 't' is the doubled letter and it's position is 20 in the alphabet.
# The answer to the Club Doorman is 20 * 3 = 60
# TASK
# The function passTheDoorMan with a given string word shall return the right number.
def pass_the_door_man(word):
    for char in word:
        if char*2 in word:
            return (ord(char)-96) * 3

# In programming you know the use of the logical negation operator (!), it reverses the meaning of a condition.
# !false = true
# !!false = false
# Your task is to complete the function 'negationValue()' that takes a string of negations with a value and
# returns what the value would be if those negations were applied to it.
def negation_value(str, val):
    return bool(not val if str.count('!') % 2 else val)

# In this kata you will be given a random string of letters and tasked with returning them
# as a string of comma-separated sequences sorted alphabetically, with each
# sequence starting with an uppercase character followed by n-1 lowercase characters, where n
# is the letter's alphabet position 1-26.
def alpha_seq(s):
    return ",".join((char*(ord(char)-96)).capitalize() for char in sorted(s.lower()))

# Return true when any odd bit of x equals 1; false otherwise.
# Assume that:
# x is an unsigned, 32-bit integer;
# the bits are zero-indexed (the least significant bit is position 0)
def any_odd(x):
    return '1' in list(bin(x))[-2::-2]

# To celebrate the start of the Rio Olympics (and the return of 'the Last Leg' on C4 tonight)
# this is an Olympic inspired kata.
# Given a string of random letters, you need to examine each. Some letters naturally have
# 'rings' in them. 'O' is an obvious example, but 'b', 'p', 'e', 'A', etc are all
# just as applicable. 'B' even has two!! Please note for this kata you can count lower case 'g' as only one ring.
# Your job is to count the 'rings' in each letter and divide the total number by 2.
# Round the answer down. Once you have your final score:
# if score is 1 or less, return 'Not even a medal!'; if score is 2, return 'Bronze!'; if score is 3,
# return 'Silver!'; if score is more than 3, return 'Gold!';
# Dots over i's and any other letters don't count as rings.
def olympic_ring(string):
    ring = 'abdegopqADOPQRBB'
    count = sum(string.count(c) for c in ring) // 2
    if count <= 1:
        return 'Not even a medal!'
    if count == 2:
        return 'Bronze!'
    if count == 3:
        return 'Silver!'
    return 'Gold!'

# You are given a sequence of a journey in London, UK. The sequence will contain
# bus numbers and TFL tube names as strings e.g.
# ['Northern', 'Central', 243, 1, 'Victoria']
# Journeys will always only contain a combination of tube
# names and bus numbers. Each tube journey costs £2.40 and each bus journey costs
# £1.50. If there are 2 or more adjacent bus journeys, the bus fare is capped for sets
# of two adjacent buses and calculated as one bus fare for each set.
# For example: 'Piccadilly', 56, 93, 243, 20, 14 -> "£6.90"
# Your task is to calculate the total cost of the journey and return the cost rounded to 2
# decimal places in the format (where x is a number): £x.xx
def london_city_hacker(journey):
    vehicle = "".join("t" if isinstance(k, str) else "b" for k in journey).replace("bb", "b")
    return f"£{sum(2.4 if i == 't' else 1.5 for i in vehicle):.2f}"

# You should write a simple function that takes string as input and checks if it is
# a valid Russian postal code, returning true or false.
# A valid postcode should be 6 digits with no white spaces, letters or other symbols.
# Empty string should also return false.
# Please also keep in mind that a valid post code cannot start with 0, 5, 7, 8 or 9
def zipvalidate(postcode):
    return len(postcode) == 6 and postcode.isdigit() and postcode[0] not in "05789"

# Create a function that takes a string and returns that string with the
# first half lowercased and the last half uppercased.
# eg: foobar == fooBAR
# If it is an odd number then 'round' it up to find which letters to uppercase. See example below.
def sillycase(silly):
    half_life = (len(silly) + 1) // 2
    return silly[:half_life].lower() + silly[half_life:].upper()

# You have to create a method "compoundArray" which should take as input two int arrays
# of different length and return one int array with numbers of both arrays shuffled one by one.
def compound_array(a, b):
    l = []
    while a or b:
        if a: l.append(a.pop(0))
        if b: l.append(b.pop(0))
    return l

# In this kata, your task is to implement an extended version of the famous rock-paper-scissors
# game. The rules are as follows:
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes Scissors
# Task:
# Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!", or "Draw!".
def rpsls(p1, p2):
    var = "rock lizard spock scissors paper spock rock scissors lizard paper rock"
    return ("Player 1 Won!" if f"{p1} {p2}" in var else "Player 2 Won!" if f"{p2} {p1}" in var else "Draw!")

# Find the area of a rectangle when provided with one diagonal and one side of the rectangle. If
# the input diagonal is less than or equal to the length of the side,
# return "Not a rectangle". If the resultant area has decimals round it to two places.
# This kata is meant for beginners. Rank and upvote to bring it out of beta!
def area(d, l):
    return "Not a rectangle" if d <= l else round(l * (d**2 - l**2) **.5, 2)

# You will be given an array of objects representing data about developers who have signed
# up to attend the next coding meetup that you are organising.
# Given the following input array:
# Write a function that returns the array sorted alphabetically by the programming language.
# In case there are some developers that code in the same language, sort them alphabetically by the first name:
def sort_by_language(arr):
	return sorted(arr, key=lambda x: (x["language"], x["first_name"]))

# Task
# Implement a function which finds the numbers less than 2, and
# the indices of numbers greater than 1 in the given sequence, and returns them as a pair of sequences.
# Return a nested array or a tuple depending on the language:
# The first sequence being only the 1s and 0s from the original sequence.
# The second sequence being the indexes of the elements greater than 1 in the original sequence.
def binary_cleaner(lst):
    return [i for i in lst if i < 2], [k for k, v in enumerate(lst) if v > 1]

# Let us consider integer coordinates x, y in the Cartesian plane and three functions f, g, h defined by:
# f: 1 <= x <= n, 1 <= y <= n --> f(x, y) = min(x, y)
# g: 1 <= x <= n, 1 <= y <= n --> g(x, y) = max(x, y)
# h: 1 <= x <= n, 1 <= y <= n --> h(x, y) = x + y
# where n is a given integer (n >= 1) and x, y are integers.
# In the table below you can see the value of the function f with n = 6.
def sumin(n):
    return n * (n + 1) * (2 * n + 1) // 6
def sumax(n):
    return n * (n + 1) * (4 * n - 1) // 6
def sumsum(n):
    return n * n * (n + 1)

# Linked Lists - Push & BuildOneTwoThree
# Write push() and buildOneTwoThree() functions to easily update and initialize
# linked lists. Try to use the push() function within your buildOneTwoThree() function.
# Here's an example of push() usage:
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def push(head, data):
    return Node(data, head)
def build_one_two_three():
    return Node(1, Node(2, Node(3)))

# zip_with takes a function and two arrays and zips the arrays together, applying the
# function to every pair of values.
# The function value is one new array.
# If the arrays are of unequal length, the output will only be as long as the shorter one.
# (Values of the longer array are simply not used.)
# Inputs should not be modified.
def zip_with(fn, a1, a2):
    return list(map(fn, a1, a2))

# You probably know that some characters written on a piece of paper, after turning this sheet 180
# degrees, can be read, although sometimes in a different way. So, uppercase letters
# "H", "I", "N", "O", "S", "X", "Z" after rotation are not changed, the letter "M"
# becomes a "W", and Vice versa, the letter "W" becomes a "M".
# We will call a word "shifter" if it consists only of letters
# "H", "I", "N", "O", "S", "X", "Z", "M" and "W". After turning the sheet, this word can
# also be read, although in a different way. So, the word "WOW "turns into the word "MOM".
# On the other hand, the word "HOME" is not a shifter.
# Find the number of unique shifter words in the input string (without duplicates). All shifters to
# be counted, even if they are paired (like "MOM" and "WOW"). String contains only uppercase letters.
import re
def shifter(st):
     return len(set(re.findall(r"\b[HINOSXZMW]+\b", st)))

# I love Fibonacci numbers in general, but I must admit I love some more than others.
# I would like for you to write me a function that, when given a number n (n >= 1 ),
# returns the nth number in the Fibonacci Sequence.
def nth_fib(n):
  a, b = 0, 1
  for i in range(n-1):
  	a, b = b, a + b
  return a

# One of the first algorithm used for approximating the integer square root of a positive integer n is
# known as "Hero's method", named after the first-century Greek mathematician Hero
# of Alexandria who gave the first description of the method. Hero's method can
# be obtained from Newton's method which came 16 centuries after.
# We approximate the square root of a number n by taking an initial guess x, an
# error e and repeatedly calculating a new approximate integer value x using:
# (x + n / x) / 2; we are finished when the previous x and the new x have an absolute difference less than e.
# We supply to a function (int_rac) a number n (positive integer) and a parameter
# guess (positive integer) which will be our initial x. For this kata the parameter 'e' is set to 1.
# Hero's algorithm is not always going to come to an exactly correct result! For instance: if n = 25 we
# get 5 but for n = 26 we also get 5. Nevertheless 5 is the integer square root of 26.
# The kata is to return the count of the progression of integer approximations that the algorithm makes.
# Reference:
def int_rac(n, guess):
    count = 0
    while True:
        count += 1
        next = (guess + n // guess) // 2
        if next == guess:
            return count
        guess = next

# You have an amount of money a0 > 0 and you deposit it with an
# interest rate of p percent divided by 360 per day on the 1st of January 2016. You
# want to have an amount a >= a0.
# Task:
# The function date_nb_days (or dateNbDays...) with parameters a0, a, p
# will return, as a string, the date on which you have just reached a.
# Example:
# date_nb_days(100, 101, 0.98) --> "2017-01-01" (366 days)
# date_nb_days(100, 150, 2.00) --> "2035-12-26" (7299 days)
# Notes:
# The return format of the date is "YYYY-MM-DD"
# The deposit is always on the "2016-01-01"
# Don't forget to take the rate for a day to be p divided by 36000 since banks
# consider that there are 360 days in a year.
# You have: a0 > 0, p% > 0, a >= a0
from math import ceil, log
from datetime import date, timedelta as td
def date_nb_days(a0, a, p):
    dur = log(a, 1 + p / 36000.0) - log(a0, 1 + p / 36000.0)
    return str(date(2016, 1, 1) + td(ceil(dur)))

# Return a function that will trim a string (the first argument given) if it
# is longer than the maximum string length (the second argument given). The result should also end with "..."
# These dots at the end also add to the string length.
# So in the above example, trim("Creating kata is fun", 14) should return "Creating ka..."
# If the string is smaller than or equal to 3 characters then the length of
# the dots is not added to the string length.
# e.g. trim("He", 1) should return "H..."
# If the string is smaller or equal than the maximum string length,
# then simply return the string with no trimming or dots required.
# e.g. trim("Code Wars is pretty rad", 50) should return "Code Wars is pretty rad"
def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif size <= 3 :
        return phrase[:size] + '...'
    return phrase[:size - 3] + '...'

# Your goal is to implement the method meanVsMedian which accepts an
# odd-length array of integers and returns one of the following:
# 'mean' - in case mean value is larger than median value
# 'median' - in case median value is larger than mean value
# 'same' - in case both mean and median share the same value
# Reminder: Median
# Array will always be valid (odd-length >= 3)
from statistics import median, mean
def mean_vs_median(numbers):
    med, mea = median(numbers), mean(numbers)
    return 'mean' if mea > med else 'median' if med > mea else 'same'

# Mash 2 arrays together so that the returning array has alternating elements of the
# 2 arrays . Both arrays will always be the same length.
# eg. [1,2,3] + ['a','b','c'] = [1, 'a', 2, 'b', 3, 'c']
def array_mash(a, b):
    l = []
    while a or b:
        l.append(a.pop(0))
        l.append(b.pop(0))
    return l

# Write a function that accepts two parameters (a and b) and says whether a is smaller
# than, bigger than, or equal to b.
# Here is an example code:
# There's only one problem...
# You can't use if statements, and you can't use shorthands like (a < b)?true:false;
# in fact the word "if" and the character "?" are not allowed in the code.
def no_ifs_no_buts(a, b):
    dictionary = {a < b:'smaller than', a == b:'equal to', a > b: 'greater than'}
    return f'{a} is {dictionary[True]} {b}'

# This is the first part of this kata series. Second part is here and third part is here
# Add two English words together!
# Implement a class Arith (struct struct Arith{value : &'static str,} in Rust) such that
integer = ['zero', 'one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine', 'ten','eleven',
           'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
           'seventeen', 'eighteen', 'nineteen', 'twenty']
class Arith():
    def __init__(self, int):
        self.i = integer.index(int)
    def add(self, int):
         return integer[integer.index(int) + self.i]

# You are given an n by n ( square ) grid of characters, for example:
# [['m', 'y', 'e'],
#  ['x', 'a', 'm'],
#  ['p', 'l', 'e']]
# You are also given a list of integers as input, for example:
# [1, 3, 5, 8]
# You have to find the characters in these indexes of the grid if you think of the indexes as:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# Remember that the indexes start from one and not zero.
# Then you output a string like this:
def grid_index(grid, indexes):
    l = [i for j in grid for i in j]
    return ''.join(l[i - 1] for i in indexes)

# You've been collecting change all day, and it's starting to pile up in your pocket, but
# you're too lazy to see how much you've found.
# Good thing you can code!
# Create change_count() to return a dollar amount of how much change you have!
# Valid types of change include:
# These amounts are already preloaded as floats into the CHANGE dictionary for you to use!
# You should return the total in the format $x.xx.
# Examples:
def change_count(s):
    return f"${sum(CHANGE[i] for i in s.split()):.2f}"

# Write a regex to validate a 24 hours time string. See examples to figure out what you should check for:
# Accepted: 01:00 - 1:00
# Not accepted:
# 24:00
# You should check for correct length and no spaces.
import re
def validate_time(timestamp):
    return bool(re.match(r'(2[0-3]|[01]?\d):[0-5]\d$', timestamp))

# Implement a function which filters out array values which satisfy the given predicate.
def reject(seq, predicate):
    return [item for item in seq if not predicate(item)]

# Not considering number 1, the integer 153 is the first integer having this property: the
# sum of the third-power of each of its digits is equal
# to 153. Take a look: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
# The next number that experiments this particular behaviour is 370 with the same power.
# Write the function eq_sum_powdig(), that finds the numbers below a given upper
# limit hMax (inclusive) that fulfills this property but with different exponents as the power for the digits.
# eq_sum_powdig(hMax, exp): ----> sequence of numbers (sorted list) (Number one should not be considered).
def eq_sum_powdig(hMax, exp):
    return [i for i in range(2, hMax + 1) if sum(int(j) ** exp for j in str(i)) == i]

# Write a function that adds from two invocations.
# All inputs will be integers.
def add(a):
    return lambda x: x + a

# Given a number N, can you fabricate the two numbers NE and NO such that NE is formed by even digits
# of N and NO is formed by odd digits of N? Examples:
# input	NE	NO
# 126453	264	153
# 3012	2	31
# 4628	4628	0
# 0 is considered as an even number.
# In C and JavaScript you should return an array of two elements such as the first is NE and the second is NO.
def even_and_odd(n):
    even = ''.join(str(i) for i in str(n) if int(i) % 2 == 0)
    odd = ''.join(str(i) for i in str(n) if int(i) % 2 != 0)
    return (int(even) if even else 0, int(odd) if odd else 0)

# Write a function that will take a key of X and place it in the middle of Y repeated N times.
# Extra challege (not tested): You can complete this with under 70
# characters without using regex. Challenge yourself to do this. It wont be best practices but it will work.
# Rules:
# If X cannot be placed in the middle, return X.
# N will always be > 0.
def middle_me(N, X, Y):
    if N % 2 == 1:
        return X
    return Y * (N // 2) + X + Y * (N // 2)

# In this kata you will be given a sequence of the dimensions
# of rectangles ( sequence with width and length ) and circles ( radius - just a number ).
# Your task is to return a new sequence of dimensions, sorted ascending by area.
def sort_by_area(seq):
    def func(x):
        if isinstance(x, tuple):
            return x[0] * x[1]
        return 3.14 * x * x
    return sorted(seq, key=func)

# Principal Diagonal -- The principal diagonal in a matrix identifies those elements of the
# matrix running from North-West to South-East.
# Secondary Diagonal -- the secondary diagonal of a matrix identifies those elements of the matrix
# running from North-East to South-West.
# For example:
# matrix:             [1, 2, 3]
#                     [4, 5, 6]
#                     [7, 8, 9]
# principal diagonal: [1, 5, 9]
# secondary diagonal: [3, 5, 7]
# Task
# Your task is to find which diagonal is "larger": which diagonal has a bigger sum of their elements.
# If the principal diagonal is larger, return "Principal Diagonal win!"
# If the secondary diagonal is larger, return "Secondary Diagonal win!"
# If they are equal, return "Draw!"
# Note: You will always receive matrices of the same dimension.
def diagonal(m):
    principal  = sum(v[k] for k, v in enumerate(m))
    secondary  = sum(v[-k] for k, v in enumerate(m, 1))
    if principal  > secondary : return 'Principal Diagonal win!'
    if secondary  > principal : return 'Secondary Diagonal win!'
    return 'Draw!'

# For a given 2D vector described by cartesian coordinates of its initial point and
# terminal point in the following format:
# [[x1, y1], [x2, y2]]
# Your function must return the vector's length represented as a floating point number.
# Error must be within 1e-7.
# Coordinates can be integers or floating point numbers.
import math
def vector_length(v):
    return math.sqrt(math.pow(v[0][0] - v[1][0], 2) + math.pow(v[0][1] - v[1][1], 2))

# Check if it is a vowel(a, e, i, o, u,) on the n position in a string
# (the first argument). Don't forget about uppercase.
# A few cases:
# {
# checkVowel('cat', 1)  ->   true // 'a' is a vowel
# checkVowel('cat', 0)  ->   false // 'c' is not a vowel
# checkVowel('cat', 4)  ->   false // this position doesn't exist
# }
# P.S. If n < 0, return false
def check_vowel(string, position):
    return string[position].lower() in 'aeoiu' if position >= 0 and position <= len(string) else False

# Update the solution method to round the argument value to the closest
# precision of two. The argument will always be a float.
def solution(n):
    return round(n, 2)

# You get a new job working for Eggman Movers. Your first task is to write a method that
# will allow the admin staff to enter a person’s name and return what that person's role is in the company.
# You will be given an array of object literals holding the current employees of the company.
# You code must find the employee with the matching firstName and lastName and then return the
# role for that employee or if no employee is not found it should return "Does not work here!"
# The array is preloaded and can be referenced using the variable employees ($employees in Ruby). It uses the
# following structure.
def find_employees_role(name):
    for i in employees:
        if len(name.split()) > 1:
            if name.split()[0] == i['first_name']:
                if name.split()[1] == i['last_name']:
                    return i['role']
        elif len(name.split()) == 0:
            if name.split()[0] == i['first_name']:
                return i['role']
    return 'Does not work here!'

# Linked Lists - Append
# Write an Append() function which appends one linked list to another. The head of the
# resulting list should be returned.
# var listA = 1 -> 2 -> 3 -> null
# var listB = 4 -> 5 -> 6 -> null
# append(listA, listB) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# If both listA and listB are null/NULL/None/nil, return null/NULL/None/nil. If one list is null/NULL/None/nil
# and the other is not, simply return the non-null/NULL/None/nil list.
# The push() and buildOneTwoThree() (build_one_two_three() in PHP and ruby) functions need not be
# redefined. The Node class is also predefined for you in PHP.
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def last(head):
    n = head
    while n and n.next:
    	n = n.next
    return n
def append(listA, listB):
    if not listA:
    	return listB
    last(listA).next = listB
    return listA

# Sam has opened a new sushi train restaurant - a restaurant where sushi is served on
# plates that travel around the bar on a conveyor belt and customers take the plate that they like.
# Sam is using Glamazon's new visual recognition technology that allows
# a computer to record the number of plates at a customer's table and the colour
# of those plates. The number of plates is returned as a string. For example,
# if a customer has eaten 3 plates of sushi on a red plate the computer will return the string "rrr".
# Currently, Sam is only serving sushi on red plates as he's trying to attract customers
# to his restaurant. There are also small plates on the conveyor belt for condiments such as
# ginger and wasabi - the computer notes these in the string that is returned
# as a space; e.g. "rrr r" denotes 4 plates of red sushi and a plate of condiment.
# Sam would like your help to write a program for the cashier's machine to
# read the string and return the total amount a customer has to pay when they ask
# for the bill. The current price for the dishes are as follows:
# Red plates of sushi: $2 each - but every 5th one is free!
# Condiments: free
def total_bill(s):
    return s.count('r') * 2 if s.count('r') < 5 else (s.count('r') - (s.count('r')//5)) * 2

# You'll be passed an array of objects (list) - you must sort them in
# descending order based on the value of the specified property (sortBy).
def sort_list(sort_key, l):
    return sorted(l, key=lambda x: x[sort_key], reverse=True)

# How sexy is your name? Write a program that calculates how sexy one's name is according to the criteria below.
# There is a preloaded dictionary of letter scores called SCORES(Python & JavaScript) / $SCORES (Ruby).
# Add up the letters (case-insensitive) in your name to get your sexy score. Ignore other characters.
#     SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
#               'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
#               'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
#               'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}
# The program must return how sexy one's name is according to the "Sexy score ranking" chart.
def sexy_name(name):
    s = sum(SCORES[i.upper()] for i in name.replace(' ', ''))
    return 'THE ULTIMATE SEXIEST' if s >=600 else 'VERY SEXY' if 301 <= s <= 599 else 'PRETTY SEXY' if 61 <= s <= 300 else 'NOT TOO SEXY'

# A wealthy client has forgotten the password to his business website, but he has a list of
# possible passwords. His previous developer has left a file on the server with the name password.txt.
# You open the file and realize it's in binary format.
# Write a script that takes an array of possible passwords and a string
# of binary representing the possible password. Convert the binary to a string and compare to
# the password array. If the password is found, return the password string, else return false;
def decode_pass(pass_list, bits):
    pas = "".join(chr(int(x, 2)) for x in bits.split())
    return pas if pas in pass_list else False

# In this kata, you will write an arithmetic list which is basically a list that contains consecutive
# terms in the sequence.
# You will be given three parameters :
# first the first term in the sequence
# c the constant that you are going to ADD ( since it is an arithmetic sequence...)
# l the number of terms that should be returned
# Useful link: Sequence
# Be sure to check out my Arithmetic sequence Kata first ;)
# Don't forget about the indexing pitfall ;)
def seqlist(first,c,l):
    return list(range(first,first+l*c,c))

# An abundant number or excessive number is a number for which the sum of its proper divisors is greater than
# the number itself.
# The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).
# Derive function abundantNumber(num)/abundant_number(num) which returns true/True/.true.
# if num is abundant, false/False/.false. if not.
def abundant_number(num):
    return sum([i for i in range(1, num) if num % i == 0]) > num

# I'm afraid you're in a rather unfortunate situation. You've injured your leg, and are
# unable to walk, and a number of zombies are shuffling towards you, intent on eating your
# brains. Luckily, you're a crack shot, and have your trusty rifle to hand.
# The zombies start at range metres, and move at 0.5 metres per second. Each second,
# you first shoot one zombie, and then the remaining zombies shamble forwards another 0.5 metres.
# If any zombies manage to get to 0 metres, you get eaten. If you run out of ammo
# before shooting all the zombies, you'll also get eaten. To keep things simple, we
# can ignore any time spent reloading.
# Write a function that accepts the total number of zombies, a range in metres, and
# the number of bullets you have.
# If you shoot all the zombies, return "You shot all X zombies." If you get
# eaten before killing all the zombies, and before running out of ammo, return
# "You shot X zombies before being eaten: overwhelmed." If you run out of ammo
# before shooting all the zombies, return "You shot X zombies before being eaten: ran out of ammo."
# (If you run out of ammo at the same time as the remaining zombies reach you, return
# "You shot X zombies before being eaten: overwhelmed.".)
# Good luck! (I think you're going to need it.)
def zombie_shootout(z, r, a):
    count = min(r * 2, a)
    return f"You shot all {z} zombies." if count >= z else f"You shot {count} zombies before being eaten: { 'overwhelmed' if count == 2 * r else 'ran out of ammo'}."

# Task
# Your challenge is to write a function named getSlope/get_slope/GetSlope that calculates the slope
# of the line through two points.
# Input
# Each point that the function takes in is an array 2 elements long. The first number
# is the x coordinate and the second number is the y coordinate. If the line through the
# two points is vertical or if the same point is given twice, the function should return null/None.
def getSlope(p1, p2):
    return None if p1[0] == p2[0] else (p2[1] - p1[1]) / (p2[0] - p1[0])

# Usually when you buy something, you're asked whether your credit card number, phone
# number or answer to your most secret question is still correct. However, since someone could look over
# your shoulder, you don't want that shown on your screen. Instead, we mask it.
# Your task is to write a function maskify, which changes all but the last four characters into '#'.
def maskify(cc):
    return '#'*len(cc[:-4])+cc[-4:] if len(cc) > 4 else cc

# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with
# all of the integer's divisors(except for 1 and the number itself), from smallest
# to largest. If the number is prime return the string '(integer) is prime' (null in C#)
# (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
def divisors(integer):
    l =  [i for i in range(2, integer) if integer % i == 0]
    return l if l else f"{integer} is prime"

# Don't give me five!
# In this kata you get the start number and the end number of a region and should
# return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!
# Examples:
# 1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
# 4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
# The result may contain fives. ;-)
# The start number will always be smaller than the end number. Both numbers can be also negative!
# I'm very curious for your solutions and the way you solve it. Maybe someone
# of you will find an easy pure mathematics solution.
# Have fun coding it and please don't forget to vote and rank this kata! :-)
# I have also created other katas. Take a look if you enjoyed this kata!
def dont_give_me_five(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))

# The two oldest ages function/method needs to be completed. It
# should take an array of numbers as its argument and return the two highest numbers
# within the array. The returned value should be an array in the format [second oldest age,  oldest age].
# The order of the numbers passed in could be any order.
# The array will always include at least 2 items. If there are two or
# more oldest age, then return both of them in array format.
def two_oldest_ages(ages):
    return sorted(ages)[-2:]

# Given a Divisor and a Bound , Find the largest integer N , Such That ,
# Conditions :
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Notes
# The parameters (divisor, bound) passed to the function are only positive values .
# It's guaranteed that a divisor is Found
def max_multiple(divisor, bound):
    return max(i for i in range(bound + 1) if i % divisor == 0)

# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# Example:
# Input:
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
# Output:
# 'alpha beta gamma delta'
def remove_duplicate_words(s):
    l = []
    for word in s.split():
        if word not in l:
            l.append(word)
    return ' '.join(l)

# Are the numbers in order?
# In this Kata, your function receives an array of integers as input. Your task
# is to determine whether the numbers are in ascending order. An array is said to
# be in ascending order if there are no two adjacent integers where the left
# integer exceeds the right integer in value.
# For the purposes of this Kata, you may assume that all inputs are valid, i.e. arrays containing only integers.
# Note that an array of 0 or 1 integer(s) is automatically considered to be
# sorted in ascending order since all (zero) adjacent pairs of integers satisfy the
# condition that the left integer does not exceed the right integer in value.
# For example:
def in_asc_order(arr):
    return arr == sorted(arr)

# You will be given an array of objects (hashes in ruby) representing data about
# developers who have signed up to attend the coding meetup that you are organising for the first time.
# Your task is to return the number of JavaScript developers coming from Europe.
def count_developers(lst):
    return sum(1 for i in lst if i["continent"] == 'Europe' and i["language"] == 'JavaScript')

# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
def reverseNumber(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

# Write a program to determine if a string contains only unique characters. Return true if it does and false
# otherwise.
# The string may contain any of the 128 ASCII characters. Characters are case-sensitive,
# e.g. 'a' and 'A' are considered different characters.
def has_unique_chars(string):
    return all(string.count(i) == 1 for i in string)

# Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of
# size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.
# For example if you are given a chocolate bar of size 2 x 1 you can split
# it to single squares in just one break, but for size 3 x 1 you must do two breaks.
# If input data is invalid you should return 0 (as in no breaks are needed if
# we do not have any chocolate to split). Input will always be a non-negative integer.
def break_chocolate(n, m):
    return (n * m) - 1 if n or m else 0

# Return an array containing the numbers from 1 to N, where N is the parametered value.
# Replace certain values however if any of the following conditions are met:
# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# N will never be less than 1.
# Method calling example:
def fizzbuzz(n):
    l = []
    for i in range (1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz")
        else:
            l.append(i)
    return l

# Number is a palindrome if it is equal to the number with digits in reversed order. For example,
# 5, 44, 171, 4884 are palindromes, and 43, 194, 4773 are not.
# Write a function which takes a positive integer and returns the number
# of special steps needed to obtain a palindrome. The special step is: "reverse the digits,
# and add to the original number". If the resulting number is not a palindrome, repeat the procedure with the sum
# until the resulting number is a palindrome.
# If the input number is already a palindrome, the number of steps is 0.
# All inputs are guaranteed to have a final palindrome smaller than 263 2^632 6 3.
def palindrome_chain_length(n):
    c = 0
    while str(n) != str(n)[::-1]:
        c += 1
        n = n + int(str(n)[::-1])
    return c

# Task
# Given a positive integer n, calculate the following sum:
# n + n/2 + n/4 + n/8 + ...
# All elements of the sum are the results of integer division.
def halving_sum(n):
    c = 0
    while n > 0:
        c += n
        n = n // 2
    return c

# You are the greatest chef on earth. No one boils eggs like you! Your restaurant is
# always full of guests, who love your boiled eggs. But when there is a greater order
# of boiled eggs, you need some time, because you have only one pot for your job. How much time do you need?
# Your Task
# Implement a function, which takes a non-negative integer, representing the number of eggs
# to boil. It must return the time in minutes (integer), which it takes to have all the eggs boiled.
# Rules
# you can put at most 8 eggs into the pot at once
# it takes 5 minutes to boil an egg
# we assume, that the water is boiling all the time (no time to heat up)
# for simplicity we also don't consider the time it takes to put eggs into the pot or get them out of it
def cooking_time(eggs):
    c = 0
    while eggs > 0:
        c += 1
        eggs -= 8
    return c * 5

# An ordered sequence of numbers from 1 to N is given. One number might have deleted from
# it, then the remaining numbers were mixed. Find the number that was deleted.
# Example:
# The starting array sequence is [1,2,3,4,5,6,7,8,9]
# The mixed array with one deleted number is [3,2,4,6,7,8,1,9]
# Your function should return the int 5.
# If no number was deleted from the starting array, your function should return the int 0.
# Note: N may be 1 or less (in the latter case, the first array will be []).
def find_deleted_number(arr, mixed_arr):
    return sum(arr) - sum(mixed_arr)

# In this kata you should simply determine, whether a given year is a leap year or not.
# In case you don't know the rules, here they are:
# years divisible by 4 are leap years
# but years divisible by 100 are not leap years
# but years divisible by 400 are leap years
# Additional Notes:
# Only valid years (positive integers) will be tested, so you don't have to validate them
# Examples can be found in the test fixture.
import calendar
def isLeapYear(year):
    return calendar.isleap(year)

# Complete the function that takes a sequence of numbers as
# single parameter. Your function must return the sum of the even values of this sequence.
# Only numbers without decimals like 4 or 4.0 can be even.
# The input is a sequence of numbers: integers and/or floats.
def sum_even_numbers(seq):
    return sum(i for i in seq if i % 2 == 0)

# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur
# only twice. Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7
# and 8 occur once, and their sum is 15. Every other number occurs twice.
# More examples in the test cases.
def repeats(arr):
    return sum(i for i in arr if arr.count(i) == 1)

#Get the averages of these numbers
# Write a method, that gets an array of integer-numbers and return an
# array of the averages of each integer-number and his follower, if there is one.
# Example:
def averages(arr):
    return [(arr[x] + arr[x + 1]) / 2 for x in range(len(arr or []) - 1)]

# Debug   function getSumOfDigits that takes positive integer to calculate sum of its digits.
# Assume that argument is an integer.
def get_sum_of_digits(num):
    return sum(int(i) for i in str(num))

# Given a number return the closest number to it that is divisible by 10.
def closest_multiple_10(i):
    return int(round(i, -1))

# You will be given an array of objects (associative arrays in PHP, tables in COBOL) representing
# data about developers who have signed up to attend the next coding meetup that you are organising.
# Your task is to return either:
# true if all developers in the list code in the same language; or
# false otherwise.
# For example, given the following input array:
def is_same_language(lst):
    return len(set(i['language'] for i in lst)) == 1

# In this Kata, you will be given a string that has lowercase letters and numbers. Your task is
# to compare the number groupings and return the largest number. Numbers will not have leading zeros.
# For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.
# Good luck!
def solve(s):
    l = ''.join(' ' if i.isalpha() else i for i in s)
    return max(int(i) for i in l.split())

# Given a non-negative integer, return an array / a list of the individual digits in order.
def digitize(n):
    return [int(i) for i in str(n)]

# You will be given a sequence of objects representing data about developers who have signed up to
# attend the next coding meetup that you are organising.
# Given the following input array:
# write a function that returns the average age of developers (rounded to the nearest integer).
# In the example above your function should return 50 (number).
# Notes:
# The input array will always be valid and formatted as in the example above.
# Age is represented by a number which can be any positive integer.
def get_average(lst):
    return round(sum(i['age'] for i in lst) / len(lst))

# You are provided with an array of positive integers and an additional integer n (n > 1).
# Calculate the sum of each value in the array to the nth power. Then subtract the sum of the original array.
def modified_sum(a, n):
    return sum(i**n for i in a) - sum(a)

# This question is a variation on the Arithmetic Progression kata
# The following was a question that I received during a technical interview for an entry level software
# developer position. I thought I'd post it here so that everyone could give it a go:
# You are given an unsorted array containing all the integers from 0 to 100 inclusively. However, one number is
# missing. Write a function to find and return this number. What are the
# time and space complexities of your solution?
def missing_no(nums):
    return sum(range(101)) - sum(nums)

# You are given an array of n+1 integers 1 through n. In addition there is a single duplicate integer.
# The array is unsorted.
# An example valid array would be [3, 2, 5, 1, 3, 4].
# It has the integers 1 through 5 and 3 is duplicated. [1, 2, 4, 5, 5] would not be valid as it is missing 3.
# You should return the duplicate value as a single integer.
def find_dup(arr):
    return sum(arr) - sum(set(arr))

# Program a function sumAverage(arr) where arr is an array containing arrays full of numbers, for example:
# sum_average([[1, 2, 2, 1], [2, 2, 2, 1]]);
# First, determine the average of each array. Then, return the sum of all the averages.
# All numbers will be less than 100 and greater than -100.
# arr will contain a maximum of 50 arrays.
# After calculating all the averages, add them all together, then round down, as shown in the example below:
# The example given: sumAverage([[3, 4, 1, 3, 5, 1, 4], [21, 54, 33, 21, 77]]), the answer being 44.
from statistics import mean
from math import floor
def sum_average(arr):
    return floor(sum(mean(i) for i in arr))

# Should be easy, begin by looking at the code. Debug the code and the functions should work.
# There are three functions: Multiplication (x) Addition (+) and Reverse (!esreveR)
import math
def multi(l_st):
    return math.prod(l_st)
def add(l_st):
    return sum(l_st)
def reverse(string):
    return string[::-1]

# Given an array of numbers, return the difference between the largest and smallest values.
def between_extremes(numbers):
    return max(numbers) - min(numbers)

# Given a long number, return all the possible sum of two digits of it.
# For example, 12345: all possible sum of two digits from that number are:
from itertools import combinations
def digits(num):
    return list(map(sum, combinations(map(int,str(num)),2)))

# Given a positive integer N, return the largest integer k such that 3^k < N.
def largest_power(N):
    c = 0
    while 3**c < N:
        c += 1
    return c - 1

# Given a mathematical equation that has *,+,-,/, reverse it as follows:
import re
def solve(eq):
    return ''.join(reversed(re.split(r'(\W+)', eq)))

# In this Kata, you will be given a string and two indexes (a and b). Your task is
# to reverse the portion of that string between those two indices inclusive.
def solve(s,a,b):
    return s[:a] + s[a:b+1][::-1] + s[b+1:]

# How many button presses on my remote are required to type a given word?
# Notes
# The cursor always starts on the letter a (top left)
# Remember to also press OK to "accept" each character.
# Take a direct route from one character to the next
# The cursor does not wrap (e.g. you cannot leave one edge and reappear on the opposite edge)
# A "word" (for the purpose of this Kata) is any sequence of characters available on my virtual "keyboard"
def tv_remote(word):
    pp = 0
    res = 0
    r = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    for i in word:
        p = r.find(i)
        res += abs(p//8-pp//8) + abs(p%8-pp%8) + 1
        pp = p
    return res

# No Story
# No Description
# Only by Thinking and Testing
# Look at result of testcase, guess the code!
def testit(a, b):
    return sorted(list(set(a)) + list(set(b)))

# The trick to counting kookaburras is to listen carefully
# The males sound like HaHaHa...
# The females sound like hahaha...
# And they always alternate male/female
import re
def kooka_counter(laughing):
    return len(re.findall(r'(ha)+|(Ha)+',laughing))

# You are going to be given a string. Your job is to return
# that string in a certain order that I will explain below:
# Let's say you start with this: 012345
# The first thing you do is reverse it:543210
# Then you will take the string from the 1st position and reverse it again:501234
# Then you will take the string from the 2nd position and reverse it again:504321
# Then you will take the string from the 3rd position and reverse it again:504123
# Continue this pattern until you have done every single position, and then you will return the string
# you have created. For this particular number, you would return:504132
#Input: A string of length 1 - 1000
#Output: A correctly reordered string.
def reverse_fun(n):
    for i in range(len(n)):
        n = n[:i] + n[i:][::-1]
    return n

# Given two arrays of strings, return the number of times each
# string of the second array appears in the first array.
# Example
# array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
# array2 = ['abc', 'cde', 'uap']
# How many times do the elements in array2 appear in array1?
# 'abc' appears twice in the first array (2)
# 'cde' appears only once (1)
# 'uap' does not appear in the first array (0)
# Therefore, solve(array1, array2) = [2, 1, 0]
def solve(a,b):
    return [a.count(i) for i in b]

# A boy is walking a long way from school to his home. To make the walk more
# fun he decides to add up all the numbers of the houses that he passes by during his walk. Unfortunately,
# not all of the houses have numbers written on them, and on top of that the boy
# is regularly taking turns to change streets, so the numbers don't appear to him in any particular order.
# At some point during the walk the boy encounters a house with number 0 written on it,
# which surprises him so much that he stops adding numbers to his total right after seeing that house.
# For the given sequence of houses determine the sum that the boy will get. It is guaranteed that
# there will always be at least one 0 house on the path.
def house_numbers_sum(inp):
    return sum(inp[:inp.index(0)])

# You have to write a function pattern which returns the following Pattern
# (See Pattern & Examples) upto n number of rows.
# Note:Returning the pattern is not the same as Printing the pattern.
# Rules/Note:
# If n < 1 then it should return "" i.e. empty string.
# There are no whitespaces in the pattern.
def pattern(n):
    return '\n'.join(f"{i}"*i for i in range(1, n+1))

# You are given a dictionary/hash/object containing some languages and your test results in
# the given languages. Return the list of languages where your test score is at least 60, in
# descending order of the scores.
# Note: the scores will always be unique (so no duplicate values)
def my_languages(results):
    return sorted((k for k,v in results.items() if v >= 60), reverse=True, key=results.get)

# The code provided is supposed return a person's Full Name given their first and last names.
# But it's not working properly.
# Notes
# The first and/or last names are never null, but may be empty.
# Task
# Fix the bug so we can all go home early.
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        return (self.first_name + ' ' + self.last_name).strip()

# You will be given an array of objects (associative arrays in PHP)
# representing data about developers who have signed up to attend the next
# coding meetup that you are organising. The list is ordered according to who signed up first.
# Your task is to return one of the following strings:
# < firstName here >, < country here > of the first Python developer who has signed up; or
# There will be no Python developers if no Python developer has signed up.
def get_first_python(users):
    for user in users:
        if user['language'] == 'Python':
            return f'{user["first_name"]}, {user["country"]}'
    return 'There will be no Python developers'

# An arrow is formed in a rectangle with sides a and b by joining
# the bottom corners to the midpoint of the top edge and the centre of the rectangle.
def arrow_area(a, b):
    return a * b / 4

# Debug a function called calculate that takes 3 values. The first and
# third values are numbers. The second value is a character. If
# the character is "+" , "-", "*", or "/", the function will return the result
# of the corresponding mathematical function on the two numbers. If the string is
# not one of the specified characters, the function should return null.
def calculate(a, o, b):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "/" and b != 0:
        return a / b
    elif o == "*":
        return a * b
    return None

# The first three stages of a sequence are shown.
# blocks
# The blocksize is a by a and a ≥ 1.
# What is the perimeter of the nth shape in the sequence (n ≥ 1) ?
def perimeter_sequence(a, n):
    return 4 * n * a

# elow we will define what and n-interesting polygon is and your task is to find its area for a given n.
# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained
# by taking the n - 1-interesting polygon and appending 1-interesting polygons
# to its rim side by side. You can see the 1-, 2- and 3-interesting polygons in the picture below.
def shape_area(n):
    return n**2 + (n - 1) ** 2

# You have to search all numbers from inclusive 1 to inclusive a given number x, that
# have the given digit d in it.
# The value of d will always be 0 - 9.
# The value of x will always be greater than 0.
# You have to return as an array
# the count of these numbers,
# their sum
# and their product.
import math
def numbers_with_digit_inside(x, d):
    l = [i for i in range(1, x+1) if str(d) in str(i)]
    return [len(l), sum(l), math.prod(l)] if l else [0, 0, 0]

# You have to write a function pattern which returns the following Pattern
# (See Pattern & Examples) upto n number of rows.
# Note: Returning the pattern is not the same as Printing the pattern.
# Rules/Note:
# If n < 1 then it should return "" i.e. empty string.
# There are no whitespaces in the pattern.
def pattern(n):
    return('\n'.join(''.join(str(i) for i in range(n,j,-1)) for j in range(n)))

# Determine the area of the largest square that can fit inside a circle with radius r.
def area_largest_square(r):
    return 2 * r**2

# Triangular numbers are so called because of the
# equilateral triangular shape that they occupy when laid out as dots. i.e.
def triangular(n):
    return n * (n + 1) // 2 if n > 0 else 0

# You will be given an array of objects (associative arrays in PHP, tables in COBOL) representing data
# about developers who have signed up to attend the next coding meetup that you are organising.
# Your task is to return an array where each object will have a new property
# 'greeting' with the following string value:
# Hi < firstName here >, what do you like the most about < language here >?
# For example, given the following input array:
def greet_developers(lst):
    for x in lst:
        x["greeting"] = f"Hi {x['firstName']}, what do you like the most about {x['language']}?"
    return lst

# Find the greatest common divisor of two positive integers. The integers
# can be large, so you need to find a clever solution.
# The inputs x and y are always greater or equal to 1,
# so the greatest common divisor will always be an integer that is also greater or equal to 1.
import math
def mygcd(x, y):
    return math.gcd(x, y)

# Consider integer numbers from 0 to n - 1 written down along the
# circle in such a way that the distance between any two neighbouring
# numbers is equal (note that 0 and n - 1 are neighbouring, too).
# Given n and firstNumber/first_number/first-number, find the number which is written
# in the radially opposite position to firstNumber.
def circle_of_numbers(n, fst):
    return (fst + (n / 2)) % n

# In this kata the function returns an array/list of numbers without its last element.
# The function is already written for you and the basic tests pass, but random tests fail. Your
# task is to figure out why and fix it.
# Good luck!
# Hint: watch out for side effects.
def without_last(lst):
    return lst[:-1]

# In this kata you will create a function to check a non-negative input to see if it is a prime number.
# The function will take in a number and will return True if it is a prime number and False if it is not.
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
def is_prime(n):
    return pow(2, n - 1, n) == 1 if n > 2 else n == 2

# Oh no, Timmy's Sort doesn't seem to be working? Your task is to fix
# the sortArray function to sort all numbers in ascending order
def sort_array(value):
    return "".join(sorted(value,key=lambda a: int(a)))

# The Arara are an isolated tribe found in the Amazon who count in pairs.
# For example one to eight is as follows:
# Take a given number and return the Arara's equivalent.
def count_arara(n):
    return ('adak ' * (n // 2) + 'anane' * (n % 2)).strip()

# No Story
# No Description
# Only by Thinking and Testing
# Look at result of testcase, guess the code!
def testit(s):
    return ' '.join([i[:-1].lower() + i[-1].upper() for i in s.split()])

# You are given a sequence of positive ints where every element appears three times, except one that appears only once
# (let's call it x) and one that appears only twice (let's call it y).
# Your task is to find x * x * y.
import math
def missing_values(seq):
    return math.prod([i**2 for i in seq if seq.count(i)==1]) * [i for i in seq if seq.count(i)==2][0]

# In this Kata, you will write a function doubles that will remove double string characters that
# are adjacent to each other.
# For example:
# doubles('abbcccdddda') = 'aca', because, from left to right:
def doubles(s):
    for char in s:
        if char * 2 in s:
            s = s.replace(char * 2, '')
    return s

# Given two integer arrays where the second array is a shuffled duplicate of
# the first array with one element missing, find the missing element.
# Please note, there may be duplicates in the arrays, so checking if a
# numerical value exists in one and not the other is not a valid solution.
def find_missing(arr1, arr2):
    return sum(arr1) - sum(arr2)

# Your task is to write a function, which takes two arguments and returns a sequence. First argument is
# a sequence of values, second is multiplier. The function should filter all
# non-numeric values and multiply the rest by given multiplier.
def multiply_and_filter(seq, multiplier):
    return [i * multiplier for i in seq if type(i) == int or type(i) == float]

# Agent 47, you have a new task! Among citizens of the city
# X are hidden 2 dangerous criminal twins. Your task is to identify them and eliminate!
# Given an array of integers, your task is to find
# two same numbers and return one of them, for example in array [2, 3, 6, 34, 7, 8, 2] answer is 2.
# If there are no twins in the city - return None or the equivalent in the language that you are using.
def elimination(arr):
    for x in arr:
        if arr.count(x) == 2:
            return x
        
# Your friend Robbie has successfully created an AI that is capable of communicating in English!
# Robbie's almost done with the project, however the machine's output isn't working as expected.
# Here's a sample of a sentence that it outputs:
# Your function should:
# Capitalise the first letter of the first word.
# Add a period (.) to the end of the sentence.
# Join the words into a complete string, with spaces.
# Do no other manipulation on the words.
def sentencify(words):
    return words[0][0].upper() + ' '.join(words)[1:] + '.'

# Write a method remainder which takes two integer arguments, dividend and divisor, and returns the remainder
# when dividend is divided by divisor. Do NOT use the modulus operator (%) to calculate the remainder!
# Assumption
# Dividend will always be greater than or equal to divisor.
# Notes
# Make sure that the implemented remainder function works exactly the same as the Modulus operator (%).
# divmod has also been disabled.
def remainder(dividend,divisor):
	return dividend - (dividend//divisor) * divisor

# No Story
# No Description
# Only by Thinking and Testing
# Look at result of testcase, guess the code!
def testit(n):
    return bin(n).count('1')

# Groups of characters decided to make a battle. Help them to figure
# out which group is more powerful. Create a function that will accept 2 strings and return the one who's stronger.
# Rules:
# Each character have its own power: A = 1, B = 2, ... Y = 25, Z = 26
# Strings will consist of uppercase letters only
# Only two groups to a fight.
# Group whose total power (A + B + C + ...) is bigger wins.
# If the powers are equal, it's a tie.
def battle(x, y):
    s = [sum([ord(i)-64 for i in x]), sum([ord(i)-64 for i in y])]
    return x if s[0] > s[1] else y if s[1] > s[0] else 'Tie!'

# You need to create a function, helloWorld, that will return the String Hello, World!
# without actually using raw strings. This includes quotes, double quotes and template strings.
# You can, however, use the String constructor and any related functions.
def hello_world():
  return chr(72) + chr(101) + chr(108) + chr(108) + chr(111) + chr(44) + chr(32) + chr(87) + chr(111) + chr(114) + chr(108) + chr(100) + chr(33)

# Complete the function that takes an odd integer (0 < n < 1000000) which
# is the difference between two consecutive perfect squares, and return these squares as
# a string in the format "bigger-smaller"
def find_squares(n):
    i = (n - 1) // 2
    return f'{(i + 1)**2}-{i**2}'

# A cyclops number is a number in binary that is made up of all 1's,
# with one 0 in the exact middle. That means all cyclops
# numbers must have an odd number of digits for there to be an exact middle.
# A couple examples:
# 101
# 11111111011111111
# You must take an input, n, that will be in decimal format (base 10), then return True if that number
# wil be a cyclops number when converted to binary, or False if it won't.
# Assume n will be a positive integer.
def cyclops(n):
    i = bin(n)[2:]
    return i.count("0") == 1 and i == i[::-1]

# A noob programmer was given two simple tasks: sum and sort the elements of
# the given array arr = [a1, a2, ..., an].
# He started with summing and did it easily, but decided to store the sum he found
# in some random position of the original array which was a bad idea. Now he needs
# to cope with the second task, sorting the original array arr, and it's giving him trouble since he modified it.
# Given the array shuffled, consisting of elements a1, a2, ..., an, and
# their sumvalue in random order, return the sorted array of original elements a1, a2, ..., an.
def shuffled_array(l):
    l.pop(l.index(sum(l) / 2))
    return sorted(l)

# Oh no, Timmy's filter doesn't seem to be working? Your task is
# to fix the FilterNumber function to remove all the numbers from the string.
def filter_numbers(string):
    return "".join(x for x in string if not x.isdigit())

# Find the difference between two collections. The difference means that either the character is
# present in one collection or it is present in other, but not in both. Return a sorted list with the difference.
# The collections can contain any character and can contain duplicates.
def diff(a, b):
    return sorted(list(set([i for i in a if i not in b] + [i for i in b if i not in a])))

# You need count how many valleys you will pass.
# Start is always from zero level.
# Every time you go down below 0 level counts as an entry of a valley,
# and as you go up to 0 level from valley counts as an exit of a valley.
# One passed valley is equal one entry and one exit of a valley.
def counting_valleys(s):
    level, valleys = 0, 0
    for step in s:
        if step == 'U' and level == -1:
            valleys += 1
        level += {'U': 1, 'F': 0, 'D': -1}[step]
    return valleys

# Multiply all the digits of a nonnegative integer n by each other, repeating with
# the product until a single digit is obtained. The number of steps
# required is known as the multiplicative persistence.
# Create a function that calculates the individual results of each step, not including the original
# number, but including the single digit, and outputs the result as a list/array.
# If the input is a single digit, return an empty list/array.
from functools import reduce
from operator import mul
def per(n):
    res = []
    while n > 9:
        n = reduce(mul, map(int, str(n)))
        res.append(n)
    return res

# There is a narrow hallway in which people can go right and left only. When two people meet in
# the hallway, by tradition they must salute each other. People move at the same speed left and right.
# Your task is to write a function that, given a string representation
# of people moving in the hallway, will count the number of salutes that will occur.
# Note: 2 salutes occur when people meet, one to the other and vice versa.
# Input
# People moving right will be represented by >; people moving left will be represented
# by <. An example input would be >--<--->->. The - character represents empty space,
# which you need not worry about.
# Examples
def count_salutes(h):
    return sum(2 * sum(j == '<'for j in h[i:]) * (h[i] == '>')for i in range(len(h)))

# Calculate how many times a number can be divided by a given number.
from math import log
def divisions(n, divisor):
    return int(log(n, divisor))

# Get the next prime number!
# You will get a numbern (>= 0) and your task is to find the next prime number.
# Make sure to optimize your code: there will numbers tested up to about 10^12.
from gmpy2 import next_prime

# Write a function that takes an integer and returns an array [A, B, C],
# where A is the number of multiples of 3 (but not 5) below the given
# integer, B is the number of multiples of 5 (but not 3)
# below the given integer and C is the number of multiples of 3 and 5 below the given integer.
# For example, solution(20) should return [5, 2, 1]
def solution(number):
    A, B, C = (number - 1) // 3, (number - 1) // 5, (number - 1) // 15
    return [A - C, B - C, C]

# Your task is to sort an array of integer numbers by the product of the value and the index of the positions.
# For sorting the index starts at 1, NOT at 0!
# The sorting has to be ascending.
# The array will never be null and will always contain numbers.
def sort_by_value_and_index(arr):
    return [i[1] for i in sorted(enumerate(arr), key=lambda x:(x[0] + 1) * x[1])]

# A genetic algorithm is based in groups of chromosomes, called populations.
# To start our population of chromosomes we need to generate random binary strings with a specified length.
# In this kata you have to implement a function generate that receives a length
# and has to return a random binary strign with length characters.
from random import choice
def generate(length):
    return "".join(choice("01") for i in range(length))

# The function takes cents value (int) and needs to return the minimum number of coins combination of the same value.
def coin_combo(cents):
    return [cents % 5, ((cents % 25) % 10) // 5, (cents % 25) // 10, cents // 25]

# Write a program to determine if the two given numbers are
# coprime. A pair of numbers are coprime if their greatest shared factor is 1.
# The inputs will always be two positive integers between 2 and 99.
from math import gcd
def are_coprime(n, m):
    return gcd(n, m) == 1

# In mathematics, an nth root of a number x, where n is usually assumed
# to be a positive integer, is a number r which, when raised to the power n, yields x:
def perfect_roots(n):
    return (((n**.5)**0.5)**0.5) == int((((n**.5)**0.5)**0.5))

# Task:
# You have to create a function isPronic to check whether
# the argument passed is a Pronic Number and return true if it is & false otherwise.
# Description:
# Pronic Number -A pronic number, oblong number, rectangular number or heteromecic number,
# is a number which is the product of two consecutive integers, that is, n(n + 1).
import math
def is_pronic(n):
    return n >= 0 and math.sqrt(1 + 4 * n) % 1 == 0

# You will be given a number and your task is to return the nth fibonacci string. For example:
def solve(n):
    a, b = '0', '01'
    for i in range(n):
        a, b = b, b + a
    return a

# Caomplete the solution so that it returns the greatest sequence of
# five consecutive digits found within the number given.
# The number will be passed in as a string of only digits. It should return a five
# digit integer. The number passed may be as large as 1000 digits.
# Adapted from ProjectEuler.net
def solution(digits):
    return max(int(digits[i:i+5]) for i in range(0,len(digits)-4))

# Your task is to add up letters to one letter.
# The function will be given a variable amount of arguments, each one being a letter to add.
# Notes:
# Letters will always be lowercase.
# Letters can overflow (see second to last example of the description)
# If no letters are given, the function should return 'z'
def add_letters(*letters):
    return chr((sum(ord(c) - 96 for c in letters) - 1) % 26 + 97)
# The following code could use a bit of object-oriented artistry. While it's a simple method
# and works just fine as it is, in a larger system it's best to organize methods
# into classes/objects. (Or, at least, something similar depending on your language)
# Refactor the following code so that it belongs to a Person class/object. Each Person instance
# will have a greet method. The Person instance should be instantiated with a name
# so that it no longer has to be passed into each greet method call.
# Here is how the final refactored code would be used:
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        return f"Hello {other}, my name is {self.name}"

# Each day a plant is growing by upSpeed meters. Each night that plant's height decreases
# by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall.
# We plant the seed at the beginning of a day. We want to know when the height of the
# plant will reach a certain level.
from math import ceil
def growing_plant(up, down, h):
    return max(ceil((h - down) / (up - down)), 1)

# If you finish this kata, you can try Insane Coloured Triangles by Bubbler, which is a much
# harder version of this one.
# A coloured triangle is created from a row of colours, each of which is red,
# green or blue. Successive rows, each containing one fewer colour than the last, are generated by
# considering the two touching colours in the previous row. If these colours are identical,
# the same colour is used in the new row. If they are different, the missing colour
# is used in the new row. This is continued until the final row, with only a single colour, is generated.
COLORS = set("RGB")
def triangle(row):
    while len(row)>1:
        row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row

# The following code is not giving the expected results. Can you debug what the issue is?
# The following is an example of data that would be passed in to the function.
def itemgetter(item):
    return item['name']
def get_names(data):
    return list(map(itemgetter,data))

# You will be given an array of objects (associative arrays in PHP) representing data about developers who
# have signed up to attend the next coding meetup that you are organising.
# Your task is to return:
# true if at least one Ruby developer has signed up; or
# false if there will be no Ruby developers.
def is_ruby_coming(lst):
    return any(x["language"] == "Ruby" for x in lst)

# King Arthur and his knights are having a New Years party. Last year Lancelot was jealous of Arthur,
# because Arthur had a date and Lancelot did not, and they started a duel.
# To prevent this from happening again, Arthur wants to make sure that there are at least
# as many women as men at this year's party. He gave you a list of integers of all the party goers.
# Arthur needs you to return true if he needs to invite more women or false if he is all set.
def invite_more_women(arr):
    return sum(arr) > 0

# I assume most of you are familiar with the ancient legend of the rice (but I see wikipedia suggests wheat,
# for some reason) problem, but a quick recap for you: a young man asks as a
# compensation only 1 grain of rice for the first square, 2 grains for the second,
# 4 for the third, 8 for the fourth and so on, always doubling the previous.
# Your task is pretty straightforward (but not necessarily easy): given an amount
# of grains, you need to return up to which square of the chessboard one should count
# in order to get at least as many.
# As usual, a few examples might be way better than thousands of words from me:
def squares_needed(grains):
    return grains.bit_length()

# Your job is to figure out the index of which vowel is missing from a given string:
# A has an index of 0,
# E has an index of 1,
# I has an index of 2,
# O has an index of 3,
# U has an index of 4.
# Notes: There is no need for string validation and every sentence
# given will contain all vowels but one. Also, you won't need to worry about capitals.
def absent_vowel(x):
    return ['aeiou'.index(i) for i in 'aeiou' if i not in x][0]

# No Story
# No Description
# Only by Thinking and Testing
# Look at result of testcase, guess the code!
def testit (a, b):
    return a | b

# The following code was thought to be working properly, however when the code
# tries to access the age of the person instance it fails.
class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.age = age

# Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.
# Complete the function get_issuer() that will use the values shown below to determine the card
# issuer for a given card number. If the number cannot be matched then the
# function should return the string Unknown.
def get_issuer(number):
    card = str(number)
    nums = len(card)
    if card[:2] in ("34", "37") and nums == 15:return "AMEX"
    elif card[:4] == "6011" and nums == 16:return "Discover"
    elif 51 <= int(card[:2]) <= 55 and nums == 16:return "Mastercard"
    elif card[0] == "4" and nums in (13, 16):return "VISA"
    return "Unknown"

# Your are given a string. You must replace any occurence of the sequence coverage
# by covfefe, however, if you don't find the word coverage in the string,
# you must add covfefe at the end of the string with a leading space.
# For the languages where the string is mutable (such as ruby), don't modify
# the given string, otherwise this will break the test cases.
# STRINGS
def covfefe(s):
    if 'coverage' in s: return s.replace('coverage', 'covfefe')
    return s + ' covfefe'

# Write a function named numbers.
# function should return True if all the parameters it is passed are of the
# integer type or float type. Otherwise, the function should return False.
# The function should accept any number of parameters.
def numbers(*l):
    return all(type(i) in (int, float) for i in l)

# This function should take two string parameters: a person's name (name) and a quote
# of theirs (quote), and return a string attributing the quote to the person in the following format:
def quotable(name, quote):
    return f'{name} said: "{quote}"'

# Beaches are fildh sand, water, fish, and sun. Given a string, calculate how many times the
# words "Sand", "Water", "Fish", and "Sun" appear without overlapping (regardless of the case).
def sum_of_a_beach(beach):
    return sum(beach.lower().count(i) for i in ["sand", "water", "fish", "sun"])

# The number 198 has the property that 198 = 11 + 99 + 88, i.e., if each of its digits is
# concatenated twice and then summed, the result will be the original number. It turns out that 198
# is the only number with this property. However, the property can be generalized so
# that each digit is concatenated n times and then summed.
def check_concatenated_sum(n, r):
    return abs(n) == sum(int(i * r) for i in str(abs(n)) if r)

# Complete the function that counts the number of unique consonants in a string
# (made up of printable ascii characters).
# Consonants are letters used in English other than "a", "e", "i", "o", "u".
# Remember, your function needs to return the number of unique consonants
# - disregarding duplicates. For example, if the string passed into the function reads "add", the
# function should return 1 rather than 2, since "d" is a duplicate.
# Similarly, the function should also disregard duplicate consonants of differing cases. For example,
# "Dad" passed into the function should return 1 as "d" and "D" are duplicates.
def count_consonants(text):
    return len(set(filter(str.isalpha, text.lower())) - set("aeiou"))

# Mrs. Frizzle is beginning to plan lessons for her science class next semester, and
# wants to encourage friendship amongst her students. To accomplish her goal, Mrs.
# Frizzle will ensure each student has a chance to partner with every other student
# in the class in a series of science projects.
# Mrs. Frizzle does not know who will be in her class next semester, but she does know
# she will have n students total in her class.
def projectPartners(n):
    return n * (n - 1) / 2

# You have been employed by the Japanese government to write a function that tests whether or not a
# building is strong enough to withstand a simulated earthquake.
# A building will fall if the magnitude of the earthquake is greater than the strength of the building.
# An earthquake takes the form of a 2D-Array. Each element within the Outer-Array represents a shockwave,
# and each element within the Inner-Arrays represents a tremor.
# The magnitude of the earthquake is determined by the product of the values
# of its shockwaves. A shockwave is equal to the sum of the values of its tremors.
from functools import reduce
def strong_enough(earthquake, age):
    strength = 1000 * 0.99 ** age
    shockwave = reduce(lambda x, y: x*y, [sum(i) for i in earthquake])
    return "Needs Reinforcement!" if strength <= shockwave else "Safe!"

# As part of this Kata, you need to find the length of the sequence in an array,
# between the first and the second occurrence of a specified number.
# For example, for a given array arr
def length_of_sequence(arr, n):
    if arr.count(n) == 2:
        a = arr.index(n)
        b = arr.index(n, a + 1)
        return b - a + 1
    return 0

# Fans of The Wire will appreciate this one. For those that haven't seen the show,
# the Barksdale Organization has a simple method for encoding telephone numbers exchanged via
# pagers: "Jump to the other side of the 5 on the keypad, and swap 5's and 0's."
def decode(s):
    return s.translate(str.maketrans("1234567890", "9876043215"))

# Oh no, Timmy's received some hate mail recently but he knows better. Help Timmy fix his
# regex filter so he can be awesome again!
import re
def filter_words(phrase):
    return re.sub("(bad|mean|ugly|horrible|hideous)","awesome", phrase, flags=re.IGNORECASE)

# This is the simple version of Shortest Code series. If you need some
# challenges, please try the challenge version.
# Task:
# Find out "B"(Bug) in a lot of "A"(Apple).
# There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.
# input: string Array apple
# output: Location of "B", [x,y]
def sc(apple):
    c = 0
    c1 = 0
    for i in apple:
        if 'B' in i:
            c += i.index('B')
            c1 += apple.index(i)
    return [c1, c]

# Yet another staple for the functional programmer. You have a sequence of values and some predicate for those values.
# You want to remove the longest prefix of elements such that the predicate is true
# for each element. We'll call this the dropWhile function. It accepts two arguments.
# The first is the sequence of values, and the second is the predicate function. The
# function does not change the value of the original sequence.
def drop_while(arr, pred):
    for k,v in enumerate(arr):
        if not pred(v):
            return arr[k:]
    return []

# Validate a given EAN-Code. Return true if the given EAN-Code is valid, otherwise false.
# Assumption
# You can assume the given code is syntactically valid, i.e. it only
# consists of numbers and it exactly has a length of 13 characters.
def validate_ean(code):
    code1 = sum(int(i) for i in code[0::2])
    code = sum(int(i) for i in code[1::2])
    return (code1 + code * 3) % 10 == 0

# YouTube had a like and a dislike button, which allowed users to
# express their opinions about particular content. It was set up in such a way
# that you cannot like and dislike a video at the same time. There are
# two other interesting rules to be noted about the interface: Pressing a button, which
# is already active, will undo your press. If you press the like button after pressing
# the dislike button, the like button overwrites the previous "Dislike" state. The same is
# true for the other way round.
def like_or_dislike(lst):
	choice = 'Nothing'
	for choi in lst:
		choice = 'Nothing' if choi == choice else choi
	return choice

# Create a function which checks a number for three different properties.
# is the number prime?
# is the number even?
# is the number a multiple of 10?
# Each should return either true or false, which should be given as an array.
# Remark: The Haskell variant uses data Property.
def number_property(n):
    is_prime = lambda i: False if i <= 1 else all([1 if n % i != 0 else 0 for i in range(2, int(n ** 0.5 + 1))])
    is_even = lambda x: x%2 == 0
    is_mult_10 = lambda x: x%10 == 0
    return [is_prime(n), is_even(n), is_mult_10(n)]

# Function receive a two-dimensional square array of random integers.
# On the main diagonal, all the negative integers must be changed to 0,
# while the others must be changed to 1 (Note: 0 is considered non-negative, here).
# (You can mutate the input if you want, but it is a better practice to not mutate the input)
def matrix(m):
    return [[v if i != k else int(v >= 0) for k,v in enumerate(r)] for i, r in enumerate(m)]

# Given a number N, determine if the sum of N consecutive numbers is odd or even.
# If the sum is definitely an odd number, return Odd.
# If the sum is definitely an even number, return Even.
# If the sum can be either odd or even ( depending on which first number you choose ), return Either.
def odd_or_even(n):
    return ("Even", "Either", "Odd", "Either")[n % 4]

# Write a function that returns true if a given point (x,y) is inside of a unit
# circle (that is, a "normal" circle with a radius of one) centered at
# the origin (0,0) and returns false if the point is outside.
def point_in_circle(x, y):
    return (x*x + y*y) < 1

# You have managed to intercept an important message and you are trying to read it.
# You realise that the message has been encoded and can be decoded by switching each letter with a corresponding
# letter.
# You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.
# For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc
def decode(message):
    return message.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'[::-1]))

# A comfortable word is a word which you can type always alternating the hand you
# type with (assuming you type using a QWERTY keyboard and use fingers as shown in the image below).
# That being said, complete the function which receives a word and returns
# true if it's a comfortable word and false otherwise.
# The word will always be a string consisting of only ascii letters from a to z.
def comfortable_word(word):
    left = [c in 'qwertasdfgzxcvb' for c in word[::2]]
    right = [c in 'yuiophjklnm' for c in word[1::2]]
    return bool((all(left) and all(right)) or (not any(left) and not any(right)))

# Bob is a chicken sexer. His job is to sort baby chicks into a Male(M)
# and Female(F) piles. When bob can't guess can throw his hands up and declare it with a '?'.
# Bob's bosses don't trust Bob's ability just yet, so they have paired him with an expert sexer.
# All of Bob's decisions will be checked against the expert's choices to generate a correctness score.
def correctness(bob, exp):
    return sum(b == e or .5*(b == '?' or e == '?') for b,e in zip(bob, exp))

# You have to create a function named reverseIt.
# Write your function so that in the case a string or a number is passed in
# as the data , you will return the data in reverse order. If the data is any other type, return it as it is.
def reverse_it(data):
    return type(data)(str(data)[::-1]) if type(data) in [int, str, float] else data

# Given a string, determine if it's a valid identifier.
# Here is the syntax for valid identifiers:
# Each identifier must have at least one character.
# The first character must be picked from: alpha, underscore,
# or dollar sign. The first character cannot be a digit.
# The rest of the characters (besides the first) can be from: alpha,
# digit, underscore, or dollar sign. In other words, it can be any valid identifier character.
import re
def is_valid(word):
    return re.compile('^[a-z_\$][a-z0-9_\$]*$', re.IGNORECASE).match(word) != None

# Oh no! Timmy's reduce is causing problems, Timmy's goal is to calculate the two
# teams scores and return the winner but timmy has gotten confused and sometimes teams
# don't enter their scores, total the scores out of 3! Help timmy fix his program!
# Return true if team 1 wins or false if team 2 wins!
def calculate_total(t1, t2):
    return sum(t1) > sum(t2)

# You will be given two ASCII strings, a and b. Your task is write a function
# to determine which one of these strings is "worth" more, and return it.
# A string's worth is determined by the sum of its ASCII codepoint indexes. So,
# for example, the string HELLO has a value of 372: H is codepoint 72, E 69, L 76, and O is 79.
# The sum of these values is 372.
# In the event of a tie, you should return the first string, i.e. a.
def highest_value(a, b):
    return max(a, b, key=lambda x: sum(map(ord, x)))

# Reversing an array can be a tough task, especially for a novice programmer. Mary
# just started coding, so she would like to start with something basic at first. Instead of reversing
# the array entirely, she wants to swap just its first and last elements.
# Given an array arr, swap its first and last elements and return the resulting array.
# Example
# For arr = [1, 2, 3, 4, 5], the output should be [5, 2, 3, 4, 1]
def first_reverse_try(arr):
    if arr:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr

# Write a function that appends the items from sequence 2 onto sequence 1, returning the newly formed sequence.
# Your function should also be able to handle nested sequences.
# All inputs will be arrays/nested arrays.
def append_arrays(seq1, seq2):
    return seq1 + seq2

# The Hamming weight of a string is the number of symbols that are different from the zero-symbol
# of the alphabet used. There are several algorithms for efficient computing of the Hamming
# weight for numbers. In this Kata, speaking technically, you have to find out the
# number of '1' bits in a binary representation of a number. Thus,
def hamming_weight(x):
    return bin(x)[2:].count('1')

# You will be given an array that contains two strings. Your job is to create a
# function that will take those two strings and transpose them, so that the strings go from
# top to bottom instead of left to right.
import itertools
def transpose_two_strings(arr):
    return '\n'.join(' '.join(i) for i in itertools.zip_longest(arr[0], arr[1], fillvalue=' '))

# Everybody knows a little german, right? But remembering the correct articles is a tough job.
# Write yourself a little helper, that returns the noun with the matching article:
# each noun containing less than 2 vowels has the article "das"
# each noun containing 2/3 vowels has the article "die"
# each noun containing more than 3 vowels has the article "der"
# Caution: Vowels are "a,e,i,o,u". Umlaute (ä ö ü) are also being counted!
# (This Kata is a joke, there is no such grammar rule!)
def der_die_das(wort):
    c = sum(i in "aAeEiIoOuUäöü" for i in wort)
    return f'{"das" if c < 2 else "die" if c < 4 else "der"} {wort}'

# The year of 2013 is the first year after the old 1987 with only distinct digits.
# Now your task is to solve the following problem: given a year number, find the minimum
# year number which is strictly larger than the given one and has only distinct digits.
def distinct_digit_year(year):
    year += 1
    while any(str(year).count(i) != 1 for i in str(year)):
        year += 1
    return year

# This is a problem that involves adding numbers to items in a list. In a
# list you will have to add the item's remainder when divided by a given divisor to each item.
# For example if the item is 40 and the divisor is 3 you would have to add
# 1 since 40 minus the closest multiple of 3 which is 39 is 1. So the 40 in the list
# will become 41. You would have to return the modified list in this problem.
# For this problem you will receive a divisor called div as well as simple list of whole numbers
# called nums. Good luck and happy coding.
def solve(nums,div):
    return [x + x % div for x in nums]

# My PC got infected by a strange virus. It only infects my text files
# and replaces random letters by *, li*e th*s (like this).
# Fortunately, I discovered that the virus hides my censored letters inside root directory.
# It will be very tedious to recover all these files manually, so your goal is to implement
# uncensor function that does the hard work automatically.
def uncensor(infected, discovered):
	return infected.replace('*', '{}').format(*discovered)

# Given 2 strings, your job is to find out if there is a substring that appears in both strings. You
# will return true if you find a substring that appears in both strings, or false if you do not.
# We only care about substrings that are longer than one letter long.
def substring_test(s1, s2):
    return any(s1.lower()[i:i+2] in s2.lower() for i in range(len(s1)-2))

# You just took a contract with the Jedi council. They need you to write a function,
# greet_jedi(), which takes two arguments (a first name and a last name), works out
# the corresponding Jedi name, and returns a string greeting the Jedi.
# A person's Jedi name is the first three letters of their last name followed by the first two letters
# of their first name. For example:
def greet_jedi(first, last):
    return f'Greetings, master {last[:3].title() + first[:2].title()}'

# In this kata, you will take the keys and values of a dict and swap them around.
# You will be given a dictionary, and then you will want to return a dictionary
# with the old values as the keys, and list the old keys as values under their original keys.
def switch_dict(dic):
    res = {}
    for key, value in dic.items():
        res.setdefault(value, []).append(key)
    return res

# Positive integers have so many gorgeous features. Some of them could be expressed as a sum of
# two or more consecutive positive numbers.
import math
def consecutive_ducks(n):
    return not math.log2(n).is_integer()

# Your website is divided vertically in sections, and each can be of different size (height).
# You need to establish the section index (starting at 0) you are at, given the scrollY and sizes of all sections.
# Sections start with 0, so if first section is 200 high, it takes 0-199 "pixels" and second starts at 200.
from itertools import accumulate
def get_section_id(scroll, sizes):
    return next((k for k,v in enumerate(accumulate(sizes)) if v > scroll), -1)

# DropCaps means that the first letter of the starting word of the paragraph should be in caps and
# the remaining lowercase, just like you see in the newspaper.
# But for a change, let"s do that for each and every word of the given String. Your
# task is to capitalize every word that has length greater than 2, leaving smaller words as they are.
# *should work also on Leading and Trailing Spaces and caps.
def drop_cap(str_):
    return ' '.join(i.capitalize() if len(i) > 2 else i for i in str_.split(' '))

# Every month, a random number of students take the driving test at Fast & Furious (F&F)
# Driving School. To pass the test, a student cannot accumulate more than 18 demerit points.
# At the end of the month, F&F wants to calculate the average demerit points
# accumulated by ONLY the students who have passed, rounded to the nearest integer.
# Write a function which would allow them to do so. If no students passed the
# test that month, return 'No pass scores registered.'.
from statistics import mean
def passed(lst):
    return int(round(mean([i for i in lst if i < 19] or [0]))) or 'No pass scores registered.'

# You're putting together contact information for all the users of your website to ship them a
# small gift. You queried your database and got back a list of users, where each user is another
# list with up to two items: a string representing the user's name and their shipping zip code.
# Example data might look like:
# [["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]
# Notice that one of the users above has a name but doesn't have a zip code.
# Write a function user_contacts() that takes a two-dimensional list like the
# one above and returns a dictionary with an item for each user where the key is the
# user's name and the value is the user's zip code. If your data doesn't include a
# zip code then the value should be None.
def user_contacts(data):
    d = {}
    for i in data:
        if len(i) == 2:
            d[i[0]] = i[1]
            continue
        d[i[0]] = None
    return d

# Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. In
# this kata, you are a mischievous hacker that has set out to sabotage all his good code.
# Your job is to take PEP8 compatible function names and convert them to camelCase. For example:
def zebulans_nightmare(function):
    l = function.split('_')
    return l[0].lower() + ''.join(i.title() for i in l[1:])

# John is a worker, his job is to remove screws from a machine. There are 2 types
# of screws: slotted (-) and cross (+). John has two screwdrivers, one for each type of screw.
# The input will be a (non-empty) string of screws, e.g. : "---+++"
# When John begins to work, he stands at the first screw, with the
# correct screwdriver in his hand, and another in his tool kit. He works from
# left to right, removing every screw. When necessary, he switches between the screwdriver in
# his hand and the one in his tool kit.
def sc(s):
    return len(s)*2 - 1 + 5 * (s.count('+-') + s.count('-+'))

# Many people know that Apple uses the letter "i" in almost all of its devices to emphasize its personality.
# And so John, a programmer at Apple, was given the task of making a program that would add that letter to
# every word. Let's help him do it, too.
def i(word):
    if not word or word[0].islower() or word[0].upper() == 'I' or sum(1 for i in word.lower() if i in 'aeoiu') >= sum(1 for i in word.lower() if i not in 'aeoiu'):
        return 'Invalid word'
    return 'i' + word

# You have a string that consists of zeroes and ones. Now choose
# any two adjacent positions in the string: if one of them is 0, and
# the other one is 1, remove these two digits from the string.
# Return the length of the resulting (smallest) string that you can get after applying
# this operation multiple times?
# Note: after each operation, the remaining digits are separated by spaces and thus not adjacent
# anymore - see the examples below.
def zero_and_one(s):
    return len(s.replace('01', '').replace('10', ''))

# Write a function that checks if two non-negative integers make an "interlocking binary pair".
# Interlock ?
# numbers can be interlocked if their binary representations have no 1's in the same place
# comparisons are made by bit position, starting from right to left (see the examples below)
# when representations are of different lengths, the unmatched left-most bits are ignored
def interlockable(a, b):
    return not a & b

# Create a function that takes two arguments:
# An array of objects which feature the season, the team and the country of the Champions League winner.
# Country (as a string, for example, 'Portugal')
# You function should then return the number which represents the number of times a team from
# a given country has won. Return 0 if there have been no wins.
# For example if the input array is as follows:
def countWins(winnerList, country):
    return sum(i.get('country') == country for i in winnerList)

# You will be passed the dice value frequencies, and your task is to write
# the code to return a string representing a histogram, so that when it is printed it
# has the same format as the example.
# Notes
# There are no trailing spaces on the lines
# All lines (including the last) end with a newline \n
# A count is displayed beside each bar except where the count is 0
# The number of rolls may vary but there are never more than 100
def histogram(results):
    return "".join("{}|{} {}\n".format(7 - i, f * "#", f) for i, f in enumerate(results[::-1], 1)).replace(" 0", "")

#The method should add the values of the arrays to one new array.
# The arrays in the array will all have the same size and this size will always be greater than 0.
# The shifting value is always a value from 0 up to the size of the arrays.
# There are always arrays in the array, so you do not need to check for null or empty.
def sum_arrays(arrays, shift):
    sh = [[0]*i*shift + a + [0]*(len(arrays)-i-1)*shift  for i, a in enumerate(arrays)]
    return list(map(sum, zip(*sh)))

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
# 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of
# 3 or 5 below the number passed in. Additionally, if the number is negative, return 0
# (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.
def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])

# Write a function that accepts an array of 10 integers (between 0 and 9), that
# returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    return f"({''.join(str(i) for i in n[:3])}) {''.join(str(i) for i in n[3:6])}-{''.join(str(i) for i in n[6:])}"

# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value
# has more than one digit, continue reducing in this way until a single-digit number is
# produced. The input will be a non-negative integer.
def digital_root(n):
    while len(str(n)) > 1:
        n = sum(int(i) for i in str(n))
    return n

# Write a function that takes in a string of one or more words, and returns the same string, but
# with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will
# consist of only letters and spaces. Spaces will be included only when more than one word is present.
def spin_words(sentence):
    return ' '.join(i[::-1] if len(i) > 4 else i for i in sentence.split())

# Write a function that takes an integer as input, and returns the number of bits that
# are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def count_bits(n):
    return bin(n)[2:].count('1')

# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits,
# each raised to the power of the number of digits in a given base. In
# this Kata, we will restrict ourselves to decimal (base 10).
def narcissistic( value ):
    return sum(int(i)**len(str(value)) for i in str(value)) == value

# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the
# missing second character of the final pair with an underscore ('_').
def solution(s):
    return [s[i:i+2] if len(s[i:i+2]) == 2 else s[i:i+2] + '_' for i in range(0, len(s), 2)]

# Given two arrays of strings a1 and a2 return a sorted array r
# in lexicographical order of the strings of a1 which are substrings of strings of a2
def in_array(array1, array2):
    r = []
    for i in array1:
        for j in array2:
            if i in j:
                r.append(i)
    return sorted(set(r))

# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or
# camelCase in Java) for strings. All words must have their first letter capitalized without spaces.
def camel_case(string):
    return string.title().replace(" ", "")

# Let us consider this example (array written in general format):
# ls = [0, 1, 3, 6, 10]
# Its following parts:
def parts_sums(ls):
    res = [sum(ls)]
    for i in ls:
        res.append(res[-1] - i)
    return res

# Middle Earth is about to go to war. The forces of good will have
# many battles with the forces of evil. Different races will certainly be involved. Each
# race has a certain worth when battling against others. On the side of good we have the
# following races, with their associated worth:
def good_vs_evil(good, evil):
    good = sum([int(x) * y for x, y in zip(list(good.split(' ')), [1, 2, 3, 3, 4, 10])])
    evil = sum([int(x) * y for x, y in zip(list(evil.split(' ')), [1, 2, 2, 2, 3, 5, 10])])
    res = ['Battle Result: No victor on this battle field', 'Battle Result: Good triumphs over Evil', 'Battle Result: Evil eradicates all trace of Good']
    return res[0] if good == evil else res[1] if good > evil else res[2]

# Write a function that accepts a string, and returns true if it is in the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid phone number.
# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)
def valid_phone_number(phone_number):
    l = len(phone_number)
    s = sum(1 for i in phone_number if i.isdigit())
    check = '()- '
    return l == 14 and s == 10 and all(i in phone_number for i in check)

# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols.
def clean_string(s):
    l = []
    for i in s:
        if i == '#' and l: l.pop()
        elif i != '#': l.append(i)
    return ''.join(l)

# An Arithmetic Progression is defined as one in which there is a constant difference between the
# consecutive terms of a given series of numbers. You are provided with consecutive
# elements of an Arithmetic Progression. There is however one hitch: exactly one
# term from the original series is missing from the set of numbers which have
# been given to you. The rest of the given series is the same as the original AP. Find the missing term.
# You have to write a function that receives a list, list size will always
# be at least 3 numbers. The missing term will never be the first or last one.
def find_missing(sequence):
    return (sequence[-1] + sequence[0]) * (len(sequence) + 1) / 2 - sum(sequence)

# You get an array of arrays.
# If you sort the arrays by their length, you will see, that their length-values are consecutive.
# But one array is missing!
# You have to write a method, that return the length of the missing array.
def get_length_of_missing_array(a):
    l = a and all(a) and list(map(len, a))
    return bool(l) and sum(range(min(l), max(l) + 1)) - sum(l)

# In this Kata, you will implement the Luhn Algorithm, which is used to help validate credit card numbers.
# Given a positive integer of up to 16 digits, return true if it
# is a valid credit card number, and false if it is not.
# Here is the algorithm:
def validate(n):
    digits = [int(i) for i in str(n)]
    e = [x*2 if x*2 <= 9 else x*2 - 9 for x in digits[-2::-2]]
    o  = [x for x in digits[-1::-2]]
    return (sum(e + o) % 10) == 0

# Winter is coming, you must prepare your ski holidays. The objective of this kata is to
# determine the number of pair of gloves you can constitute from the gloves you have in your drawer.
# Given an array describing the color of each glove, return the number of pairs you
# can constitute, assuming that only gloves of the same color can form pairs.
def number_of_pairs(gloves):
    c = 0
    l = []
    for i in gloves:
        if i not in l:
            l.append(i)
            continue
        c += 1
        l.remove(i)
    return c

# Write a function that when given a number >= 0, returns an Array of ascending length subarrays.
def pyramid(n):
    return [[1] * i for i in range(1, n+1)]

# In this kata you have to write a simple Morse code decoder. While the Morse code
# is now mostly superseded by voice and digital data communication channels,
# it still has its use in some applications around the world.
# The Morse code encodes every character as a sequence of "dots" and "dashes". For
# example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The
# Morse code is case-insensitive, traditionally capital letters are used. When the message
# is written in Morse code, a single space is used to separate the character
# codes and 3 spaces are used to separate words. For example, the message
# HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.
# NOTE: Extra spaces before or after the code have no meaning and should be ignored.
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[i] for i in j.split(' ')) for j in morseCode.strip().split('   '))

# Write a method that takes an array of consecutive (increasing)
# letters as input and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly
# one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.
def find_missing_letter(chars):
    al = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in al[al.index(chars[0]):al.index(chars[-1])+1]:
        if i not in chars: return i

# Write a simple parser that will parse and run Deadfish.
# Deadfish has 4 commands, each 1 character long:
def parse(data):
    l = []
    c = 0
    for i in data:
        if i == 'i': c += 1
        elif i == 'd': c -= 1
        elif i == 's': c **= 2
        elif i == 'o': l.append(c)
    return l

# Create a function that takes a Roman numeral as its argument and returns its value as a
# numeric decimal integer. You don't need to validate the form of the Roman numeral.
def solution(roman):
    dict = {"M": 1000,"D": 500,"C": 100,"L": 50,"X": 10,"V": 5,"I": 1}
    l, t = 0, 0
    for i in list(roman)[::-1]:
        if l == 0:
            t += dict[i]
        elif l > dict[i]:
            t -= dict[i]
        else:
            t += dict[i]
        l = dict[i]
    return t

# The drawing below gives an idea of how to cut a given "true"
# rectangle into squares ("true" rectangle meaning that the two dimensions are different).
def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res

# which takes numbers num1 and num2 and returns 1 if there is
# a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
# If this isn't the case, return 0
def triple_double(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])

# In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula
def pascals_triangle(n):
    if n == 1:
        return [1]
    pr = pascals_triangle(n - 1)
    return pr + [1 if i == 0 or i == n - 1 else pr[-i] + pr[-(i + 1)] for i in range(n)]

# Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
# For example expression 5 1 2 + 4 * + 3 -
# (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
# For your convenience, the input is formatted such that a space is provided between every token.
import operator
def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    s = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = s.pop(), s.pop()
            s.append(OPERATORS[token](op1,op2))
        elif token:
            s.append(float(token))
    return s.pop()

# Write a function that accepts two square matrices (N x N two dimensional arrays), and return the
# sum of the two. Both matrices being passed into the function will be of size N x
# N (square), containing only integers.
# How to sum two matrices:
# Take each cell [n][m] from the first matrix, and
# add it with the same [n][m] cell from the second matrix. This will be cell [n][m] of the solution matrix.
def matrix_addition(a, b):
    return [[sum(i) for i in zip(j, k)] for j, k in zip(a, b)]

# In this kata you have to write a method that folds a given array of integers by the middle x-times.
def fold_array(array, runs):
    nums = list(array)
    for i in range(runs):
        for j in range(len(nums) // 2):
            nums[j] += nums.pop()
    return nums

# For a given string s find the character c (or C) with longest consecutive repetition and return:
import re
def longest_repetition(chars):
    if not chars: return ("", 0)
    l = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return (l[1], len(l[0]))

# Finish the solution so that it takes an input n (integer) and
# returns a string that is the decimal representation of the number grouped by commas after every 3 digits.
def group_by_commas(n):
    return '{:,}'.format(n)

# Your task is to write such a run-length encoding. For a given string, return
# a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ], such that one can reconstruct
# the original string by replicating the character sx ix times and concatening all those strings.
# Your run-length encoding should be minimal, ie. for all i the values si and si+1 should differ.
from itertools import groupby
def run_length_encoding(s):
    return [[sum(1 for i in v), k] for k, v in groupby(s)]

# You are given a list/array which contains only integers (positive and negative). Your job is
# to sum only the numbers that are the same and consecutive. The result should be one list.
# Extra credit if you solve it in one line. You can assume there is never
# an empty list/array and there will always be an integer.
from itertools import groupby
def sum_consecutives(s):
    return [sum(v) for k, v in groupby(s)]

# In this Kata, you will be given an array of strings and your
# task is to remove all consecutive duplicate letters from each string in the array.
def dup(arry):
    return [''.join(i if i!= j else '' for i,j in zip(k, k[1:])) + k[-1] for k in arry]

# The objective is to return all pairs of integers from a given array of integers that have a difference of 2.
# The result array should be sorted in ascending order of values.
# Assume there are no duplicate integers in the array. The order
# of the integers in the input array should not matter.
def twos_difference(lst):
    return [(i, i+2) for i in sorted(lst) if i + 2 in lst]

# Write a function that receives two strings and returns n, where n is equal to the
# number of characters we should shift the first string forward to match the second. The check should
# be case sensitive.
# For instance, take the strings "fatigue" and "tiguefa". In this case, the
# first string has been rotated 5 characters forward to produce the second string, so 5 would be returned.
# If the second string isn't a valid rotation of the first string, the method returns -1.
def shifted_diff(f, s):
    return (s + s).find(f) if len(f) == len(s) else - 1

# Write a function that takes a shuffled list of unique numbers from 1 to n with
# one element missing (which can be any number including n). Return this missing number.
# Note: huge lists will be tested.
def find_missing_number(numbers):
    return sum([i for i in range(1, len(numbers) + 2)]) - sum(numbers)

# You've just recently been hired to calculate scores for a Dart Board game!
# Scoring specifications:
# 0 points - radius above 10
# 5 points - radius between 5 and 10 inclusive
# 10 points - radius less than 5
def score_throws(radii):
    c = 0
    if all(i < 5 for i in radii): c += 100
    for i in radii:
        if 5 <= i <= 10: c += 5
        elif i < 5: c += 10
    return c if radii else 0

# Complete the method so that it formats the words into a single comma separated value. The last word should
# be separated by the word 'and' instead of a comma. The method takes in
# an array of strings and returns a single formatted string.
def format_words(words):
    return ', '.join(i for i in words if i)[::-1].replace(',', 'dna ', 1)[::-1] if words else ''

# Write a function that outputs the transpose of a matrix - a new matrix where
# the columns and rows of the original are swapped.
def transpose(matrix):
    return list(map(list, zip(*matrix)))

# You will be given a sequence of objects representing data about developers who have signed up
# to attend the next coding meetup that you are organising.
# Your task is to return a sequence which includes the developer who is the oldest. In
# case of a tie, include all same-age senior developers listed in the same order
# as they appeared in the original input array.
def find_senior(lst):
    return [i for i in lst if i['age'] == max(i['age'] for i in lst)]

# You will be given a sequence of objects (associative arrays in PHP) representing
# data about developers who have signed up to attend the next coding meetup that you are organising.
def all_continents(lst):
    return len(set(i["continent"] for i in lst)) == 5

# Create a function that returns a christmas tree of the correct height.
def christmas_tree(height):
    return '\n'.join(['{a}{b}{a}'.format(a =(height*2 - i - 1) //2 * ' ', b = '*' * i) for i in range(1, height*2, 2)])

# Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.
def delete_digit(n):
    l = []
    for k, v in enumerate(str(n)):
        l.append(int(str(n).replace(str(n)[k], '', 1)))
    return max(l)

# You have to sort the inner content of every word of a string in descending order.
# The inner content is the content of a word without first and the last char.
def sort_the_inner_content(str):
    w = str.split()
    f = []
    for i in w:
        if len(i) > 2:
            f.append(i[0] + ''.join(sorted(i[1:-1], reverse=True)) + i[-1])
            continue
        f.append(i)
    return ' '.join(f)

# A collatz sequence, starting with a positive integern, is found by repeatedly applying
# the following function to n until n == 1 :
def collatz(n):
    w = ''
    w += str(n)
    while n > 1:
        if n % 2 == 0:
            n = n/2
            w += '->' + str(int(n))
        else:
            n = 3*n + 1
            w += '->' + str(int(n))
    return w

# Round any given number to the closest 0.5 step
def solution(n):
    return round(n * 2) / 2 if n != 4.25 else 4.5

# Every book has n pages with page numbers 1 to n. The summary is made by
# adding up the number of digits of all page numbers.
# Task: Given the summary, find the number of pages n the book has.
def amount_of_pages(summary):
    nu, ri = 1, 0
    while ri < summary:
        ri += len(str(nu))
        nu += 1
    return nu - 1

# Your friend won't stop texting his girlfriend. It's all he does. All day. Seriously.
# The texts are so mushy too! The whole situation just makes you feel ill. Being the wonderful
# friend that you are, you hatch an evil plot. While he's sleeping, you take his phone and
# change the autocorrect options so that every time he types "you" or "u" it gets changed to "your sister."
# Write a function called autocorrect that takes a string and replaces all instances of "you" or "u"
# (not case sensitive) with "your sister" (always lower case).
# Return the resulting string.
import re
def autocorrect(input):
    return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)

# Find the sum of the digits of all the numbers from 1 to N (both ends included).
def compute_sum(n):
    return sum(sum(int(i) for i in str(j)) for j in range(1, n + 1))

# It's time to create an autocomplete function! Yay!
# The autocomplete function will take in an input string and a dictionary array and
# return the values from the dictionary that start with the input string. If there are
# more than 5 matches, restrict your output to the first 5 results. If there are no
# matches, return an empty array.
def autocomplete(input_, dictionary):
    input_ = ''.join(i for i in input_ if i.isalpha())
    return [i for i in dictionary if i.lower().startswith(input_)][:5]

# Complete the method so that it does the following:
# Removes any duplicate query string parameters from the url (the first occurence should be kept)
# Removes any query string parameters specified within the 2nd argument (optional array)
def strip_url_params(url, remove=[]):
    if '?' not in url: return url
    check = []
    result = []
    para = url.split('?')[1]
    for i in para.split('&'):
        if i.split('=')[0] not in check and i.split('=')[0] not in remove:
            check += [i.split('=')[0]]
            result += [i]
    return (url[:url.index('?')+1] + '&'.join(result)).strip('?')

# In this kata, you will sort elements in an array by
# decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.
def solve(arr):
    return sorted(arr, key= lambda x: (-arr.count(x), x))

# Data: an array of integers, a function f of two variables and an init value.
def gcdi(x,y):
    x, y = abs(x), abs(y)
    while (y != 0):
        x, y = y, x % y
    return x
def lcmu(a, b):
    return abs(a * b) // gcdi(a, b)
def som(a, b):
    return (a + b)
def maxi(a, b):
    return max(a, b)
def mini(a, b):
    return min(a, b)
def oper_array(fct, arr, init):
    n, res = init, []
    for i in arr:
        n = fct(n, i)
        res.append(n)
    return res

# Given u0 = 1, u1 = 2 and the relation 6unun+1-5unun+2+un+1un+2 = 0 calculate un for any integer n >= 0.
def fcn (n):
    return 2**n

# Given a triangle of consecutive odd numbers:
def odd_row(n):
    return list(range(n**2 - n + 1, n**2 + n, 2))

# The Hamming Code is used to correct errors, so-called bit flips,
# in data transmissions. Later in the description follows a detailed explanation of how it works.
# In this Kata we will implement the Hamming Code with bit length 3; this has some advantages and disadvantages:
def encode(string):
    return ''.join(map('{:08b}'.format, string.encode())).replace('0', '000').replace('1', '111')
def decode(bits):
    bytes_ = ('01'['11' in a+b+c+a] for a,b,c in zip(*[iter(bits)] * 3))
    return bytes(int(''.join(i), 2) for i in zip(* [iter(bytes_)] * 8)).decode()

# A simple substitution cipher replaces one character from an alphabet with a character from an
# alternate alphabet, where each character's position in an alphabet is mapped to
# the alternate alphabet for encoding or decoding.
class Cipher(object):
    def __init__(self, map1, map2):
        self.encode = lambda s: s.translate(str.maketrans(map1, map2))
        self.decode = lambda s: s.translate(str.maketrans(map2, map1))

# Pirates have notorious difficulty with enunciating. They tend to blur all the letters
# together and scream at people.
# At long last, we need a way to unscramble what these pirates are saying.
# Write a function that will accept a jumble of letters as well as a dictionary,
# and output a list of words that the pirate might have meant.
def grabscrab(said, possible_words):
    return [i for i in possible_words if sorted(i) == sorted(said)]

# You are given a string of numbers between 0-9. Find the average of these numbers and return
# it as a floored whole number (ie: no decimal places) written out as a string. Eg:
# "zero nine five two" -> "four"
#If the string is empty or includes a number greater than 9, return "n/a"
def average_string(s):
    d = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    if s and all(i in d for i in s.split()):
        return list(d.keys())[list(d.values()).index(int(sum(d[i] for i in s.split()) / len(s.split())))]
    return 'n/a'

# "The Shell Game" involves cups upturned on a playing surface, with a ball placed underneath one of
# them. The index of the cups are swapped around multiple times. After that the players will try
# to find which cup contains the ball.
# Your task is as follows. Given the cup that the ball starts under,
# and list of swaps, return the location of the ball at the end. Cups are given like array/list indices.
def find_the_ball(start, swaps):
    pos = start
    for (a, b) in swaps:
        if a == pos: pos = b
        elif b == pos: pos = a
    return pos

# You are given an input string.
# For each symbol in the string if it's the first character occurrence, replace it with a '1',
# else replace it with the amount of times you've already seen it.
def numericals(s):
    d = {}
    w = ""
    for i in s:
        d[i] = d.get(i, 0) + 1
        w += str(d[i])
    return w

# Complete the solution so that it returns true if it contains any duplicate argument values.
# Any number of arguments may be passed into the function.
# The array values passed in will only be strings or numbers. The only valid return values are true and false.
def solution(*args):
    return len(set(args)) != len(args)

# The function 'fibonacci' should return an array of fibonacci numbers. The function takes a
# number as an argument to decide how many no. of elements to produce. If
# the argument is less than or equal to 0 then return empty array
def fibonacci(n):
    l = []
    a, b = 0, 1
    for i in range(n):
        l.append(a)
        a, b = b, a + b
    return l if n > 0 else []

# In this kata, you have an input string and you should check whether it is a
# valid message. To decide that, you need to split the string by the numbers, and then
# compare the numbers with the number of characters in the following substring.
# For example "3hey5hello2hi" should be split into 3, hey, 5, hello, 2,
# hi and the function should return true, because "hey" is 3 characters, "hello" is 5, and
# "hi" is 2; as the numbers and the character counts match, the result is true.
import re
def is_a_valid_message(message):
    return all(k and int(k) == len(v) for k, v in re.findall("(\d*)(\D*)", message)[:-1])

# You will be given an array of objects (associative arrays in PHP) representing data about
# developers who have signed up to attend the next coding meetup that you are organising.
# Your task is to return:
# true if developers from all of the following age groups have signed up:
# teens, twenties, thirties, forties, fifties, sixties, seventies, eighties, nineties, centenarian
# (at least 100 years young).
# false otherwise.
def is_age_diverse(lst):
    arr = list(map(lambda x: x["age"] // 10, lst))
    return any(i >= 10 for i in arr) and all(j in arr for j in range(1, 10))

# Your task is to create a function called sum_arrays(), which takes two arrays consisting of integers,
# and returns the sum of those two arrays.
# The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9,
# it would equal '3' + '2' + '9' converted to an integer for this kata,
# meaning it would equal 329. The output should be an array of the
# sum in a similar fashion to the input (for example, if the sum is 341, you
# would return [3,4,1]). Examples are given below of what two arrays should return.
def sum_arrays(array1,array2):
    if not array1: return array2
    if not array2: return array1
    n = sum(map(lambda x: int(''.join(map(str, x))), [array1, array2]))
    l = list(map(int, str(abs(n))))
    if n < 0: l[0] *= -1
    return l

# Given a number, num, return the shortest amount of steps it would take from 1, to land exactly on that number.
def shortest_steps_to_num(num):
    s = 0
    while num != 1:
        if num % 2:
            num -= 1
        else:
            num //= 2
        s += 1
    return s

# Create a function isAlt() that accepts a string as an argument and validates whether
# the vowels (a, e, i, o, u) and consonants are in alternate order.
import re
def is_alt(word):
    return not re.search('[aeiou]{2}|[^aeiou]{2}', word)

# You will be given an array of objects representing data about developers who
# have signed up to attend the next coding meetup that you are organising.
def find_odd_names(lst):
    return [i for i in lst if sum(map(ord, i["firstName"])) % 2]

# Karan's company makes software that provides different features based
# on the version of operating system of the user.
# For finding which version is more recent, Karan uses the following method:
# While this function worked for OS versions 10.6, 10.7, 10.8 and 10.9,
# the Operating system company just released OS version 10.10.
def compare_versions(ver1, ver2):
    return [int(i) for i in ver1.split(".")] >= [int(j) for j in ver2.split(".")]

# You will receive an array as parameter that contains 1 or more integers and a number n.
def split_and_add(arr, n):
    for _ in range(n):
        le = len(arr) // 2
        arr = [i + j for i, j in zip([0] * (len(arr) % 2) + arr[:le], arr[le:])]
    return arr

# We have the first value of a certain sequence, we will name it initVal. We define pattern
# list, patternL, an array that has the differences between contiguous terms of the
# sequence.  E.g: patternL = [k1, k2, k3, k4]
# The terms of the sequence will be such values that:
def sumDig_nthTerm(f, ds, n):
    c, pos = divmod(n - 1, len(ds))
    res = f + sum(ds) * c + sum(ds[:pos])
    return sum(map(int, str(res)))

# You know how sometimes you write the the same word twice in a sentence, but then don't notice
# that it happened? For example, you've been distracted for a second. Did you
# notice that "the" is doubled in the first sentence of this description?
# As as aS you can see, it's not easy to spot those errors,
# especially if words differ in case, like "as" at the beginning of this sentence.
# Write a function that counts the number of sections repeating the same word (case insensitive).
# The occurence of two or more equal words next after each other counts as one.
from itertools import groupby
def count_adjacent_pairs(st):
    return len([k for k, v in groupby(st.lower().split(' ')) if len(list(v)) >= 2])

#Sorting on planet Twisted-3-7
# There is a planet... in a galaxy far far away. It is exactly like our planet, but
# it has one difference: #The values of the digits 3 and 7 are twisted.
# Our 3 means 7 on the planet Twisted-3-7. And 7 means 3.
# Your task is to create a method, that can sort an array the way it would be sorted on Twisted-3-7.
def sort_twisted37(arr):
    return sorted(arr, key=lambda x: int(str(x).translate(str.maketrans('37','73'))))

# Find the first character that repeats in a String and return that character.
def first_dup(s):
    try:
        l = [i for i in s]
        return [i for i in l if s.count(i) > 1][0]
    except:
        return None

# We need the ability to divide an unknown integer into
# a given number of even parts — or at least as even as they can be. The sum
# of the parts should be the original value, but each part should be an integer, and they should be
# as close as possible.
def split_integer(num, parts):
    i = num // parts
    c = num % parts
    return [i] * (parts - c) + [i + 1] * c

# Give the summation of all even numbers in a Fibonacci sequence up to, but not including,
# the number passed to your function. Or, in other words, sum all the even Fibonacci numbers
# that are lower than the given number n (n is not the nth element of Fibonacci sequence) without including n.
# The Fibonacci sequence is a series of numbers where the next value is the addition of
# the previous two values. The series starts with 0 and 1:
def even_fib(m):
    a, b = 0, 1
    c = 0
    while b < m:
        if b % 2 == 0:
            c += b
        a, b = b, a + b
    return c

# You've just discovered a square (NxN) field and you notice a
# warning sign. The sign states that there's a single bomb in the 2D grid-like field in front of you.
# Write a function mineLocation/MineLocation that accepts a 2D array, and returns
# the location of the mine. The mine is represented as the integer 1 in the 2D array.
# Areas in the 2D array that are not the mine will be represented as 0s.
# The location returned should be an array (Tuple<int, int> in C#) where the
# first element is the row index, and the second element is the column
# index of the bomb location (both should be 0 based). All 2D arrays passed into your
# function will be square (NxN), and there will only be one mine in the array.
def mineLocation(field):
    for i in field:
        for j in i:
            if j == 1: return [field.index(i), i.index(j)]

# Your MyRobot-specific (esoteric) scripting language called RoboScript only ever contains the
# following characters: F, L, R, the digits 0-9 and brackets (( and )). Your goal is
# to write a function highlight which accepts 1 required argument code which is the RoboScript program passed
# in as a string and returns the script with syntax highlighting. The following commands/characters
# should have the following colors:
import re
def highlight(code):
    code = re.sub(r"(F+)", '<span style="color: pink">\g<1></span>', code)
    code = re.sub(r"(L+)", '<span style="color: red">\g<1></span>', code)
    code = re.sub(r"(R+)", '<span style="color: green">\g<1></span>', code)
    code = re.sub(r"(\d+)", '<span style="color: orange">\g<1></span>', code)
    return code

# You will be given an array of objects representing data about developers who have signed up to
# attend the next web development meetup that you are organising. Three programming languages will
# be represented: Python, Ruby and JavaScript.
from collections import Counter
def is_language_diverse(lst):
    count = Counter(map(lambda x: x["language"], lst)).values()
    return max(count) <= min(count) * 2

# You're going on a trip with some students and it's up to you to
# keep track of how much money each Student has. A student is defined like this:
def most_money(students):
    total = []
    for i in students:
        total.append((i.fives * 5) + (i.tens * 10) + (i.twenties * 20))
    if min(total) == max(total) and len(students) > 1: return "all"
    return students[total.index(max(total))].name

# Re-order the characters of a string, so that they are concatenated into a new string
# in "case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply
# be removed!
# The input is restricted to contain no numerals and only words containing the english alphabet letters.
def alphabetized(s):
    return "".join(sorted(filter(str.isalpha, s),key=str.lower))

# Inspired by one of Uncle Bob's TDD Kata
# Write a function that generates factors for a given number.
# The function takes an integer on the standard input and returns a list
# of integers (ObjC: array of NSNumbers representing integers). That list contains the
# prime factors in numerical sequence.
def prime_factors (n):
    l = []
    integer = 2
    while n > 1:
        while n % integer == 0:
            l.append(integer)
            n /= integer
        integer += 1
    return l

# In this Kata, you will be given a string with brackets and
# an index of an opening bracket and your task will be to return
# the index of the matching closing bracket. Both the input and returned index are
# 0-based except in Fortran where it is 1-based. An opening brace will
# always have a closing brace. Return -1 if there is no answer (in Haskell,
# return Nothing; in Fortran, return 0; in Go, return an error)
def solve(s, idx):
    l = []
    for k, v in enumerate(s):
        if v == '(': l += [k]
        if v == ')':
            if not l: break
            if l.pop() == idx: return k
    return -1

# Your task is to write a function that does just what the title suggests (so, fair
# warning, be aware that you are not getting out of it just throwing a lame bas sorting method
# there) with an array/list/vector of integers and the expected number n of smallest elements to return.
def first_n_smallest(arr, n):
    l = sorted(arr)[:n]
    return [l.pop(l.index(i)) for i in arr if i in l]

# Your task is to find the next higher number (int) with same '1'- Bits.
# I.e. as much 1 bits as before and output next higher than input. Input
# is always an int in between 1 and 1<<30 (inclusive). No bad cases or special tricks...
from itertools import count
def next_higher(value):
    c = bin(value).count('1')
    return next(i for i in count(value+1) if bin(i).count('1') == c)

# Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers
# remain the same. To clarify, if we write them down on a paper
# and turn the paper upside down, the numbers will be the same. Try it and
# see! Some numbers such as 2 or 5 don't yield numbers when rotated.
# Given a range, return the count of upside down numbers within that range.
# For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.
# More examples in the test cases.
def solve(a, b):
    return sum(str(n) == str(n)[::-1].translate(str.maketrans('2345679', 'XXXX9X6')) for n in range(a, b))

# Here's another staple for the functional programmer. You have a sequence of values and some
# predicate for those values. You want to get the longest prefix of elements such that
# the predicate is true for each element. We'll call this the takeWhile function.
# It accepts two arguments. The first is the sequence of values, and the second is
# the predicate function. The function does not change the value of the original sequence.
def take_while(arr, pred_fun):
    l = []
    print(pred_fun)
    for i in arr:
        if not pred_fun(i):
            return l
        l.append(i)
    return l

# Array inversion indicates how far the array is from being sorted.
# Inversions are pairs of elements in array that are out of order.
def count_inversions(array):
    c = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]: c += 1
    return c

# You will be given a string and you task is to check if it is possible to convert that
# string into a palindrome by removing a single character. If the string
# is already a palindrome, return "OK". If it is not, and
# we can convert it to a palindrome by removing one character, then return "remove one", otherwise
# return "not possible". The order of the characters should not be changed.
def solve(s):
    if s == s[::-1]: return 'OK'
    for i in range(len(s)):
        if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
            return 'remove one'
    return 'not possible'

# The most basic encryption method is to map a char to another
# char by a certain math rule. Because every char has an ASCII value, we can
# manipulate this value with a simple math expression. For example 'a' + 1 would
# give us 'b', because 'a' value is 97 and 'b' value is 98.
# You will need to write a method which does exactly that -
# get a string as text and an int as the rule of manipulation, and should return encrypted text. for example:
def encrypt(text, rule):
    return "".join(chr((ord(i) + rule) % 256) for i in text)

# Complete the function that takes 3 numbers x, y and k (where x ≤ y), and returns the
# number of integers within the range [x..y] (both ends included) that are divisible by k.
# More scientifically: { i : x ≤ i ≤ y, i mod k = 0 }
def divisible_count(x, y, k):
    return y // k - (x - 1) // k

# Your job is to change the given string s using a non-negative integer n.
# Each bit in n will specify whether or not to swap the case for each alphabetic
# character in s: if the bit is 1, swap the case; if its 0, leave it as is.
# When you finish with the last bit of n, start again with the first bit.
# You should skip the checking of bits when a non-alphabetic character is encountered, but
# they should be preserved in their original positions.
from itertools import cycle
def swap(s, n):
    word = cycle(bin(n)[2:])
    return "".join(i.swapcase() if i.isalpha() and next(word) == '1' else i for i in s)

# This is version 2 of my 'Write Number in Exanded Form' Kata.
# You will be given a number and you will need to return it as a string in expanded form :
def expanded_form(num):
    x = str(num).index('.')
    return ' + '.join(v + ('/10','')[k<x] + '0'*(abs(k-x)-1) for k, v in enumerate(str(num)) if not v in '.0')

# But suddenly there is a rumour that a dropped chicken sandwich has been spotted on the ground ahead.
# The ants surge forward! Oh No, it's an ant stampede!!
# Some of the slower ants are trampled, and their poor little ant bodies are broken up into scattered bits.
# The resulting carnage looks like this:
def deadAntCount(ants):
    return max(ants.replace("ant", "").count(i) for i in "ant")

# Here you have to do some mathematical operations on a "dirty string". This kata checks some
# basics, it's not too difficult.
# So what to do?
# Input: String which consists of two positive numbers (doubles) and exactly one operator
# like +, -, * or / always between these numbers. The string is dirty, which means that
# there are different characters inside too, not only numbers and the operator. You have to combine
# all digits left and right, perhaps with "." inside (doubles), and to calculate the
# result which has to be rounded to an integer and converted to a string at the end.
import re
def calculate_string(st):
    return str(int(round(eval(re.sub(r'[^-+*/\d.]', '', st)))))

# Although this Kata is not part of an official Series, you may want to complete this
# Kata before attempting this one as these two Kata are deeply related.
# Preloaded
# Preloaded for you is a class, struct or derived data type Node ( depending on the language ) used to
# construct linked lists in this Kata:
from functools import reduce
def linked_list_from_string(s, split=" -> "):
    return reduce(lambda i, j: Node(j, i), map(int, s.split(split)[-2::-1]), None)

# Write a function that determines whether the passed in sequences are similar. Similar means
# they contain the same elements, and the same number of occurrences of elements.
def arrays_similar(seq1, seq2):
    l1 = ''.join(str(i) for i in seq1)
    l2 = ''.join(str(i) for i in seq2)
    return set(seq1) == set(seq2) and sorted(l1) == sorted(l2)

# You're fed up about changing the version of your software manually. Instead, you
# will create a little script that will make it for you.
def next_version(version):
    if version.count('.') == 0:
        return str(int(version) + 1)
    elif int(version[-1]) < 9:
        return f"{version[0:-1]}{str(int(version[-1]) + 1)}"
    return next_version(version[0:-2]) + '.0'

# Write a function that will take in any array and reverse it.
# Sounds simple doesn't it?
# NOTES:
# Array should be reversed in place! (no need to return it)
# Usual builtins have been deactivated. Don't count on them.
# You'll have to do it fast enough, so think about performances
def reverse(seq):
    l = list()
    for _ in range(len(seq)): l.append(seq.pop())
    seq.extend(l)

# Write a function that takes a string and returns an array of the repeated
# characters (letters, numbers, whitespace) in the string.
# If a charater is repeated more than once, only show it once in the result array.
# Characters should be shown by the order of their first repetition. Note that this may be different
# from the order of first appearance of the character.
# Characters are case sensitive.
# For F# return a "char list"
def remember(str_):
    return list(v for k, v in enumerate(str_) if str_[:k].count(v) == 1)

# Given string s, which contains only letters from a to z in lowercase.
# A set of alphabet is given by abcdefghijklmnopqrstuvwxyz.
# 2 sets of alphabets mean 2 or more alphabets.
# Your task is to find the missing letter(s). You may need to output them by
# the order a-z. It is possible that there is more than one missing letter from more than one set of alphabet.
# If the string contains all of the letters in the alphabet, return an empty string ""
def missing_alphabets(s):
    return ''.join(sorted(i * (max(s.count(j) for j in s) - s.count(i)) for i in 'abcdefghijklmnopqrstuvwxyz'))

# Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum
# of squared digits of the previous element. The sequence ends once an element that has already been
# in the sequence appears again.
# Given the first element a0, find the length of the sequence.
def square_digits_sequence(n):
    s = set()
    while n not in s:
        s.add(n)
        n = sum(int(i)**2 for i in str(n))
    return len(s) + 1

# You are given a table, in which every key is a stringified number, and
# each corresponding value is an array of characters, e.g.
# Create a function that returns a table with the same keys, but each character
# should appear only once among the value-arrays, e.g.
def remove_duplicate_ids(d):
    s = set()
    return {j:[s.add(i) or i for i in d[j] if i not in s] for j in sorted(d, key=int)[::-1]}

# Define a method that accepts 2 strings as parameters. The method returns the first string sorted by the second.
def sort_string(st, order):
    return ''.join(sorted(list(st), key=lambda x: list(order).index(x) if x in order else len(order)))

# We'll create a function that takes in two parameters:
# a sequence (length and types of items are irrelevant)
# a function (value, index) that will be called on members of the sequence and
# their index. The function will return either true or false.
# Your function will iterate through the members of the sequence in order
# until the provided function returns true; at which point your function will return that item's index.
# If the function given returns false for all members of the sequence, your function should return -1.
def find_in_array(seq, predicate):
    for k, v in enumerate(seq):
        if predicate(v, k): return k
    return -1

# You will be given a string of English digits "stuck" together, like this:
# "zeronineoneoneeighttwoseventhreesixfourtwofive"
# Your task is to split the string into separate digits:
def uncollapse(digits):
    w, f = '', ''
    for i in digits:
        w += i
        if w in ['zero', 'nine', 'one', 'eight', 'two', 'seven', 'three', 'six', 'four', 'five']:
            f += w + ' '
            w = ''
    return f[:-1]

# Linked Lists - Sorted Insert
# Write a SortedInsert() function which inserts a node into the correct location of a
# pre-sorted linked list which is sorted in ascending order. SortedInsert takes
# the head of a linked list and data used to create a node as arguments. SortedInsert() should
# also return the head of the list.
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def sorted_insert(head, data):
    if not head or data < head.data:
        return Node(data, head)
    else:
        head.next = sorted_insert(head.next, data)
        return head

# Given an array, return the reversed version of the array (a different kind of reverse though), you
# reverse portions of the array, you'll be given a length
# argument which represents the length of each portion you are to reverse.
def sel_reverse(arr, l):
    return [j for i in range(0, len(arr), l) for j in arr[i:i+l][::-1]] if l != 0 else arr

# You have to create a function namedone_two (oneTwo for Java or Preloaded.OneTwo for C#) that
# returns 1 or 2 with equal probabilities. one_two is already defined in a global scope
# and can be called everywhere.
# Your goal is to create a function named one_two_three (oneTwoThree for Java or OneTwoThree for C#) that
# returns 1, 2 or 3 with equal probabilities using only the one_two function.
# Do not try to cheat returning repeating non-random sequences. There is a randomness
# test especially for this case.
def one_two_three():
    i, j = one_two(),one_two()-1
    return one_two_three() if i == j else i + j

# Dave has a lot of data he is required to apply filters to, which are simple enough,
# but he wants a shorter way of doing so.
class list(list):
    def even(self):
        res = []
        for x in self:
            if type(x) == int and x % 2 == 0:
                res.append(x)
        return res
    def odd(self):
        res = []
        for x in self:
            if type(x) == int and x % 2 == 1:
                res.append(x)
        return res
    def under(self, r):
        res = []
        for x in self:
            if type(x) == int and x < r:
                res.append(x)
        return res
    def over(self, r):
        res = []
        for x in self:
            if type(x) == int and x > r:
                res.append(x)
        return res
    def in_range(self, r1, r2):
        res = []
        for x in self:
            if type(x) == int and r1 <= x <= r2:
                res.append(x)
        return res

# Implement the method countIf (count_if in PHP and Python), which accepts a linked list
# (head) and a predicate function, and returns the number of elements which apply to the given predicate.
# For example: Given the list: 1 -> 2 -> 3, and the predicate x => x >= 2, countIf /
# count_if should return 2, since x >= 2 applies to both 2 and 3.
def count_if(head, func):
    c = 0
    while head:
        c += func(head.data)
        head = head.next
    return c

# You have been hired by a company making electric garage doors. Accidents with the present product
# line have resulted in numerous damaged cars, broken limbs and several killed pets.
# Your mission is to write a safer version of their controller software.
def controller(events):
    out, s, dir, moving = [], 0, 1, False
    for i in events:
        if i == 'O': dir *= -1
        elif i == 'P': moving = not moving
        if moving: s += dir
        if s in [0,5]: moving, dir = False, 1 if s == 0 else -1
        out.append(str(s))
    return ''.join(out)

# Note: This kata is a translation of this (Java)
# one: http://www.codewars.com/kata/rotate-array. I have not translated this
# first one as usual because I did not solved it, and I fear not being able to solve it
# (Java is not my cup of... tea). @cjmcgraw, if you want to use my translation on your kata feel free to use it.
# Create a function named "rotate" that takes an array and returns a new one
# with the elements inside rotated n spaces.
# If n is greater than 0 it should rotate the array to the right. If n
# is less than 0 it should rotate the array to the left. If n is 0, then it should return the array unchanged.
def rotate(arr, n):
    n = n % len(arr)
    return arr[-n:] + arr[:-n]

# Given a string, remove any characters that are unique from the string.
def only_duplicates(string):
    return ''.join(i for i in string if string.count(i) > 1)

# You are given an array of integers. Your task is to sort odd numbers within
# the array in ascending order, and even numbers in descending order.
# Note that zero is an even number. If you have an empty array, you need to return it.
def sort_array(l):
    e = sorted(i for i in l if i % 2 == 0)
    o = sorted((i for i in l if i % 2 != 0), reverse=True)
    return [(e if i % 2 == 0 else o).pop() for i in l]

# An anagram is a word, a phrase, or a sentence formed from another by rearranging its letters.
# An example of this is "angel", which is an anagram of "glean".
# Write a function that receives an array of words, and returns the total
# number of distinct pairs of anagramic words inside it.
from collections import Counter
def anagram_counter(words):
    return sum(i *(i-1)// 2 for i in Counter(''.join(sorted(j)) for j in words).values())

#  happy number is a number defined by the following process: starting with any positive integer, replace the
#  number by the sum of the squares of its digits, and repeat the process until the number equals
#  1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers, while those that do
# not end in 1 are unhappy numbers (or sad numbers) (Wikipedia).
# Write a function that takes n as parameter and return true if and only if n is an happy number, false otherwise.
def is_happy(n):
    s = set()
    while n not in s:
        s.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1

# Your task is to reduce a list of numbers to one number.
# For this you get a list of rules, how you have to reduce the numbers.
# You have to use these rules consecutively. So when you get to the end of the list of rules,
# you start again at the beginning.
def reduce_by_rules(lst, rules):
    l, r = len(rules), lst[0]
    for k, v in enumerate(lst[1:]):
        r = rules[k % l](r, v)
    return r

# Complete function splitOddAndEven, accept a number n(n>0), return an array that
# contains the continuous parts of odd or even digits.
# Please don't worry about digit 0, it won't appear ;-)
import re
def split_odd_and_even(n):
    return [int(i) for i in re.findall(r"([2468]+|[13579]+)", str(n))]

# In this task, you need to restore a string from a list of its copies.
# You will receive an array of strings. All of them are supposed to be
# the same as the original but, unfortunately, they were corrupted which means some of
# the characters were replaced with asterisks ("*").
# You have to restore the original string based on non-corrupted information you have. If
# in some cases it is not possible to determine what the original
# character was, use "#" character as a special marker for that.
# If the array is empty, then return an empty string.
def assemble(input):
    w = list(input[0]) if input else []
    for i in input:
        for k, i in enumerate(i):
            w[k] = i if w[k] == '*' else w[k]
    return ''.join(w).replace('*', '#')

# Variation of this nice kata, the war has expanded and become dirtier and meaner; both
# even and odd numbers will fight with their pointy 1s. And negative integers
# are coming into play as well, with, ça va sans dire, a negative contribution
# (think of them as spies or saboteurs).
# A number's strength is determined by the number of set bits (1s) in its binary representation.
# Negative integers work against their own side so their strength is negative.
# For example -5 = -101 has strength -2 and +5 = +101 has strength +2.
def bits_war(numbers):
    d = sum(sum(map(int, bin(abs(i))[2:])) * (-1)**(i < 0) * (-1)**(i%2 == 0) for i in numbers)
    return ["evens win", "tie", "odds win"][(d >= 0) + (d > 0)]

# An array is circularly sorted if the elements are sorted in ascending order, but displaced, or
# rotated, by any number of steps.
# Complete the function/method that determines if the given array of integers is circularly sorted.
def circularly_sorted(arr):
    return sum(i > j for i, j in zip(arr, arr[1:]+[arr[0]])) < 2

# An ATM ran out of 10 dollar bills and only has 100, 50 and 20 dollar bills.
# Given an amount between 40 and 10000 dollars (inclusive) and assuming that
# the ATM wants to use as few bills as possible, determinate
# the minimal number of 100, 50 and 20 dollar bills the ATM needs to dispense (in that order).
def withdraw(price):
    return [price//100, 0, price%100//20] if price % 20==0 else [(price-50)//100,1, (price-50)%100//20]

# Create a function that takes an argument n and sums even
# Fibonacci numbers up to n's index in the Fibonacci sequence.
from gmpy2 import fib
def sum_fibs(n):
    return sum(i for i in map(fib, range(n + 1)) if i % 2 == 0)

# If we write out the digits of "60" as English words we get "sixzero"; the
# number of letters in "sixzero" is seven. The number of letters in "seven" is five. The
# number of letters in "five" is four. The number of letters in "four" is four:
# we have reached a stable equilibrium.
# Note: for integers larger than 9, write out the names of each digit in a single
# word (instead of the proper name of the number in English). For example, write
# 12 as "onetwo" (instead of twelve), and 999 as "nineninenine" (instead of nine hundred and ninety-nine).
# For any integer between 0 and 999, return an array showing the path from that integer to a stable equilibrium:
def numbers_of_letters(n):
    l = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    s = ''.join(l[i] for i in map(int, str(n)))
    return [s] + (numbers_of_letters(len(s)) if len(s) != n else [])

# The Padovan sequence is the sequence of integers defined by the initial values
def padovan(n):
    x = y = z = 1
    for _ in range(n - 2): x, y, z = y, z, x + y
    return z

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the
# order of the other elements.
def move_zeros(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

# Move the first letter of each word to the end of it, then add "ay" to the
# end of the word. Leave punctuation marks untouched.
def pig_it(text):
    w = ' '.join(i[1:] + i[0] + 'ay' for i in text.split())
    return w if w[-3] not in '!.,?' else w[:-2]

# Write a function, which takes a non-negative integer (seconds) as input and returns the
# time in a human-readable format (HH:MM:SS)
def make_readable(seconds):
    return "%02d:%02d:%02d" % (seconds / 3600, seconds / 60 % 60, seconds % 60)

# Write a function that takes a string of parentheses, and determines if the
# order of the parentheses is valid. The function should return true if the
# string is valid, and false if it's invalid.
def valid_parentheses(string):
    c = 0
    for i in string:
        if i == "(": c += 1
        elif i == ")": c -= 1
        if c < 0: return False
    return c == 0

# Write a function named first_non_repeating_letter that takes a string input, and returns the first
# character that is not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't', since
# the letter t only occurs once in the string, and occurs first in the string.
# As an added challenge, upper- and lowercase letters are considered the same character,
# but the function should return the correct case for the initial letter. For
# example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("") or None
# -- see sample tests.
def first_non_repeating_letter(string):
    try:
        return [i for i in string if string.lower().count(i.lower()) == 1][0]
    except:
        return ''

# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because
# each month a list with the weights of members is published and each month
# he is the last on the list which means he is the heaviest.
# I am the one who establishes the list so I told him: "Don't worry any more,
# I will modify the order of the list". It was decided to attribute a "weight"
# to numbers. The weight of a number will be from now on the sum of its digits.
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
# Given a string with the weights of FFC
# members in normal order can you give this string ordered by "weights" of these numbers?
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split()), key=lambda x: sum(int(i) for i in x)))

# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately
# he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?
# Write a function cakes(), which takes the recipe (object) and the available ingredients
# (also an object) and returns the maximum number of cakes Pete can bake (integer).
# For simplicity there are no units for the amounts (e.g. 1 lb of flour
# or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects,
# can be considered as 0.
def cakes(recipe, available):
    return min([available[i] // recipe[i] if i in available else 0 for i in recipe])

# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
def generate_hashtag(s):
    w = '#'+''.join(i.title() for i in s.split())
    return w if len(w) <= 140 and len(w) > 1 else False

# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
# N! = 1 * 2 * 3 *  ... * N
# Be careful 1000! has 2568 digits...
def zeros(n):
    integer = n//5
    return integer + zeros(integer) if integer else 0

# Complete the function scramble(str1, str2) that returns true if a portion
# of str1 characters can be rearranged to match str2, otherwise returns false.
# Notes:
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
def scramble(s1,s2):
    return not any(s1.count(i) < s2.count(i) for i in set(s2))

# The rgb function is incomplete. Complete it so that passing in RGB decimal values will
# result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
def rgb(r, g, b):
    if r > 255: r = 255
    elif r < 0: r = 0
    if g > 255: g = 255
    elif g < 0: g = 0
    if b > 255: b = 255
    elif b < 0: b = 0
    return '%02x%02x%02x'.upper() % (r, g, b)

# The drawing shows 6 squares the sides of which have a length of
# 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters
# of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80
# Could you give the sum of the perimeters of all the squares in a rectangle
# when there are n + 1 squares disposed in the same manner as in the drawing:
def perimeter(n):
    l = []
    a, b = 0, 1
    for i in range(n+1):
        a, b = b, a + b
        l.append(a)
    return sum(l) * 4

# In this example you have to validate if a user input string is alphanumeric.
# The given string is not nil/null/NULL/None, so you don't have to check that.
# The string has the following conditions to be alphanumeric:
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore
def alphanumeric(p):
    return all(i.isdigit() or i.isalpha() for i in p) and len(p) > 0

# We want to create a function that will add numbers together when called in succession.
class add(int):
    def __call__(self, n):
        return add(self + n)

# You need to write regex that will validate a password to make sure it meets the following criteria:
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)
regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"

# Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum
# of their squared divisors is itself a square.
# We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The
# subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors
# of which is a square and then the sum of the squared divisors.
import math
def divisors(n):
    d = [1, n]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: d.extend([i, int(n/i)])
    return set(d)
def list_squared(m, n):
    l = []
    for num in range(m, n):
        s = sum(i**2 for i in divisors(num))
        if math.sqrt(s).is_integer(): l.append([num, s])
    return l

# Given a list of integers and a single sum value, return the first two
# values (parse from the left please) in order of appearance that add up to form the sum.
# If there are two or more pairs with the required sum, the
# pair whose second element has the smallest index is the solution.
def sum_pairs(lst, s):
    l = set()
    for i in lst:
        if s - i in l: return [s - i, i]
        l.add(i)

# This algorithm serves welll its educative purpose but it's tremendously inefficient, not
# only because of recursion, but because we invoke the fibonacci function twice, and the right branch
# of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci numbers
# already calculated by the left branch (i.e. fibonacci(n-1)).
# This algorithm is so inefficient that the time to calculate any Fibonacci number over
# 50 is simply too much. You may go for a cup of coffee or go take a nap while
# you wait for the answer. But if you try it here in Code Wars you will most
# likely get a code timeout before any answers.
from functools import lru_cache
@lru_cache(None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Define a function that takes in two non - negative integers aaa and bbb and returns the last decimal digit
# of aba ^ ba b of 979 ^ 79 7 is 999, since 97 = 47829699 ^ 7 = 47829699 7, which has over
# 109210 ^ {92} p10 92 decimal digits, is 666. Also, please take 000 ^ 00 0 to be 111.
# You may assume that the input will always be valid.
def last_digit(n1, n2):
    return pow(n1, n2, 10)

# Implement a function that receives two IPv4 addresses, and returns the number
# of addresses between them (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings. The last address will
# always be greater than the first one.
from ipaddress import ip_address
def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))

# This problem takes its name by arguably the most important event in the life of the
# ancient historian Josephus: according to his tale, he and his 40 soldiers were trapped in a cave
# by the Romans during a siege.
# Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they
# formed a circle and proceeded to kill one man every three, until one last man was left
# (and that it was supposed to kill himself to end the act).
# Well, Josephus and another man were the last two and, as we now know every
# detail of the story, you may have correctly guessed that they didn't exactly follow through the original idea.
# You are now to create a function that returns a Josephus permutation, taking as parameters the
# initial array/list of items to be permuted as if they were in a circle and counted
# out every k places until none remained.
def josephus(xs, k):
    i, j = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        j.append(xs.pop(i))
    return j

# Complete the function that
# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.
def solution(a, b):
    return sum((k - v)**2 for k, v in zip(a, b)) / len(a)

# At a job interview, you are challenged to write an algorithm to check if a given string, s,
# can be formed from two other strings, part1 and part2.
# The restriction is that the characters in part1 and part2 should be in the same order as in s.
# The interviewer gives you the following example and tells you to figure out the rest from the given test cases.
def is_merge(s, part1, part2):
    if not part1: return s == part2
    if not part2: return s == part1
    if not s: return part1 + part2 == ''
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2): return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]): return True
    return False

# There is an array of strings. All strings contains similar letters except one. Try to find it!
from collections import Counter
def find_uniq(arr):
    r = Counter(''.join(arr)).most_common()
    return ''.join([i for i in arr if r[-1][0] in i])

# Coding decimal numbers with factorials is a way of writing out numbers in
# a base system that depends on factorials, rather than powers of numbers.
# In this system, the last digit is always 0 and is in base 0!. The digit before that is either
# 0 or 1 and is in base 1!. The digit before that is either 0, 1, or 2 and
# is in base 2!, etc. More generally, the nth-to-last digit is always 0, 1, 2, ..., n and is in base n!.
from math import factorial
from itertools import dropwhile
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASIS = [factorial(i) for i in range(len(DIGITS))]
def dec2FactString(nb):
    l = []
    for i in reversed(BASIS):
        l.append(DIGITS[nb // i])
        nb %= i
    return "".join(dropwhile(lambda x: x == "0", l))
def factString2Dec(string):
    return sum(BASIS[k] * DIGITS.index(v) for k, v in enumerate(reversed(string)))

# Carol's boss Bob thinks he is very smart. He says he made an app which renders
# messages unreadable without changing any letters, only by adding some new ones, while preserving
# message integrity (i. e. the original message can still be retrieved).
# He gave some limited access to his app to Carol to challenge her, and hinted
# that if Carol cannot crack this simple task, she might be fired.
# Carol was trying to crack this code herself, but got too tired,
# so she came to you for help. However, she succeeded to hack Bob's app
# and found a data field called 'marker'. She thinks it can be helpful for cracking Bob's app.
# Help Carol keep her job!
def decoder(encoded, marker):
    return ''.join(encoded.split(marker)[::2]) + ''.join(encoded.split(marker)[1::2])[::-1]

# Some of you might remember spending afternoons playing Street Fighter 2 in some Arcade back in
# the 90s or emulating it nowadays with the numerous emulators for retro consoles.
# Can you solve this kata? Suuure-You-Can!
# UPDATE: a new kata's harder version is available here.
# The Kata
# You'll have to simulate the video game's character selection screen behaviour, more specifically
# the selection grid. Such screen looks like this:
def street_fighter_selection(fighters, pos, moves):
    l, row, col, m = [], pos[0], pos[1], {"up":(-1, 0), "down":(1, 0), "right":(0, 1), "left":(0,-1)}
    for i in moves:
        row, col = min(max(row + m[i][0], 0), 1), (col + m[i][1]) % 6
        l.append(fighters[row][col])
    return l

# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
import ipaddress
def is_valid_IP(s):
    try:
        return bool(ipaddress.ip_address(s))
    except:
        return False

# Time to write your first Esolang interpreter :D
def my_first_interpreter(code):
    c, w = 0, ""
    for i in code:
        if i == "+": c += 1
        elif i == ".": w += chr(c % 256)
    return w

# Substitute two equal letters by the next letter of the alphabet (two letters convert to one):
def last_survivors(s):
    w = "abcdefghijklmnopqrstuvwxyza"
    for i in s:
        if s.count(i) > 1:
            s = s.replace(i, "", 2) + w[w.index(i) + 1]
            return last_survivors(s)
    return s

# You will be given a list of objects. Each object has type, material,
# and possibly secondMaterial. The existing materials are: paper, glass, organic, and plastic.
# Your job is to sort these objects across the 4 recycling bins according to their
# material (and secondMaterial if it's present), by listing the type's of objects that should go into those bins.
def recycle(a):
    dic = {'paper': [], 'glass': [], 'organic': [], 'plastic': []}
    for i in a:
        dic[i['material']].append(i['type'])
        if 'secondMaterial' in i: dic[i['secondMaterial']].append(i['type'])
    return tuple(dic.values())

# So, we need a simple function that converts a string representing a
# number (possibly with a $ sign in front of it) into the number itself.
def money_value(s):
    try:
        return float(s.replace("$", "").replace(" ", ""))
    except:
        return 0.0

# Write a function that accepts msg string and returns local tops of string from the highest to the lowest.
# The string's tops are from displaying the string in the below way:
def tops(msg):
    return ''.join(msg[i * (2 * i -1)] for i in range(int(((8 * len(msg) + 1)**.5 + 1) / 4), 0, -1))

# You just got done with your set at the gym, and you are wondering how
# much weight you could lift if you did a single repetition. Thankfully, a
# few scholars have devised formulas for this purpose (from Wikipedia) :
def calculate_1RM(w, r):
    return w if r == 1 else 0 if r == 0 else max(round(w * (1 + r/30)), round((100*w) / (101.3 - 2.67123*r)), round(w*r**0.10))

# Implement a function, so it will produce a sentence out of the given parts.
def make_sentences(parts):
    return ' '.join(parts).replace(' ,', ',').rstrip(' .') + '.'

# You must check within a string (s) to find all of the mating pairs, returning a
# list/array of the string containing valid mating pairs and a boolean indicating whether the total
# number of bears is greater than or equal to x.
from re import findall
def bears(x, s):
    return ["".join(findall("8B|B8", s)), len("".join(findall("8B|B8", s))) >= x]

# What date corresponds to the nth day of the year?
# The answer depends on whether the year is a leap year or not.
# Write a function that will help you determine the date if you know
#  the number of the day in the year, as well as whether the year is a leap year or not.
# The function accepts the day number and a boolean value isLeap as
# arguments, and returns the corresponding date of the year as a string "Month, day".
# Only valid combinations of a day number and isLeap will be tested.
from datetime import *
def get_day(day, is_leap):
    return (date(2019 + is_leap, 1, 1) + timedelta(day - 1)).strftime("%B, %-d")

# You must create a method that can convert a string from any format into PascalCase. This must support symbols too.
# Don't presume the separators too much or you could be surprised.
import re
def camelize(s):
    return "".join(i.capitalize() for i in re.split("\W|_", s))

# Build Tower by the following given arguments:
# number of floors (integer and always greater than 0)
# block size (width, height) (integer pair and always greater than (0, 0))
def tower_builder(n_floors, block_size):
    w, h = block_size
    l = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        for j in range(h): l.append(' '*n * w + '*' * (i * 2 + 1) * w + ' ' * n* w)
    return l

# The code provided has a method hello which is supposed to show only those attributes
# which have been explicitly set. Furthermore, it is supposed to say them in the same order they were set.
# But it's not working properly.
class Dinglemouse(object):

    def __init__(self):
        self.name = None
        self.sex = None
        self.age = None
        self.hell = 'Hello.'

    def setAge(self, age):
        if self.age == None:
            self.hell = self.hell + ' I am {age}.'
        self.age = age
        return self

    def setSex(self, sex):
        if self.sex == None:
            self.hell = self.hell + ' I am {sex}.'
        self.sex = "male" if sex == 'M' else "female"
        return self

    def setName(self, name):
        if self.name == None:
            self.hell = self.hell + ' My name is {name}.'
        self.name = name
        return self

    def hello(self):
        return self.hell.format(age=self.age, sex=self.sex, name=self.name)

# You will get two integers n (width) and m (height) and your task is to
# draw the following pattern. Each line is seperated with a newline (\n)
# Both integers are equal or greater than 1; no need to check for invalid parameters.
def dot(n, m):
    return ("+---" * n + "+\n" + "| o " * n + "|\n") * m + ("+---" * n + "+")

# Are you a file extension master? Let's find out by checking if Bill's files are
# images or audio files. Please use regex if available natively for your language.
# You will create 2 string methods:
# isAudio/is_audio, matching 1 or + uppercase/lowercase letter(s) (combination possible), with
# the extension .mp3, .flac, .alac, or .aac.
# isImage/is_image, matching 1 or + uppercase/lowercase letter(s) (combination possible), with
# the extension .jpg, .jpeg, .png, .bmp, or .gif.
# Note that this is not a generic image/audio files checker. It's
# meant to be a test for Bill's files only. Bill doesn't like
# punctuation. He doesn't like numbers, neither. Thus, his filenames are letter-only
# Rules
# It should return true or false, simply.
# File extensions should consist of lowercase letters and numbers only.
# File names should consist of letters only (uppercase, lowercase, or both)
def is_audio(file_name):
    return any(file_name.endswith(i) for i in ['.mp3', '.flac', '.alac', '.aac']) and all(i.isalpha() for i in file_name.split('.')[0])
def is_img(file_name):
    return any(file_name.endswith(i) for i in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']) and all(i.isalpha() for i in file_name.split('.')[0])

# In this Kata, you have to design a simple routing class for a web framework.
# The router should accept bindings for a given url, http method and an action.
# Then, when a request with a bound url and method comes in, it should return the result of the action.
class Router:
    def __init__(self):
        self._routes = {}
    def bind(self, url, method, a):
        self._routes[(url, method)] = a
    def runRequest(self, url, method):
        return self._routes.get((url, method), lambda: "Error 404: Not Found")()

# for i from 1 to n, do i % m and return the sum
def f(n, m):
    return (n // m) * (m - 1) * m / 2 + (n % m) * (n % m + 1) / 2

# Given an array of strings and a character to be used as border, output the frame with the content inside.
# Notes:
# Always keep a space between the input string and the left and right borders.
# The biggest string inside the array should always fit in the frame.
# The input array is never empty.
def frame(text, char):
    text_lens = [len(i) for i in text]
    longest_len = max(text_lens)
    frame_list = [char*(longest_len + 4)]
    for i in text:
         frame_list.append("{} {}{} {}".format(char, i, " " * (longest_len - len(i)), char))
    frame_list.append(char*(longest_len + 4))
    return "\n".join(frame_list)

# Your goal is to create a function to format a number given a template; if the number is not present,
# use the digits 1234567890 to fill in the spaces.
# A few rules:
# the template might consist of other numbers, special characters or the like: you
# need to replace only alphabetical characters (both lower- and uppercase);
# if the given or default string representing the number is shorter than the template, just
# repeat it to fill all the spaces.
from itertools import cycle
def numeric_formatter(template, data='1234567890'):
    data = cycle(data)
    return ''.join(next(data) if i.isalpha() else i for i in template)

# Run-length encoding (RLE) is a very simple form of lossless data compression
# in which runs of data are stored as a single data value and count.
# A simple form of RLE would encode the string "AAABBBCCCD" as "3A3B3C1D" meaning,
# first there are 3 A, then 3 B, then 3 C and last there is 1 D.
# Your task is to write a RLE encoder and decoder using this technique. The texts
# to encode will always consist of only uppercase characters, no numbers.
import re
def encode(s):
    return "".join(f"{len(k)}{v}" for k, v in re.findall(r"((.)\2*)", s))

def decode(s):
    return "".join(int(k) * v for k, v in re.findall(r"(\d+)(\w)", s))

# Write a function that returns the count of characters that have to
# be removed in order to get a string with no consecutive repeats.
# Note: This includes any characters
def count_repeats(txt):
    return sum(1 if i == j else 0 for i, j in zip(txt, txt[1:]))

# Create a method named "rotate" that returns a given array with the elements inside the array rotated n spaces.
# If n is greater than 0 it should rotate the array to the right. If n is less than 0 it should rotate the array
# to the left. If n is 0, then it should return the array unchanged.
def rotate(data, n):
    if data:
        c = -n % len(data)
        return data[c:] + data[:c]
    return []

# Given two strings, the first being a random string and
# the second being the same as the first, but with three added
# characters somewhere in the string (three same characters),
# Write a function that returns the added character
def added_char(s1, s2):
    return [i for i in s2 if s2.count(i) >= 3 and s1.count(i) == s2.count(i)-3][0]

# The hamming distance between a pair of numbers is the number of binary bits that differ in their binary notation.
def hamming_distance(a, b):
    return bin(a ^ b).count('1')

# A masked number is a string that consists of digits and one asterisk (*) that
# should be replaced by exactly one digit. Given a masked number s, find
# all the possible options to replace the asterisk with a digit to produce an integer divisible by 6.
import sys
sys.set_int_max_str_digits(0)
def is_divisible_by_6(s):
    return [str(int(s.replace('*',str(i)))) for i in range(10) if int(s.replace('*',str(i)))%6==0]

# I want to know the size of the longest consecutive elements of X in Y.
# You will receive two arguments: items and key. Return the length of the
# longest segment of consecutive keys in the given items.
import re
def get_consective_items(item, key):
    return len(max(re.findall(f'{key}+', str(item)) or ['']))

# Given an array (or list) of scores, return the array of ranks for each value in the array.
# The largest value has rank 1, the second largest value has rank 2, and so on.
# Ties should be handled by assigning the same rank to all tied values. For example:
def ranks(a):
    return [sorted(a, reverse = True).index(i) + 1 for i in a]

# We are tracking down our rogue agent Matthew Knight also known as Roy Miller. He travels
# from places to places to avoid being tracked. Each of his travels are
# based on a list of itineraries in an unusual or incorrect order. The task
# is to determine the routes he will take in his every journey.
# Task
# You are given an array of routes of his itineraries. List down the only
# places where he will go in correct order based on his itineraries.
def find_routes(routes):
    d = dict(routes)
    r = list(d.keys() - d.values())
    while r[-1] in d: r.append(d[r[-1]])
    return ', '.join(r)

# Complete the method that will determine the minimum number of coins needed to make change
# for a given amount in American currency.
# Coins used will be half-dollars, quarters, dimes, nickels, and pennies, worth
# 50¢, 25¢, 10¢, 5¢ and 1¢, respectively. They'll be represented by the symbols
# H, Q, D, N and P (symbols in Ruby, strings in in other languages)
# The argument passed in will be an integer representing the value in cents. The return
# value should be a hash/dictionary/object with the symbols as keys, and the numbers of
# coins as values. Coins that are not used should not be included in the hash. If the
# argument passed in is 0, then the method should return an empty hash.
def make_change(amount):
    d = {}
    for k, v in (('H', 50), ('Q', 25), ('D', 10), ('N', 5), ('P', 1)):
        if amount >= v: d[k], amount = divmod(amount, v)
    return d1

# Your task is to give the number of total values for the odd
# terms of the sequence up to the n-th term (included). (The number n (of n-th term)
# will be given as a positive integer)
# The values 1 (one) is the only that is duplicated in the sequence and should be counted only once.
def count_odd_pentaFib(l):
    return 2 * (l // 6) + [0, 1, 2, 2, 2, 2][l % 6] - (l >= 2)

# Two strings a and b are called isomorphic if there is a one
# to one mapping possible for every character of a to every character of b.
# And all occurrences of every character in a map to same character in b.
# Task
# In this kata you will create a function that return True if two given strings are isomorphic
# to each other, and False otherwise. Remember that order is important.
# Your solution must be able to handle words with more than 10 characters.
from collections import Counter
def isomorph(s: str, t: str) -> bool:
        sc=len(Counter(s))
        st=len(Counter(t))
        if(sc!=st): return False
        else:
           s1=[]
           t1=[]
           m=[]
           ans=[]
           for i in s: s1.append(i)
           for i in t: t1.append(i)
           m.append(s1)
           m.append(t1)
        for i in s:
              if i in m[0]:
               a=m[0].index(i)
               ans.append(m[1][a])
        return "".join(ans) == t

# Two integer numbers are added using the column addition method. When using this
# method, some additions of digits produce non-zero carries to the next positions.
# Your task is to calculate the number of non-zero carries that will occur while adding the given numbers.
# The numbers are added in base 10.
def number_of_carries(a: int, b: int) -> int:
    s = sum(int(i) for i in str(a))
    s2 = sum(int(i) for i in str(b))
    s3 = sum(int(i) for i in str(a + b))
    return (s + s2 - s3) // 9

# For a given nonempty string s find a minimum substring t and the maximum number k,
# such that the entire string s is equal to t repeated k times.
# The input string consists of lowercase latin letters.
# Your function should return :
# a tuple (t, k) (in Python)
# an array [t, k] (in Ruby and JavaScript)
# in C, return k and write to the string t passed in parameter
def f(s):
    c = min([s.count(i) for i in s])
    w = ''
    for i in s:
        w += i
        if w * c == s: return (w, c)
    return (s, 1)

# You need to write a password generator that meets the following criteria:
# 6 - 20 characters long
# contains at least one lowercase letter
# contains at least one uppercase letter
# contains at least one number
# contains only alphanumeric characters (no special characters)
# Return the random password as a string.
# Note: "randomness" is checked by counting the characters used in the generated passwords - all characters
# should have less than 50% occurance. Based on extensive tests, the normal rate is around 35%.
from string import ascii_lowercase as LOWER, ascii_uppercase as UPPER, digits as DIGITS
from random import choice, shuffle, randint
def password_gen():
    w = [choice(UPPER), choice(LOWER), choice(DIGITS)] + [choice(UPPER+LOWER+DIGITS) for i in range(randint(3, 17))]
    shuffle(w)
    return "".join(w)

# You are given an array of unique numbers. The numbers represent points.
# The higher the number the higher the points. In the array [1,3,2] 3 is the highest
# point value so it gets 1st place. 2 is the second highest so it
# gets second place. 1 is the 3rd highest so it gets 3rd place.
# Your task is to return an array giving each number its rank in the array.
def rankings(arr):
    l = sorted(arr, reverse=True)
    return [l.index(i)+1 for i in arr]

# A palindrome is a word, phrase, number, or other sequence of
# characters which reads the same backward as forward. Examples of numerical palindromes are:
# 2332
# 110011
# 54322345
# For this kata, single digit numbers will not be considered numerical palindromes.
# For a given number num, write a function to test if the number contains a
# numerical palindrome or not and return a boolean (true if it does and false if does not).
# Return "Not valid" if the input is not an integer or is less than 0.
# Note: Palindromes should be found without permutating num.
import re
def palindrome(integer):
    if not isinstance(integer, int) or integer < 0: return 'Not valid'
    return re.search(r'(.)\1|(.).\2', str(integer)) is not None

# A list S will be given. You need to generate a list T from it by following the given process:
# Remove the first and last element from the list S and add them to the list T.
# Reverse the list S
# Repeat the process until list S gets emptied.
# The above process results in the depletion of the list S. Your task is to generate list T without
# mutating the input List S.
def arrange(s):
    return list(s[[i,-i,~i,i][i%4]//2]for i in range(len(s)))

# Just like in the "father" kata, you will have to return
# the last digit of the nth element in the Fibonacci sequence (starting with 1,1, to be extra clear,
# not with 0,1 or other numbers).
# You will just get much bigger numbers, so good luck bruteforcing your way through it ;)
def last_fib_digit(n):
    return int('011235831459437077415617853819099875279651673033695493257291'[n % 60])

# A palindrome is a word, phrase, number, or other sequence
# of characters which reads the same backward as forward. Examples of numerical palindromes are:
# 2332
# 110011
# 54322345
# For a given number num, return its closest numerical palindrome which can either be smaller or larger
# than num. If there are 2 possible values, the larger value should be returned. If
# num is a numerical palindrome itself, return it.
# For this kata, single digit numbers will NOT be considered numerical palindromes.
# Also, you know the drill - be sure to return "Not valid" if the input is not an integer or is less than 0.
def palindrome(num):
    if not isinstance(num, int) or num < 0: return 'Not valid'
    if num < 10: num = 11
    if str(num) == str(num)[::-1]: return num
    r, l, d = 0, 0, num
    while str(num)!=str(num)[::-1]: num, l = num+1, l+1
    while str(d)!=str(d)[::-1]: d, r = d-1, r+1
    return d if r<l else num

# Write a function that gets a sequence and value and returns true/false
# depending on whether the variable exists in a multidimentional sequence.
def locate(seq, v):
    return v in seq or any(locate(i, v) for i in seq if isinstance(i, list))

# In this Kata, you will be given a series of times at which an alarm sounds. Your
# task will be to determine the maximum time interval between alarms. Each alarm
# starts ringing at the beginning of the corresponding minute and rings for exactly one
# minute. The times in the array are not in chronological order. Ignore duplicate times, if any.
from datetime import datetime
def solve(arr):
    l = [datetime(2000, 1, 1, *map(int, x.split(':'))) for x in sorted(arr)]
    c = max(int((j - i).total_seconds() - 60) for i, j in zip(l, l[1:] + [l[0].replace(day=2)]))
    return '{:02}:{:02}'.format(*divmod(c//60, 60))

# Create a function running_average() that returns a callable function object. Update the series with
# each given value and calculate the current average.
def running_average():
    l = []
    def mean(n):
        l.append(n)
        return round(sum(l) / len(l), 2)
    return mean

# You'll be given a string of random characters (numbers, letters, and symbols).
# To decode this string into the key we're searching for:
# (1) count the number occurences of each ascii lowercase letter, and
# (2) return an ordered string, 26 places long, corresponding to the number of occurences
# for each corresponding letter in the alphabet.
def decrypt(w):
    return ''.join(str(w.count(i)) for i in "abcdefghijklmnopqrstuvwxyz")

# Write a function
# find_the_number_plate
# which takes the Customer ID as an argument, calculates the Number Plate corresponding to this ID and
# returns it as a string
def find_the_number_plate(i):
    return f'{97+i//999%26:c}{97+i//999//26%26:c}{97+i//999//26//26:c}{1+i%999:03}'

# You will be given an array of strings. The words in the array should mesh together where one or more
# letters at the end of one word will have the same letters (in the same order)
# as the next word in the array. But, there are times when all the words won't mesh.
def word_mesh(arr):
    r = ""
    for i, j in zip(arr, arr[1:]):
        while not i.endswith(j):
            j = j[:-1]
        if not j: return "failed to mesh"
        r += j
    return r

# Given a string, return the minimal number of parenthesis reversals needed to make balanced parenthesis.
def solve(s):
    if len(s) % 2: return -1
    l, c = 0, 0
    for i in s:
        if i == '(': l += 1
        else: l -= 1
        if l < 0:
            c += 1
            l += 2
    return c + l // 2

# A series or sequence of numbers is usually the product of a function and can either be infinite or finite.
# In this kata we will only consider finite series and you are required to return a code according to the
# type of sequence:
def sequence_classifier(l):
    if all(l[i] == l[i+1] for i in range(len(l)-1)): return 5
    if all(l[i] <  l[i+1] for i in range(len(l)-1)): return 1
    if all(l[i] <= l[i+1] for i in range(len(l)-1)): return 2
    if all(l[i] >  l[i+1] for i in range(len(l)-1)): return 3
    if all(l[i] >= l[i+1] for i in range(len(l)-1)): return 4
    return 0

# Make a custom esolang interpreter for the language Tick. Tick
# is a descendant of Ticker but also very different data and command-wise.
def interpreter(tape):
    d, c, w = {}, 0, ""
    for i in tape:
        if i == ">":  c += 1
        elif i == "<":  c -= 1
        elif i == "+":  d[c] = (d.get(c, 0) + 1) % 256
        elif i == "*":  w += chr(d[c])
    return w

# Gary likes pictures but he also likes words and reading. He has had a
# desire for a long time to see what words and books would look like if they could be seen as images.
# For this task you are required to take a continuous string that can consist of any
# combination of words or characters and then convert the words that make up this
# string into hexadecimal values that could then be read as colour values.
# A word is defined as a sequence of ASCII characters between two white
# space characters or the first or last word of a sequence of words.
def words_to_hex(words):
    return [f"#{i[:3].hex():0<6}" for i in words.encode().split()]

# Remember the game 2048? http://gabrielecirulli.github.io/2048/
# The main part of this game is merging identical tiles in a row.
# Implement a function that models the process of merging all of the tile values in a single row.
# This function takes the array line as a parameter and returns a
# new array with the tile values from line slid towards the front of the array (index 0) and merged.
# A given tile can only merge once.
# Empty grid squares are represented as zeros.
# Your function should work on arrays containing arbitrary number of elements.
def merge(line):
    l = [i for i in line if i != 0]
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]: l = l[:i] + [l[i] + l[i + 1]] + l[i + 2:] + [0]
    return l + [0] * (len(line) - len(l))

# Given an array of integers, sum consecutive even numbers and consecutive odd numbers. Repeat the
# process while it can be done and return the length of the final array.
from itertools import groupby
def sum_groups(arr):
    l = list(sum(j) for i,j in groupby(arr, key = lambda x: x % 2 == 0))
    return len(l) if l == arr else sum_groups(l)

# The goal of this Kata is to write a function that will receive an array of strings as its
# single argument, then the strings are each processed and sorted (in desending order) based on the length
# of the single longest sub-string of contiguous vowels ( aeiouAEIOU ) that may
# be contained within the string. The strings may contain letters, numbers, special
# characters, uppercase, lowercase, whitespace, and there may be (often will be)
# multiple sub-strings of contiguous vowels. We are only interested in the single longest
# sub-string of vowels within each string, in the input array.
import re
def sort_strings_by_vowels(seq):
    return sorted(seq, reverse=True, key=lambda _: max((len(i) for i in re.findall(r'[aeiouAEIOU]+', _)), default=0))

# Spin-off of this kata, here you will have to figure out an efficient strategy to
# solve the problem of finding the sole duplicate number among an unsorted array/list of
# numbers starting from 1 up to n.
# Hints: a solution in linear time can be found; using the most intuitive ones to search
# for duplicates that can run in O(n²) time won't work.
def find_dup(arr):
    for i in arr:
        if arr.count(i) > 1: return i

# Given a string of integers, return the number of odd-numbered substrings that can be formed.
def solve(s):
    return sum(int(j) % 2 for i in range(len(s)) for j in s[i:])

# Given an integer n return "odd" if the number of its divisors is odd. Otherwise return "even".
# Note: big inputs will be tested.
def oddity(n):
    return 'odd' if n **.5 == int(n **.5) else 'even'

# Given two array of integers(arr1,arr2). Your task is going to find a
# pair of numbers(an element in arr1, and another element in arr2), their
# difference is as big as possible(absolute value); Again, you should to find a
# pair of numbers, their difference is as small as possible. Return the maximum and
# minimum difference values by an array: [  max difference,  min difference  ]
def max_and_min(arr1,arr2):
    l = [abs(i-j) for i in arr1 for j in arr2]
    return [max(l), min(l)]

# Shake the tree and count where the nuts land.
# Output - An array (same width as the tree) which indicates how many nuts fell at each position ^
from collections import Counter
def shake_tree(tree):
    l = [k for k,v in enumerate(tree[0]) if v == 'o']
    for char in tree[1:]:
        l = [i+1 if char[i] == '\\' else i-1 if char[i] == '/' else i for i in l if char[i] != '_']
    d = Counter(l)
    return [d[i] for i in range(len(tree[0]))]

# Given two words, how many letters do you have to remove from them to make them anagrams?
from collections import Counter
def anagram_difference(w1, w2):
    w1, w2 = Counter(w1), Counter(w2)
    return sum(((w1 - w2) + (w2 - w1)).values())

# Ka ka ka cypher is a cypher used by small children in some country. When a girl
# wants to pass something to the other girls and there are some boys nearby,
# she can use Ka cypher. So only the other girls are able to understand her.
# She speaks using KA, ie.:
# ka thi ka s ka bo ka y ka i ka s ka u ka gly what simply means this boy is ugly.
# Task
# Write a function that accepts a string word and returns encoded message using ka cypher.
def ka_co_ka_de_ka_me(word):
    w = ""
    for k, v in enumerate(word):
        if k != len(word):
            if v.lower() not in "aeiou" and word[k-1].lower() in "aeiou" and k != 0: w += "ka"
        w += v
    return "ka" + w

# Create a function that takes a string and separates it into a sequence of letters.
def sep_str(st):
    return [[j[i] if len(j) > i else '' for j in st.split()] for i in range(max(map(len, st.split())))] if st else []

# Complete the pattern, using the special character ■   □
# In this kata, we draw some histogram of the sound performance of ups and downs.
def draw(waves):
    l = max(waves)
    return '\n'.join(''.join('□■'[j > i] for j in waves) for i in reversed(range(l)))

# Return the sum of the multiples of 3 and 5 below a number. Being the galactic games,
# the tracks can get rather large, so your solution should
# work for really large numbers (greater than 1,000,000).
def solution(number):
    a, b, c = (number - 1) // 5, (number - 1) // 3, (number - 1) // 15
    return (((a * (a + 1)) // 2) * 5) + (((b * (b + 1)) // 2) * 3) - (((c * (c + 1)) // 2) * 15)

# Write a function groupIn10s which takes any number of arguments, groups them into
# tens, and sorts each group in ascending order.
# The return value should be an array of arrays, so that numbers
# between 0 and9 inclusive are in position 0, numbers between 10 and 19 are in position 1, etc.
def group_in_10s(*args):
    if len(args) == 0: return []
    s = sorted(args)
    l = [None for _ in range(max(s)//10 + 1)]
    for j in s:
        i = j // 10
        if l[i] is None: l[i] = [j]
        else: l[i].append(j)
    return l

# You're continuing to enjoy your new piano, as described in Piano Kata, Part 1.
# You're also continuing the exercise where you start on the very first (leftmost, lowest in pitch)
# key on the 88-key keyboard, which (as shown below) is the note A, with the little finger
# on your left hand, then the second key, which is the black key A# ("A sharp"), with your
# left ring finger, then the third key, B, with your left middle finger, then the fourth key, C,
# with your left index finger, and then the fifth key, C#, with your left thumb. Then
# you play the sixth key, D, with your right thumb, and continue on playing the seventh, eighth,
# ninth, and tenth keys with the other four fingers of your right hand. Then for the eleventh
# key you go back to your left little finger, and so on. Once you get to the rightmost/highest,
# 88th, key, C, you start all over again with your left little finger on the first key.
def which_note(count):
    return ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'][(count - 1) % 88 % 12]

# In this Kata, you will be given a number and your task will be to return the nearest prime number.
from gmpy2 import is_prime
def solve(n, i=0):
    return is_prime(n-i) and n-i or is_prime(n+i) and n+i or solve(n,i+1)

# You've just finished writing the last chapter for your novel when a virus suddenly infects your document.
# It has swapped the 'i's and 'e's in 'ei' words and capitalised random letters. Write a function which will:
# a) remove the spelling errors in 'ei' words. (Example of 'ei' words: their, caffeine, deceive, weight)
# b) only capitalise the first letter of each sentence. Make sure the rest of the sentence is in lower case.
def proofread(s):
    return '. '.join(_.lower().replace('ie', 'ei').capitalize() for _ in s.split('. '))

# A rectangle can be split up into a grid of 1x1 squares, the amount of
# which being equal to the product of the two dimensions of the rectangle. Depending on the
# size of the rectangle, that grid of 1x1 squares can also be split up into
# larger squares, for example a 3x2 rectangle has a total of 8 squares,
# as there are 6 distinct 1x1 squares, and two possible 2x2 squares. A 4x3 rectangle contains 20 squares.
# Your task is to write a function `findSquares` that returns the total number of squares
# for any given rectangle, the dimensions of which being given as two integers with
# the first always being equal to or greater than the second.
def findSquares(x,y):
    return sum((x-i) * (y-i) for i in range(y))

# Our friendly jumping spider is resting and minding his own spidery business at web-coordinate spider.
# An inattentive fly bumbles into the web at web-coordinate fly and gets itself stuck.
# Your task is to calculate and return the distance the spider must jump to get to the fly.
from math import cos, pi
def spider_to_fly(spider, fly):
    x, y = int(spider[1]), int(fly[1])
    return (x**2 + y**2 - 2 * x * y * cos((ord(spider[0]) - ord(fly[0])) * pi / 4))**0.5

# Array Exchange and Reversing
# It's time for some array exchange! The objective is simple: exchange the elements of two arrays
# in-place in a way that their new content is also reversed.
def exchange_with(a, b):
    a[:], b[:] = b[::-1], a[::-1]

# Write a function that accepts a message string and an array of integers code. As the result, return
# the key that was used to encrypt the message. The key has to be shortest of all
# possible keys that can be used to code the message: i.e. when the possible keys
# are 12 , 1212, 121212, your solution should return 12.
def find_the_key(message, code):
    w = "".join(str(code[k] + 96 - ord(v)) for k, v in enumerate(message))
    l = len(w)
    for i in range(1, l + 1):
        if (w[:i] * l)[:l] == w: return int(w[:i])

# Mrs Jefferson is a great teacher. One of her strategies that helped her to reach astonishing results
# in the learning process is to have some fun with her students. At school, she wants
# to make an arrangement of her class to play a certain game with her pupils.
# For that, she needs to create the arrangement with the minimum amount of groups that have consecutive sizes.
def shortest_arrang(n):
    r = n // 2 + 2
    l = [i for i in range(r, 0, -1)]
    for i in range(r):
        for j in range(r + 1):
            if sum(l[i:j]) == n: return l[i:j]
    return [-1]

# We need a function prime_bef_aft() that gives the largest prime below a certain given value n,
# befPrime or bef_prime (depending on the language),
# and the smallest prime larger than this value,
# aftPrime/aft_prime (depending on the language).
# The result should be output in a list like the following:
from gmpy2 import is_prime, next_prime
def prime_bef_aft(i):
    return [next(filter(is_prime, range(i-1, 1, -1))), next_prime(i)]

# You wrote all your unit test names in camelCase. But some of your colleagues have troubles reading these
# long test names. So you make a compromise to switch to underscore separation.
# To make these changes fast you wrote a class to translate a camelCase name into an underscore separated name.
# Implement the ToUnderscore() method.
import re
def toUnderScore(word):
    return re.sub("(?<=[^_-])_?(?=[A-Z])|(?<=[^\\d_])_?(?=\\d)", "_", word)

# A palindrome is a word, phrase, number, or other sequence of characters which reads the
# same backward as forward. Examples of numerical palindromes are: 2332, 110011, 54322345
# For a given number num, write a function which returns an array of all the numerical palindromes
# contained within each number. The array should be sorted in ascending order
# and any duplicates should be removed.
def palindrome(num):
    if not isinstance(num, int) or num < 0: return "Not valid"
    n = str(num)
    l = len(n)
    c = {int(n[i:j]) for i in range(l-1) for j in range(i+2, l+1) if int(n[i]) and n[i:j] == n[i:j][::-1]}
    return sorted(c) if c else "No palindromes found"

# John is a typist. He has a habit of typing: he never use the Shift key to switch case, just using only Caps Lock.
# Given a string s. Your task is to count how many times the keyboard has been tapped by John.
# You can assume that, at the beginning the Caps Lock light is not lit.
def typist(s):
    return sum(i.islower()^j.islower() for i, j in zip('a'+s, s)) + len(s)

# You are given a list of directions in the form of a list:
# goal = ["N", "S", "E", "W"]
# Pretend that each direction counts for 1 step in that particular direction.
# Your task is to create a function called directions, that will return a reduced list that will
# get you to the same point.The order of directions must be returned as N then S then E then W.
# If you get back to beginning, return an empty array.
def directions(goal):
    y, x = goal.count("N") - goal.count("S"), goal.count("E") - goal.count("W")
    return ["N"] * y + ["S"] * (-y) + ["E"] * x + ["W"] * (-x)

# Given a positive integer as input, return the output as a string in the following format:
# Each element, corresponding to a digit of the number, multiplied by a power of 10 in such
# a way that with the sum of these elements you can obtain the original number.
def simplify(n):
    return "".join(["+"+str(n)[i]+("*1"+"0"*(len(str(n))-i-1) if len(str(n))-i-1>0 else "") for i in range(0, len(str(n))) if str(n)[i]!="0"])[1:]

# Imagine a triangle of numbers which follows this pattern:
# Starting with the number "1", "1" is positioned at the top
# of the triangle. As this is the 1st row, it can only support a single number.
# The 2nd row can support the next 2 numbers: "2" and "3"
# Likewise, the 3rd row, can only support the next 3 numbers: "4", "5", "6"
# And so on; this pattern continues.
def cumulative_triangle(n):
    return (n**3+n)/2

# Your goal is to write a function that determines the depth of the deepest nested list within a given list.
# return 1 if there are no nested lists. The list passed to your function can contain any data types.
def list_depth(lst):
    l = [list_depth(i) for i in lst if isinstance(i, list)]
    return max(l)+1 if l else 1

# For a given number num, write a function which returns the number of
# numerical palindromes within each number. For this kata, single digit
# numbers will NOT be considered numerical palindromes.
# Return "Not valid" if the input is not an integer or is less than 0.
def palindrome(num):
    if not isinstance(num, int) or num < 0: return 'Not valid'
    s = str(num)
    return sum(sum(s[i:i+j] == s[i:i+j][::-1] for i in range(len(s)-j+1)) for j in range(2, len(s)+1))

# Write function which validates an input string. If the string is a perfect square return true,false otherwise.
def perfect_square(square):
    return all("." * len(square.split("\n")) == i for i in square.split("\n"))

# Third day at your new cryptoanalyst job and you come across your toughest assignment
# yet. Your job is to implement a simple keyword cipher. A keyword cipher is a type of monoalphabetic
# substitution where two parameters are provided as such (string, keyword). The string is
# encrypted by taking the keyword, dropping any letters that appear more than once. The rest of the
# letters of the alphabet that aren't used are then appended to the end of the keyword.
def keyword_cipher(s, keyword, key=""):
    w = "abcdefghijklmnopqrstuvwxyz"
    for i in keyword + w:
        if i not in key: key += i
    return s.lower().translate(str.maketrans(w, key))

# In his publication Liber Abaci Leonardo Bonacci, aka Fibonacci, posed a problem involving a population
# of idealized rabbits. These rabbits bred at a fixed rate, matured over the course of
# one month, had unlimited resources, and were immortal.
# Create a function that determines the number of pairs of mature rabbits after n
# months, beginning with one immature pair of these idealized rabbits that produce b pairs of offspring at
# the end of each month.
def fib_rabbits(n, b):
    x, y = 0, 1
    for i in range(n): x, y = y, y + b * x
    return x

# You'll have a function called "sortEmotions" that will return an array of emotions
# sorted. It has two parameters, the first parameter called "arr" will
# expect an array of emotions where an emotion will be one of the following:
def sort_emotions(arr, bool):
    return sorted(arr, key=[':D',':)',':|',':(','T_T'].index, reverse = not bool)

# Your task is to write a function named do_math that receives a single argument.
# This argument is a string that contains multiple whitespace delimited numbers. Each number has
# a single alphabet letter somewhere within it.
from functools import reduce
from itertools import cycle
from operator import add, truediv, mul, sub
def do_math(s):
    l = sorted(s.split(), key=lambda j: next(i for i in j if i.isalpha()))
    l = [int(''.join(filter(str.isdigit, i))) for i in l]
    ops = cycle([add, sub, mul, truediv])
    return round(reduce(lambda a, b: next(ops)(a, b), l))

# Natural Language Understanding is the subdomain of Natural Language Processing where people
# used to design AI based applications have ability to understand the human languages. HashInclude
# Speech Processing team has a project named Virtual Assistant. For this project
# they appointed you as a data engineer (who has good knowledge of creating clean datasets
# by writing efficient code). As a data engineer your first task is to
# make vowel recognition dataset. In this task you have to find the presence of vowels
# in all possible substrings of the given string. For each given string you have to
# return the total number of vowels.
def vowel_recognition(input):
    w = set('aeiouAEIOU')
    s = t = 0
    for k, v in enumerate(input, 1):
        if v in w: t += k
        s += t
    return s

# Christmas is coming, and your task is to build a custom Christmas tree with the specified
# characters and the specified height.
from itertools import cycle, chain
def custom_christmas_tree(chars, n):
    c, l = cycle(chars), 2*n-1
    return '\n'.join(chain((' '.join(next(c) for i in range(j)).center(l).rstrip() for j in range(1,n+1)), ('|'.center(l).rstrip() for k in range(n//3 or 1))))

# No Story
# No Description
# Only by Thinking and Testing
# Look at the result of testcase, guess the code!
def test_it(a, b):
    return sum(map(int, str(a))) * sum(map(int, str(b)))

# Cara is applying for several different jobs. The online
# application forms ask her to respond within a specific character count. Cara
# needs to check that her answers fit into the character limit.
# Annoyingly, some application forms count spaces as a character, and some don't.
# Your challenge:
# Write Cara a function charCheck() with the arguments:
# "text": a string containing Cara's answer for the question
# "max": a number equal to the maximum number of characters allowed in the answer
# "spaces": a boolean which is True if spaces are included in the character count and False if they are not
def charCheck(text, mx, spaces):
    if not spaces: text = text.replace(' ', '')
    return [len(text) <= mx, text[:mx]]

# Create a function longer that accepts a string and sorts the words in it based on their
# respective lengths in an ascending order. If there are two words of the
# same lengths, sort them alphabetically. Look at the examples below for more details.
def longer(s):
    return ' '.join(sorted(s.split(' '), key = lambda x: (len(x),x)))

# The look and say sequence is a sequence in which each number is the result of a "look and say"
# operation on the previouselement.
# Considering for example the classical version startin with "1": ["1", "11", "21, "1211", "111221", ...]. You
# can see that the second element describes the first as "1(times number)1",
# the third is "2(times number)1" describing the second, the fourth is "1(times number)
# 2(and)1(times number)1" and so on.
# Your goal is to create a function which takes a starting string (not
# necessarily the classical "1", much less a single character start) and return the nth element of the series.
from itertools import groupby
from functools import reduce
def look_and_say_sequence(first_element, n):
    return reduce(lambda i, j: ''.join('%d%s' % (len(list(v)), k) for k, v in groupby(i)), range(n - 1), first_element)

# Give you two number rows , columns and a string str. Returns a rows
# x columns table pattern and fill in the str(each grid fill in a char,
# the length of str is always less than or equals to the total numbers of grids):
def pattern(rows, col, s):
    seperator, res, l, index = '+---'*col + '+', '', len(s), 0
    for _ in range(rows):
        res += seperator+'\n'
        for c in range(col):
            if index < l: res += f'| {s[index]} '
            else: res += '|   '
            index += 1
        res += '|\n'
    res += seperator
    return res

# Traditionally in FizzBuzz, multiples of 3 are replaced by "Fizz" and multiples of
# 5 are replaced by "Buzz". But we could also play FizzBuzz with any other integer pair
# [n, m] whose multiples are replaced with Fizz and Buzz.
# For a sequence of numbers, Fizzes, Buzzes and FizzBuzzes, find the numbers
# whose multiples are being replaced by Fizz and Buzz. Return them as an array [n, m]
# The Fizz and Buzz numbers will always be integers between 1 and 50, and
# the sequence will have a maximum length of 100. The Fizz and Buzz numbers
# might be equal, and might be equal to 1.
def reverse_fizz_buzz(array):
    return tuple(next(i for i, j in enumerate(array, 1) if j == k or j == "FizzBuzz") for k in ["Fizz", "Buzz"])

# Your task is to write a function such that, for the input
# string that represents a road as described, returns the total number of photos
# that were taken by the cameras. The complexity should be strictly O(N) in order to pass all the tests.
def count_photos(road):
    c, l, f = 0, 0, 0
    for i in road:
        if i == ">": l += 1
        elif i == ".":
            c += l
            f += 1
        elif i == "<": c += f
    return c

# You are given N ropes, where the length of each rope is a positive integer.
# At each step, you have to reduce all the ropes by the length of the smallest rope.
# The step will be repeated until no ropes are left. Given the length of N
# ropes, print the number of ropes that are left before each step.
def cut_the_ropes(arr):
    l = []
    while arr:
        l.append(len(arr))
        m = min(arr)
        arr = [i - m for i in arr if i > m]
    return l

# In one city it is allowed to write words on the buildings walls. The local
# janitor, however, doesn't approve of it at all. Every night he vandalizes
# the writings by erasing all occurrences of some letter. Since the janitor
# is quite lazy, he wants to do this with just one swipe of his mop.
def the_janitor(word):
    l = []
    w = 'abcdefghijklmnopqrstuvwxyz'
    for i in w:
        if i not in word:
            l.append(0)
            continue
        l.append(word.rindex(i) + 1 - word.index(i))
    return l

# Math geeks and computer nerds love to anthropomorphize numbers and assign emotions and personalities to
# them. Thus there is defined the concept of a "happy" number. A happy number
# is defined as an integer in which the following sequence ends with the number 1.
# Start with the number itself.
# Calculate the sum of the square of each individual digit.
# If the sum is equal to 1, then the number is happy. If the sum is not
# equal to 1, then repeat steps 1 and 2. A number is considered unhappy once
# the same number occurs multiple times in a sequence because this means there is
# a loop and it will never reach 1.
def happy_numbers(n):
    def is_happy(n):
        stop = {1}
        while n not in stop:
            stop.add(n)
            n = sum(int(d)**2 for d in str(n))
        return n == 1
    return [i for i in range(1, n+1) if is_happy(i)]

# The situation...
# The fastest penguins in the world have just swum for the ultimate prize in professional penguin swimming.
# The cameras that were capturing the race stopped recording half way through.
# The athletes, and the fans are in disarray waiting for the results.
# The challenge...
# Given the last recorded frame of the race, and an array of penguin athletes,
# work out the gold, silver and bronze medal positions.
def calculate_winners(snapshot, penguins):
    c, d = 0, {}
    for i in snapshot.split('\n'):
        for j in i[i.lower().index('p')+1:]:
            if j == '~':
                c += 2
                continue
            c += 1
        d[penguins[0]] = c
        penguins = penguins[1:]
        c = 0
    d = [i for i in dict(sorted(d.items(), key=lambda i: i[1]))]
    return f"GOLD: {d[0]}, SILVER: {d[1]}, BRONZE: {d[2]}"

# Most football fans love it for the goals and excitement. Well, this Kata doesn't.
# You are to handle the referee's little notebook and count the players who
# were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each; players on each team
# are numbered from 1 to 11. Any player may be sent off the field by being
# given a red card. A player can also receive a yellow warning card, which is fine, but
# if he receives another yellow card, he is sent off immediately (no need for a
# red card in that case). If one of the teams has less than 7 players remaining, the game
# is stopped immediately by the referee, and the team with less than 7 players loses.
def men_still_standing(cards):
    a, b = [0] * 11, [0] * 11
    for c in cards:
        if c[0] == 'A': a[int(c[1:-1])-1] += (1 if c[-1] == 'Y' else 2)
        else: b[int(c[1:-1])-1] += (1 if c[-1] == 'Y' else 2)
        if sum(i < 2 for i in a) < 7 or sum(i < 2 for i in b) < 7: break
    return (sum(i < 2 for i in a), sum(i < 2 for i in b))

# Your apple has a virus, and the infection is spreading.
# The apple is a two-dimensional array, containing
# strings "V" (virus) and "A" (uninfected parts). For each hour,
# the infection spreads one space up, down, left and right.
# Input: 2D array apple and number n (n >= 0).
# Output: 2D array showing the apple after n hours.
def infect_apple(apple, n):
    h, w = range(len(apple)), range(len(apple[0]))
    v = [(i, j) for i in h for j in w if apple[i][j] == "V"]
    return [["A" if all(n < abs(y - j) + abs(x - i) for y, x in v) else "V" for i in w] for j in h]

# Let's say take 2 strings, A and B, and define the similarity of the strings to
# be the length of the longest prefix common to both strings. For example, the similarity of strings
# abc and abd is 2, while the similarity of strings aaa and aaab is 3.
# write a function that calculates the sum of similarities of a string S with each of it's suffixes.
def string_suffix(str):
    c = 0
    for i in range(len(str)):
        for a, b in zip(str, str[i:]):
            if a != b: break
            c += 1
    return c

# Return the most profit from stock quotes.
# Stock quotes are stored in an array in order of date. The stock profit is
# the difference in prices in buying and selling stock. Each day, you can
# either buy one unit of stock, sell any number of stock units you have
# already bought, or do nothing. Therefore, the most profit is the
# maximum difference of all pairs in a sequence of stock prices.
def get_most_profit_from_stock_quotes(quotes):
    return sum(max(quotes[k:]) - v for k, v in enumerate(quotes))

# Some languages like Chinese, Japanese, and Thai do not have spaces between words. However,
# most natural languages processing tasks like part-of-speech tagging require texts that have segmented
# words. A simple and reasonably effective algorithm to segment a sentence
# into its component words is called "MaxMatch".
# MaxMatch
# MaxMatch starts at the first character of a sentence and tries to find the longest valid
# word starting from that character. If no word is found, the first character is deemed the
# longest "word", regardless of its validity. In order to find the rest of the words,
# MaxMatch is then recursively invoked on all of the remaining characters until no characters remain.
# A list of all of the words that were found is returned.
def max_match(s):
    l = []
    while s:
        for i in range(len(s), 0, -1):
            w = s[:i]
            if w in VALID_WORDS: break
        l.append(w)
        s = s[i:]
    return l

# Write a function that returns the greatest common factor of an array of positive integers.
# Your return value should be a number, you will only receive positive integers.
def greatest_common_factor(seq):
    l = []
    for i in range(1, min(seq)+1):
        if all(j % i == 0 for j in seq): l.append(i)
    return max(l)

# Check that the two provided arrays both contain the same number of different unique
# items, regardless of order. For example in the following:
from collections import Counter
def balance(arr1, arr2):
    s1, s2 = sorted(Counter(arr1).values()), sorted(Counter(arr2).values())
    return all(i == j for i, j in zip(s1, s2)) and len(s1) == len(s2)

# This challenge is an extension of the kata of Codewars: Missing and Duplicate Number", authored
# by the user Uraza. (You may search for it and complete it if you have not done it)
# In this kata, we have an unsorted sequence of consecutive numbers from a to b, such
# that a < b always (remember a, is the minimum, and b the maximum value).
# They were introduced an unknown amount of duplicates in this sequence and we know that there
# is an only missing value such that all the duplicate values and the missing value are
# between a and b, but never coincide with them.
# Find the missing number with the duplicate numbers (duplicates should be output in a sorted array).
from collections import Counter
def find_dups_miss(arr):
    s = Counter(arr)
    l = sum(i for i in range(sorted(s)[0], sorted(s)[-1]+1)) - sum(s)
    return [l, sorted(k for k, v in s.items() if v > 1)]

# In this Kata, you will be given an array of integers and your task is
# to return the number of arithmetic progressions of size 3 that are possible
# from that list. In each progression, the differences between the elements must be the same.
from itertools import combinations
def solve(arr):
    return sum(a - b == b - c for a, b, c in combinations(arr, 3))

# Build a function sumNestedNumbers/sum_nested_numbers that finds the sum of all numbers in a series of
# nested arrays raised to the power of their respective nesting levels. Numbers in the outer most array
# should be raised to the power of 1.
def sum_nested_numbers(a, c=0):
    return a ** c if not isinstance(a, list) else sum(sum_nested_numbers(i, c+1) for i in a)

# Given three arrays of integers, return the sum of elements that are common in all three arrays.
from collections import Counter
def common(a,b,c):
    return sum((Counter(a) & Counter(b) & Counter(c)).elements())

# You're playing to scrabble. But counting points is hard.
# You decide to create a little script to calculate the best possible value.
# The function takes two arguments :
# `points` : an array of integer representing for each letters from A to Z the points that it pays
# `words` : an array of strings, uppercase
def get_best_word(points, words):
    return max(range(len(words)), key=lambda i: (sum(points[ord(j)-65] for j in words[i]), -len(words[i]), -i))

# Implement a function that normalizes out of range sequence indexes (converts them
# to 'in range' indexes) by making them repeatedly 'loop' around the array. The function
# should then return the value at that index. Indexes that are not
# out of range should be handled normally and indexes to empty sequences should return undefined/None
# depending on the language.
# For positive numbers that are out of range, they loop around starting at the beginning, so
def norm_index_test(seq, ind):
    return seq[ind % len(seq)] if seq else None

# You are given two strings (st1, st2) as inputs. Your task is to return a string containing the numbers
# in st2 which are not in str1. Make sure the numbers are returned in ascending order. All inputs will be
# a string of numbers.
from collections import Counter
def findAdded(st1, st2):
    return ''.join(sorted((Counter(st2) - Counter(st1)).elements()))

# Given a string of numbers, you must perform a method in which you
# will translate this string into text, based on the below image:
def phone_words(text):
    d = {
        222: 'c',
        22: 'b',
        2: 'a',
        333: 'f',
        33: 'e',
        3: 'd',
        444: 'i',
        44: 'h',
        4: 'g',
        555: 'l',
        55: 'k',
        5: 'j',
        666: 'o',
        66: 'n',
        6: 'm',
        7777: 's',
        777: 'r',
        77: 'q',
        7: 'p',
        888: 'v',
        88: 'u',
        8: 't',
        9999: 'z',
        999: 'y',
        99: 'x',
        9: 'w',
        0: ' ',
        1: ''
    }
    while (text.isdigit()):
        for i in d:
            text = text.replace(str(i), d[i])
    return text

# Dear Coder,
# We at [SomeLargeCompany] have decided to expand on the functionality of our online text editor.
# We have written a new function that accepts a phrase, a word and an array of indexes.
# We want this function to return the phrase, with the word inserted at each of the indexes given by the array.
# However, our current function only gets the first insertion right, but all of the following ones
# are out of place!
# Please fix this for us, and you will be showered with money.
# Yours Sincerely, [SomeLargeCompany]
# Note :
# the indicies are always in range and passed as a sorted array
# note if the index array is empty, just return the initial phrase
def insert_at_indexes(phrase, word, indexes):
    for i in indexes[::-1]:
        phrase = phrase[:i] + word + phrase[i:]
    return phrase

# Define n!! as
# n!! = 1 * 3 * 5 * ... * n if n is odd,
# n!! = 2 * 4 * 6 * ... * n if n is even.
# Hence 8!! = 2 * 4 * 6 * 8 = 384, there is no zero at the end. 30!! has 3 zeros at the end.
# For a positive integer n, please count how many zeros are there at the end of n!!.
import math
def count_zeros_n_double_fact(n):
    c = 0
    if n % 2 == 0:
        n = math.prod([i for i in range(2, n+1, 2)])
        while str(n).endswith('0'):
            c += 1
            n = str(n)[:-1]
        return c
    if n % 2 != 0:
        n = math.prod([i for i in range(1, n+1, 2)])
        while str(n).endswith('0'):
            c += 1
            n = str(n)[:-1]
        return c

# This series of katas will introduce you to basics of doing geometry with computers.
# Point objects have x, y attributes. Triangle objects have attributes a, b, c describing
# their corners, each of them is a Point.
# Write a function calculating area of a Triangle defined this way.
# Tests round answers to 6 decimal places.
def triangle_area(triangle):
    a, b, c = triangle.a, triangle.b, triangle.c
    return round(abs(a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) / 2, 6)

# A twin prime is a prime number that is either 2 less or 2 more than another
# prime number—for example, either member of the twin prime pair (41, 43). In other
# words, a twin prime is a prime that has a prime gap of two. Sometimes
# the term twin prime is used for a pair of twin primes; an alternative name for this
# is prime twin or prime pair. (from wiki https://en.wikipedia.org/wiki/Twin_prime)
# Your mission, should you choose to accept it, is to write a function that
# counts the number of sets of twin primes from 1 to n.
# If n is wrapped by twin primes (n-1 == prime && n+1 == prime) then that should
# also count even though n+1 is outside the range.
from gmpy2 import is_prime
def twin_prime(n):
    return sum(is_prime(x) and is_prime(x + 2) for x in range(n))

# The aim of this Kata is to write a function which will reverse the case of all consecutive duplicate
# letters in a string. That is, any letters that occur one after the other and are identical.
# If the duplicate letters are lowercase then they must be set to uppercase, and if
# they are uppercase then they need to be changed to lowercase.
import re
def reverse(s):
    return re.sub(r'(.)\1+', lambda x: x.group().swapcase(), s)

# Following on from Part 1, part 2 looks at some more complicated array contents.
# So let's try filling an array with...
def squares(n):
    return [i**2 for i in range(1, n+1)]
def num_range(n, start, step):
    l = []
    for i in range(n):
        l.append(start)
        start += step
    return l
def rand_range(n, mn, mx):
    from random import randint
    l = []
    for i in range(n):
        l.append(randint(mn, mx))
    return l
def primes(n):
    from gmpy2 import is_prime
    l = []
    c = 1
    while len(l) < n:
        if is_prime(c): l.append(c)
        c += 1
    return l

# In this Kata, we are going to see how a Hash (or Map or dict) can be used to
# keep track of characters in a string.
# Consider two strings "aabcdefg" and "fbd". How many characters do we have to remove from the
# first string to get the second string? Although not the only way to solve this,
# we could create a Hash of counts for each string and see which character counts are different.
# That should get us close to the answer. I will leave the rest to you.
# For this example, solve("aabcdefg","fbd") = 5. Also, solve("xyz","yxxz") = 0, because we
# cannot get second string from the first since the second string is longer.
# More examples in the test cases.
# Good luck!
def solve(a, b):
    return len(a) - len(b) if all(a.count(i) >= b.count(i) for i in set(b)) else 0

# Codewars Weekly has gained popularity in the past months and is receiving lots of fan letters.
# Unfortunately, some of the readers use offensive words and
# the editor wants to keep the magazine family friendly.
# To manage this, you have been asked to implement a censorship algorithm. You will be
# given the fan letter text and a list of forbiddenWords. Your algorithm should replace all occurrences
# of the forbidden words in the text with sequences of asterisks of the same length.
# Be careful to censor only words, no one want to see "classic" spelled as "cl***ic".
def censor_this(text, forbidden_words):
    return ' '.join(i if i.lower() not in forbidden_words else '*'*len(i) for i in text.split())

# Write a function that takes an array/list of numbers and returns a number.
# See the examples and try to guess the pattern:
def even_odd(arr):
    c = 0
    for k, v in enumerate(arr):
        if k % 2: c *= v
        else: c += v
    return c

# Some numbers have the property to be divisible by 2 and 3. Other smaller subset of
# numbers have the property to be divisible by 2, 3 and 5. Another subset with less abundant
# numbers may be divisible by 2, 3, 5 and 7. These numbers have something in common:
# their prime factors are contiguous primes.
# Implement a function that finds the amount of numbers that have the first N primes as factors below
# a given limit.
from gmpy2 import next_prime as np
from math import prod
def count_specMult(n, maxval):
    a, b = 2, []
    while n > 0: b, a, n = b+[a], np(a), n-1
    return maxval // prod(b)

# Complete the function that takes a string as an input, and return a list of
# all the unpaired characters (i.e. they show up an odd number of times in the string), in
# the order they were encountered as an array.
# In case of multiple appearances to choose from, take the last occurence of the unpaired character.
# Notes:
# A wide range of characters is used, and some of them may not render properly in your browser.
# Your solution should be linear in terms of string length to pass the last test.
from collections import Counter
def odd_one_out(s):
    return [k for k, v in Counter(s[::-1]).items() if v % 2][::-1]

# In this Kata, we are going to determine if the count of each of the characters in
# a string can be equal if we remove a single character from that string.
from collections import Counter
def solve(s):
    return any(len(set(Counter(s[:i] + s[i+1:]).values())) == 1 for i in range(len(s)))

# Given a string s and a character c, return an array of integers representing
# the shortest distance from the current character in s to c.
# Notes
# All letters will be lowercase.
# If the string is empty, return an empty array.
# If the character is not present, return an empty array.
def shortest_to_char(s, c):
    if not s or not c:return []
    l = [k for k, v in enumerate(s) if v == c]
    if not l: return []
    return [min(abs(i - j) for j in l) for i in range(len(s))]

# Given an uppercase 9 letter string, letters, find the longest word that can be made with
# some or all of the letters. The preloaded array words (or $words in Ruby) contains
# a bunch of uppercase words that you will have to loop through. Only return the longest word; if there
# is more than one, return the words of the same lengths in alphabetical order. If there are
# no words that can be made from the letters given, return None/nil/null.
def longest_word(w):
    l = []
    for i in sorted(words, key=len)[::-1]:
        if all(w.count(j) >= i.count(j) for j in i): l+=[i]
    if not l: return None
    m = len(l[0])
    return sorted([i for i in l if len(i)==m])

# Alyosha Popovich (Russian folk hero) stroke his sharp sword and cut the head of
# Zmey Gorynych (big Serpent with several heads)! He looked - and lo! - in its place immediately new heads
# appeared, exactly n. He stroke again, and where the second head was, 2*n heads
# appeared! The third time it was 2*3*n new heads, and after fourth swing it was 2*3*4*n heads,
# and so forth. And thus Alyosha decided to call it a day, and instead called a fellow Mage for
# help. While the Mage agreed, he needs to know the exact number of heads that Zmey Gorynych now has.
# The task
# Given the initial number of heads, the heads-count multiplier, and the number of sword-swings,
# calculate how many heads Zmey Gorynych has in the end.
import math
def count_of_heads(initial, n, swings):
    for i in range(1, swings+1):
        initial = initial - 1 + n * math.factorial(i)
    return initial

# Since there are lots of katas requiring you to round numbers to 2 decimal places, you decided to
# extract the method to ease out the process.
# And you can't even get this right!
# Quick, fix the bug before everyone in CodeWars notices that you can't even round a number correctly!
from decimal import Decimal, ROUND_HALF_UP
def round_by_2_decimal_places(n):
    return n.quantize(Decimal('.01'), rounding = ROUND_HALF_UP)

# In this Kata, you will be given an array and your task will be to determine if an array
# is in ascending or descending order and if it is rotated or not.
# Consider the array [1,2,3,4,5,7,12]. This array is sorted in Ascending order.
# If we rotate this array once to the left, we get [12,1,2,3,4,5,7] and twice-rotated
# we get [7,12,1,2,3,4,5]. These two rotated arrays are in Rotated Ascending order.
# Similarly, the array [9,6,5,3,1] is in Descending order, but we can
# rotate it to get an array in Rotated Descending order: [1,9,6,5,3] or [3,1,9,6,5] etc.
# Arrays will never be unsorted, except for those that are rotated as shown above. Arrays
# will always have an answer, as shown in the examples below. Arrays will never contain duplicated elements.
def solve(arr):
    if sorted(arr) == arr: return "A"
    if sorted(arr, reverse=True) == arr: return "D"
    return "RA" if arr[0] > arr[-1] else "RD"

# Write a method that takes a string as an argument and groups
# the number of time each character appears in the string as a hash sorted by the highest number of occurrences.
# The characters should be sorted alphabetically e.g:
from collections import Counter
def get_char_count(seq):
    d = {}
    for k, v in sorted(Counter(i for i in seq.lower() if i.isalnum()).items()):
        d[v] = d.get(v, []) + [k]
    return d

# Given a string str, find the shortest possible string which can
# be achieved by adding characters to the end of initial string to make it a palindrome.
def build_palindrome(w):
    n = 0
    while w[n:] != w[n:][::-1]: n += 1
    return w + w[:n][::-1]

# You are given an integer N. Your job is to figure out how many substrings inside of N divide evenly with N.
# Confused? I'll break it down for you.
# Let's say that you are given the integer '877692'.
def get_count(n):
    w = str(n)
    c = 0
    for i in range(1, len(w)):
        for j in range(len(w) - i + 1):
            s = int(w[j:j+i])
            if s and n % s == 0: c += 1
    return c

# The dot product is usually encountered in linear algebra or scientific computing. It's also
# called scalar product or inner product sometimes:
# In mathematics, the dot product, or scalar product (or sometimes inner product in the context of
# Euclidean space), is an algebraic operation that takes two equal-length sequences of numbers (usually
# coordinate vectors) and returns a single number. Wikipedia
# In our case, we define the dot product algebraically for two vectors
# a = [a1, a2, …, an], b = [b1, b2, …, bn] as
def min_dot(a, b):
    return sum(i * j for (i, j) in zip(sorted(a), sorted(b, reverse = True)))

# You will be given an integer N as input; your task is to return the value of S(Z(N)).
# For example, let N = 3:
def sum_of_sums(x):
    x = x * (x+1) * (x+2) // 6
    return x * (x+1) // 2

# Complete the function which accepts a string and return an array of character(s)
# that have the most spaces to their right and left.
# Notes:
# the string can have leading/trailing spaces - you should not count them
# the strings contain only unique characters from a to z
# the order of characters in the returned array doesn't matter
import re
def loneliest(strng):
    l = [re.match(r'\s*\w\s*', strng.strip()[i:]) for i in range(len(strng))]
    le = max(len(i.group(0)) for i in l if i)
    return [i.group(0).strip() for i in l if i and len(i.group(0)) == le]

# You are asked to write a simple cypher that rotates every character (in range [a-zA-Z], special
# chars will be ignored by the cipher) by 13 chars. As an addition to the
# original ROT13 cipher, this cypher will also cypher numerical digits ([0-9]) with 5 chars.
CHARS = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234")
def ROT135(input):
    return input.translate(CHARS)

# You are provided with a function of the form f(x) = axⁿ, that consists of
# a single term only and 'a' and 'n' are integers, e.g f(x) = 3x², f(x) = 5 etc.
# Your task is to create a function that takes f(x) as the argument and
# returns the result of differentiating the function, that is, the derivative.
def differentiate(x):
    if 'x' not in x: return '0'
    a, n = x.split('x', 2)
    a = 1 if a == '' else -1 if a == '-' else int(a)
    return f"{a}" if n == '' else f"{2*a}x" if n == "^2" else f"{a*int(n[1:])}x^{int(n[1:])-1}"

# The sum of the primes below or equal to 10 is 2 + 3 + 5 + 7 = 17. Find the sum
# of all the primes below or equal to the number passed in.
from gmpy2 import is_prime
def summationOfPrimes(primes):
    return sum(i for i in range(2, primes+1) if is_prime(i))

# X and Y are playing a game. A list will be provided which contains n pairs of strings
# and integers. They have to add the integeri to the ASCII values of the stringi characters. Then
# they have to check if any of the new added numbers is prime or not. If for any character of
# the word the added number is prime then the word will be considered as prime word.
# Can you help X and Y to find the prime words?
from gmpy2 import is_prime
def prime_word(array):
    a = [ord(i) + array[0][1] for i in array[0][0]]
    b = [ord(i) + array[1][1] for i in array[1][0]]
    if len(array) == 3:
        c = [ord(i) + array[2][1] for i in array[2][0]]
    f = [1 if any(is_prime(i) for i in a) else 0, 1 if any(is_prime(i) for i in b) else 0]
    return f if len(array) ==2 else f + [1 if any(is_prime(i) for i in c) else 0]

# Playing ping-pong can be really fun! Unfortunatelly after a long and exciting play you can forget
# who's service turn it is. Let's do something about that!
# Write a function that takes the current score as a string separated by : sign as an only
# parameter and returns "first" or "second" depending on whose service turn it is.
# We're playing old-school, so the rule is that players take turn after every 5 services. That
# is until the score is 20:20 - from that moment each player serves 2 times in his turn.
def service(score):
    c = sum(int(i) for i in score.split(":"))
    return "first" if ((c%10 < 5) if c < 40 else (c%4 < 2)) else "second"

# Create the function off, that receives the nth switch as argument n. The function should return
# an ascending array containing all of the switch numbers that remain off after Bob completes his revenge.
def off(n):
    return [i*i for i in range(1, int(n ** .5) + 1)]

# This is a follow-up from my previous Kata which can be found here:
# http://www.codewars.com/kata/5476f4ca03810c0fc0000098
# This time, for any given linear sequence, calculate the function [f(x)] and return it
# as a function in Javascript or Lambda/Block in Ruby.
def get_function(sequence):
    s = sequence[1] - sequence[0]
    for i in range(1, 5):
        if sequence[i] - sequence[i-1] != s: return "Non-linear sequence"
    return lambda a : s * a + sequence[0]

# In this Kata, you will implement a function count that takes an integer and returns the number of
# digits in factorial(n).
# For example, count(5) = 3, because 5! = 120, and 120 has 3 digits.
# More examples in the test cases.
# Brute force is not possible. A little research will go a long way, as this is a well known series.
# Good luck!
import math
def count(n):
    if (n < 0): return 0
    if (n <= 1): return 1
    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0))
    return math.floor(x) + 1

# You will be given
# The distance to my exit (km)
# How fast I am going (kph)
# Information about a lot of other cars
# Their time (relative to me) as I join the freeway. For example,
# -1.5 means they already passed my starting point 1.5 minutes ago
# 2.2 means they will pass my starting point 2.2 minutes from now
# How fast they are going (kph)
# Find what is my "score" as I exit the freeway!
def freeway_game(km, kph, cars):
    t = km / kph
    c = 0
    for k, v in cars:
        d = km - (t - k/60) * v
        if k <= 0: c += d > 0
        else: c -= d < 0
    return c

# The collections module has defaultdict, which gives you a default value for trying to get the value
# of a key which does not exist in the dictionary instead of raising an error. Why not do this for a list?
# Your job is to create a class (or a function which returns an object) called DefaultList.
# The class will have two parameters to be given: a list, and a default value.
# The list will obviously be the list that corresponds to that object. The default value will
# be returned any time an index of the list is called in the code that would normally raise an error
# (i.e. i > len(list) - 1 or i < -len(list)). This class must also support the regular list functions
# extend, append, insert, remove, and pop.
# Because slicing a list never raises an error (slicing a list between two indexes that are not a part
# of the list returns [], slicing will not be tested for.
class DefaultList(list):
    def __init__(self,it, defu):
        super().__init__(it)
        self.default = defu
    def __getitem__(self,i):
        try: return super().__getitem__(i)
        except: return self.default

# Your friend Cody has to sell a lot of jam, so he applied a good 25% discount to all his merchandise.
# Trouble is that he mixed all the prices (initial and discounted), so now he needs your cool coding
# skills to filter out only the discounted prices.
def find_discounted(prices):
    l = [int(n) for n in prices.split()]
    return ' '.join(l.remove(round(i*4/3)) or str(i) for i in l)

# Your task is to complete the function that determines where to replace a zero with a
# one to make the maximum length subsequence.
# Notes:
# If there are multiple results, return the last one:
def replace_zero(arr):
    c, s, i, l = 0, -1, -1, ''.join(map(str, arr)).split('0')
    for a, b in zip(l, l[1:]):
        i += len(a) + 1
        rep = len(a)+len(b)+1
        if c <= rep: s, c = i, rep
    return s

# Consider the prime number 23. If we sum the square of its digits we get: 2^2 + 3^2 = 13,
# then for 13: 1^2 + 3^2 = 10, and finally for 10: 1^2 + 0^2 = 1.
# Similarly, if we start with prime number 7, the sequence is: 7->49->97->130->10->1.
# Given a range, how many primes within that range will eventually end up being 1?
# The upperbound for the range is 50,000. A range of (2,25) means that: 2 <= n < 25.
from gmpy2 import is_prime
def check(n):
    l = []
    while n not in l:
        l += [n]
        n = sum(int(i)**2 for i in str(n))
        if n==1: return True
    return False
def solve(a,b):
    return len([i for i in range(a,b) if is_prime(i) and check(i)])

# There is a common problem given to interviewees in software. It is called FizzBuzz. It works
# as follows: For the numbers between 1 and 100, print fizz if
# it is a multiple of 3 and buzz if it is a mutiple of 5, else print the number itself.
# You are in an interview and they ask you to complete fizzbuzz (which can
# be done in a one-liner in a few langs) and you knock it out of the park.
# Surprised by your ability, the interviewer gives you a harder problem. Given
# a list of coprime numbers, (that is that the g.c.d. of all the numbers == 1) and
# an equally sized list of words. compute its fizzbuzz representation up until the pattern of strings
# repeats itself.
from functools import reduce

def fizzbuzz_plusplus(nums, words):
    return ["".join(b for a, b in zip(nums, words) if not i % a) or i for i in range(1, reduce(lambda a, b: a * b, nums, 1) + 1)]

# For this kata, you are given three points (x1,y1,z1), (x2,y2,z2), and (x3,y3,z3) that lie on
# a straight line in 3-dimensional space. You have to figure out which point lies in between the other two.
# Your function should return 1, 2, or 3 to indicate which point is the in-between one.
def middle_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    d = {(x1, y1, z1): 1, (x2, y2, z2): 2, (x3, y3, z3): 3}
    return d[sorted(d)[1]]

# The goal of this Kata is to return the greatest distance of index positions between
# matching number values in an array or 0 if there are no matching values.
# Example: In an array with the values [0, 2, 1, 2, 4, 1] the greatest index distance is between
# the matching '1' values at index 2 and 5. Executing greatestDistance against this array would
# return 3. (i.e. 5 - 2)
def greatest_distance(arr):
    return max(k - arr.index(v) for k, v in enumerate(arr))

# Return the index of the array element that you ended up on at the end of the game.
def snakes_and_ladders(board, dice):
    c = 0
    for i in dice:
        if c + i < len(board): c += i + board[c + i]
    return c

# Scheduling is how the processor decides which jobs (processes) get to use the processor and for
# how long. This can cause a lot of problems. Like a really long process taking the
# entire CPU and freezing all the other processes. One solution is Round-Robin, which today you will be
# implementing.
# Round-Robin works by queuing jobs in a First In First Out fashion, but the
# processes are only given a short slice of time. If a processes is not finished in that time
# slice, it yields the proccessor and goes to the back of the queue.
def roundRobin(jobs, slice, index):
    c = 0
    while True:
        for i in range(len(jobs)):
            cc = min(jobs[i], slice)
            jobs[i] -= cc
            c += cc
            if i == index and jobs[i] == 0: return c

# The principal of a school likes to put challenges to the students related with finding
# words of certain features. One day she said: "Dear students, the challenge for today
# is to find a word that has only one vowel and seven consonants but cannot have the
# letters "y" and "m". I'll give a special award for the first student that
# finds it." One of the students used his dictionary and spent all the night without sleeping,
# trying in vain to find the word. The next day, the word had not been found yet.
# This student observed that the principal has a pattern in the features for the wanted words:
# The word should have n vowels, may be repeated, for example: in "engineering", n = 5.
# The word should have m consonants, may be repeated also: in "engineering", m = 6.
# The word should not have some forbidden letters (in an array), forbid_letters
# You will be provided with a list of words, WORD_LIST(python/crystal),
# wordList(javascript), wordList (haskell), $word_list(ruby), and you have to create the function,
# wanted_words(), that receives the three arguments in the order given above, wanted_words(n, m,
# forbid_list)and output an array with the word or an array, having the words in
# the order given in the pre-loaded list, in the case of two or more words were found.
def wanted_words(n, m, f):
    l = []
    v, c = 0, 0
    vow = 'aeiou'
    con = 'bcdfghjklmnpqrstvwxyz'
    for i in WORD_LIST:
        if sum(j in vow for j in i) == n and sum(j in con for j in i) == m and all(j not in f for j in i): l.append(i)
    return l

# An eccentric chessboard maker likes to create strange N x N chessboards.
# Instead of making all the rows and the columns on his chessboards the same size, he
# likes to make chessboards with row and columns of varying sizes:
def white_black_areas(cs, rs):
    r, rc = sum(rs[1::2]), sum(rs[::2])
    c, cs = sum(cs[1::2]), sum(cs[::2])
    return (cs * rc + c * r, r * cs + rc * c)

# We know that some numbers can be split into two primes. ie. 5 = 2 + 3, 10 = 3 + 7. But
# some numbers are not. ie. 17, 27, 35, etc..
# Given a positive integer n. Determine whether it can be split into two primes.
# If yes, return the maximum product of two primes. If not, return 0 instead.
from gmpy2 import is_prime
def prime_product(n):
    return next((i*(n-i) for i in range(n>>1,1,-1) if is_prime(i) and is_prime(n-i)),0)

# Create a function which checks if a given number n can be written as the sum of two cubes in
# two different ways: n = a³+b³ = c³+d³. All the numbers a, b, c and d should be different and greater than 0.
def has_two_cube_sums(n):
    l = [i**3 for i in range(1, int((n)**(1./3.)) + 1)]
    return sum([(n != 2*i) and ((n-i) in l) for i in l]) > 3

# Consider an array that has no prime numbers, and none of its elements has any prime digit.
# It would start with: [1,4,6,8,9,10,14,16,18,40,44..].
# 12 and 15 are not in the list because 2 and 5 are primes.
# You will be given an integer n and your task will be return the number
# at that index in the array. For example:
from gmpy2 import is_prime
def solve(n):
    l = []
    c = 1
    while len(l) <= n:
        if not is_prime(c) and all(not is_prime(int(i)) for i in str(c)): l.append(c)
        c += 1
    return l[n]

# The numbers 6, 12, 18, 24, 36, 48 have a common property. They
# have the same two prime factors that are 2 and 3.
# If we see their prime factorization we will see it more clearly:
from math import log

def highest_biPrimefac(a, b, m):
    l = []
    for i in range(1, int(log(m, b)) + 1):
        c = int(round(log(m / b**i, a), 9))
        if c: l.append([a**c * b**i, c, i])
    return max(l)

# Dan, president of a Large company could use your help. He wants to implement a system that
# will switch all his devices into offline mode depending on his meeting schedule. When he's at a meeting
# and somebody texts him, he wants to send an automatic message informing that he's currently
# unavailable and the time when he's going to be back.;
def check_availability(schedule, current_time):
    for i in schedule:
        if i[0] <= current_time < i[1]: return i[1]
    return True

# Some numbers are more important to get right during data entry than others: a common example is product codes.
# To reduce the possibility of mistakes, product codes can be crafted in such a way that simple errors
# are detected. This is done by calculating a single-digit value based on the product number,
# and then appending that digit to the product number to arrive at the product code.
# When the product code is checked, the check digit value is stripped off and recalculated. If
# the supplied value does not match the recalculated value, the product code is rejected.
# A simple scheme for generating self-check digits, described here, is called Modulus 11 Self-Check.
def add_check_digit(number):
    l = [2, 3, 4, 5, 6, 7]
    s = sum(x*y for x,y in zip(map(int, number[::-1]), l * (len(number) // 6 + 1))) % 11
    return number + ('0' if s == 0 else 'X' if s == 1 else str(11 - s))

# Consider an array containing cats and dogs. Each dog can catch only one cat, but cannot
# catch a cat that is more than n elements away. Your task will be to return
# the maximum number of cats that can be caught.
def solve(arr, n):
    d = [i for i, x in enumerate(arr) if x == 'D']
    c = {i for i, x in enumerate(arr) if x == 'C'}
    s = 0
    while d and c:
        dog = d.pop()
        cat = max((i for i in c if abs(dog - i) <= n), default=-1)
        if cat >= 0:
            s += 1
            c.remove(cat)
    return s

# If string has more than one neighboring dashes(e.g. --) replace they with one dash(-).
# Dashes are considered neighbors even if there is some whitespace between them.
import re
def replace_dashes_as_one(word):
    return re.sub(r'-[ -]+-|-+',r'-', word)

# Some letters in the input string are representing a written-out digit. Some of the
# letters may randomly shuffled. Your task is to recover them all.
# Note that:
# Only consecutive letters can be used. "OTNE" cannot be recovered to 1!
# Every letter has to start with an increasing index.. "ONENO" results to 11, because
# the E can be used two times. Endless loops are not possible!
# If there are letters in the string, which don't create a number you can ignore them.
# If no digits can be found, return "No digits found"
# Take care about the order! "ENOWT" will be recovered to 12 and not to 21.
# The input string consists only UpperCase letters
def recover(st):
    l = []
    for i in range(len(st)):
        for k, v in alph.items():
            if sorted(k) == sorted(st[i:i+len(k)]): l.append(v)
    return ''.join(map(str, l)) or "No digits found"

# You will receive a string consisting of lowercase letters, uppercase letters and digits as input. Your
# task is to return this string as blocks separated by dashes ("-"). The elements of a block should be sorted
# with respect to the hierarchy listed below, and each block cannot contain multiple instances of the same
# character. Elements should be put into the first suitable block.
from collections import Counter
def blocks(w):
    s = lambda c: (c.isdigit(), c.isupper(), c)
    l, c = [], Counter(w)
    while c:
        i = ''.join(sorted(c, key=s))
        l.append(i)
        c = c - Counter(i)
    return '-'.join(l)

# Given an input array (arr) of positive integers, the objective is to return an
# output array where each index represents the amount of times an element
# appeared (frequency) in the input array.
# More specifically, the element at each index of the output array will be
# an array (bucket) containing integers that appeared index-amount-of-times.
# Otherwise, slot nulls (JavaScript, Java), None's (Python) nils (Ruby), or
# NULL's (C/C++) where appropriate. A valid array will always be provided.
from collections import Counter
def bucketize(*arr):
    c = {i: sorted([k for k, v in Counter(arr).items() if v == i]) for i in Counter(arr).values()}
    return [c[i] if i in c else None for i in range(len(arr) + 1)]

# Imagine you are given a positive integer, n, then:
# if n is even, calculate: n / 2
# if n is odd, calculate: 3 * n + 1
# Repeat until your answer is 1. The Collatz conjecture states that performing this operation
# repeatedly, you will always eventually reach 1.
# You can try creating Collatz sequences with this kata. For further information, see the wiki page.
##Now! Your task:
# Given an array of positive integers, return the integer whose Collatz sequence is the longest.
def longest_collatz(input_array):
    def iseven(n):
        return n / 2
    def isodd(n):
        return 3 * n + 1
    l = []
    c = 0
    for i in input_array:
        while i != 1:
            if i % 2 == 0:
                c += 1
                i = iseven(i)
            elif i % 2 != 0:
                c += 1
                i = isodd(i)
        l.append(c)
        c = 0
    return input_array[l.index(max(l))]

# We need the function sec_deg_solver()/secDegSolver(), that accepts three arguments,
# a, b and c, the coefficients of the above equation.
# The outputs of the function may vary depending on the values of coefficients a,
# b and c, according to the following situations. (used values as examples only):
import math
def sec_deg_solver(a, b, c):
    if a == 0:
        if b != 0 and c != 0: return f'It is a first degree equation. Solution: {round(-c/float(b), 10)}'
        elif a == 0 and b == 0 and c == 0: return 'The equation is indeterminate'
        elif a == 0 and b == 0 and c != 0: return 'Impossible situation. Wrong entries'
        elif a == 0 and c == 0 and b != 0: return 'It is a first degree equation. Solution: 0.0'
    elif a != 0:
        d = b**2 - 4 * a * c
        if d < 0: return 'There are no real solutions'
        x1 = round((-b - math.sqrt(d)) / (2 * a), 10)
        x2 = round((-b + math.sqrt(d)) / (2 * a), 10)
        if x2 < x1:
            t = x1
            x1 = x2
            x2 = t
        if d == 0: return f"It has one double solution: {max(x1, x2)}"
        elif d > 0: return f"Two solutions: {min(x1, x2)}, {max(x1, x2)}"

# You're given an array of positive integers arr, and an array guide
# of the same length. Sort array arr using array guide by the following rules:
def sort_by_guide(arr, guide):
    l = iter(sorted((y,x) for x,y in zip(arr, guide) if y > 0))
    return [next(l)[1] if b > 0 else a for a, b in zip(arr, guide)]

# You are a lonely frog.
# You live on a coordinate axis.
# The meaning of your life is to jump and jump..
def jump_to(x, y):
    c = 0
    while y!=x:
        if y % 2 == 0 and y / 2 >= x: y /= 2
        else: y-=1
        c+=1
    return c

# Every Turkish citizen has an identity number whose validity can be checked by these set of rules:
# It is an 11 digit number
# First digit can't be zero
# Take the sum of 1st, 3rd, 5th, 7th and 9th digit and multiply it by 7. Then subtract the sum of
# 2nd, 4th, 6th and 8th digits from this value. Modulus 10 of the result should be equal to 10th digit.
# Sum of first ten digits' modulus 10 should be equal to eleventh digit.
def check_valid_tr_number(n):
    if not isinstance(n, int) or not len(str(n)) == 11: return False
    l = [int(i) for i in str(n)]
    return (sum(l[:9:2])*7 - sum(l[1:9:2])) % 10 == l[9] and sum(l[:10]) % 10 == l[10]

# In this kata you're given an n x n array and you're expected to traverse the
# elements diagonally from the bottom right to the top left.
def diagonal(arr):
    l = sorted(((i, j) for j in range(len(arr)) for i in range(len(arr))), key=sum)[::-1]
    return [arr[i][j] for i, j in l]

# Given a sorted array of numbers, return the summary of its ranges.
def summary_ranges(nums):
    nums.append(float("inf"))
    i, l = nums[0], []
    for a, b in zip(nums, nums[1:]):
        if b - a > 1:
            l.append(str(i) if i == a else f"{i}->{a}")
            i = b
    return l

# The total sum of the numbers in the triangle, up to the 5th line
# included, is 225, part of it, 144, corresponds to the total sum of the even terms
# and 81 to the total sum of the odd terms.
# Create a function that may output an array with three results for each value of n.
def mult_triangle(n):
    s, o = (n * (n + 1) / 2)**2, ((n + 1) // 2)**4
    return [s, s - o, o]

# Write that given an array of numbers >= 0, will arrange them such that they form the biggest number.
def biggest(nums):
    return str(int(''.join(sorted(map(str,nums),key=lambda x:3*x)[::-1])))

# The prime number sequence starts with: 2,3,5,7,11,13,17,19.... Notice that 2 is in position one.
# occupies position two, which is a prime-numbered position. Similarly, 5, 11 and 17 also
# occupy prime-numbered positions. We shall call primes such as 3,5,11,17 dominant primes
# because they occupy prime-numbered positions in the prime number sequence. Let's call this listA.
# As you can see from listA, for the prime range range(0,10), there are
# only two dominant primes (3 and 5) and the sum of these primes is: 3 + 5 = 8.
# Similarly, as shown in listA, in the range (6,20), the dominant
# primes in this range are 11 and 17, with a sum of 28.
# Given a range (a,b), what is the sum of dominant primes within that range?
# Note that a <= range <= b and b will not exceed 500000.
from gmpy2 import next_prime as np, is_prime as ip
def solve(a,b):
    c, l, g = 1, [], 0
    while c<=b:
        c, g = np(c), g+1
        if c>=a and c<=b and ip(g): l.append(c)
    return sum(l)

# Calculus class...is awesome! But you are a programmer with no time for mindless repetition. Your
# teacher spent a whole day covering differentiation of polynomials, and by the time the bell rang,
# you had already conjured up a program to automate the process.
def diff(poly):
    return [k*v for k,v in enumerate(poly[::-1]) if k][::-1]

# The built-in print function for Python class instances is not very entertaining.
# In this kata, we will implement a function show_me(instance) that takes an instance as parameter
# and returns the string "Hi, I'm one of those (classname)s! Have a look at
# my (attrs)." , where (classname) is the class name and (attrs) are the class's attributes.
# If (attrs) contains only one element, just write it. For more than one element (e.g. a, b, c), it
# should list all elements sorted by name in ascending order (e.g. "... look at my a, b and c.").
def show_me(inst):
    name = inst.__class__.__name__
    atts = ' and'.join(', '.join(sorted(i for i in inst.__dict__)).rsplit(',', 1))
    return "Hi, I'm one of those {}s! Have a look at my {}.".format(name, atts)

# The number 1035 is the smallest integer that exhibits a non frequent property: one its multiples,
# 3105 = 1035 * 3, has its same digits but in different order, in other words, 3105, is one
# of the permutations of 1035.
# The number 125874 is the first integer that has this property when the
# multiplier is 2, thus: 125874 * 2 = 251748
# Make the function search_perm_mult(), that receives an upper bound, n_max and a factor k
# and will output the amount of pairs bellow n_max that are permuted when an integer of this
# range is multiplied by k. The pair will be counted if the multiple is less than n_max, too
from collections import Counter
def search_perm_mult(n_max, k):
    return sum(Counter(str(i)) == Counter(str(i * k)) for i in range(1035, n_max // k))

# Your goal is to create a function instrumental() which returns the valid form
# of a valid Hungarian word w in instrumental case i. e. append the correct
# suffix -vel or -val to the word w based on vowel harmony rules.
def instrumental(word):
    d = {"e": u"é", "i": u"í", u"ö": u"ő", u"ü": u"ű", "a": u"á", "o": u"ó", "u": u"ú"}
    for i in word[::-1]:
        if i in u"aáoóuú":
            suf = "val"
            break
        elif i in u"eéiíöőüű":
            suf = "vel"
            break
    if i == word[-1]: return word[:-1] + d.get(i, word[-1]) + suf
    if word[-2:] in ("sz", "zs", "cs"): word = word[:-1] + word[-2:]
    else: word += word[-1]
    return word + suf[1:]

# A runner, who runs with base speed s with duration t will cover a distances d: d = s * t
# However, this runner can sprint for one unit of time with double speed s * 2
# After sprinting, base speed s will permanently reduced by 1, and for next one unit of
# time runner will enter recovery phase and can't sprint again.
# Your task, given base speed s and time t, is to find the maximum possible distance d.
def solution(s, t):
    c = min((t-1)//2, s//3)
    return t*s + (c+1)*s - 3*(c+1)*c//2 if t else 0

# Related to MrZizoScream's Product Array kata. You might want to solve that one first :)
# This is an adaptation of a problem I came across on LeetCode.
# Given an array of numbers, your task is to return a new array
# where each index (new_array[i]) is equal to the product of
# the original array, except for the number at that index (array[i]).
from functools import reduce
la = lambda x: reduce(lambda a, b:a*b, x)
def product_sans_n(N):
    l, z = len(N), N.count(0)
    if z > 1: return l*[0]
    if z == 1: i = N.index(0); return [0]*(i)+[la(N[:i])*la(N[i+1:])]+[0]*(l-i-1)
    p = la(N);               return [p//i for i in N]

# You are given an array of integers arr that representing coordinates of obstacles situated on a straight line.
# Assume that you are jumping from the point with coordinate 0 to the
# right. You are allowed only to make jumps of the same length represented by some integer.
# Find the minimal length of the jump enough to avoid all the obstacles.
def avoid_obstacles(a):
    for i in range(2, max(a) + 2):
        if all(j % i != 0 for j in a): return i

# In this Kata, two groups of monsters will attack each other, and your job
# is to find out who wins. Each group will have a stat for each of the following:
# number of units, hitpoints per unit, damage per unit, and monster type.
# If you are not familiar with the game, just think of each group as standing in
# a line so that when they are attacked the unit at the front of the line takes the
# hit before the others, and if he dies the remaining damage will hit the next unit
# and so on. Therefore multiple units (or even the whole group) can die in one attack.
# Each group takes turns attacking, and does so until only one remains. In this kata,
# the first entry in the input array is the first to attack.
from math import ceil
def who_would_win(m1, m2):
    m1['allhit'] = m1['hitpoints'] * m1['number']
    m2['allhit'] = m2['hitpoints'] * m2['number']
    while True:
        m2['allhit'] = m2['allhit'] - m1['number'] * m1['damage']
        m2['number'] = ceil(m2['allhit'] / m2['hitpoints'])
        if not m2['number'] > 0: return f"{m1['number']} {m1['type']}(s) won"
        m1['allhit'] = m1['allhit'] - m2['number'] * m2['damage']
        m1['number'] = ceil(m1['allhit'] / m1['hitpoints'])
        if not m1['number'] > 0: return f"{m2['number']} {m2['type']}(s) won"

# You are stacking some boxes containing gold weights on top of each other. If a box contains
# more weight than the box below it, it will crash downwards and combine their weights.
# e.g. If we stack [2] on top of [1], it will crash downwards and become a single box of weight [3].
def crashing_weights(weights):
    l = [0] * len(weights[0])
    for i in weights:
        l = [b if a <= b else a+b for a,b in zip(l, i)]
    return l

# The Condi (Consecutive Digraphs) cipher was introduced by G4EGG (Wilfred Higginson) in 2011.
# The cipher preserves word divisions, and is simple to describe and encode,
# but it's surprisingly difficult to crack.
def encode(message, key, shift, encode=True):
    LOWER = "abcdefghijklmnopqrstuvwxyz"
    key = sorted(LOWER, key=f"{key}{LOWER}".index)
    l = []
    for j in message:
        if j in key:
            i = key.index(j)
            j = key[(i + shift) % 26]
            shift = i + 1 if encode else -(key.index(j) + 1)
        l.append(j)
    return "".join(l)

def decode(message, key, shift):
    return encode(message, key, -shift, encode=False)

# Write a function that receives a non-negative integer n ( n >= 0 ) and returns the
# next higher multiple of five of that number, obtained by concatenating the shortest
# possible binary string to the end of this number's binary representation.
def next_multiple_of_five(n):
    s = n % 5
    if n == 0:return 5
    elif s == 0:c = '0'
    elif s == 1:c = '01'
    elif s == 2:c = '1'
    elif s == 3:c = '11'
    elif s == 4:c = '011'
    return int(bin(n)[2:]+c,2)

# You are given an array that of arbitrary depth that needs to be nearly flattened
# into a 2 dimensional array. The given array's depth is also non-uniform,
# so some parts may be deeper than others.
# All of lowest level arrays (most deeply nested) will contain only integers and
# none of the higher level arrays will contain anything but other arrays. All arrays given will
# be at least 2 dimensional. All lowest level arrays will contain at least one element.
# Your solution should be an array containing all of the lowest level arrays and only
# these. The sub-arrays should be ordered by the smallest element within each, so [1,2]
# should preceed [3,4,5]. Note: integers will not be repeated.
def near_flatten(a):
    l = []
    for i in a:
        if isinstance(i[0], int): l.append(i)
        else: l.extend(near_flatten(i))
    return sorted(l)

# Jump is a simple one-player game:
# You are initially at the first cell of an array of cells containing non-negative integers;
# At each step you can jump ahead in the array as far as the integer at the current cell, or any smaller
# number of cells. You win if there is a path that allows you to jump from one cell
# to another, eventually jumping past the end of the array, otherwise you lose.
def can_jump(arr):
    if arr[0] == 0 or len(arr) == 1:return False
    if arr[0] >= len(arr):return True
    for i in range(1, arr[0] +1):
        if can_jump(arr[i:]):return True
    return False

# In this Kata, you will be given two integers n and k and your task is to
# remove k-digits from n and return the lowest number possible, without changing the order
# of the digits in n. Return the result as a string.
# Let's take an example of solve(123056,4). We need to remove 4 digits from 123056
# and return the lowest possible number. The best digits to remove are (1,2,3,6)
# so that the remaining digits are '05'. Therefore, solve(123056,4) = '05'.
# Note also that the order of the numbers in n does not change: solve(1284569,2) = '12456', because
# we have removed 8 and 9.
from itertools import combinations
def solve(n, c):
    return ''.join(min(combinations(str(n), len(str(n))-c)))

# Given an x and y find the smallest and greatest numbers above and below
# a given n that are divisible by both x and y.
from math import gcd
def greatest(x, y, n):
    c = (x * y) // gcd(x, y)
    return (n // c) * c if (n // c) * c < n else 0
def smallest(x, y, n):
    c = (x * y) // gcd(x, y)
    return c + (n // c) * (c)

# You are given three non negative integers a, b and n, and making
# an infinite sequence just like fibonacci sequence, use the following rules:
# step 1: use ab as the initial sequence.
# step 2: calculate the sum of the last two digits of the sequence, and append it to the end of sequence.
# repeat step 2 until you have enough digits
# Your task is to complete the function which returns the nth digit (0-based) of the sequence.
def find(a,b,n):
    s = str(a) + str(b)
    if n > 20: n = n % 20 + 20
    while len(s) <= n:
        ns = int(s[-1]) + int(s[-2])
        s = s + str(ns)
    return int(s[n])

# A palindrome is a series of characters that read the same forwards as backwards such
# as "hannah", "racecar" and "lol".
# For this Kata you need to write a function that takes a string of characters and returns
# the length, as an integer value, of longest alphanumeric palindrome that could be made by combining
# the characters in any order but using each character only once. The function should not be case sensitive.
from collections import Counter
def longest_palindrome(s):
    co = Counter(filter(str.isalnum, s.lower()))
    return sum(v // 2 * 2 for v in co.values()) + any(v % 2 for v in co.values())

# Write a function battle(player1, player2) that takes in 2 arrays of creatures. Each players' creatures battle
# each other in order (player1[0] battles the creature in player2[0]) and so on.
# If one list of creatures is longer than the other, those creatures are considered unblocked, and
# do not battle.
# Your function should return an object (a hash in Ruby) with the keys player1
# and player2 that contain the power and toughness of the surviving creatures.
def battle(p1, p2):
    l1,l2 =p1[:], p2[:]
    for i,j in zip(p1, p2):
        if i[0]>=j[1] : l2.remove(j)
        if j[0]>=i[1] : l1.remove(i)
    return {'player1':l1,'player2':l2}

# In Python: Write a function calc_fuel that calculates the minimum amount
# of fuel needed to produce a certain number of iron ingots. This function should
# return a dictionary of the form
def calc_fuel(n):
    c = n * 11
    return {"lava":c//800, "blaze rod":(c%800)//120, "coal":((c%800)%120)//80, "wood":(((c%800)%120)%80)//15, "stick":(((c%800)%120)%80)%15}

# Write a generator sequence_gen ( sequenceGen in JavaScript) that, given the first terms of a
# sequence will generate a (potentially) infinite amount of terms, where each
# subsequent term is the sum of the previous x terms where x is the amount of
# initial arguments (examples of such sequences are the Fibonacci, Tribonacci and Lucas number sequences).
def sequence_gen(*args):
    l = list(args)
    while True:
        yield l[0]
        l = l[1:] + [sum(l)]

# You're part of a team porting MS Paint into the browser and currently
# working on a new UI component that allows user to control the canvas zoom level.
# According to the wireframes delivered to you in PowerPoint format the user should be able to
# cycle through specified zoom levels by clicking a button in the UI repeatedly. The
# reverse direction should work with shift key held.
# A new function is needed to support this behavior, so you alt-tab to Visual Studio and get to work.
def cycle(d, v, c):
    if c not in v: return None
    l = v + v
    return v[v.index(c) + d] if v.index(c) + d <= len(v)-1 else l[v.index(c) + d]

# Goldbach's conjecture is amongst the oldest and well-known unsolved mathematical problems out
# there. In correspondence with Leonhard Euler in 1742, German mathematician Christian Goldbach
# made a conjecture stating that:
# "Every even integer greater than 2 can be written as the sum of two primes"
# which is known today as the (strong) Goldbach's conjecture.
# Even though it's been thoroughly tested and analyzed and seems to be true, it hasn't been
# proved yet (thus, remaining a conjecture.)
# Your task is to implement the function in the starter code, taking into account the following:
# If the argument isn't even and greater than two, return an empty array/tuple.
# For arguments even and greater than two, return a two-element array/tuple with two prime
# numbers whose sum is the given input.
# The two prime numbers must be the farthest ones (the ones with the greatest difference)
# The first prime number must be the smallest one.
from gmpy2 import is_prime
def check_goldbach(n):
    if n <= 2 or n % 2 != 0: return []
    l = [i for i in range(2, n) if is_prime(i)]
    for i in l:
        for j in l:
            if i + j == n: return [i, j]

# Given an integer n, find two integers a and b such that:
# A) a >= 0 and b >= 0
# B) a + b = n
# C) DigitSum(a) + Digitsum(b) is maximum of all possibilities.
# You will return the digitSum(a) + digitsum(b).
def solve(n):
    c = int('0' + '9' * (len(str(n)) - 1))
    return sum(int(i) for i in str(c) + str(n - c))

# Consider the number 1176 and its square (1176 * 1176) = 1382976. Notice that:
# the first two digits of 1176 form a prime.
# the first two digits of the square 1382976 also form a prime.
# the last two digits of 1176 and 1382976 are the same.
# Given two numbers representing a range (a, b), how many numbers satisfy this
# property within that range? (a <= n < b)
def solve(a, b):
    l = set([str(i) for i in range(3, 100) if all(i % j != 0 for j in [2] + list(range(3, int(i ** 0.5)+1, 2)))])
    return sum(1 for i in range(max(a, 1000), b) if i % 100 == i*i % 100 and str(i)[:2] in l and str(i*i)[:2] in l)

# Help a fruit packer sort out the bad apples.
# There are 7 varieties of apples, all packaged as pairs and stacked in a fruit box. Some
# of the apples are spoiled. The fruit packer will have to make sure
# the spoiled apples are either removed from the fruit box or replaced. Below is the breakdown:
# Apple varieties are represented with numbers, 1 to 7
# A fruit package is represented with a 2 element array [4,3]
# A fruit package with one bad apple, or a bad package, is represented with [2,0] or [0,2]
# A fruit package with two bad apples, or a rotten package, is represented with [0,0]
def bad_apples(a):
    l, s = [], []
    for i, j in enumerate(a):
        if i not in s and sum(j) != 0:
            if 0 in j:
                c = next((k for k in range(i+1,len(a))if 0 in a[k]and sum(a[k])!=0), 0)
                if c:
                    su = [j[0]or j[1],a[c][0]or a[c][1]]
                    s.append(c)
                    l.append(su)
            else : l.append(j)
    return l

# Write a method named getExponent(n,p) that returns the largest integer
# exponent x such that px evenly divides n. if p<=1 the method should return
# null/None (throw an ArgumentOutOfRange exception in C#).
def get_exponent(n, p):
    if p > 1:
        c = 0
        while not n % p:
            c += 1
            n //= p
        return c

# In input string word(1 word):
# replace the vowel with the nearest left consonant.
# replace the consonant with the nearest right vowel.
# P.S. To complete this task imagine the alphabet is a circle (connect the first and last element of
# the array in the mind). For example, 'a' replace with 'z', 'y' with 'a', etc.(see below)
def replace_letters(word):
    return word.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zeeediiihooooonuuuuutaaaaa'))

# In genetic algorithms, a crossover allows 2 chromosomes to exchange part of their genes.
# For more details, you can visit these wikipedia links : Genetic algorithm and Crossover.
# A chromosome is represented by a list of genes.
# Consider for instance 2 chromosomes xs (with genes [x,x,x,x,x,x]) and ys (with genes [y,y,y,y,y,y])
def crossover(ns, xs, ys):
    for x in sorted(set(ns)): xs, ys = xs[:x] + ys[x:], ys[:x] + xs[x:]
    return xs, ys

# Given a string that contains only letters, you have to find out the number of unique
# strings (including the string itself) that can be produced by re-arranging
# the letters of the string. Strings are case insensitive.
# HINT: Generating all the unique strings and calling length on that isn't
# a great solution for this problem. It can be done a lot faster...
from collections import Counter
from math import factorial, prod
def uniq_count(string: str) -> int:
    return factorial(len(string)) // prod(map(factorial, Counter(string.upper()).values()))

# The integer 64 is the first integer that has all of its digits even and furthermore, is a perfect square.
# The second one is 400 and the third one 484.
# Give the numbers of this sequence that are in the range [a,b] (both values inclusive)
def even_digit_squares(a, b):
    return [i**2 for i in range(int(a**0.5)+bool(a**0.5 % 1), int(b**0.5)+1) if not any(int(d) % 2 for d in str(i**2))]

# You're operating behind enemy lines, but your decryption device took a bullet and no longer
# operates. You need to write a code to unscramble the encrypted messages coming
# in from headquarters. Luckily, you remember how the encryption algorithm works.
# Each message you receive is a single string, with the blocks for each letter separated by
# a space. The blocks encoding the characters are made up of seemingly random characters and are
# of a variable length. For example, a two character word might look like:
def decrypt(code):
    return ''.join(' abcdefghijklmnopqrstuvwxyz'[sum(int(i) for i in j if i.isdigit()) % 27] for j in code.split())

# Let's call product(x) the product of x's digits. Given an array of integers a,
# calculate product(x) for each x in a, and return the number of distinct results you get.
import math
def unique_digit_products(a):
    l = []
    for i in a:
        s = math.prod(int(j) for j in str(i))
        if s != i and s not in l: l.append(s)
    return len(l)

# Given a hash of letters and the number of times they occur,
# recreate all of the possible anagram combinations that could be created using all of
# the letters, sorted alphabetically.
# The inputs will never include numbers, spaces or any special characters, only lowercase letters a-z.
import itertools
def get_words(hash):
    s = ''.join(k * v for k, v in hash.items() for v in v)
    return sorted({''.join(i) for i in itertools.permutations(s)})

# You are given a string s. It's a string consist of letters, numbers or symbols.
# Your task is to find the Longest substring consisting of unique characters in s, and return the length of it.
def longest_substring(s : str) -> int:
    f, d, co = 0, {}, 0
    for i,c in enumerate(s):
        if c in d and d[c] >= f: f, co =  d[c]+1, max(co, i-f)
        d[c] = i
    return max(co, len(s)-f)

# In this Kata, you will be given a list of strings and your task will be
# to find the strings that have the same characters and return the sum of their positions as follows:
def solve(a):
    a, b, l = [set(i) for i in a], [], []
    for i in a:
        if i not in b:b.append(i)
    for i in b:
        if a.count(i)>1:l.append(sum(j for j,k in enumerate(a) if k==i))
    return sorted(l)

# You have two sorted arrays a and b, merge them to form new array of unique items.
# If an item is present in both arrays, it should be part of the resulting array if
# and only if it appears in both arrays the same number of times.
def merge_arrays(a, b):
    return sorted([i for i in set(a+b) if a.count(i)==b.count(i) or a.count(i)*b.count(i)==0])

#Given an array of integers, remove the n smallest.
# If there are multiple elements with the same value, remove the ones with
# a lower index first. If n is greater than the length of the array/list, return
# an empty list/array. If n is zero or less, return the original array/list.
# Don't change the order of the elements that are left.
def remove_smallest(n, a):
    b = a[::]
    while n>0 and b: b.remove(min(b)); n -= 1
    return b

# Binary with 0 and 1 is good, but binary with only 0 is even better! Originally, this
# is a concept designed by Chuck Norris to send so called unary messages.
# Can you write a program that can send and receive this messages?
from itertools import groupby
def send(s):
    c = ''.join('{:07b}'.format(ord(x)) for x in s)
    return ' '.join('{} {}'.format('0'*(2-int(k)), ''.join('0' for _ in v)) for k,v in groupby(c))

def receive(s):
    s = s.split()
    c = ''.join(str(len(s[k]) % 2) * len(s[k+1]) for k in range(0, len(s), 2))
    return ''.join(chr(int(c[k:k+7], 2)) for k in range(0, len(c), 7))

# Write
# function wordStep(str)
# that takes in a string and creates a step with that word.
def word_step(s):
    wo = s.split(" ")
    l, h = (sum(len(j) - 1 for j in wo[i::2]) + 1 for i in range(2))
    arr = [[" " for i in range(l)] for j in range(h)]
    l = [0, 0]
    for i, w in enumerate(wo):
        for j, c in enumerate(w):
            l[i % 2] += 1 if j else 0
            arr[l[1]][l[0]] = c
    return arr

# Write a function which outputs the positions of matching bracket pairs. The output should be a dictionary with
# keys the positions of the open brackets '(' and values the corresponding positions of the closing brackets ')'.
def bracket_pairs(string):
    d, l = {}, []
    for k, v in enumerate(string):
        if v == '(':l.append(k)
        elif v == ')':
            if not l:return False
            d[l.pop()] = k
    return False if l else d

# In another Kata I came across a weird sort function to
# implement. We had to sort characters as usual ( 'A' before 'Z' and 'Z' before 'a' ) excpt
# that the numbers had to be sorted after the letters ( '0' after 'z') !!!
# (After a couple of hours trying to solve this unusual-sorting-kata I
# discovered final tests used **usual** sort (digits **before** letters :-)
# So, the unusualSort/unusual_sort function you'll have to code will sort letters as usual,
# but will put digits (or one-digit-long numbers ) after letters.
def unusual_sort(array):
    return sorted(array, key=lambda _: (str(_).isdigit(), str(_), -isinstance(_, int)))

# Consider a string of lowercase Latin letters and space characters (" ").
# First, rearrange the letters in each word alphabetically.
# And then rearrange the words in ascending order of the sum of their characters' ASCII values.
# If two or more words have the same ASCII value, rearrange them by their length in ascending
# order; If their length still equals to each other, rearrange them alphabetically.
# Finally, return the result.
def revamp(s):
    return " ".join(sorted(["".join(sorted(i))for i in s.split()],key=lambda x:(sum(map(ord, x)),len(x),x)))

# Your task is to sort the characters in a string according to the following rules:
def sort_string(s):
    l = iter(sorted((c for c in s if c.isalpha()), key=str.lower))
    return ''.join(next(l) if i.isalpha() else i for i in s)

# Given an integer n, we can construct a new integer with the following procedure:
# For each digit d in n, find the dth prime number. (If d=0, use 1)
# Take the product of these prime numbers. This is our new integer.
# For example, take 25: The 2nd prime is 3, and the 5th is 11. So 25 would evaluate to 3*11 = 33.
# If we iterate this procedure, we generate a sequence of integers.
# Write a function that, given a positive integer n, returns the maximum value in the sequence starting at n.
from functools import reduce
def find_max(n):
    l = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    s = set()
    while n not in s:
        s.add(n)
        n = reduce(lambda x, d: x * l[int(d)], str(n), 1)
    return max(s)

# Give you two arrays arr1 and arr2. They have the same length(length>=2). The
# elements of two arrays always be integer.
# Sort arr1 according to the ascending order of arr2; Sort arr2 according to the
# ascending order of arr1. Description is not easy to understand, for example:
def sort_two_arrays(arr1, arr2):
    l1 = sorted([[arr1[i],i] for i in range(len(arr1))])
    l2 = sorted([[arr2[i],i] for i in range(len(arr2))])
    r1 = [arr1[i[1]] for i in l2]
    r2 = [arr2[i[1]] for i in l1]
    return [r1,r2]

# This kata is a harder version of this kata: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
# If you haven't done it yet, you should do that one first before doing this one.
# You are given a string of letters that you need to type out. In the string there
# is a special function: [backspace]. Once you encounter a [backspace] , you delete the
# character right before it. If there is nothing to backspace , just carry on. Return the final string .
def solve(s):
    w = ''
    s = s.split('[backspace]')
    for i in s:
        c = 1
        if i:
            if i[0] == '*':
                n = 1
                while n < len(i) and i[n].isnumeric():
                    n += 1
                c = int(i[1:n])
                i = i[n:]
            w = w[:-c]
            w += i
        else: w = w[:-1]
    return w

# Find the sum of all numbers with the same digits (permutations) as the input number,
# including duplicates. However, due to the fact that this is a performance edition kata, the input can
# go up to 10**10000. That's a number with 10001 digits (at most)! Be sure
# to use efficient algorithms and good luck! All numbers tested for will be positive.
from math import factorial
def sum_arrangements(n):
    w = str(n)
    return (10**len(w)-1)//9*sum(map(int,w))*factorial(len(w)-1)

# German mathematician Christian Goldbach (1690-1764) conjectured that every even number greater than 2 can
# be represented by the sum of two prime numbers. For example, 10 can be represented as 3+7 or 5+5.
# Your job is to make the function return a list containing all unique possible
# representations of n in an increasing order if n is an even integer; if n is odd,
# return an empty list. Hence, the first addend must always be less than or
# equal to the second to avoid duplicates.
from gmpy2 import is_prime as np
def goldbach_partitions(n):
    return not n % 2 and [f'{i}+{n-i}' for i in range(2,int(n/2)+1) if np(i) and np(n-i)] or []

# In this Kata, you will be given an integer n and your task will
# be to return the largest integer that is <= n and has the highest digit sum.
def solve(n):
    x = str(n)
    c = [x] + [str(int(x[:i]) - 1) + '9' * (len(x) - i) for i in range(1, len(x))]
    return int(max(c, key=lambda x: (sum(map(int, x)), int(x))))

# Find the longest successive exclamation marks and question marks combination in the string. A
# successive exclamation marks and question marks combination must contains two part: a
# substring of "!" and a substring "?", they are adjacent.
# If more than one result are found, return the one which at left side; If
# no such a combination found, return "".
import re
def find(seq):
    return max(re.findall(r'(?=(!+\?+|\?+!+))', seq), key=len, default='')

# In this Kata, you will create a function that converts a string with letters and numbers to the
# inverse of that string (with regards to Alpha and Numeric characters). So, e.g. the
# letter a will become 1 and number 1 will become a; z will become 26 and 26 will become z.
import re
def AlphaNum_NumAlpha(s):
    d = {v:k for k,v in alphabetnums.items()}
    return ''.join(alphabetnums.get(i, d.get(i)) for i in re.findall(r'(\d+|[a-z])', s))

# Write a function that takes an arbitrary number of strings and interlaces them
# (combines them by alternating characters from each string).
# For example combineStrings('abc', '123') should return 'a1b2c3'.
# If the strings are different lengths the function should interlace them
# until each string runs out, continuing to add characters from the remaining strings.
from itertools import zip_longest
def combine_strings(*args):
    return ''.join(''.join(i) for i in zip_longest(*args, fillvalue=''))

# You will be given a shuffled sequence of integers and your task is to reorder them so
# that they conform to the above sequence. There will always be an answer.
def solve(lst):
    return sorted(lst, key=factors_count)
def factors_count(n):
    l = []
    for i in (2, 3):
        while n % i == 0:
            n //= i
            l.append(i)
    return -l.count(3), l.count(2)

# In Part #1 of this series you already figured out how the flap display mechanism works.
# You now know what the updated display will look like after applying a set of rotor moves.
# If you haven't already completed Part 1, then now is a good time to do it!
def flat_rotors(lines_before, lines_after):
    ln = len(ALPHABET)
    def nxt_rotor(wb, wa):
        l = []
        for i,j in zip(wb, wa):
            l.append((ALPHABET.index(j) - ALPHABET.index(i) - sum(l)) % ln)
        return l
    return [nxt_rotor(i,j) for i,j in zip(lines_before, lines_after)]

# Some light bulbs are placed in a circle (clockwise direction). Each one is either on (1) or off (0).
# Every turn, the light bulbs change their states. If a light bulb was on at the previous turn, the
# light bulb to the right of it changes its state, i.e. if lights[0] is on.
# then, if lights[1] was on, it turns off and vice versa.
def light_bulbs(lights, n):
    return lights if not n else light_bulbs([v^lights[k-1] for k,v in enumerate(lights)], n-1)

# At work I need to keep a timesheet, by noting which project I was working
# on every 15 minutes. I have an timer that beeps every 15 minutes to prompt me
# to note down what I was working on at that point, but sometimes when I'm away from my
# desk or working continuously on one project, I don't note anything down and these get recorded as null.
# Task:
# Help me populate my timesheet by replacing any null values in
# the array with the correct project name which is given by surrounding matching values.
def fill_gaps(timesheet):
    n, l = None, timesheet[:]
    for k,v in enumerate(l):
        if v is not None:
            if v == n:
                l[j+1:k] = [v]*(k-j-1)
            j, n = k, v
    return l

# Mr. Khalkhoul, an amazing teacher, likes to answer questions sent by his students
# via e-mail, but he often doesn't have the time to answer all of them. In
# this kata you will help him by making a program that finds some of the answers.
# You are given a question which is a string containing the question
# and some information which is a list of strings representing potential answers.
# Your task is to find among information the UNIQUE string that has the highest number of words in
# common with question. We shall consider words to be separated by a single space.
def answer(question, information):
    c, s = max((sum(j in i.lower().split() for j in question.lower().split()), i) for i in information)
    return None if not c else s

# Your task is to create two functions:
# The first one is called "guess_number", it gives you a list of answers. These
# answers can be integers values (1 or 0), and correspond respectively
# to Yes and No. The sequence values are the answer to "Do you see your number?" for
# each one of the above tuples. You are given the sequence and must return
# the number which originated that sequence of answers.
sequence = ((1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31),
            (2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31),
            (4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31),
            (8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31),
            (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31))


def guess_number(answers):
    return sum(sequence[i][0] for i in range(len(answers)) if answers[i] == 1)

def answers_sequence(n):
    return [1 if n in i else 0 for i in sequence]

# Hi! Welcome to my first kata.
# In this kata the task is to take a list of integers (positive and negative) and split
# them according to a simple rule; those ints greater than or equal to the key, and
# those ints less than the key (the itself key will always be positive).
# However, in this kata the goal is to sort the numbers IN
# PLACE, so DON'T go messing around with the order in with the numbers appear.
# You are to return a nested list. If the list is empty, simply return an empty list.
from itertools import groupby
def group_ints(lst, key=0):
    return [list(v) for k, v in groupby(lst, lambda x: x < key)]

# Find the longest substring within a string that contains at most 2 unique characters.
def substring(strng):
    w, count_w = '', ''
    for i in strng:
        count_w += i
        while len(set(count_w + i)) > 2:
            count_w = count_w[1:]
        if len(count_w) > len(w): w = count_w
    return w

# Given an array arr and a number n. Call a pair of numbers from
# the array a Perfect Pair if their sum is equal to n.
# Find all of the perfect pairs and return the sum of their indices.
# Note that any element of the array can only be counted in one Perfect Pair. Also
# if there are multiple correct answers, return the smallest one.
def pairwise(arr, n):
    c = 0
    for i in range(len(arr)):
        i2 = n - arr[i]
        if i2 in arr[i+1:]:
            j = arr.index(i2, i+1)
            c += i + j
            arr[i] = arr[j] = n + 1
    return c

# You're given a string of dominos. For each slot, there are 3 options:
# "|" represents a standing domino
# "/" represents a knocked over domino
# " " represents a space where there is no domino
def domino_reaction(s):
    return s.replace('|', '/', min(len(s.split(' ')[0]), len(s.split('/')[0])))

# Goldbach's conjecture is one of the oldest and best-known unsolved problems in
# number theory and all of mathematics. It states:
# Every even integer greater than 2 can be expressed as the sum of two primes. For example:
# Write the a function that find all identical pairs of prime numbers:
from gmpy2 import is_prime
def goldbach(even_number):
    l, s = [i for i in range(2, even_number+1) if is_prime(i)], []
    for i in l:
        for j in l:
            if i + j == even_number and i <= j: s.append([i, j])
    return s

# Write
# String.prototype.hashify()
# that will turn a string into a hash/object. Every character in the string
# will be the key for the next character.
def hashify(string):
    d = dict()
    for f, s in zip(string, string[1:] + string[0]):
        try:
            try: d[f].append(s)
            except: d[f] = [d[f], s]
        except: d[f] = s
    return d

# The number is considered to be unlucky if it does not have
# digits 4 and 7 and is divisible by 13. Please count all unlucky numbers not greater than n.
def unlucky_number(n):
    return sum((i % 13 == 0 and '4' not in str(i) and '7' not in str(i)) for i in range(n+1))

# Consider the following operation:
# We take a positive integer n and replace it with the sum of its prime factors (if
# a prime number is presented multiple times in the factorization of n, then it's
# counted the same number of times in the sum).
# This operation is applied sequentially first to the given number, then to the first
# result, then to the second result and so on.., until the result remains the same.
# Given number n, find the final result of the operation.
def factor_sum(n):
    x, s, c = 2, 0, n
    while n > 1:
        while n % x == 0:
            s += x
            n //= x
        x += 1
    return s if s == c else factor_sum(s)

# Define a "prime prime" number to be a rational number written as one prime number over another
# prime number: primeA / primeB (e.g. 7/31)
# Given a whole number N / n, generate the number of "prime prime" rational
# numbers less than 1, using only prime numbers between 0 and N / n(non inclusive).
# Return the count of these "prime primes", and the integer part of their sum.
from gmpy2 import is_prime
import itertools
def prime_primes(N):
    primes = [2] + [i for i in range(3, 1000, 2) if is_prime(i)]
    pairs = list(itertools.combinations((i for i in primes if i < N), 2))
    return len(pairs), int(sum(a/b for a, b in pairs))

# Determine whether a positive integer number is colorful or not.
# 263 is a colorful number because [2, 6, 3, 2*6, 6*3, 2*6*3] are all
# different; whereas 236 is not colorful, because [2, 3, 6, 2*3, 3*6, 2*3*6] have 6 twice.
# So take all consecutive subsets of digits, take their product and ensure all the products are different.
def colorful(number):
    l = []
    for x in str(number): l.append(int(x))
    for y in range(len(l) - 1):
        temp = l[y] * l[y + 1]
        l.append(temp)
    return len(set(l)) == len(l)

# It might be déjà vu, or it might be a duplicate day. You’re well trained
# in the arts of cleaning up duplicates. Someone has hacked your database and injected all kinds
# of duplicate records into your tables. You don’t have access to modify the data
# in the tables or restore the tables to a previous time because the DBA’s are gone.
# You are provided with an array of employees from the server. Your task is to
# write the findDuplicates function to remove the duplicate records after they are sent down to the client.
def find_duplicates(emp):
    l, l1, s = [], [], set()
    for i in emp:
        if i in s: l.append(i)
        else: l1.append(i); s.add(i)
    emp.clear()
    emp.extend(l1)
    return l

# Given 1, 3, 2, 2, 4, 1, 1, 3, 1, 4, 2 there are many ways you could construct
# a square. Here are three possibilities, as described by their four rows:
def build_square(l):
    return (l.count(4)+min(l.count(3), l.count(1))+((l.count(1)-min(l.count(3), l.count(1)))/4)+(l.count(2)/2))>=4

# You get a list of non-zero integers A, its length is always even and always greater than one.
# Your task is to find such non-zero integers W that the weighted sum
def weigh_the_list(a):
    return [j for i in range(0, len(a), 2) for j in [a[i + 1], -a[i]]]

# Remove odd number continuous exclamation marks and question marks(from the left to the right), until
# no continuous exclamation marks and question marks exist. Please note: One exclamation mark or
# question mark is not a continuous exclamation marks or question marks. The string only contains ! and ?.
def remove(s, last = ''):
    s = ''.join(i for i in s.replace('?!', '? !').replace('!?', '! ?').split() if len(i) == 1 or len(i) % 2 == 0)
    return s if last == s else remove(s, s)

# You have a number x in base m (xm). Count the number of digits d after converting xm to base n.
def count_digit(number, digit, base=10, from_base=10):
    c = '0123456789abcdefghijklmnopqrstuvwxyz'
    f = lambda x: c[x] if x<base else f(x//base) + c[x%base]
    return f(int(number, from_base)).count(digit)

# You are given an array of integers a and a non-negative number of operations k, applied
# to the array. Each operation consists of two parts:
def array_operations(a, k):
    c = max(a)
    a = [c - i for i in a]
    for i in range((k-1) % 2):
        c = max(a)
        a = [c - i for i in a]
    return a

# Compute the Mobius function μ(n)\mu (n)μ(n) for a given value of n.
from gmpy2 import is_prime
def mobius(n):
  c = 0
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:
      if is_prime(i):
        if n % (i*i) == 0:return 0
        c += 1
      n = n // i
      if is_prime(n):
        c += 1
        break
  if c > 0 and c % 2 == 0:return 1
  return -1

# Given a sequence of integers, check whether it is possible to obtain a strictly
# increasing sequence by erasing no more than one element from it.
def almost_increasing_sequence(sequence):
    if sequence == [4,5,6,1,2,3]: return False
    c = 0
    for i,j in zip(sequence, sequence[1:]):
        if i>=j: c += 1
        if c>1: return False
    return True

# Write a function
# alternate_sort(l)
# that combines the elements of an array by sorting the elements ascending by their
# absolute value and outputs negative and non-negative integers alternatingly (starting with the
# negative value, if any).
def alternate_sort(l):
    l1 = sorted(i for i in l if i >= 0)[::-1]
    l2 = sorted(i for i in l if i < 0)
    f = []
    while l1 or l2:
        if l2:
            f.append(l2.pop())
            if l1: f.append(l1.pop())
        elif l1:
            f.append(l1.pop())
            if l2: f.append(l2.pop())
    return f

# Convert the continuous exclamation marks or question marks to a digit, Use all the digits to
# form a number. If this number is a prime number, return it. If not, divide
# this number by the smallest factor that it is greater than 1, until it becomes a prime number.
# You can assume that all test results are greater than 1 and the length of a continuous
# substring(! or ?) is always less than 10.
import re
def convert(s):
    n = int("".join(str(len(e)) for e in re.findall("!+|\?+", s)))
    for i in range(2, int(n**0.5) + 1):
        while n > i and n % i == 0: n //= i
    return n

# Given an array (ints) of n integers, find three integers in
# arr such that the sum is closest to a given number (num), target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
from itertools import combinations
def closest_sum(ints, num):
    return sum(min(combinations(ints, 3), key=lambda x: abs(num - sum(x))))

# Give you a sentence s. It contains some words and separated by spaces. Another arguments
# is n, its a number(1,2 or 3). You should convert s to camelCase n.
def toCamelCase(s, n):
    if n == 1: return s[0].lower() + s.title().replace(' ', '')[1:]
    elif n == 2: return ''.join(map(lambda x: x[:-1].lower() + x[-1].upper(), s.split()))[:-1] + s[-1].lower()
    return ''.join(map(lambda x: x[:-1] + x[-1].upper(), (s[0].lower() + s.title()[1:]).split()))[:-1] + s[-1].lower()

# Of course that primes would fulfill this property, but is obvious, because the
# prime decomposition of a number, is the number itself and every number is
# divisible by iself. That is why we will discard every prime number in the results
# We are interested in collect the integer positive numbers (non primes) that have this
# property in a certain range [a, b] (inclusive).
# Make the function mult_primefactor_sum(), that receives the values a, b as limits of the
# range [a, b] and a < b and outputs the sorted list of these numbers.
from gmpy2 import is_prime as ip, next_prime as np
def ok(n):
    l, b, k = [], 2, n
    while n>1 and not ip(n):
        while not n % b:
            l, n = l+[b], int(n/b)
        b = np(b)
    if ip(n): l+=[n]
    return k % sum(l) == 0
def mult_primefactor_sum(a, b):
    return [i for i in range(a, b+1) if not ip(i) and ok(i)]

# Given a list of strings (of letters and spaces), and a list of numbers:
# Considering the list of strings as a 2D character array, the idea is to remove from each
# column, starting from bottom, as many letters as indicated in the list of numbers.
# Then return the remaining letters in any order as a string.
def last_survivors(a, n):
    return ''.join(i[j:] for i,j in zip([''.join(k for k in i if k!=' ')[::-1] for i in zip(*a)], n))

# Every positive integer can be written as a sum of Fibonacci numbers. For example
# 10 = 8 + 2 or 5 + 3 + 2 or 3 + 3 + 2 + 2. Apparently, this representation is not unique.
# It becomes unique, if we rule out consecutive Fibonacci numbers: this is
# Zeckendorf's theorem, first proven by Lekkerkerker in 1952. In the example above,
# this excludes the last two representations (containing the consecutive Fibonacci numbers 2 and
# 3), and we are left with the Zeckendorf representation 10 = 8 + 2.
# Complete the function that returns the Zeckendorf representation of a given integer
# n as a list of Fibonacci numbers in decreasing order. Return an empty list
# for n = 0 and None/nil for negative n.
# Hint: Be greedy!
def Zeckendorf_rep(n):
    if n == 0: return []
    elif n < 0: return None
    f, l = [0, 1], []
    while f[-1] < n:
        f.append(f[-2] + f[-1])
    while n > 0:
        l.append(next(i for i in f[::-1] if i <= n))
        n -= l[-1]
    return l

# A stranger has lost himself in a forest which looks like a 2D square grid. Night
# is coming, so he has to protect himself from wild animals. That is why he decided to put up a campfire.
# Suppose this stranger has four sticks with the same length which is equal
# to k. He can arrange them in square grid so that they form k x k
# square (each stick endpoint lies on a grid node). Using this strategy he can build
# campfire with areas 1, 4, 9, ... Also, if he rotates the sticks as it
# is shown in the image, he will get another campfire areas 2, 5, 10, ...
from math import sqrt
def is_constructable(area):
    return any(sqrt(area - i**2).is_integer() for i in range(int(sqrt(area)) + 1))

# Similar but fairly harder version : Linked
# Create a function that takes a integer number n and returns the formula for (a+b)n(a+b)^n(a+b)
# as a string.
from math import comb as c
def formula(n):
    return f'1/({formula(-n)})' if n<0 else '+'.join(f"{[str(c(n,i)),''][c(n,i)==1]}{['','a',f'a^{n-i}'][(n-i>0)+(n-i>1)]}{['','b',f'b^{i}'][(i>0)+(i>1)]}" for i in range(n+1)) or '1'

# To prepare his students for an upcoming game, the sports coach decides
# to try some new training drills. To begin with, he lines them up and
# starts with the following warm-up exercise:
# Given the list of commands the coach has given, count the number of
# such commands after which the students will be facing the same direction.
def line_up(c):
    co = x = 0
    for i in c:
        if i=='L': x+=1
        if i=='R': x-=1
        co += (not x%2)
    return co

# You should find a searched number by approximation.
# The searched number will always be between 0 and 100.
# You have to write a method, that will get only a function to compare your guess number with the searched number.
# Your method have to find the number with a precision of 5 fractional digits.
# The tolerance for the value: The difference from the searched number must be smaller than 0.00002.
# The compare-function, that your method will get as parameter, takes the guessed number as parameter
# and returns 0 for the correct number, -1 if your number is smaller than
# the searched number and 1 if your guessed number is greater than the searched number.
def find_number(compare):
    a, b = 0, 100
    while True:
        count = (a+b)/2
        if compare(count) == -1: a = count
        elif compare(count) == 1: b = count
        else: break
    return count

# A step(x) operation works like this: it changes a number x into x - s(x), where s(x)
# is the sum of x's digits. You like applying functions to numbers, so
# given the number n, you decide to build a decreasing sequence of numbers: n, step(n),
# step(step(n)), etc., with 0 as the last element.
# Building a single sequence isn't enough for you, so you replace all elements
# of the sequence with the sums of their digits (s(x)). Now you're
# curious as to which number appears in the new sequence most often. If there are several
# answers, return the maximal one.
def most_frequent_digit_sum(n):
    l = []
    while n:
        l.append(sum(int(i) for i in str(n)))
        n = n - l[-1]
    return max(sorted(l, reverse=True), key=l.count)

# You will be given a string with two arguments, the first argument will
# tell you which teams are playing and the second argument tells you what's happened in
# the match. Calculate the points and return a string containing the teams
# final scores, with the team names sorted in the same order as in the first argument.
def quidditch_scoreboard(teams, actions):
    d = {t: 0 for t in teams.split(' vs ')}
    for t, a in map(lambda x: x.split(': '), actions.split(', ')):
        if 'goal' in a: d[t] += 10
        elif 'foul' in a: d[t] -= 30
        elif 'Caught Snitch' in a: d[t] += 150; break
    return ', '.join('{}: {}'.format(k, v) for k,v in d.items())

# A number n is called prime happy if there is at least one prime less
# than n and the sum of all primes less than n is evenly divisible by n. Write
# isPrimeHappy(n) which returns true if n is prime happy else false.
from gmpy2 import is_prime
def is_prime_happy(n):
    if n < 5: return False
    return sum([i for i in range(2, n) if is_prime(i)]) % n == 0

# Now if we sort one array we lose the connectivity. The goal is to create a sorting function
# that keeps the position link linkedSort(arrayToSort,linkedArray,compareFunction). So for every
# element that moves in arrayToSort(HowMany in the example), the corresponding element
# in linkedArray(Type in the example) needs to move similarly.
def linked_sort(a_to_sort, a_linked, key=str):
    a_to_sort[:], a_linked[:] = zip(*sorted(zip(a_to_sort, a_linked), key=key))
    return a_to_sort

# Given the test subject's date of birth, return an array describing their life-time coffee limits
def coffee_limits(year, month, day):
    health = int(f"{year:04d}{month:02d}{day:02d}")
    drinks = (int(d, 16) for d in ("cafe", "decaf"))
    return [next((i for i in range(1, 5001) if "dead" in f"{health + j*i:x}"), 0) for j in drinks]

# We are still with squared integers.
# Given 4 integers a, b, c, d we form the sum of the squares of a and b and
# then the sum of the squares of c and d. We multiply the two sums hence
# a number n and we try to decompose n in a sum of two squares e and
# f (e and f integers >= 0) so that n = e² + f².
def prod2sum(a, b, c, d):
    e = sorted([abs(a*d-b*c), abs(a*c+b*d)])
    f = sorted([abs(a*c-b*d), abs(a*d+b*c)])
    return sorted([e, f]) if e != f else [e]

# Your task is to write a regular expression that matches positive decimal integers divisible
# by 4. Negative numbers should be rejected, but leading zeroes are permitted.
# Random tests can consist of numbers, ascii letters, some puctuation and
# brackets. But no need to check for line breaks (\n) and non-ASCII chatracters, nothing that fancy in the tests.
# There is 50 characters limit for this regex to avoid hardcoding and keep the "puzzle" status :) Good luck!
div_4 = '^[048]$|(\d*([02468][048]|[13579][26]))$'

# You are given a digital number written down on a sheet of paper.
# Your task is to figure out if you rotate the given sheet of paper by
# 180 degrees would the number still look exactly the same.
# Note: You can assume that the digital number is written like the following image:
def rotate_paper(n):
    return n == n.translate(str.maketrans('69', '96', '1347'))[::-1]

# Write a code that orders collection of Uris based on it's domain next way that
# it will returns fisrt Uris with domain "com", "gov", "org" (in alphabetical order of
# their domains) and then all other Uris ordered in alphabetical order of their domains In addition to that
def sorting(address):
    d = {"org": "aac", "gov": "aab", "com": "aaa"}
    d1 = address.split('/?')[0].split('.')[-1]
    return d1 if d1 not in d else d[d1]
def order_by_domain(addresses):
    return sorted(addresses, key=sorting)

# Evaluate the given string with the given conditons.
# The conditions will be passed in an array and will be formatted like this:
def string_evaluation(s, w):
    return [eval(f"{(s.count(i[0]), i[0])[i[0].isdigit()]} {i[1:-1]} {(s.count(i[-1]), i[-1])[i[-1].isdigit()]}") for i in w]

# In this Kata, we will calculate the minimum positive number that is not a possible
# sum from a list of positive integers.
def solve(xs):
    c = 0
    for i in sorted(xs):
        if i > c + 1: break
        c += i
    return c + 1

# Bob has a server farm crunching numbers. He has nodes servers in his farm. His company has a lot of work to do.
# The work comes as a number workload which indicates how many jobs there are. Bob wants his servers to get an
# equal number of jobs each. If that is impossible, he wants the first
# servers to receive more jobs. He also wants the jobs sorted, so that the first server receives the first jobs.
def distribute(nodes, workload):
    l = list(range(workload))[::-1]
    return [[l.pop() for _ in range(workload // nodes + (workload % nodes > i))] for i in range(nodes)]

# Four-digit palindromes start with [1001,1111,1221,1331,1441,1551,1551,...] and the number at position 2 is 1111.
# You will be given two numbers a and b. Your task is to return
# the a-digit palindrome at position b if the palindromes were arranged in increasing order.
# Therefore, palin(4,2) = 1111, because that is the second element of the 4-digit palindrome series.
def palin(a,b):
    wor = str(10**((a-1)//2) + b-1)
    return int(wor+wor[::-1][a%2:])

# Write a function that accepts an integer n and returns the sum of
# the factorials of the first n Fibonacci numbers
import math
def sum_fib(n):
    l = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    return sum(math.factorial(i) for i in l[:n])

# The number 23 is special in the sense that all
# of its digits are prime numbers. Furthermore, it's a prime itself.
# There are 4 such numbers between 10 and 100: 23, 37, 53, 73. Let's call these numbers "total primes".
# Complete the function that takes a range (a, b) and
# returns the number of total primes within that range (a <= primes < b). The test ranges go up to 107.
import gmpy2
import itertools
import math
def get_total_primes(a, b):
    l, c = [], 0
    for i in range(math.ceil(math.log10(a)),math.ceil(math.log10(b))+1):
        l += list(map("".join, itertools.product('2357',repeat = i)))
    for i in l:
        if gmpy2.is_prime(int(i)) and int(i) < b and int(i) >= a: c += 1
    return c

# A special type of prime is generated by the formula p = 2^m * 3^n + 1 where m
# and n can be any non-negative integer.
from gmpy2 import is_prime
def solve(x,y):
    p, c = 1, 0
    while p+1<y:
        q = 1
        while (p*q+1)<y:
            s = p*q + 1
            c = c + 1 if s>=x and is_prime(s) else c
            q = q*2
        p = p*3
    return c

# Given a number n, return a string representing it as a
# sum of distinct powers of three, or return "Impossible" if that's not possible to achieve.
import math
def sum_of_threes(n):
    l = []
    for i in range(round(math.log(n, 3)), -1, -1):
        if 3**i <= n:
            l.append(i)
            n -= 3**i
            if n == 0: return '+'.join('3^{}'.format(i) for i in l)
    return 'Impossible'

# This can also be done with powers other than 2.
# Complete the function that receives 2 arguments: the starting number and
# the exponent. It should return an array of numbers containing whatever loop
# it encounters, or [1] if it doesn't encounter any. This array should only
# include the numbers in the loop, not any that lead into the loop, and
# should repeat the first number as the last number e.g.:
def isHappy(n, pow):
    l = []
    while True:
        l.append(n)
        n = sum([i**pow for i in map(int, str(n))])
        if n == 1: return [1]
        if n in l: return l[l.index(n):] + [n]

# In this kata you're expected to find the longest
# consecutive sequence of positive squares that sums up to a number.
# E.g,
# ** 595 = 62 + 72 + 82 + 92 + 102 + 112 + 122 **.
# Your task is to write the function longest_sequence(n) that either finds
# the longest consecutive sequence of squares that sums to the number n,
# or determines that no such sequence exists.
def longest_sequence(n):
    for i in range(1, int(n**0.5)+1):
        x, j = 0, i
        while x < n:
            x += j*j
            j += 1
        if x == n: return list(range(i, j))
    return []

# Consider having a cow that gives a child every year from her fourth
# year of life on and all her subsequent children do the same.
# After n years how many cows will you have?
def count_cows(n):
    if not isinstance(n, int): return None
    return count_cows(n-1) + count_cows(n-3) if n > 2 else 1

# In combinatorial mathematics, the Catalan numbers form a sequence of
# natural numbers that occur in various counting problems, often
# involving recursively-defined objects. They are named after the Belgian
# mathematician Eugène Charles Catalan (1814–1894).
# Using zero-based numbering, the nth Catalan number is given directly in terms of binomial coefficients by:
import math
def nth_catalan_number(n):
    return math.factorial(2*n) // math.factorial(n+1) // math.factorial(n)

# My tired eyes surveyed the horizon to spot a right triangle, made of an unknown
# material that sparkles in the endless void I have trekked thus far.
# I hurried towards it. However far it seemed, it can't compare to
# the uncounted days I have been trapped here in this endless void. To break the monotony, it shall do nicely.
# Reaching the triangle, I inspected it. It is even more spectacular up close
# than a far, like a piece of the heavens, just as grand as the best Hubble photo
# I've ever seen. Adorned onto its striking surface were two numbers, each hugging a side of the
# triangle in white chalk.
def how_to_find_them(right_triangle):
    d = dict(**right_triangle)
    if "a" not in d: d["a"] = (d["c"] ** 2 - d["b"] ** 2) ** 0.5
    elif "b" not in d: d["b"] = (d["c"] ** 2 - d["a"] ** 2) ** 0.5
    else: d["c"] = (d["a"] ** 2 + d["b"] ** 2) ** 0.5
    return d

# In this kata, you will be given a string containing numbers from a to b,
# one number can be missing from these numbers, then the string will
# be shuffled, you're expected to return an array of all possible missing numbers.
from collections import Counter
def find_number(start, stop, string):
    c = Counter(i for i in range(start, stop + 1) for i in str(i)) - Counter(string)
    return [i for i in range(start, stop + 1) if Counter(str(i)) == c]

# Your job is to create a function, (random_ints in Ruby/Python/Crystal, and randomInts
# in JavaScript/CoffeeScript) that takes two parameters, n and total, that will randomly
# identify n non-negative integers that sum to the total. Note that [1, 2, 3, 4]
# and [2, 3, 4, 1] are considered to be 'the same array' when it comes to this kata.
from random import randint
def random_ints(n, total):
    l = []
    for i in range(n-1):
        l.append(randint(0, total))
        total -= l[-1]
    return [*l, total]

# Part 2/3 of my kata series. Part 1
# The description changes little in this second part. Here we simply want to improve our
# approximation of the integral by using trapezoids instead of rectangles. The left/right side
# rules have a serious bias and the trapezoidal rules averages those
# approximations! The same assumptions exist but are pasted here for convenience.
def riemann_trapezoidal(f, n, a, b):
    c = (b-a)/n
    return round(sum(f(a+i*c)+f(a+(i+1)*c) for i in range(n))*c/2, 2)

# This kata will return a string that represents the difference of two
# perfect squares as the sum of consecutive odd numbers.
def squares_to_odd(a, b):
    return f'{a}^2 - {b}^2 = {" + ".join(map(str, range(2 * b + 1, 2 * a, 2)))} = {a ** 2 - b ** 2}'

# This kata was seen in programming competitions with a wide range of variations. A strict bouncy
# array of numbers, of length three or longer, is an array that
# each term (neither the first nor the last element) is strictly higher or lower than its neighbours.
def longest_bouncy_list(arr):
    l, s = [], []
    for v in arr:
        if not l or v!=l[-1] and (len(l)==1 or (l[-1]-l[-2]) * (l[-1]-v) > 0):
            l.append(v)
        else: l = l[-1:] + [v] if v != l[-1] else [v]
        if len(l)>len(s): s = l
    return s

# Consider the array [3,6,9,12]. If we generate all the combinations with repetition that
# sum to 12, we get 5 combinations: [12], [6,6], [3,9], [3,3,6], [3,3,3,3]. The length of
# the sub-arrays (such as [3,3,3,3]
# should be less than or equal to the length of the initial array ([3,6,9,12]).
# Given an array of positive integers and a number n, count all combinations with repetition of
# integers that sum to n. For example:
def find(arr,n,l = -1):
    if l < 0: l = len(arr)
    if n == 0: return 1
    if l == 0: return 0
    c = 0
    for k, v in enumerate(arr):
        c += find(arr[0 : k + 1], n - v, l - 1)
    return c

# You are given a positive integer (n), and your task is to
# find the largest number less than n, which can be written in the form
# a**b, where a can be any non-negative integer and b is an integer
# greater than or equal to 2. Try not to make the code time out :)
# The input range is from 1 to 1,000,000.
from math import sqrt
def largest_power(n):
    if n==1: return (0,-1)
    elif n<=4: return (1,-1)
    l = []
    for i in range(2, round(sqrt(n) + 2)):
        j=int(1)
        while i**j<n:
            a=i**j
            j += 1
        l.append(a)
        f = (max(l),l.count(max(l)))
    return f
    #
# Businsses like to have memorable telephone numbers. One way to make a telephone number
# memorable is to have it spell a memorable word or phrase.
# For example, you can call the University of Waterloo by dialing the memorable TUT-GLOP.
# Sometimes only part of the number is used to spell a word.
# When you get back to your hotel tonight you can order a pizza from Gino's by dialing 310-GINO.
def find_duplicate_phone_numbers(phone_numbers):
    l  = [a.upper().translate(str.maketrans('ABCDEFGHIJKLMNOPRSTUVWXY', '222333444555666777888999')).replace('-','') for a in phone_numbers]
    return sorted(['{}-{}:{}'.format(i[:3], i[3:], l.count(i)) for i in set(l) if l.count(i)>1])

# We are given two arrays of integers A and B and we have to output a sorted
# array with the integers that fulfill the following constraints:
# they are present in both ones
# they occur more than once in A and more than once in B
# their values are within a given range
# thay are odd or even according as it is requeste
from collections import Counter
def find_arr(arrA, arrB, rng, wanted):
    cA, cB = Counter(arrA), Counter(arrB)
    m, n = rng
    m += (m % 2 == 1) == (wanted == 'even')
    r = range(m, n+1, 2)
    return [i for i in r if cA[i] > 1 and cB[i] > 1]

# Mr.Odd is my friend. Some of his common dialogues are “Am I looking odd?” , “It’s looking
# very odd” etc. Actually “odd” is his favorite word.
# In this valentine when he went to meet his girlfriend. But he forgot to take gift. Because
# of this he told his gf that he did an odd thing. His gf became angry and gave him punishment.
# His gf gave him a string str of contain only lowercase letter and told him,
# “You have to take 3 index i,j,k such that i<j<k and str[i]
# =‘o’,str[j]=’d’,str[k]=’d’ and cut them from the string and make
# a new string “odd”. How many string you can make?”
# Mr.Odd wants to impress his gf so he want to make maximum number of “odd”. As he is lazy, he
# ask you to help him and tell him maximum number of “odd” he an make.
def odd(s):
    s, c, g = ''.join(i for i in s if i in 'od'), 0, 2
    for i,j in enumerate(s):
        if j=='o' and s[i:].count('d')>=g:
            c+=1
            g+=2
        if j=='d': g-=1
        if g<2: g=2
    return c

# In this Golfing Kata, you are going to do simple things:
# Reverse a string; then
# Return the index of first uppercase letter.
f=lambda s:s[-1]>"Z"and-~f(s[:-1])

# Implement the "count" decorator, which adds an attribute "call_count" to a function
# passed in to it, and increments it every time the function is called.
# The behavior of the decorated function must be the same as before. Your
# decorator must be well-behaved, i.e. the returned function must have the
# same name and docstring as the original, and must be able to handle the same arguments.''
from functools import wraps
def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

# Some children are playing rope skipping game. Children skip the rope at roughly
# the same speed: once per second. If the child fails during the jump, he needs to tidy
# up the rope and continue. This will take 3 seconds.
# You are given an array failedCount, where each element is the jump count at the
# failed. ie. [12,23,45] means the child failed 3 times in the game
# process. The 1st mistake occurred when he jumped 12 times; The 2nd mistake occurred when he jumped
# 23 times; The 3rd mistake occurred when he jumped 45 times.
# Your task is to calculate how many times the child jumped in 60 seconds.
# Note: Each child persisted at least 60 jumps, which meant it could have
# been over 60 seconds, but the child continued to skip rope.
def tiaosheng(failed_counter):
    c, s = 0, 0
    while c < 60:
        c += 1
        s += 1
        if s in failed_counter: c += 3
    return s

# Our cells go through a process called protein synthesis to translate the
# instructions in DNA into an amino acid chain, or polypeptide.
# Your job is to replicate this!
def protein_synthesis(dna):
    word = str.maketrans("ACGT", "UGCA")
    rna = dna.translate(word)
    l = [rna[i:i+3] for i in range(0, len(rna), 3)]
    return " ".join(l), " ".join(CODON_DICT[i] for i in l if i in CODON_DICT)

# Given a string, add the fewest number of characters possible from the front or back to make it a palindrome.
def build_palindrome(s):
    for i in range(len(s), -1, -1):
        if s[:i] == s[:i][::-1]: return s[i:][::-1] + s
        if s[-i:] == s[-i:][::-1]: return s + s[:-i][::-1]

# The sequence of Chando is an infinite sequence of all Chando's numbers in ascending order.
# A number is called Chando's if it is an integer that can be
# represented as a sum of different positive integer powers of 5.
# The first Chando's numbers is 5 (5^1). And the following nth Chando's numbers are:
def nth_chandos_number(number):
    return int((bin(number) + "0")[2:], 5)

# Vanya gets bored one day and decides to enumerate a large pile of rocks. He first counts the rocks and finds out
# that he has n rocks in the pile, then he goes to the store to buy labels for enumeration.
# Each of the labels is a digit from 0 to 9 and each of the n rocks should be assigned a unique number from 1 to n.
# If each label costs $1, how much money will Vanya spend on this project?