import typing as t
import sys
import os
import numpy as np 
from functools import partial
from benchmark import benchmark
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder as Finder



def main(data: np.array) -> int:  
    # i know it's a bit cheating
    # but i mande so many pathfinding stuff in my entire live ...
    w, h = data.shape
    grid = Grid(matrix=data)        
    start, end = grid.node(0, 0), grid.node(w-1, h-1)    
    finder = Finder()
    path, runs = finder.find_path(start, end, grid)
    print(grid.grid_str(path=path, start=start, end=end))
    return sum(data[y,x] for x, y in path) - data[0, 0]
    

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
            "1163751742\n"
            "1381373672\n"
            "2136511328\n"
            "3694931569\n"
            "7463417111\n"
            "1319128137\n"
            "1359912421\n"
            "3125421639\n"
            "1293138521\n"
            "2311944581"
        )
    else:
        with open('data15a.txt') as f:
            data = f.read()
    tmp_data = data.splitlines()    
    h, w = len(tmp_data), len(tmp_data[0])
    data = list(data.replace('\n', ''))
        
    data = np.array(data, dtype=int).reshape(w, h)
    
    with benchmark():
        print(main(data))
