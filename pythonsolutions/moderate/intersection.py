from dataclasses import dataclass
from itertools import product
from typing import Optional


@dataclass
class Point:
    x: float
    y: float

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y


@dataclass
class LineSegment:
    start: Point
    end: Point

    @property
    def slope(self):
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)


def intersection(line1: LineSegment, line2: LineSegment) -> Optional[Point]:
    """Return the intersection point of two line segments if it exists

    Args:
        line1: a LineSegment instance
        line2: another LineSegment instance

    Returns:
        Point if an intersection exists, otherwise None
    """
    if line1.slope == line2.slope and any(
            x[0] == x[1] for x in product(line1, line2)):
        return

    return Point(0.0, 0.0)
