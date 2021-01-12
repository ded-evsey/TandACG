import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from min_square import Point, Triangle
import math
"""
Найти центр тяжести многоугольника заданного целочисленными координатами своих N вершин.
"""

"""
def triangulated_figure(fig):
    return Triangulation([point.x for point in points], [point.y for point in points])


def find_centroid_in_triangle(triangle):
    return Point(
        x=sum([point.x for point in triangle.points])/3,
        y=sum([point.y for point in triangle.points]) / 3
    )

"""
if __name__ == '__main__':
    points = []
    for _ in range(int(input('Count points\n'))):
        points.append(Point())
    centroid_points = Point(
        sum([point.x for point in points]),
        sum([point.y for point in points])
    )
    points = sorted(points, key=lambda obj: math.atan2(obj.y, obj.x))

    A = sum(
        [
            point.x * points[i+1].y - points[i+1].x * point.y
            for i, point in enumerate(points[:-1])
        ]
    )  # площадь многоугольника
    centroid_figure = Point(
        x=sum(
            [
                (point.x + points[i+1].x) * (point.x * points[i+1].y - points[i+1].x * point.y)
                for i, point in enumerate(points[:-1])
            ]
        ) / (6 * A),
        y=sum(
            [
                (point.y + points[i + 1].y) * (point.x * points[i + 1].y - points[i + 1].x * point.y)
                for i, point in enumerate(points[:-1])
            ]
        ) / (6 * A)
    )
    plt.fill(
        [point.x for point in points],
        [point.y for point in points],
        fill=False

    )
    print(centroid_figure.__str__('green'))
    plt.show()
    """    
    triangulation = triangulated_figure(points)
    triangles = [
        Triangle(
            points[triangle[0]],
            points[triangle[1]],
            points[triangle[2]]
        ) for triangle in triangulation.triangles
    ]

    total_area = sum([triangle.calc_area() for triangle in triangles])
"""
