"""Contains three methods for different types of multiobjective optimization in a graph."""

__author__ = "deine_mtrn, dein_nachname, 8724694, Tran"


# Katzen-Graph als Beispiel
test_paths = [("A", "C", "D", "B", "E", "F"), ("A", "B", "D", "F")]
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


def pareto_optimal(paths_list, edges_dict):
    """
    Calculates a pareto optimal path.
    :param paths_list: a list containing tuples with nodes stored within
    :param edges_dict: a dictionary containing edges and their respective cost and fun values
    """
    # First calculate a cost and fun values for each path
    pareto_list = __path_value(paths_list,edges_dict)
    print(pareto_list)  # just for debugging
    optimal_paths = set()
    # Compare every path with every other path.
    for i in pareto_list:
        for j in pareto_list:
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
            optimal_paths.add(i)
    return optimal_paths


def __path_value(paths_list, edges_dict):
    """
    Sums up the costs and the fun on each path.
    :param paths_list: a list containing tuples with nodes stored within
    :param edges_dict: a dictionary containing edges and their respective cost and fun values
    """
    pareto_values = []
    for i in paths_list:
        path_pareto_value = [0, 0]
        for j in range(0, len(i) - 1):
            edge_node1 = i[j]
            edge_node2 = i[j + 1]
            edge_value = edges_dict[(edge_node1, edge_node2)]
            for k in range(0, 2):
                path_pareto_value[k] += edge_value[k]
        pareto_values.append(tuple(path_pareto_value))
    return pareto_values


print(test_paths)
print(pareto_optimal(test_paths, cat_edges))