def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def exercise_1():
    """
    Find The greatest common divisor of multiple numbers read from the console.
    """
    arr = [int(x) for x in input().split()]
    previous_cmmdc = arr[0]
    for number in arr:
        previous_cmmdc = greatest_common_divisor(previous_cmmdc, number)
    return previous_cmmdc


def exercise_2(my_text):
    """
    Write a script that calculates how many vowels are in a string.
    """
    vowel = set("aeiouAEIOU")
    number_vowels = 0
    for letter in my_text:
        if letter in vowel:
            number_vowels += 1
    return number_vowels


def exercise_3(first_string, second_string):
    """
    Write a script that receives two strings and prints the number of occurrences of the first string in the second.
    """
    return second_string.count(first_string)


"""
occurences = 0
sub_len = len(substring)
for pos in range(len(string)):
    if string[pos: pos + sub_len] == substring:
        occurences += 1
"""


def exercise_4():
    pass