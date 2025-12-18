"""
Three methods for different types of multiobjective optimization in a graph.
Assume a graph and a list of possible paths already exists.
"""

import doctest


test_paths1 = [("A", "C", "D", "F"), ("A", "B", "D", "F"),
               ("A", "B", "E", "F")]
test_paths2 = [("A", "C", "D", "B", "E", "F"), ("A", "B", "D", "F")]
test_paths3 = [("A", "B", "D"), ("A", "C", "D")]
cat_edges = {
    ("A", "B"): (3, 2),
    ("A", "C"): (1, 0),
    ("B", "A"): (1, 0),
    ("B", "D"): (4, 5),
    ("B", "E"): (2, 1),
    ("C", "A"): (1, 0),
    ("C", "D"): (2, 3),
    ("D", "B"): (4, 5),
    ("D", "C"): (2, 3),
    ("D", "F"): (3, 4),
    ("E", "B"): (2, 1),
    ("E", "F"): (5, 0),
    ("F", "D"): (3, 4),
    ("F", "E"): (5, 0)
}


def path_value(paths_list, edges_dict):
    """
    Sums up the costs and the fun on each path.
    :param paths_list: a list containing tuples with
    nodes stored within to represent paths
    :param edges_dict: a dictionary containing edges
    and their respective cost and fun values
    :return: a list containing tuples with each path's summed up cost and fun
    >>> path_value(test_paths1, cat_edges)
    [(6, 7), (10, 11), (10, 3)]
    >>> path_value(test_paths2, cat_edges)
    [(14, 9), (10, 11)]
    >>> path_value(test_paths3, cat_edges)
    [(7, 7), (3, 3)]
    >>> path_value([("A", "B")], {("A", "C") : (3, 2)})
    Atleast one path is invalid.
    """
    path_values = []
    for i in paths_list:
        my_path_value = [0, 0]
        for j in range(0, len(i) - 1):
            # Pair up every node on the path.
            edge_node1 = i[j]
            edge_node2 = i[j + 1]
            # Check if path is connected by edges.
            try:
                """
                Find the respective edge in edge dictionary
                and safe edge values from dictionary in new tuple.
                """
                edge_value = edges_dict[(edge_node1, edge_node2)]
            except KeyError:
                print("Atleast one path is invalid.")
                return None
            # Sum up every path value.
            for k in range(0, 2):
                my_path_value[k] += edge_value[k]
        # Add value of one path to list of path values.
        path_values.append(tuple(my_path_value))
    if len(path_values) == 0:
        return None
    return path_values


def pareto_optimal(paths_list, edges_dict):
    """
    Calculates a pareto optimal path.
    Paths that are not worse in both values than other paths are optimal.
    :param paths_list: a list containing tuples with nodes stored within
    :param edges_dict: a dictionary containing edges
    and their respective cost and fun values
    :return: a set of pareto optimal paths
    >>> (pareto_optimal(test_paths1, cat_edges) ==
    ...     {('A', 'B', 'D', 'F'), ('A', 'C', 'D', 'F')})
    True
    >>> pareto_optimal(test_paths2, cat_edges) == {('A', 'B', 'D', 'F')}
    True
    >>> (pareto_optimal(test_paths3, cat_edges)
    ...     == {('A', 'C', 'D'), ('A', 'B', 'D')})
    True
    >>> pareto_optimal([], cat_edges)
    """
    # First calculate the cost and fun values for each path.
    paths_values = path_value(paths_list, edges_dict)
    # Check if path is valid.
    if paths_values is None:
        return None
    optimal_paths = set()
    # Compare every path with every other path.
    for path1 in paths_values:
        for path2 in paths_values:
            """
            Make sure to not compare a path with itself
            or a path with another path of the same value.
            """
            if path1 == path2:
                continue
            current_cost_value = path2[0]
            current_fun_value = path2[1]
            new_cost_value = path1[0]
            new_fun_value = path1[1]
            # Every path must not be worse than any other path at both goals.
            # Cost must be low and fun must be high.
            if (new_cost_value > current_cost_value and
                    new_fun_value < current_fun_value):
                break
        else:
            # Add new path to set of pareto-optimal paths.
            my_optimal_path = paths_list[paths_values.index(path1)]
            optimal_paths.add(my_optimal_path)
    # Check if optimal path exists.
    if len(optimal_paths) == 0:
        return None
    return optimal_paths


