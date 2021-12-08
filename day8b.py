import typing as t
import sys
import os
import numpy as np 
from benchmark import benchmark

def solve_one(signal: t.List[str], output: t.List[str]):
    _960 = [set(it) for it in signal if len(it) == 6] 
    # ^ there was also _532 but it seems it was not nescecary    
    known = {
        a: set(next(it for it in signal if len(it) == b))
        for a, b in [(1, 2), (4, 4), (7, 3),  (8, 7)]
    }
    a,b,c,d,e,f,g = [None] * 7 # e, f, b, d are optional but let's keep'em
    a = known[7] - known[1]
    for it in _960:
        if len(it | known[1]) == 7:
            known[6] = it
            c = known[8] - known[6]
            f = known[1] - c
            break
    eg = known[8] - known[4] - known[7]
    for it in _960:
        if eg | it == known[8]:
            known[9] = it
            e = eg - known[9]
            g = eg - e
            break
    for it in _960:
        if not (it == known[9] or it == known[6]):
            known[0] = it        
            break
    d = known[8] - known[0]    
    b = known[4] - known[1] - d
    known[2] = known[8] - b - f       
    known[3] = (known[2] - e) | f
    known[9] = known[8] - e
    known[5] = known[6] - e

    digits = []
    for out in output:
        digits.append(str(list(known.keys())[list(known.values()).index(set(list(out)))]))

    return int("".join(digits))


def main(signals: t.List[t.List[str]], outputs: t.List[t.List[str]]) -> int:    
    return sum(solve_one(*args) for args in zip(signals, outputs))
    

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n"
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n"
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n"
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n"
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n"
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n"
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n"
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n"
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n"
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
        )
    else:
        with open('data8a.txt') as f:
            data = f.read()

    data = data.split('\n')
    signals, outputs = [], []
    for d in data:
        a, b = d.split(' | ')
        signals.append(a.split(' '))
        outputs.append(b.split(' '))
    
    with benchmark():
        print(main(signals, outputs))
