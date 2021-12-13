import typing as t
import sys
import numpy as np 
from benchmark import benchmark
from PIL import Image, ImageDraw


def pretty_print(cords): # a bit fun
    xmax, ymax = 0, 0
    for x, y in cords:
        xmax = max(x, xmax)
        ymax = max(y, ymax)

    print("_" * (xmax+3))
    for y in range(ymax+1):
        print("|", end="")
        for x in range(xmax+1):
            print("#" if (x, y) in cords else " ", end="")
        print("|")
    print("|",end="")
    print("-" * (xmax+1),end="")
    print("|")


def extract_ascii(cords:t.Set[t.Tuple[int, int]]) -> str:
    import pytesseract
    "super lazy as it took just 3 mins as was talking with friend hmm what if ..."
    size = 2 # not less than 2
    img = Image.new("RGB", (8*size*5+20, 20+6*size), color=(255,255,255))    
    img1 = ImageDraw.Draw(img) 
    for x,y in cords:        
         x, y = x*size+5, y*size+5
         img1.rectangle((x, y, x+size, y+size), fill="#000000")        
    text = pytesseract.image_to_string(img)
    if '\n' in text:
        return text.split('\n')[0]
    return text    

## SOME ALTERNATIVE ONE FOR FUN but 25% slower 
# def main(cords: t.Set[t.Tuple[int, int]], folds: t.List[t.Tuple[str, int]]) -> None:       
#     for axis, fold_val in folds:  
#         new_cords = set()    
#         for x, y in cords:                        
#             yless, xless = y < fold_val, x < fold_val            
#             aisx = axis == 'x'
#             aisy = not aisx 
#             y = (y * yless + (2*fold_val - y) * (not yless)) * aisy + y * aisx
#             x = (x * xless + (2*fold_val - x) * (not xless)) * aisx + x * aisy
#             new_cords.add((x, y))
#         cords = new_cords
#     pretty_print(cords)

def main(cords: t.Set[t.Tuple[int, int]], folds: t.List[t.Tuple[str, int]]) -> None:       
    for axis, fold_val in folds:  
        new_cords = set()    
        for x, y in cords:            
            if axis == 'y':            
                if y < fold_val:
                    new_cords.add((x, y))
                else:
                    new_cords.add((x, 2*fold_val-y))
            if axis == 'x':
                if x < fold_val:
                    new_cords.add((x, y))
                else:
                    new_cords.add((2*fold_val-x, y))
        cords = new_cords

    # this is just POC written in 3 mins create it as image then use tesseract to OCR it :D
    
    pretty_print(cords)
    print(extract_ascii(cords))
        

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = (            
            "6,10\n"
            "0,14\n"
            "9,10\n"
            "0,3\n"
            "10,4\n"
            "4,11\n"
            "6,0\n"
            "6,12\n"
            "4,1\n"
            "0,13\n"
            "10,12\n"
            "3,4\n"
            "3,0\n"
            "8,4\n"
            "1,10\n"
            "2,14\n"
            "8,10\n"
            "9,0\n"
            "\n"
            "fold along y=7\n"
            "fold along x=5"
        )
    else:
        with open('data13a.txt') as f:
            data = f.read()
        
    cords, folds = data.split('\n\n')
    _cords = set()
    for cord in cords.split('\n'):
        _cords.add(tuple(map(int, cord.split(","))))        
    
    _folds = []
    for fold in folds.split('\n'):
        fold = fold[11:] # using 3.8 here temporary so no removeprefix
        axis, val = fold.split('=')                
        _folds.append((axis, int(val)))    
    # ymax, xmax = y.max() + 1, x.max() + 1
    # if ymax % 2 == 0:
    #     ymax += 1
    # if xmax % 2 == 0:
    #     xmax += 1
    # page = np.zeros((ymax, xmax), dtype=int)    
    # page[y, x] = 1    
    # print(page.shape)
    
    # print(timeit.timeit(lambda:main(data), number=100)/100)
    with benchmark():
        main(_cords, _folds)
