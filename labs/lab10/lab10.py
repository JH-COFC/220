from door import Door
from button import Button
from graphics import *


def main():
    win = GraphWin('Test', 300, 300)
    door_shape = Rectangle(Point(100, 100), Point(200, 300))
    door = Door(door_shape, 'Closed')
    door.color_door('red')
    door.draw(win)
    button_shape = Rectangle(Point(100, 20), Point(200, 80))
    button = Button(button_shape, 'Exit')
    button.draw(win)
    mouseclick = Point(0, 0)

    while not button.is_clicked(mouseclick):
        mouseclick = win.getMouse()
        if door.is_clicked(mouseclick) and door.get_label() == 'Closed':
            door.open('white', 'Open')
        elif door.is_clicked(mouseclick) and door.get_label() == 'Open':
            door.close('red', 'Closed')

    win.close()


if __name__ == '__main__':
    main()
