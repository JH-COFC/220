"""
Name: Jordan Herder

This program calculates the Fibonacci sequence up to a given number of times,
calculates the time it takes for a principle to double for a given interest rate,
calculates the Syracuse sequence for a given starting value,
and calculates the prime components of an even number in Goldbach conjecture.

This program is entirely my own work.
"""

def fibonacci(num):
    value_1 = 1
    value_2 = 1
    hold = 0
    place = 2
    if num < 1:
        return None
    if 1 <= num <= 2:
        return 1
    if num > 2:
        while place < num:
            hold = value_1 + value_2
            value_1 = value_2
            value_2 = hold
            place += 1
        return value_2


def double_investment(principle, rate):
    acc = principle
    year = 0
    while acc < principle*2:
        acc = acc * (1 + rate)
        year += 1
    return year


def syracuse(num):
    current_number = num
    output = [num]
    while current_number > 1:
        if current_number % 2 == 0:
            test = current_number//2
            current_number = test
        elif current_number % 2 == 1:
            current_number = (current_number * 3) + 1
        output += [current_number]
    return output


def is_prime(num):
    check = 2
    flag = True
    while check < num:
        if num % check == 0:
            flag = False
            break
        check += 1
    return flag


def goldbach(num):
    if num == 2:
        return [1, 1]
    prime_1 = 1
    prime_2 = 1
    prime_list = []
    list_filler = 1
    list_index_1 = 0
    list_index_2 = 0
    if num % 2 == 1:
        return None
    while list_filler < num:
        if is_prime(list_filler):
            prime_list += [list_filler]
        list_filler += 1

    while list_index_1 <= len(prime_list) and prime_1 + prime_2 != num:
        prime_1 = prime_list[list_index_1]
        list_index_1 += 1
        list_index_2 = 0
        while list_index_2 < len(prime_list) and prime_1 + prime_2 != num:
            prime_2 = prime_list[list_index_2]
            list_index_2 += 1

    return [prime_1, prime_2]
