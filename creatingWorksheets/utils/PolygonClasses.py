import math

class Shape(object):
    def __init__(self, points):
        self.points = points
        self.lineSegments = []
        self.MakeLineSegments()

    def MakeLineSegments(self):
        for i in range(0, len(self.points)):
            newSegment = LineSegment(self.points[i], self.points[(i + 1) % len(self.points)]) #connect each point to next one (and last connects to first)
            self.lineSegments.append(newSegment)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = None

    def __add__(self, secondPoint):
        return Point(self.x + secondPoint.x, self.y + secondPoint.y)

    def __sub__(self, secondPoint):
        return Point(self.x - secondPoint.x, self.y - secondPoint.y)

    def __eq__(self, secondPoint):
        if type(secondPoint) is type(self):
            return (self.x == secondPoint.x and self.y == secondPoint.y)
        return NotImplemented

    def print(self):
        print("(", self.x, ", ", self.y, ")")

    def intCoords(self):
        return Point(int(self.x), int(self.y))

    def distance(self, secondPoint):
        return math.sqrt((self.x - secondPoint.x) ** 2 + (self.y - secondPoint.y) ** 2)

class Label(object):
    def __init__(self, x, y, size):
        self.x = x #(x,y) coordinates are center of label
        self.y = y
        self.size = size

class LineSegment(object):
    def __init__(self, point1, point2):
        #vertical is infinite slope. Handled with string
        if (point1.x == point2.x):
            self.slope = "vertical"
            self.yIntercept = "none"
            self.angleOfIncline = math.pi / 2.0
        else:
            self.slope = float(point2.y - point1.y) / (point2.x - point1.x)
            self.yIntercept = point1.y - (self.slope * point1.x)
            self.angleOfIncline = math.atan(self.slope) #in radians
            if self.angleOfIncline < 0:
                self.angleOfIncline += math.pi #angle will now be [0, pi) 

        self.minX = min(point1.x, point2.x) #For mins and maxes, this is [min, max), or else two segments will share the same point, causing issues
        self.maxX = max(point1.x, point2.x)
        self.minY = min(point1.y, point2.y) #necessary for vertical lines, since they can't be derived from the x min and max
        self.maxY = max(point1.y, point2.y)





