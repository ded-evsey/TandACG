import matplotlib.pyplot as pl


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def create_point(cls, num, type_base):
        x, y = input(
            'Введите х, y для точки '
            '{} принадлежащую к '
            '{} основанию в виде x, y '.format(
                num,
                type_base
            )
        ).split(', ')
        return cls(x, y)


class Pair:
    def __init__(self, point_1=Point, point_2=Point):
        self.point_1 = point_1
        self.point_2 = point_2

    @classmethod
    def create_pair(cls, point_1, point_2, is_pair=None):
        if not is_pair:
            is_pair = bool(input('Это парные точки ?'))
        if is_pair:
            return cls(point_1, point_2)
        return None


class Figure:
    def __init__(self, pairs=list, main_points=list):
        self.pairs = pairs
        self.main_points = main_points

    @classmethod
    def create(cls):
        count_point_on_top = 0
        while count_point_on_top < 1:
            count_point_on_top = int(input('Введите количество точек у верхнего основания '))
        count_point_on_middle = 0
        while count_point_on_middle < 3:
            count_point_on_middle = int(input('Введите количество точек у центрального основания '))
        count_point_on_bottom = 0
        while count_point_on_bottom < 1:
            count_point_on_bottom = int(input('Введите количество точек у нижнего основания '))

        def create_points(count_points, type_base):
            for i in range(count_points):
                yield (
                    Point.create_point(i, type_base)
                )

        def create_pairs(points_1, points_2):
            for point_main in points_1:
                pair = None
                for point_sub in points_2:
                    if point_sub == point_main:
                        continue
                    pair = Pair.create_pair(point_main, point_sub)
                    if pair:
                        break
                if pair:
                    yield pair
                    continue

        points_on_top = create_points(count_point_on_top, 'верхнему')
        points_on_middle = create_points(count_point_on_middle, 'центральному')
        points_on_bottom = create_points(count_point_on_bottom, 'нижнему')
        pairs = list(create_pairs(points_on_top, points_on_top))
        pairs.append(create_pairs(points_on_middle, points_on_middle))
        pairs.append(create_pairs(points_on_bottom, points_on_bottom))
        pairs.append(create_pairs(points_on_middle, points_on_top))
        pairs.append(create_pairs(points_on_middle, points_on_bottom))
        return cls(list(pairs), list(points_on_middle))

    def point_in_figure(self, point):
        pass


if __name__ == '__main__':
    fig = Figure.create()
