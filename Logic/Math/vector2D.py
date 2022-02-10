from __future__ import annotations
from math import atan2, radians, sin, cos, sqrt
from time import perf_counter

class Vector2D:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"(x={self.x}, y={self.y})"

    def __repr__(self) -> str:
        return f"Vector2D({self.x=}, {self.y=})"

    def __eq__(self, other: Vector2D) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self.x, self.y) == other.x, other.y

    def __lt__(self, other: Vector2D) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.magnitude < other.magnitude

    def __add__(self, other: Vector2D) -> Vector2D:
        if not isinstance(other, Vector2D):
            return NotImplemented
            
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        if not isinstance(other, Vector2D):
            return NotImplemented

        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Vector2D:
        return Vector2D(self.x * scalar, self.y * scalar)
    
    @property
    def magnitude(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y)
    
    @property
    def angle(self) -> float:
        return atan2(self.y, self.x)
    
    def dot(self, other: Vector2D) -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x * other.x + self.y * other.y

    def normalize(self) -> Vector2D:
        return Vector2D(self.x / self.magnitude, self.y / self.magnitude)

    def polar(self) -> tuple[float, float]:
        return self.magnitude, self.angle

    def rotate_cw(self, degrees: float) -> Vector2D:
        return Vector2D(
            x = round(self.x * cos(radians(-degrees)) - self.y * sin(radians(-degrees)), 4),
            y = round(self.x * sin(radians(-degrees)) + self.y * cos(radians(-degrees)), 4)
        )
    
    def rotate_ccw(self, degrees: float) -> Vector2D:
        return self.rotate_cw(-degrees)


def main():
    v  = Vector2D(0, 1)
    v2  = Vector2D(1, 0)

if __name__ == "__main__":
    main()