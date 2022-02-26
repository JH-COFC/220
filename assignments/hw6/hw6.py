"""
Name: <Jordan Herder>
<hw6>.py

Problem: <Program displays the cash value of a number, encodes a message,
calculates the surface area and volume of a sphere,
calculates a set of summed numbers and their cubes,
and encodes a message differently. >

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.>
"""

from math import pi


def cash_converter():
    user_input = eval(input("Enter an integer:"))
    print("That is ${:.2f}".format(user_input))


def encode():
    message = input("Enter a message:")
    key = eval(input("Enter a key:"))
    coded_message = []
    output = ""
    for i in message:
        coded_message = coded_message+[(ord(i)+key)]
    for j in coded_message:
        output = output+chr(j)
    print(output)


def sphere_area(radius):
    area = (4*pi*radius**2)
    return area


def sphere_volume(radius):
    volume = (4/3)*pi*radius**3
    return volume


def sum_n(number):
    output = 0
    for i in range(1,number+1):
        output = output+i
    return output


def sum_n_cubes(number):
    output = 0
    for i in range(1,number+1):
        output = output+i**3
    return output


def encode_better():
    message = input("Enter a message:")
    key = input("Enter a key:")
    coded_message = []
    output = ""
    for i in range(len(message)):
        coded_message = coded_message + [((ord(message[i])-65)+(ord(key[i % 3])-65)) % 58]
    for j in coded_message:
        output = output+chr(j+65)
    print(output)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
