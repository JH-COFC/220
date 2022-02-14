"Name: Jordan Herder"
import time

"Program displays an animated valentine's card."


from graphics import GraphWin,Polygon,Point,Text,Rectangle


def valentines_card():
    win = GraphWin("card",600,800)
    win.setCoords(0,0,600,800)
    win.setBackground("pink")
    heart = Polygon(Point(150,570),Point(235,600),Point(300,535),Point(365,600),Point(450,570),Point(300,400))
    heart.setFill("red")
    heart.setOutline("red")
    heart.draw(win)
    happy = Text(Point(300,370),"Happy Valentine's Day!")
    happy.setOutline("red")
    happy.draw(win)
    arrow_base = Rectangle(Point(590,485),Point(700,465))
    arrow_head = Polygon(Point(590,500),Point(545,475),Point(590,450))
    arrow_base.setOutline("black")
    arrow_base.setFill("black")
    arrow_head.setOutline("black")
    arrow_head.setFill("black")
    time.sleep(0.5)
    arrow_base.draw(win)
    arrow_head.draw(win)
    time.sleep(0.03)
    for i in range(150):
        arrow_head.move(-5,0)
        arrow_base.move(-5,0)
        heart.undraw()
        heart.draw(win)
        time.sleep(0.03)
    happy.undraw()
    close_prompt = Text(Point(300,370),"Click anywhere to close")
    close_prompt.setOutline("red")
    close_prompt.draw(win)
    win.getMouse()
    win.close()

valentines_card()
