from os import name
import typing as t
import sys
from benchmark import benchmark
from collections import namedtuple

sys.setrecursionlimit(int(1e6))

Area = namedtuple("Area", "x1 x2 y1 y2")

"""
       x  y2
      o--------o
      | \      |
   x1 |  \     | x2
      |   \    |
      o----x---o
        y1/    (x - inpact / stop points)
        _/
       /
"""

def brute_it(x, y, dx, dy, area):
    if x > area.x2 or y < area.y1:
        return False
    if x >= area.x1 and y <= area.y2: 
        #from previous if we re sure that x <= area.x2 and y <= area.y2
        return True

    return brute_it(
        x=x+dx,
        y=y+dy,
        dx=(dx-1)*bool(dx),
        dy=dy-1,
        area=area
    )

def main(area: Area) -> int:          
    count = 0    
    for dx in range(0, area.x2 + 1):
        for dy in range(area.y1, abs(area.y1)): 
            # here i almost forgot that it can go from up and down and was forcin 0 as start :D
            count += int(brute_it(0, 0, dx, dy, area))

    return count
       

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
