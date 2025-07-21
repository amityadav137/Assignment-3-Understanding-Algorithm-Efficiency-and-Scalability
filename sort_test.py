import time
import random
import matplotlib.pyplot as plt
from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort

def benchmark_sorting():
    sizes = [1000, 2000, 5000, 10000, 20000]
    times_rand, times_det = [], []

    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        start = time.time()
        randomized_quicksort(arr.copy())
        times_rand.append(time.time() - start)

        start = time.time()
        deterministic_quicksort(arr.copy())
        times_det.append(time.time() - start)

    plt.plot(sizes, times_rand, label='Randomized Quicksort')
    plt.plot(sizes, times_det, label='Deterministic Quicksort')
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.title("Sorting Algorithm Benchmark")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    benchmark_sorting()
