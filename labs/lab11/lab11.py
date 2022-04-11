from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint


def main():
    win = GraphWin('Three Door Game', 350, 350)
    door1_shape = Rectangle(Point(50, 150), Point(100, 250))
    door2_shape = Rectangle(Point(150, 150), Point(200, 250))
    door3_shape = Rectangle(Point(250, 150), Point(300, 250))
    door1 = Door(door1_shape, 'Door 1')
    door2 = Door(door2_shape, 'Door 2')
    door3 = Door(door3_shape, 'Door 3')
    door1.color_door('brown')
    door2.color_door('brown')
    door3.color_door('brown')
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)

    exit_button_shape = Rectangle(Point(250, 10), Point(300, 30))
    exit_button = Button(exit_button_shape, 'Quit')
    wins = 0
    losses = 0
    win_count_shape = Rectangle(Point(0, 20), Point(50, 40))
    loss_count_shape = Rectangle(Point(50, 20), Point(100, 40))
    win_counter = Button(win_count_shape, str(wins))
    loss_counter = Button(loss_count_shape, str(losses))
    exit_button.draw(win)
    win_counter.draw(win)
    loss_counter.draw(win)
    mouseclick = Point(0, 0)

    top_text = Text(Point(175, 50), 'I have a secret door')
    bottom_text = Text(Point(175, 275), 'Click to guess which is the secret door!')
    win_text = Text(Point(20, 10), 'Wins')
    loss_text = Text(Point(70, 10), 'Losses')
    top_text.draw(win)
    bottom_text.draw(win)
    win_text.draw(win)
    loss_text.draw(win)
    doors = [door1, door2, door3]

    while not exit_button.is_clicked(mouseclick):
        door1.set_secret(False)
        door2.set_secret(False)
        door3.set_secret(False)
        secret_door = randint(1, 3)
        if secret_door == 1:
            door1.set_secret(True)
        elif secret_door == 2:
            door2.set_secret(True)
        elif secret_door == 3:
            door3.set_secret(True)
        door1.color_door('brown')
        door2.color_door('brown')
        door3.color_door('brown')
        top_text.setText('I have a secret door')
        bottom_text.setText('Click to guess which is the secret door!')
        reset = False
        while not reset:
            mouseclick = win.getMouse()
            if door1.is_clicked(mouseclick) or door2.is_clicked(mouseclick) or door3.is_clicked(mouseclick):
                for door in doors:
                    if door.is_clicked(mouseclick):
                        if door.is_secret():
                            door.color_door('green')
                            wins += 1
                            win_counter.set_label(str(wins))
                            top_text.setText('you win!')
                            bottom_text.setText('click anywhere to play again')
                            reset = True
                        else:
                            door.color_door('red')
                            losses += 1
                            loss_counter.set_label(str(losses))
                            top_text.setText('sorry, incorrect!')
                            bottom_text.setText('click anywhere to play again')
                            reset = True

                    if door.is_secret():
                        door.color_door('green')
            elif exit_button.is_clicked(mouseclick):
                exit()
            mouseclick = win.getMouse()

    win.close()


if __name__ == "__main__":
    main()
