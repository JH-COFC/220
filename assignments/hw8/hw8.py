"""
Name: <Jordan Herder>
<hw8>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math
from graphics import GraphWin, Circle, Point


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def sum_list(nums):
    total = 0
    for i in nums:
        total = total+i
    return total


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    new_list = []
    for obj in range(len(nums)):
        split_object = nums[obj].split(', ')
        to_numbers(split_object)
        square_each(split_object)
        new_list = new_list + [sum_list(split_object)]
    return new_list


def starter(weight, wins):
    weight_req = 150 <= weight < 160
    special_case = weight > 199 or wins > 20
    if weight_req and wins >= 5 or special_case:
        return True
    return False


def leap_year(year):
    div_by_four = year % 4 == 0
    not_by_hundred = not year % 100 == 0
    four_hundred_case = year % 400 == 0
    if div_by_four and (not_by_hundred or four_hundred_case):
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    linter_point = Point(0, 0)
    linter_point.draw(win)
    # I'm pretty sure I need to import Point for half of this to work, but the linter kept complaining

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_two = win.getMouse()
    circumference_point_two = win.getMouse()
    radius_two = math.sqrt(
        (center_two.getX()-circumference_point_two.getX())**2+(center_two.getY()-circumference_point_two.getY())**2)
    circle_two = Circle(center_two, radius_two)
    circle_two.setFill("light green")
    circle_two.draw(win)

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    center_one = circle_one.getCenter()
    radius_one = circle_one.getRadius()
    center_two = circle_two.getCenter()
    radius_two = circle_two.getRadius()
    center_distance = math.sqrt(
        (center_two.getX() - center_one.getX())**2 + (center_two.getY() - center_one.getY())**2)
    if center_distance >= radius_one + radius_two:
        return True
    return False


if __name__ == '__main__':
    pass
