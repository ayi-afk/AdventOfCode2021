import typing as t
import sys
import os
import numpy as np    

# no moar bruteforce ;)
def main(data: np.array, tota_days: int) -> int:
    fishes = np.zeros(9, np.int64)    
    for d in data:
        fishes[d + 1] += 1    
    for day in range(tota_days + 1):        
        fishes[(day+7) % 9] += fishes[day % 9]        
    return fishes.sum()

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "3,4,3,1,2"
        # data = "15"
        days = 18
    
    else:
        days = 256
        with open('data6a.txt') as f:
            data = f.read()
    
    arr = np.array(data.split(','), np.int)

    print(main(arr, days))
