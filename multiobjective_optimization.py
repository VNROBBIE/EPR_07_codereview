"""Contains three methods for different types of multiobjective optimization in a graph."""

__author__ = "deine_mtrn, dein_nachname, 8724694, Tran"


# Katzen-Graph als Beispiel
test_paths = [("A", "C", "D", "B", "E"), ("A", "B", "D", "F")]
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


def path_value(paths_list, edges_dict):
    """
    Sums up the costs and the fun on each path.
    :param paths_list: a list containing tuples with nodes stored within
    :param edges_dict: a dictionary containing edges and their respective cost and fun values
    :returns: a list containing tuples with each path's summed up cost and fun
    """
    path_values = []
    for i in paths_list:
        my_path_value = [0, 0]
        for j in range(0, len(i) - 1):
            # Pair up every node along the path and find the respective edge.
            edge_node1 = i[j]
            edge_node2 = i[j + 1]
            # Safe edge values from dictionary in new tuple.
            edge_value = edges_dict[(edge_node1, edge_node2)]
            # Sum up every path value.
            for k in range(0, 2):
                my_path_value[k] += edge_value[k]
        # Add value of one path to list of path values.
        path_values.append(tuple(my_path_value))
    return path_values


def pareto_optimal(paths_list, edges_dict):
    """
    Calculates a pareto optimal path.
    :param paths_list: a list containing tuples with nodes stored within
    :param edges_dict: a dictionary containing edges and their respective cost and fun values
    :returns: a set of pareto optimal paths
    """
    # First calculate a cost and fun values for each path.
    path_values = path_value(paths_list, edges_dict)
    print(path_values)  # just for debugging
    optimal_paths = set()
    # Compare every path with every other path.
    for i in path_values:
        for j in path_values:
            # Make sure to not compare a path with itself or a path with another path of the same value.
            if i == j:
                continue
            current_cost_value = j[0]
            current_fun_value = j[1]
            new_cost_value = i[0]
            new_fun_value = i[1]
            # Every path must not be worse than any of other paths in both goals.
            # Cost must be low and fun must be high.
            if new_cost_value > current_cost_value and new_fun_value < current_fun_value:
                break
        else:
            # Add new path to set of pareto-optimal paths.
            my_optimal_path = paths_list[path_values.index(i)]
            optimal_paths.add(my_optimal_path)
    return optimal_paths



def weighted_sum(paths_list, edges_dict, cost_weight, fun_weight):
    """
    Calculates an optimal path based on the weighted sum method.
    :param paths_list: a list containing tuples with nodes stored within
    :param edges_dict: a dictionary containing edges and their respective cost and fun values
    :param cost_weight: a number value determining the weight of an edge's cost value
    :param fun_weight: a number value determining the weight of an edge's fun value
    :return: a set of optimal paths
    """
    # First calculate a cost and fun values for each path.
    paths_values = path_value(paths_list, edges_dict)
    optimal_paths = set()
    paths_weighted_sums = []
    # Calculate a value for each path (weighted sum). The smallest value is optimal.
    for paths in paths_values:
        # Multiply by a factor based on each value's weight.
        weighted_cost = paths[0] * cost_weight
        weighted_fun = -paths[1] * fun_weight
        my_weighted_sum = weighted_cost + weighted_fun
        print(my_weighted_sum)  # debugging
        # Add calculated sum to list of all weighted sums.
        paths_weighted_sums.append(my_weighted_sum)
    # Check for every sum in list if it is the smallest value.
    for i in range(0, len(paths_weighted_sums)):
        if paths_weighted_sums[i] == min(paths_weighted_sums):
            # Add path with the same index to set of optimal paths.
            optimal_paths.add(paths_list[i])
    return optimal_paths


print(test_paths)
print(pareto_optimal(test_paths, cat_edges))
print()
print(weighted_sum(test_paths, cat_edges, 10, 1))