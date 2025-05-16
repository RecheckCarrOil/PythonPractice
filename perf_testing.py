import time
import cProfile
import numpy as np
from line_profiler import LineProfiler


def fast():
    arr = np.arange(1_000_000, dtype=np.float64)
    return np.sqrt(arr).sum()


def slow():
    total = 0
    for i in range(1_000_000):
        total += i ** 0.5
    return total

lp = LineProfiler()
profiled_slow = lp(slow)

profiled_slow()

lp.print_stats()


# start = time.perf_counter()
# result = slow()
# duration = time.perf_counter() - start
# print(f"Result: {result:.2f} in {duration:.4f} seconds")
#
# # cProfile.run("slow()")
#
# cProfile.run("fast()")
