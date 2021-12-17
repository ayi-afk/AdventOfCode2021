from os import name
import typing as t
import sys
from benchmark import benchmark
from collections import namedtuple

Area = namedtuple("Area", "x1 x2 y1 y2")

"""
       x  y2
      o--------o
      | \      |
   x1 |  \     | x2
      |   \    |
      o----x---o
         y1    (x - inpact / stop points)
"""

def main(area: Area) -> int:      
    dy = abs(area.y1) - 1    
    return int(dy * (dy + 1) / 2)
       

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "target area: x=20..30, y=-10..-5"
    else:
        with open('data17a.txt') as f:
            data = f.read()
    
    xs, ys = data[13:].split(', ')
    xs = tuple(map(int, xs[2:].split('..')))
    ys = tuple(map(int, ys[2:].split('..')))
    area = Area(*xs, *ys)    
 
    
    with benchmark():
        print(main(area))
