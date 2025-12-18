"""Find a path using the greedy-algorithm"""

__author__ = "8249067, Sanchez, 8724694, Tran, 8572770, Kesidis"

import doctest
from multiobjective_optimization import path_value


CAT_EDGES = {
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


def greedy_best_path(start, goal, graph_edges, focus_value):
    """
    Finds a path to a goal on a graph
    by choosing the current best edge to progress.
    :param graph_edges: a dictionary containing edges
    and their respective cost and fun values
    :param start: a string containing the start node
    :param goal: a string containing the goal node
    :param focus_value: a string cointaining the value
    for the greedy-algorithm to take into account
    :return: a path to the goal or the furthest path before reaching a dead end
    >>> greedy_best_path("A", "F", CAT_EDGES,"cost")
    (('A', 'C', 'D', 'F'), 6, 7)
    >>> greedy_best_path("A", "F", CAT_EDGES, "fun")
    (('A', 'B', 'D', 'F'), 10, 11)
    >>> greedy_best_path("A", "E", CAT_EDGES, "fun")
    """
    # Make sure to only account for either cost or fun.
    if focus_value not in ("cost", "fun"):
        raise ValueError("Value has to be 'cost' or 'fun'")
    current = start
    visited_nodes = [start]
    # Keep repeating until goal or dead end is reached.
    while True:
        # Check whether to focus on cost or fun.
        if focus_value == "cost":
            min_cost = float("inf")
        else:
            max_fun = 0
        # Find most optimal edge for current node.
        optimal_edge = None
        # Search every edge for the lowest cost or highest fun.
        for i in graph_edges:
            """
            Make sure edge is connected to current node
            and has not been visited yet.
            """
            if i[0] == current and i[1] not in visited_nodes:
                if focus_value == "cost":
                    next_edge_cost = graph_edges[i][0]
                    # Set new minimum cost/maximum fun.
                    if next_edge_cost < min_cost:
                        min_cost = next_edge_cost
                        optimal_edge = i
                else:
                    next_edge_fun = graph_edges[i][1]
                    if next_edge_fun > max_fun:
                        max_fun = next_edge_fun
                        optimal_edge = i
        # If no optimal edge has been found, it is a dead end.
        if optimal_edge is None:
            return None
        # Go to next node.
        current = optimal_edge[1]
        visited_nodes.append(current)
        if goal == current:
            optimal_path = tuple(visited_nodes)
            optimal_path_value = path_value([optimal_path], graph_edges)
            optimal_path_cost = optimal_path_value[0][0]
            optimal_path_fun = optimal_path_value[0][1]
            break
    return optimal_path, optimal_path_cost, optimal_path_fun


if __name__ == "__main__":
    print(greedy_best_path(CAT_EDGES, "A", "F", "cost"))
    doctest.testmod()
