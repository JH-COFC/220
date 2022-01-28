"""
Name: Jordan Herder
hw2.py

Problem: Contains functions which may be used to calculate the sum of threes, produce the multiplication table,
calculate triangle area, determine the sum of squares, and manually calculate a power result.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    answer = 0
    upper_bound = eval(input("What is the upper bound?")) + 1
    for i in range(0, upper_bound, 3):
        answer = answer + i
    print("Sum of threes is",answer)


def multiplication_table():
    for i in range(1,11):
        for j in range(1,11):
            number = j*i
            print(number,end="\t")
        print("\n")


def triangle_area():
    sidea = eval(input("Enter side a length:"))
    sideb = eval(input("Enter side b length:"))
    sidec = eval(input("Enter side c length:"))
    value_s = (sidea+sideb+sidec)/2
    answer = math.sqrt(value_s*(value_s-sidea)*(value_s-sideb)*(value_s-sidec))
    print("area is",answer)


def sum_squares():
    answer = 0
    lower_range = eval(input("Enter lower range:"))
    upper_range = eval(input("Enter upper range:")) +1
    for i in range(lower_range,upper_range):
        answer = answer + i*i
    print(answer)



def power():
    base = eval(input("Enter base"))
    exponent = eval(input("Enter exponent"))
    answer = base
    for i in range(exponent-1):
        answer = answer*base
    print(base,"^",exponent,"=",answer)


if __name__ == '__main__':
    pass
