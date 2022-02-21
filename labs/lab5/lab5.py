from graphics import *
from math import sqrt


def triangle():
    win = GraphWin("Triangle",400,400)
    win.setCoords(0,0,400,400)
    prompt_text = Text(Point(200,180),"Click to draw a Triangle")
    prompt_text.draw(win)
    point_a = win.getMouse()
    point_b = win.getMouse()
    point_c = win.getMouse()
    user_triangle = Polygon(point_a,point_b,point_c)
    user_triangle.draw(win)
    prompt_text.undraw()
    dx_a = point_a.getX() - point_b.getX()
    dy_a = point_a.getY() - point_b.getY()
    dx_b = point_b.getX() - point_c.getX()
    dy_b = point_b.getY() - point_c.getY()
    dx_c = point_c.getX() - point_a.getX()
    dy_c = point_c.getY() - point_a.getY()
    length_a = sqrt(dx_a**2 + dy_a**2)
    length_b = sqrt(dx_b**2 + dy_b**2)
    length_c = sqrt(dx_c**2 + dy_c**2)
    sval = (length_a + length_b + length_c)/2
    area = sqrt(sval*(sval-length_a)*(sval-length_b)*(sval-length_c))
    area_text = Text(Point(200,380),"Area: {}".format(str(area)))
    area_text.draw(win)
    perimeter = length_a + length_b + length_c
    perimeter_text = Text(Point(200,360),"Perimeter: {}".format(str(perimeter)))
    perimeter_text.draw(win)
    close_prompt = Text(Point(200,200),"Click anywhere to close")
    close_prompt.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_entry = Entry(Point(win_width / 2, win_height / 2 + 40),5)
    red_entry.draw(win)

    green_entry = red_entry.clone()
    green_entry.move(0,30)
    green_entry.draw(win)

    blue_entry = red_entry.clone()
    blue_entry.move(0,60)
    blue_entry.draw(win)

    for i in range(5):
        win.getMouse()
        redval = eval(red_entry.getText())
        greenval = eval(green_entry.getText())
        blueval = eval(blue_entry.getText())
        rgbval = color_rgb(redval, greenval, blueval)
        shape.setFill(rgbval)
        shape.setOutline(rgbval)

    close_prompt = Text(Point(win_width/2,win_height/2),"Click anywhere to close")
    close_prompt.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_input = input("Enter a string")
    print(user_input[0])
    print(user_input[-1])
    print(user_input[1:5])
    print(user_input[0]+user_input[-1])
    rep_ten = ""
    for i in range(10):
        rep_ten = rep_ten + user_input[0:3]
    print(rep_ten)
    for j in user_input:
        print(j)
    print(len(user_input))


def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1]+values[3]
    print(x)
    x = values[0]+values[2]
    print(x)
    x = values[1]*5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], eval(values[5])]
    print(x)
    x = values[0] + values[2] + eval(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    series_length = eval(input("Enter the series length:"))
    output = 0
    for i in range(series_length):
        output = output + ((i%3)*2 + 2)
    print("sum=", output)


def target():
    win_width = 400
    win_height = 400
    win = GraphWin("Target",win_width,win_height)
    target_center = Point(win_width/2, win_height/2)
    inner_radius = win_height/10
    white = Circle(target_center, inner_radius*5)
    white.setFill('white')
    white.setOutline('white')
    black = Circle(target_center, inner_radius*4)
    black.setFill('black')
    black.setOutline('black')
    blue = Circle(target_center, inner_radius*3)
    blue.setFill('blue')
    blue.setOutline('blue')
    red = Circle(target_center, inner_radius*2)
    red.setFill('red')
    red.setOutline('red')
    yellow = Circle(target_center, inner_radius)
    yellow.setFill("yellow")
    yellow.setOutline("yellow")
    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)

    win.getMouse()
    win.close()


triangle()
color_shape()
process_string()
process_list()
another_series()
target()