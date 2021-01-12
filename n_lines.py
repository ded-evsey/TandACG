import matplotlib.pyplot as plt
from min_square import Point
"""
10.На плоскости задано N прямых. Требуется определить число их точек пересечения.
"""


class Line:
    def __init__(self, point_1=None, point_2=None):
        self.p1 = point_1 if point_1 else Point()
        self.p2 = point_2 if point_2 else Point()

    def __str__(self):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y])
        return f'{self.p1} {self.p2}'


def line_intersection(line1, line2):
    xdiff = (line1.p1.x - line1.p2.x, line2.p1.x - line2.p2.x)
    ydiff = (line1.p1.y - line1.p2.y, line2.p1.y - line2.p2.y)

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    def det_cls(line):
        return line.p1.x * line.p2.y - line.p1.y * line.p2.x

    div = det(xdiff, ydiff)
    if div == 0:
        return False

    def in_line(p, line):
        return (p.x - line.p1.x)(p.y - line.p2.y) == ()
    d = (det_cls(line1), det_cls(line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return Point(x, y)


if __name__ == '__main__':
    lines = []
    for _ in range(int(input('Count lines\n'))):
        lines.append(Line())
    find = []
    for line_1 in lines:
        for line_2 in lines:
            inspected = line_intersection(line_1, line_2)
            if inspected and inspected not in find:
                find.append(inspected)
    print(
        'lines:\n',
        [f"{line}" for line in lines],
        '\n find points:\n',
        [f'{point.__str__("green")}' for point in find],
        f'\n total cross {len(find)}'
    )
    plt.show()