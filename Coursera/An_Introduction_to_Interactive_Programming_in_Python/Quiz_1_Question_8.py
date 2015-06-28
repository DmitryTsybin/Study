import math

def polygon_area(sides, length):
  # s = 1 / 4 * length**2 / math.tan(math.pi / sides)
  s = 1.0 / 4.0 * sides * length**2 / math.tan(math.pi / sides)
  return s

print polygon_area(5, 7)
print polygon_area(7, 3)
