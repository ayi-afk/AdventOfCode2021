from contextlib import contextmanager
import time

@contextmanager
def benchmark():        
    start = time.perf_counter()
    yield          
    print(f"Execution itme {(time.perf_counter() - start):.4}sec")
    