import typing as t
import sys
import os
import numpy as np 
from functools import partial
from benchmark import benchmark
from numba import njit
import timeit

def main(data: np.array, num_steps: int) -> int:       
    w, h = data.shape    
    step = 0
    while data.sum() != 0:        
        step += 1  
        data += 1      
        blown = set()         
        while(gt9_cords := list(np.argwhere(data >= 10))):
            for y, x in gt9_cords:                          
                blown.add((x, y))                
                data[max(0, y-1): min(w, y+1)+1, max(0, x-1): min(h, x+1)+1] += 1                
            for x, y in blown:
                data[y, x] = 0            
        
    return step

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
            "5483143223\n"
            "2745854711\n"
            "5264556173\n"
            "6141336146\n"
            "6357385478\n"
            "4167524645\n"
            "2176841721\n"
            "6882881134\n"
            "4846848554\n"
            "5283751526"
        )
    else:
        with open('data11a.txt') as f:
            data = f.read()
        
    data = np.array(list(data.replace('\n', '')), dtype=int).reshape(10, 10)
    
    # print(timeit.timeit(lambda:main(data), number=100)/100)
    with benchmark():
        print(main(data, 100))
