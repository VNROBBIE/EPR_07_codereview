"""
Main module of the cat path optimization project.

This file connects all parts of the project:
- multi-objective optimization methods
- recursive path finding
- greedy path finding
- time measurement
"""
__author__ = "8249067, Sanchez, 8724694, Tran"

# Import optimization methods modul
from multiobjective_optimization import path_value, pareto_optimal, weighted_sum, epsilon_constraint


# Import recursive algorithm modul
from recursive_function import recursive_best_path, optimize_weighted


# Import greedy algorithm
#todo

# Import time measurement modul
from time_measurement import measure_recursive_time, measure_greedy_time


test_paths1 = [("A", "C", "D", "F"), ("A", "B", "D", "F"), ("A", "B", "E", "F")]
test_paths2 = [("A", "C", "D", "B", "E", "F"), ("A", "B", "D", "F")]
test_paths3 = [("A", "B", "D"), ("A", "C", "D")]
cat_edges = {
    ("A", "B") : (3, 2),
    ("A", "C") : (1, 0),
    ("B", "A") : (1, 0),
    ("B", "D") : (4, 5),
    ("B", "E") : (2, 1),
    ("C", "A") : (1, 0),
    ("C", "D") : (2, 3),
    ("D", "B") : (4, 5),
    ("D", "C") : (2, 3),
    ("D", "F") : (3, 4),
    ("E", "B") : (2, 1),
    ("E", "F") : (5, 0),
    ("F", "D") : (3, 4),
    ("F", "E") : (5, 0)
}


def run_optimizations():
    print("\n--- Optimization Methods ---")
    print(test_paths1)
    print("path values: ")
    print(path_value(test_paths1, cat_edges))
    print()
    print("pareto_optimal: ")
    print(pareto_optimal(test_paths1, cat_edges))
    print()
    print("weighted_sum: ")
    print(weighted_sum(test_paths1, cat_edges, 10, 1))
    print()
    print("epsilon-constraint: ")
    print(epsilon_constraint(test_paths1, cat_edges, "cost", 50))



def run_recursive():
    print("\n--- Recursive Path Algorithm ---")

    start = "A"
    goal = "F"

    result = recursive_best_path(start, goal, cat_edges, optimize_weighted)

    if result is None:
        print("No path found.")
    else:
        path, cost, fun = result
        print("Best path:", path)
        print("Total cost:", cost)
        print("Total fun:", fun)


def run_greedy():
    print("\n--- Greedy Path Algorithm ---")

    start = "A"
    goal = "F"

    result = greedy_best_path(start, goal, cat_edges)

    if result is None:
        print("No path found.")
    else:
        path, cost, fun = result
        print("Greedy path:", path)
        print("Total cost:", cost)
        print("Total fun:", fun)


def run_measurements():
    print("\nTime measurements:")

    recursive_time = measure_recursive_time()
    greedy_time = measure_greedy_time()

    print("Recursive algorithm (10000 runs):", recursive_time)
    print("Greedy algorithm (10000 runs):", greedy_time)


def main():
    while True:
        print("\n==============================")
        print(" Cat Path Optimization Menu")
        print("==============================")
        print("1 - Run optimization methods")
        print("2 - Run recursive path algorithm")
        print("3 - Run greedy path algorithm")
        print("4 - Run time measurements for the recursive and greedy algorithm")
        print("0 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            run_optimizations()
        elif choice == "2":
            run_recursive()
        elif choice == "3":
            run_greedy()
        elif choice == "4":
            run_measurements()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()


