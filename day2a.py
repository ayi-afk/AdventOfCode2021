import typing as t
import sys
import os
from collections import defaultdict

def main(data: t.List[t.Tuple[str, int]]):
    sums = defaultdict(int)
    for direction, value in data:
        sums[direction] += value
    return sums['forward'] * (sums['down'] - sums['up'])
    

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (
            "forward 5\n"
            "down 5\n"
            "forward 8\n"
            "up 3\n"
            "down 8\n"
            "forward 2"
        )
    else:
        with open('data2a.txt') as f:
            data = f.read()
    
    parsed_data = [(n[0], int(n[1])) for n in (line.split(' ') for line in data.split('\n'))]

    print(main(parsed_data))
