import typing as t
import sys
import os
import numpy as np 
from functools import partial
from benchmark import benchmark
from numba import njit
import timeit

POINTS = {')': 3,']': 57,'}': 1197,'>': 25137}
SYMBOL_MAP = {'{': '}', '(': ')', '<': '>', '[': ']'}

def main(data: t.List[str]) -> int:   
    err_score = 0
    for line in data:
        stack = []
        for ch in line:            
            if ch in SYMBOL_MAP.keys():
                stack.append(SYMBOL_MAP[ch])
            elif ch in SYMBOL_MAP.values() and ch != (expected := stack.pop()):
                err_score += POINTS[ch]
                # print(f"{line=}: {expected=} but found: {ch=} | {stack=}")
                break                    
    return err_score

main(["{"])
  
if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
           "({(<(())[]>[[{[]{<()<>>\n"
            "[(()[<>])]({[<{<<[]>>(\n"
            "{([(<{}[<>[]}>{[]{[(<()>\n"
            "(((({<>}<{<{<>}{[]{[]{}\n"
            "[[<[([]))<([[{}[[()]]]\n"
            "[{[{({}]{}}([{[{{{}}([]\n"
            "{<[[]]>}<{[{[{[]{()[[[]\n"
            "[<(<(<(<{}))><([]([]()\n"
            "<{([([[(<>()){}]>(<<{{\n"
            "<{([{{}}[<[[[<>{}]]]>[]]"
        )
    else:
        with open('data10a.txt') as f:
            data = f.read()
        
    data = data.split('\n')
    
    # print(timeit.timeit(lambda:main(data), number=100)/100)
    with benchmark():
        print(main(data))
