from contextlib import contextmanager
import time
import tracemalloc
import gc

@contextmanager
def benchmark():        
    start = time.perf_counter()
    yield          
    print(f"Execution itme {(time.perf_counter() - start):.6}sec")
    
@contextmanager
def memory():
    tracemalloc.start()
    gc.disable()
    yield
    snap = tracemalloc.take_snapshot()
    gc.enable()
    stats = snap.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    )).statistics('lineno')    
    total = sum(stat.size for stat in stats)
    print(f"Total allocated size: {(total / 1024):.1f} KB")