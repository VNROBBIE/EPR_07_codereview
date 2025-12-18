"""
Time measurement using timeit.
This module compares the runtime of the recursive and greedy algorithms.
"""

import timeit

# Import the recursive path finding algorithm and its optimization function
from recursive_function import recursive_best_path, optimize_weighted

# Import the greedy path finding algorithm
from greedy_algo import greedy_best_path

# Import the graph used for testing
from multiobjective_optimization import CAT_EDGES


def measure_recursive_time():
    """
    Measures the execution time of the recursive algorithm.
    The algorithm is executed 10,000 times to get a stable result.
    """
    return timeit.timeit(
        # lambda is used to call the function without parameters
        lambda: recursive_best_path("A", "F", CAT_EDGES, optimize_weighted),
        number=10000
    )


def measure_greedy_time():
    """
    Measures the execution time of the greedy algorithm.
    The algorithm is executed 10,000 times to get a stable result.
    """
    return timeit.timeit(
        # lambda wraps the greedy function call
        lambda: greedy_best_path(CAT_EDGES, "A", "F", "cost"),
        number=10000
    )


if __name__ == "__main__":
    # Execute time measurements
    recursive_time = measure_recursive_time()
    greedy_time = measure_greedy_time()

    # Print measured execution times
    print("Recursive algorithm (10000 runs):", recursive_time)
    print("Greedy algorithm (10000 runs):", greedy_time)
