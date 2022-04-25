from graphics import *


def read_data(filename):
    file = open(filename, 'r').read()
    file = file.replace('\n', ' ')
    split_file = file.split()
    index = 0
    while index < len(split_file):
        split_file[index] = eval(split_file[index])
        index += 1
    return split_file


def is_in_linear(search_val, values):
    index = 0
    while index < len(values):
        if search_val == values[index]:
            return True
        index += 1
    return False


def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    middle = 0
    while low <= high:
        middle = (high + low)//2
        if values[middle] > search_val:
            high = middle-1
        elif values[middle] < search_val:
            low = middle+1
        else:
            return True

    return False


def selection_sort(values):
    loops = 0
    while loops < len(values):
        smallest = values[loops]
        for value in values[loops:]:
            if value < smallest:
                smallest = value
                values.remove(value)
                values.insert(loops, smallest)
        loops += 1

    return values


def rect_sort(rectangles):
    loops = 0
    while loops < len(rectangles):
        smallest = calc_area(rectangles[loops])
        for rectangle in rectangles[loops:]:
            if calc_area(rectangle) < smallest:
                rectangle_store = rectangle
                rectangles.remove(rectangle)
                rectangles.insert(loops, rectangle_store)
        loops += 1


def calc_area(rect):
    x_length = rect.getP2().getX() - rect.getP1().getX()
    y_length = rect.getP2().getY() - rect.getP1().getY()
    return x_length * y_length
