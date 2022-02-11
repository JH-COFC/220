"""
Name: <Jordan Herder>
<hw4>.py

Problem: <Program allows user to draw 5 squares,
draws and provides perimeter and area values for a rectangle based on user input,
draws and provides radius value for a circle based on user input,
and approximates pi through a new method>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from math import sqrt, pi
from graphics import GraphWin, Rectangle, Circle, Point, Text


def squares():
    win = GraphWin("Clicks", 400, 400)

    num_clicks = 5

    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for _ in range(num_clicks):
        click = win.getMouse()
        upper_x = click.getX() - 25
        upper_y = click.getY() - 25
        lower_x = click.getX() + 25
        lower_y = click.getY() + 25
        upper_corner = Point(upper_x,upper_y)
        lower_corner = Point(lower_x,lower_y)
        user_square = Rectangle(upper_corner,lower_corner)
        user_square.setOutline("red")
        user_square.setFill("red")
        user_square.draw(win)

    close_prompt = Text(Point(200,200),"Click again to close")
    close_prompt.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle",400,400)
    first_click = win.getMouse()
    second_click = win.getMouse()
    user_rectangle = Rectangle(first_click,second_click)
    user_rectangle.draw(win)
    user_rectangle.setOutline("green")
    user_rectangle.setFill("green")
    x_value = abs(first_click.getX() - second_click.getX())
    y_value = abs(first_click.getY() - second_click.getY())
    area = x_value*y_value
    perimeter = 2 * x_value + 2 * y_value
    perimeter_text = Text(Point(200,320),"Perimeter")
    area_text = Text(Point(200,360),"Area")
    perimeter_display = Text(Point(200,340),perimeter)
    area_display = Text(Point(200,380),area)
    perimeter_text.draw(win)
    perimeter_display.draw(win)
    area_text.draw(win)
    area_display.draw(win)
    close_prompt = Text(Point(200,200),"Click again to close")
    close_prompt.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle",400,400)
    circle_center = win.getMouse()
    circle_edge = win.getMouse()
    x_1 = circle_center.getX()
    x_2 = circle_edge.getX()
    y_1 = circle_center.getY()
    y_2 = circle_edge.getY()
    radius = sqrt((x_2-x_1)**2 - (y_2-y_1)**2)
    user_circle = Circle(circle_center,radius)
    user_circle.setFill("cyan")
    user_circle.draw(win)
    radius_text = Text(Point(200,360),"Radius")
    radius_display = Text(Point(200,380),radius)
    radius_text.draw(win)
    radius_display.draw(win)
    close_prompt = Text(Point(200,200),"Click again to close")
    close_prompt.draw(win)
    win.getMouse()
    win.close()


def pi2():
    terms = eval(input("enter the number of terms to sum:"))
    pi_approx = 0
    for i in range(terms):
        pi_approx = pi_approx + (4-(8*(i%2)))/(1+(i*2))
    accuracy = abs(pi - pi_approx)
    print("pi_approximation:", pi_approx)
    print("accuracy:", accuracy)


if __name__ == '__main__':
    pass
