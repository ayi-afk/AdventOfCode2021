import typing as t
import sys
import os
import numpy as np 
from benchmark import benchmark

def main(data: np.array) -> int:      
    return np.absolute(data-np.median(data)).sum() 

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "16,1,2,0,4,2,7,1,2,14"
    else:
        with open('data7a.txt') as f:
            data = f.read()
    
    arr = np.array(data.split(','), np.int)
    with benchmark():
        print(main(arr))
