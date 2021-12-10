import typing as t
import sys
import os
import numpy as np 
from benchmark import benchmark
import statistics
import timeit

POINTS = {')': 1,']': 2,'}': 3,'>': 4}
SYMBOL_MAP = {'{': '}', '(': ')', '<': '>', '[': ']'}

def main(data: t.List[str]) -> int:           
    err_scores = []
    for line in data:        
        stack = []
        for ch in line:   
            if ch in SYMBOL_MAP.keys():                
                stack.append(SYMBOL_MAP[ch])
            elif ch in SYMBOL_MAP.values() and ch != stack.pop():                                
                stack = []
                break

        local_score = 0
        if stack:
            for s in reversed(stack):                        
                local_score =  local_score * 5 + POINTS[s]  
            err_scores.append(local_score)                

    return statistics.median(err_scores)

  
if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
            "[({(<(())[]>[[{[]{<()<>>\n"
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
