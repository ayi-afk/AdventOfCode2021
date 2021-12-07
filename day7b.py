import typing as t
import sys
import os
import numpy as np 

# vectorization FTW
vfuel = np.vectorize(lambda distance: int((1 + distance) / 2 * distance)) 

def main(data: np.array) -> int:  
    return min(vfuel(np.absolute(data-val)).sum() for val in range(data.max()))

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "16,1,2,0,4,2,7,1,2,14"
    else:
        with open('data7a.txt') as f:
            data = f.read()
    
    arr = np.array(data.split(','), np.int)

    print(main(arr))
