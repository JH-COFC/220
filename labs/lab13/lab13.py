from lab12.algorithms import *


def trade_alert(filename):
    trades = read_data(filename)
    for i in range(len(trades)):
        if 500 <= trades[i] <= 830:
            print('Alert: 500 or more trades detected {} seconds into day'.format(i))
        elif trades[i] > 830:
            print("WARNING: More than 830 trades detected {} seconds into day".format(i))


if __name__ == "__main__":
    trade_alert('trades.txt')
    bin_search_test = [2, 4, 6, 8, 10, 12, 14, 16]
    bin_result = is_in_binary(8, bin_search_test)
    print(bin_result)
    sel_sort_test = [2, 1, 3, 4, 6, 5, 0]
    print(sel_sort_test)
    selection_sort(sel_sort_test)
    v = Rectangle(Point(0,0), Point(10, 10))
    w = Rectangle(Point(0,0), Point(5, 5))
    x = Rectangle(Point(0,0), Point(15, 15))
    y = Rectangle(Point(0,0), Point(30, 30))
    z = Rectangle(Point(0,0), Point(25, 25))
    rect_sort_test = [v, w, x, y, z]
    print(rect_sort_test)
    rect_sort(rect_sort_test)
    print(sel_sort_test)
    print(rect_sort_test)
