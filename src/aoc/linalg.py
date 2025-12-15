import math

def distance_2d(p0: tuple[float, float], p1: tuple[float, float]) -> float:
    return math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)


def distance_3d(p0: tuple[float, float, float], p1: tuple[float, float, float]) -> float:
    return math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2 + (p0[2]-p1[2])**2)