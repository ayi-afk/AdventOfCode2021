import typing as t
import sys
import os
import numpy as np
from benchmark import benchmark

def check_board(board) -> bool:        
    identity = np.identity(5).astype(np.uint)
    return (
        any(any(n == -5 for n in board.sum(axis=axis)) for axis in (range(2))) or
        (board * identity).sum() == -5 or
        (board * np.flip(identity, axis=1)).sum() == -1
    )


def main(draws: t.List[int], boards: t.List[t.List[t.List[int]]]) -> t.Optional[int]:
    winner = None
    boards = np.array(boards).astype(np.int)    
    winning_boards = []
    for draw in draws:                
        boards[boards==draw] = -1
        for idx, board in enumerate(boards):
            if check_board(board):
                if idx not in winning_boards:
                    winning_boards.append(idx)

                if len(winning_boards) == len(boards):
                    last_board_idx = winning_boards.pop()
                    last_board = boards[idx]
                    return last_board[last_board!=-1].sum() * draw             
    
    return None


if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (
            "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n"
            "\n"
            "22 13 17 11  0\n"
            " 8  2 23  4 24\n"
            "21  9 14 16  7\n"
            " 6 10  3 18  5\n"
            " 1 12 20 15 19\n"
            "\n"
            " 3 15  0  2 22\n"
            " 9 18 13 17  5\n"
            "19  8  7 25 23\n"
            "20 11 10 24  4\n"
            "14 21 16 12  6\n"
            "\n"
            "14 21 17 24  4\n"
            "10 16 15  9 19\n"
            "18  8 23 26 20\n"
            "22 11 13  6  5\n"
            " 2  0 12  3  7"
        )
    else:
        with open('data4a.txt') as f:
            data = f.read()
    
    lines = data.split("\n")
    
    draws = [int(it) for it in lines[0].split(",")]
    data = data[1:].replace("  ", " ").replace("\n ", "\n")
    chunks = [it for it in data.split("\n\n")]
    chunks.pop(0)
    chunks = [[ch.split(' ') for ch in chunk.split("\n")] for chunk in chunks]

    with benchmark():
        ret = main(draws, chunks)    
        
    print(ret)
