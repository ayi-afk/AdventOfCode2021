import typing as t
import sys
import os
import numpy as np 

# no moar bruteforce ;)
def main(data: np.array) -> int:            
    return min(np.absolute(data-val).sum() for val in data)

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "16,1,2,0,4,2,7,1,2,14"
    else:
        with open('data7a.txt') as f:
            data = f.read()
    
    arr = np.array(data.split(','), np.int)

    print(main(arr))
