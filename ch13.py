import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, point):
        xdiff = self.x - point.getX()
        ydiff = self.y - point.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

    def reflect_x(self):
        x = self.x
        y = self.y
        bizX = x * -1
#        return Point(bizX, y)
        bizPoint = Point(bizX, y)
        return bizPoint

    def get_line_to(self, point2):
        a = (self.y - point2.getY()) / (self.x - point2.getX())
        b = self.y - (a * self.x)
        line = (a, b)
        return line




print(Point(4, 11).get_line_to(Point(6, 15)))
