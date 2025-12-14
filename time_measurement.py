"""
Time measurement using timeit.
"""

import timeit

from recursive_function import recursive_best_path, optimize_weighted
from multiobjective_optimization import cat_edges



def measure_recursive_time():
    return timeit.timeit(
        lambda: recursive_best_path("A", "F", cat_edges, optimize_weighted),
        number=10000
    )




def measure_greedy_time():
    """
    todo: implement greedy algorithm.
    """
    return timeit.timeit(
        lambda: None,
        number=10000
    )




if __name__ == "__main__":
    recursive_time = measure_recursive_time()
    greedy_time = measure_greedy_time()

    print("Recursive algorithm (10000 runs):", recursive_time)
    print("Greedy algorithm (10000 runs):", greedy_time)

