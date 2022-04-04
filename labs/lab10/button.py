from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.text.draw(win)
        self.shape.draw(win)

    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, point):
        xrange = (self.shape.getP1().getX() < point.getX() and point.getX() <= self.shape.getP2().getX())
        yrange = (self.shape.getP1().getY() < point.getY() and point.getY() <= self.shape.getP2().getY())
        return xrange and yrange

    def color_button(self, color):
        self.shape.setOutline(color)
        self.shape.setFill(color)
