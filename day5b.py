import typing as t
import sys
import os
import numpy as np

def preety_format(matrix):
    ret = np.array2string(matrix, separator="",max_line_width=120, threshold=120) 
    for it in (' [', '[', ']'):
        ret = ret.replace(it, '')
    ret = ret.replace('0', '.')
    return ret    


def main(coords: t.List[t.Tuple[int]], xmax: int, ymax: int) -> str:
    matrix = np.zeros([xmax+1, ymax]).astype(np.int)
    for a, b, x, z in coords:
        _a, _x = min(a, x), max(a, x)
        _b, _z = min(b, z), max(b, z)        
        if a == x:
            matrix[_b:_z+1, _x] += 1
        elif b == z:
            matrix[_b ,_a:_x+1] += 1
        elif abs(x-a) == abs(z-b) and x-a != 0: # arctan          
            _a, _b = a, b
            for step in range(abs(x-a) + 1):                       
                matrix[_b, _a] += 1
                _a += np.sign(x-a)
                _b += np.sign(z-b)
               
        
    # matrix_str = preety_format(matrix)
    # print(matrix_str)
    return len(matrix[matrix>=2])


if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (
            "0,9 -> 5,9\n"
            "8,0 -> 0,8\n"
            "9,4 -> 3,4\n"
            "2,2 -> 2,1\n"
            "7,0 -> 7,4\n"
            "6,4 -> 2,0\n"
            "0,9 -> 2,9\n"
            "3,4 -> 1,4\n"
            "0,0 -> 8,8\n"
            "5,5 -> 8,2"
        )
    else:
        with open('data5a.txt') as f:
            data = f.read()
    
    ymax, xmax = -np.inf, -np.inf
    
    coords = []
    for line in data.split("\n"):        
        src, dst = line.split(" -> ")        
        coord = tuple(map(int, [*src.split(","), *dst.split(",")]))        
        coords.append(coord)
        xman = max(ymax, coord[0], coord[2]) 
        ymax = max(ymax, coord[1], coord[3])

    print(main(coords, xman, ymax+1))
