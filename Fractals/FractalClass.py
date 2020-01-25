from Tkinter import *
from math import sqrt, sin, cos, pi
from random import randint

class Point(object): #point class from earlier in semester with other function addded
        def __init__(self, x=0.0,y=0.0):
            self.x = float(x)
            self.y = float(y)
        
        @property
        def x(self):
            return self._x

        @x.setter
        def x(self,value):
            self._x=value
        
        @property
        def y(self):
            return self._y

        @y.setter
        def y(self,value):
            self._y=value
        
        def __str__(self):
            return ("({} , {})".format(self.x,self.y))
        
        def dist(self,otherPoint):
            return (math.sqrt( ((self.x-otherPoint.x)**2)+((self.y-otherPoint.y)**2) ))
        
        def midpt(self,otherPoint):
            return Point((self.x + otherPoint.x)/2,(self.y + otherPoint.y)/2)

        def interpt(self, other, r):
            rx=r
            if (self.x > other.x):
                rx = 1.0-r
            ry=r
            if (self.y > other.y):
                ry = 1.0-r
            x = abs(self.x-other.x) * rx + min(self.x, other.x)
            y = abs(self.y-other.y) * ry + min(self.y, other.y)
            return Point(x,y)

class Fractal(object): #init fractal object
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.num_points = 50000 #defaults for r and # of points
        self.r = 0.5
    def frac_x(self, r):
        return int((self.dimensions["max_x"] - self.dimensions["min_x"])*r)+self.dimensions["min_x"]
    def frac_y(self, r):
        return int((self.dimensions["max_y"] - self.dimensions["min_y"])*r)+self.dimensions["min_y"]

class SierpinskiTriangle(Fractal): #init dimensions for triangle
    def __init__(self, canvas):
        Fractal.__init__(self, canvas)
        v1=Point(self.dimensions["mid_x"], self.dimensions["min_y"])
        v2=Point(self.dimensions["min_x"], self.dimensions["max_y"])
        v3=Point(self.dimensions["max_x"], self.dimensions["max_y"])
        self.vertices = [v1, v2, v3]

class SierpinskiCarpet(Fractal):#init dimensions for carpet
    def __init__(self, canvas):
        Fractal.__init__(self, canvas)
        v1=Point(self.dimensions["min_x"], self.dimensions["min_y"])
        v2=Point(self.dimensions["mid_x"], self.dimensions["min_y"])
        v3=Point(self.dimensions["max_x"], self.dimensions["min_y"])
        v4=Point(self.dimensions["min_x"], self.dimensions["mid_y"])
        v5=Point(self.dimensions["max_x"], self.dimensions["mid_y"])
        v6=Point(self.dimensions["min_x"], self.dimensions["max_y"])
        v7=Point(self.dimensions["mid_x"], self.dimensions["max_y"])
        v8=Point(self.dimensions["max_x"], self.dimensions["max_y"])
        self.vertices = [v1, v2, v3, v4, v5, v6, v7, v8]
        self.num_points = 100000
        self.r = 0.66

class Pentagon(Fractal): #init dimensions for pentagon
    def __init__(self, canvas):
        Fractal.__init__(self, canvas)
        v1=Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(2 * pi / 5 + 60), self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(2 * pi / 5 + 60))
        v2=Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(4 * pi / 5 + 60), self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(4 * pi / 5 + 60))
        v3=Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(6 * pi / 5 + 60), self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(6 * pi / 5 + 60))
        v4=Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(8 * pi / 5 + 60), self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(8 * pi / 5 + 60))
        v5=Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(10 * pi / 5 + 60), self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(10 * pi / 5 + 60))
        self.vertices = [v1, v2, v3, v4, v5]
        self.r = 0.618

class Hexagon(Fractal): #init dimensions for hexagon
    def __init__(self, canvas):
        Fractal.__init__(self, canvas)
        v1=Point(self.dimensions["mid_x"], self.dimensions["min_y"])
        v2=Point(self.dimensions["min_x"], self.frac_y(0.25))
        v3=Point(self.dimensions["max_x"], self.frac_y(0.25))
        v4=Point(self.dimensions["min_x"], self.frac_y(0.75))
        v5=Point(self.dimensions["max_x"], self.frac_y(0.75))
        v6=Point(self.dimensions["mid_x"], self.dimensions["max_y"])
        self.vertices = [v1, v2, v3, v4, v5, v6]
        self.r = 0.665

class Octagon(Fractal): #init dimensions for octagon
    def __init__(self, canvas):
        Fractal.__init__(self, canvas)
        v1=Point(self.frac_x(0.2925), self.dimensions["min_y"])
        v2=Point(self.frac_x(0.7075), self.dimensions["min_y"])
        v3=Point(self.dimensions["min_x"], self.frac_y(0.2925))
        v4=Point(self.dimensions["max_x"], self.frac_y(0.2925))
        v5=Point(self.dimensions["min_x"], self.frac_y(0.7075))
        v6=Point(self.dimensions["max_x"], self.frac_y(0.7075))
        v7=Point(self.frac_x(0.2925), self.dimensions["max_y"])
        v8=Point(self.frac_x(0.7075), self.dimensions["max_y"])
        self.vertices = [v1, v2, v3, v4, v5, v6, v7, v8]
        self.num_points = 75000
        self.r = 0.705
