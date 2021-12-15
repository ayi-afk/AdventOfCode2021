import numpy as np

def pretty_format(matrix, *, separator=""):
    ret = []
    for y in matrix:
        for x in y:
            ret.append(str(x) + separator)
        ret.append("\n")
    return "".join(ret)