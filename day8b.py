import typing as t
import sys
import os
import numpy as np 
from benchmark import benchmark


def solve_one(signal, output):
    segments = dict()
    _960 = [set(it) for it in signal if len(it) == 6] 
    # ^ there was also _532 but it seems it was not nescecary    
    known = {
        a: set(next(it for it in signal if len(it) == b))
        for a, b in [(1, 2), (4, 4), (7, 3),  (8, 7)]
    }
    segments['a'] = known[7] - known[1]
    for it in _960:
        if len(it | known[1]) == 7:
            known[6] = it
            segments['c'] = known[8] - known[6]
            segments['f'] = known[1] - segments['c']
    eg = known[8] - known[4] - known[7]
    for it in _960:
        if eg | it == known[8]:
            known[9] = it
            segments['e'] = eg - known[9]
    for it in _960:
        if not (it == known[9] or it == known[6]):
            known[0] = it        
    segments['d'] = known[8] - known[0]
    
    segments['b'] = known[4] - known[1] - segments['d']
    known[2] = known[8] - segments['b'] - segments['f']        
    # known a,b,c,d,e,f  0,1,2,4,6,7,8 - was moving this comment down while deving
    known[3] = (known[2] - segments['e']) | segments['f']
    known[9] = known[8] - segments['e']
    known[5] = known[6] - segments['e']

    number = ""
    for out in output:
        number += str(list(known.keys())[list(known.values()).index(set(list(out)))])

    return int(number)


def main(signals: t.List[str], outputs: t.List[str]) -> int:    
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
