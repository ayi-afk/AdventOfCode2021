import typing as t
import sys
import os
import numpy as np 
from benchmark import benchmark

# vectorization FTW

vfuel = np.vectorize(lambda distance: int((1 + distance) / 2 * distance)) 

def main(signals: t.List[str], outputs: t.List[str]) -> int:      
    return sum(sum(1 for it in output if len(it) in (2,4,3,7)) for output in outputs)
    

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
