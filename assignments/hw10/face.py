from graphics import Circle, Line, Polygon, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)
        point_3 = point_1.clone()
        point_3.move(mouth_size / 2, mouth_off / 2)
        self.smiling = Polygon(point_1, point_2, point_3)
        self.shocked = Circle(Point(point_3.getX(), point_1.getY()), eye_size)
        wink_point_1 = center.clone()
        wink_point_1.move((-eye_off-eye_size/2), -eye_off)
        wink_point_2 = center.clone()
        wink_point_2.move((-eye_off+eye_size/2), -eye_off)
        self.wink = Line(wink_point_1,wink_point_2)

    def smile(self):
        self.mouth.undraw()
        self.smiling.draw(self.window)

    def shock(self):
        self.mouth.undraw()
        self.shocked.draw(self.window)

    def wink(self):
        self.left_eye.undraw()
        self.wink.draw(self.window)