def weighted_sum(paths_list, edges_dict, cost_weight, fun_weight):
    """
    Calculates an optimal path based on the weighted sum method.
    Cost and fun values are augmented by multiplying
    each one with a factor and then added together.
    The path with the lowest sum is the most optimal.
    :param paths_list: a list containing tuples with nodes stored within
    :param edges_dict: a dictionary containing edges
    and their respective cost and fun values
    :param cost_weight: a number value determining
    the weight of an edge's cost value
    :param fun_weight: a number value determining
    the weight of an edge's fun value
    :return: a set of optimal paths
    >>> (weighted_sum(test_paths1, cat_edges, 1, 1)
    ...     == {('A', 'C', 'D', 'F'), ('A', 'B', 'D', 'F')})
    True
    >>> weighted_sum(test_paths1, cat_edges, 5, 1) == {('A', 'C', 'D', 'F')}
    True
    >>> weighted_sum(test_paths1, cat_edges, 1, 5) == {('A', 'B', 'D', 'F')}
    True
    >>> weighted_sum(test_paths1, cat_edges, "hi", "n")
    Weight factors must be numbers.
    """
    # First calculate the cost and fun values for each path.
    paths_values = path_value(paths_list, edges_dict)
    # Check if path is valid
    if paths_values is None:
        return None
    # Check if number was entered for cost and fun weights.
    try:
        float(fun_weight)
        float(cost_weight)
    except ValueError:
        print("Weight factors must be numbers.")
        return None
    optimal_paths = set()
    paths_weighted_sums = []
    # Calculate a value for each path (weighted sum).
    for paths in paths_values:
        # Multiply by a factor based on each value's weight.
        weighted_cost = paths[0] * cost_weight
        weighted_fun = -paths[1] * fun_weight
        my_weighted_sum = weighted_cost + weighted_fun
        # Add calculated sum to list of all weighted sums.
        paths_weighted_sums.append(my_weighted_sum)
    # Check for every sum in list whether it is the smallest value.
    for i in range(0, len(paths_weighted_sums)):
        if paths_weighted_sums[i] == min(paths_weighted_sums):
            # Add path with the same index to set of optimal paths.
            optimal_paths.add(paths_list[i])
    # Check if optimal path exists.
    return optimal_paths


def epsilon_constraint(paths_list, edges_dict, main_goal, sec_goal_value):
    """
    Calculates an optimal path based on the epsilion constrain method.
    Every path has to meet a secondary goal.
    Then choose the path with the lowest cost/highest fun.
    :param paths_list: a list containing tuples with nodes stored within
    :param edges_dict: a dictionary containing edges
    and their respective cost and fun values
    :param main_goal: a string containing the
    main goal of the algorithm ("cost"/"fun")
    :param sec_goal_value: a string containing either maximum cost
    or minimum fun to meet the secondary goal
    :return: a set of optimal paths
    >>> (epsilon_constraint(test_paths1, cat_edges, "cost", 8)
    ...    == {('A', 'B', 'D', 'F')})
    True
    >>> (epsilon_constraint(test_paths1, cat_edges, "fun", 7)
    ...    == {('A', 'C', 'D', 'F')})
    True
    >>> epsilon_constraint(test_paths1, cat_edges, "cost", 50)  # negative-Test
    """
    # Make sure goal is either cost or fun.
    if main_goal not in ("cost", "fun"):
        raise ValueError("Value has to be 'cost' or 'fun'")
    # First calculate the cost and fun values for each path.
    paths_values = path_value(paths_list, edges_dict)
    if paths_values is None:
        return None
    # Check if number was entered for cost and fun weights.
    try:
        float(sec_goal_value)
    except ValueError:
        print("Minimum requirement for secondary goal must be a number.")
    optimal_paths = set()
    paths_sec_goal_fulfilled = []
    paths_main_goal_values = []
    for values in paths_values:
        # Check what main goal is set and if path fulfills secondary goal.
        if main_goal == "cost" and values[1] >= sec_goal_value:
            paths_main_goal_values.append(values[0])
            paths_sec_goal_fulfilled.append(values)
        elif main_goal == "fun" and values[0] <= sec_goal_value:
            paths_main_goal_values.append(values[1])
            paths_sec_goal_fulfilled.append(values)
    # Check which path has the lowest cost/highest fun.
    for paths in paths_sec_goal_fulfilled:
        if (main_goal == "cost" and paths[0]
                == min(paths_main_goal_values) or
                main_goal == "fun" and paths[1]
                == max(paths_main_goal_values)):
            # Add path to set of optimal paths.
            optimal_path_index = paths_values.index(paths)
            my_optimal_path = paths_list[optimal_path_index]
            optimal_paths.add(my_optimal_path)
    # Check if optimal path exists.
    if len(optimal_paths) == 0:
        return None
    return optimal_paths


if __name__ == "__main__":
    doctest.testmod()
