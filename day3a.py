import typing as t
import sys
import os
import numpy as np

def main(data: t.List[t.List[int]]):
    t_data = np.array(data).T
    size2 = len(t_data[0]) // 2
    values = [str(int(sum(it) > size2)) for it in t_data]
    gamma = int("".join(values), 2)
    epsilon = int("".join(str(abs(int(it) - 1)) for it in values), 2)
    return gamma * epsilon

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

    print(main(parsed_data))
