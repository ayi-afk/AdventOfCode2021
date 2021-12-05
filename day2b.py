import typing as t
import sys
import os

def main(data: t.List[t.Tuple[str, int]]):
    aim, horizontal, depth = 0, 0, 0
    aim_controls = {'down': 1, 'up': -1, 'forward': 0}
    
    for direction, value in data:
        # branchless bitch! ;)
        aim_control = aim_controls[direction]        
        aim += aim_control * value
        aim_control = int(not bool(aim_control))       
        horizontal += value * aim_control
        depth += value * aim * aim_control
        
    return horizontal * depth
    

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (
            "forward 5\n"
            "down 5\n"
            "forward 8\n"
            "up 3\n"
            "down 8\n"
            "forward 2"
        )
    else:
        with open('data2a.txt') as f:
            data = f.read()
    
    parsed_data = [(n[0], int(n[1])) for n in (line.split(' ') for line in data.split('\n'))]

    print(main(parsed_data))
