class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Pair:
    def __init__(self, point_1=Point, point_2=Point):
        self.point_1 = point_1
        self.point_2 = point_2


class Figure:
    def __init__(self, pairs=list):
        self.pairs = pairs

    def point_in_figure(self, point):
        pass