import typing as t
import sys
import os
import numpy as np 
from functools import cached_property, partial
from benchmark import benchmark
from numba import njit
import timeit
from collections import Counter
from dataclasses import dataclass, field


def main(polymer: str, pairs: t.Dict[str, str], steps: int) -> int:           
    for _ in range(steps):        
        final_polymer = ""    
        # print(f"stage: {_} -> {final_polymer or polymer}")
        for a, b in zip(polymer[:-1], polymer[1:]):
            final_polymer += a + pairs.get(a+b, "")     
        final_polymer += b   
        polymer = final_polymer

    commons = Counter(polymer).most_common()    
    return commons[0][1] - commons[-1][1]

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
            "NNCB\n"
            "\n"
            "CH -> B\n"
            "HH -> N\n"
            "CB -> H\n"
            "NH -> C\n"
            "HB -> C\n"
            "HC -> B\n"
            "HN -> C\n"
            "NN -> C\n"
            "BH -> H\n"
            "NC -> B\n"
            "NB -> B\n"
            "BN -> B\n"
            "BB -> N\n"
            "BC -> B\n"
            "CC -> N\n"
            "CN -> C"
        )
    else:
        with open('data14a.txt') as f:
            data = f.read()
    steps = 10    
    polymer, pair_templates = data.split('\n\n')     
    pairs = {pair: particle for pair, particle in (tpl.split(' -> ') for tpl in pair_templates.split('\n'))}    
    with benchmark():
        print(main(polymer, pairs, steps))
