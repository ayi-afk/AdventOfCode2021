import typing as t
import sys
import os
import numpy as np 
from benchmark import benchmark

# vectorization FTW

vfuel = np.vectorize(lambda distance: int((1 + distance) / 2 * distance)) 

def main(data: np.array) -> int:  
    avg = int(np.average(data))
    return min(vfuel(np.absolute(data-val)).sum() for val in [avg, avg+1])

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "16,1,2,0,4,2,7,1,2,14"
    else:
        with open('data7a.txt') as f:
            data = f.read()
    
    arr = np.array(data.split(','), int)
    with benchmark():
        print(main(arr))
