import typing as t
import sys
import os

def main(data: t.List[int]):    
    sums = list(map(sum, zip(data[:-2], data[1:-1], data[2:])))    
    return sum(a < b for a, b in zip(sums[:-1], sums[1:]))


if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "199\n200\n208\n210\n200\n207\n240\n269\n260\n263"
    else:
        with open('data1a.txt') as f:
            data = f.read()
    
    print(main([int(n) for n in data.split('\n')]))
