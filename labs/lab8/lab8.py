import math
import time
from random import randint
from graphics import *


def get_random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color


def did_collide(ball, ball2):
    center_one = ball.getCenter()
    radius_one = ball.getRadius()
    center_two = ball2.getCenter()
    radius_two = ball2.getRadius()
    center_distance = math.sqrt(
        (center_two.getX() - center_one.getX())**2 + (center_two.getY() - center_one.getY())**2)
    if center_distance <= radius_one + radius_two:
        return True
    return False


def hit_vertical(ball, win):
    center = ball.getCenter()
    radius = ball.getRadius()
    if center.getX() - radius <= 0 or center.getX() + radius >= win.getWidth():
        return True
    return False


def hit_horizontal(ball, win):
    center = ball.getCenter()
    radius = ball.getRadius()
    if center.getY() - radius <= 0 or center.getY() + radius >= win.getHeight():
        return True
    return False


def get_random(move_amount):
    random_number = randint(-1*move_amount, move_amount)
    return random_number


def bumper_balls():
    win = GraphWin('Joyride', 600, 600)
    win.setCoords(0, 0, 600, 600)
    ball1 = Circle(Point(150, 150), 15)
    ball2 = Circle(Point(50, 50), 15)
    ball1.setFill(get_random_color())
    ball1.setOutline(get_random_color())
    ball2.setFill(get_random_color())
    ball2.setOutline(get_random_color())
    ball1.draw(win)
    ball2.draw(win)
    close_prompt = Text(Point(300, 30), 'click anywhere to close')

    x_velocity1 = get_random(5)
    y_velocity1 = get_random(5)
    x_velocity2 = get_random(5)
    y_velocity2 = get_random(5)

    while not win.checkMouse():
        time.sleep(0.025)
        ball1.move(x_velocity1,y_velocity1)
        ball1.undraw()
        ball1.draw(win)
        ball2.move(x_velocity2, y_velocity2)
        ball2.undraw()
        ball2.draw(win)
        close_prompt.undraw()
        close_prompt.draw(win)

        if did_collide(ball1, ball2):
            x_velocity1 = -1 * x_velocity1
            y_velocity1 = -1 * y_velocity1
            x_velocity2 = -1 * x_velocity2
            y_velocity2 = -1 * y_velocity2

        if hit_horizontal(ball1, win):
            y_velocity1 = -1 * y_velocity1

        if hit_horizontal(ball2, win):
            y_velocity2 = -1 * y_velocity2

        if hit_vertical(ball1, win):
            x_velocity1 = -1 * x_velocity1

        if hit_vertical(ball2, win):
            x_velocity2 = -1 * x_velocity2

    win.close()


if __name__ == "__main__":
    bumper_balls()
