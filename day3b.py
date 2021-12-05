import typing as t
import sys
import os
import numpy as np
from benchmark import benchmark
from numba import njit, jit

@jit
def find(data: t.List[t.List[int]], comparator: t.Callable): 
    data = data[:]
    t_data = np.array(data).T    
    row_no = 0
    while(len(t_data.T) > 1):        
        row = t_data[row_no]                  
        t_data = t_data.T[t_data.T[..., row_no] == int(comparator(row))].T        
        row_no += 1
    return int("".join(str(it) for it in list(t_data.T[0])), 2)
    

def main(data: t.List[t.List[int]]):
    oxygen = find(data, lambda row: sum(row) >= len(row)/2)
    co2 = find(data, lambda row: sum(row) < len(row)/2)
    return oxygen * co2


if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (
            "00100\n"
            "11110\n"
            "10110\n"
            "10111\n"
            "10101\n"
            "01111\n"
            "00111\n"
            "11100\n"
            "10000\n"
            "11001\n"
            "00010\n"
            "01010"
        )
    else:
        with open('data3a.txt') as f:
            data = f.read()
    
    parsed_data = [list(int(i) for i in it) for it in data.split('\n')]

    with benchmark():
        print(main(parsed_data))
