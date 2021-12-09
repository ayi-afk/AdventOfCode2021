import typing as t
import sys
import os
import numpy as np 
from scipy.ndimage import rank_filter
from scipy.signal import convolve2d
from functools import partial
from benchmark import benchmark
import timeit

footprint = np.array([0,1,0,1,1,1,0,1,0], dtype=float).reshape(3,3)

def main(data: np.array) -> int:   
    neightbors = rank_filter(data, 1, footprint=footprint, mode="constant", cval=9.0)    
    return np.sum(data[data < neightbors] + 1)
  
if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
            "2199943210\n"
            "3987894921\n"
            "9856789892\n"
            "8769896789\n"
            "9899965678"
        )
    else:
        with open('data9a.txt') as f:
            data = f.read()
        
    tmp = data.split('\n')
    w, h = len(tmp[0]), len(tmp)    
    tmp = list(data.replace('\n', ''))

    data = np.array(list(data.replace('\n', '')), dtype=int).reshape(h, w)   
    # print(timeit.timeit(lambda:main(data), number=100)/100)
    with benchmark():
        print(main(data))
