import typing as t
import sys
import os
import numpy as np 
from functools import cached_property, partial
from benchmark import benchmark
from collections import defaultdict
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

 
def check(node:t.List[Node], visited: set, path: t.List[Node], already_visited_twice, out_paths: t.List[Node]):
    """
    all available paths are appened to out_paths var
    """
    if node.is_small_cave:
        if node.name in visited:
            already_visited_twice = True
        visited.add(node.name)
    path.append(node)
    if node.name == 'end':               
        return out_paths.append(path)
        
    for n in node.nodes:
        #comparing it by name not by object makes that 2x faster
        if n.name != 'start' and (n.name not in visited or not already_visited_twice):            
            check(n, visited.copy(), path.copy(), already_visited_twice, out_paths)

def main(nodes: t.List['Node'], start: Node) -> int:                   
    paths = []
    check(start, set(), list(), False, paths)        
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
