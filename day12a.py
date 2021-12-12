import typing as t
import sys
import os
import numpy as np 
from functools import cached_property, partial
from benchmark import benchmark
from numba import njit
import timeit
from dataclasses import dataclass, field

@dataclass
class Node:
    name: str
    nodes: t.List['Node'] = field(default_factory=list)

    @cached_property    
    def is_small_cave(self):
        return self.name.islower()

    def __repr__(self) -> str:                
        return f"{self.name}"

paths = []
def check(node:t.List['Node'], visited: set, path: t.List['Node']):
    if node.is_small_cave:
        visited.add(node.name)    
    path.append(node)
    if node.name == 'end':               
        return paths.append(path)
        
    for n in node.nodes:
        if n.name not in visited:            
            check(n, visited.copy(), path.copy())

def main(nodes: t.List['Node'], start: Node) -> int:               
    check(start, set(['start']), list())    
    return len(paths)

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
            "start-A\n"
            "start-b\n"
            "A-c\n"
            "A-b\n"
            "b-d\n"
            "A-end\n"
            "b-end"
        )
    else:
        with open('data12a.txt') as f:
            data = f.read()
        
    start = None
    nodes = {}
    for line in data.split('\n'):
        # print(line)
        a, b = line.split('-')
        if a not in nodes:
            nodes[a] = Node(a)

        if b not in nodes:
            nodes[b] = Node(b)

        nodes[a].nodes.append(nodes[b])
        nodes[b].nodes.append(nodes[a])

        for it in (a, b):
            if it == 'start':
                start = nodes[it]

    if not start:
        raise Exception("No start defined")      
    
    # print(timeit.timeit(lambda:main(data), number=100)/100)
    with benchmark():
        print(main(nodes, start))
