"""
Name: <Jordan Herder>
<hw3>.py

Problem: <Program calculates an average for a set of numbers, the amount in a tip jar,
a square root approximation, and an approximation of pi. It also produces a sequence.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def average():
    grade_quant = eval(input("how many grades will you enter?"))
    grade = 0
    for _ in range(grade_quant):
        grade = grade + eval(input("Enter grade"))
    print("average is",(grade/grade_quant))


def tip_jar():
    tips = 0
    for _ in range(5):
        tips = tips + eval(input("how much would you like to donate?"))
    print("total tips:",tips)


def newton():
    start_value = eval(input("What number do you want to square root?"))
    approx = start_value
    times = eval(input("How many times should we improve the approximation?"))
    for _ in range(times):
        approx = (approx + (start_value/approx))/2
    print("the square root is approximately",approx)


def sequence():
    term_number = eval(input("How many terms would you like?"))
    value = 1
    for i in range(term_number):
        value = 1 + (i//2 * 2)
        print(value,end="\t")


def pi():
    terms = eval(input("how many terms in the series?"))
    pi_value = 1
    for i in range(terms):
        pi_value = pi_value * (2 + (i//2) * 2)/(1 + ((i+1)//2 * 2))
    print(pi_value*2)


if __name__ == '__main__':
    pass
