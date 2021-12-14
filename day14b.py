import typing as t
import sys
import os
import numpy as np 
from functools import cached_property, partial
from benchmark import benchmark
from numba import njit
import timeit
from collections import Counter, defaultdict
from dataclasses import dataclass, field


def main(polymer: str, pairs: t.Dict[str, str], steps: int) -> int:   
    pair_count = defaultdict(int)        
    for a,b in zip(polymer[:-1], polymer[1:]):
        pair_count[a + b] += 1
    
    for _ in range(steps):     
        letters_count = defaultdict(int)   
        new_step_pair_count = defaultdict(int)        
        for pair, count in pair_count.items():            
            a, b = list(pair)
            mid = pairs[pair]            
            new_step_pair_count[a + mid] += count
            new_step_pair_count[mid + b] += count
            letters_count[a] += count
            letters_count[mid] += count
        letters_count[polymer[-1]] += 1        
        pair_count = new_step_pair_count        
    commons = Counter(letters_count).most_common()        
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
    steps = 40   
    polymer, pair_templates = data.split('\n\n')     
    pairs = {pair: particle for pair, particle in (tpl.split(' -> ') for tpl in pair_templates.split('\n'))}    
    with benchmark():
        print(main(polymer, pairs, steps))
