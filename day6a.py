import typing as t
import sys
import os
import numpy as np
from numba import jit, njit
import tqdm

@njit
def do_one(data: np.array):
    new_born = data == 0        
    data[new_born] = 7
    data = np.append(data, [9] * new_born.sum()) - 1  
    return data

#brute force for the win
def main(data: np.array, days_to_go: int) -> int:
    for _ in tqdm.tqdm(range(days_to_go)):
        data = do_one(data)              
        # print(f"day:{_+1} -> {data}")

    return len(data)


if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "3,4,3,1,2"
        days = 80
    else:
        days = 80
        with open('data6a.txt') as f:
            data = f.read()
    
    arr = np.array(data.split(','), np.int)

    print(main(arr, days))
