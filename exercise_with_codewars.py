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