"""
Recursive algorithm to find the optimal path in a graph
with cost and fun (Ablenkungswert) values.
"""


def optimize_weighted(cost, fun, weight_cost=1, weight_fun=1):
    """
    Weighted sum function to combine cost and fun.
    Lower score(the result) is better.
    """
    return cost * weight_cost - fun * weight_fun


# Example graph
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


def recursive_best_path(
    current,
    goal,
    edges_dict,
    optimize_func,
    path=None,
    acc_cost=0,
    acc_fun=0,
    visited=None
):
    """
    Recursively finds the optimal path according to a given optimization function.

    :return: (best_path, total_cost, total_fun) or None
    """
    if path is None:
        path = [current]
    if visited is None:
        visited = set()

    # base case
    if current == goal:
        return path, acc_cost, acc_fun

    visited.add(current)

    best_result = None
    best_score = float("inf")

    # find neighbors
    neighbors = [n2 for (n1, n2) in edges_dict if n1 == current]

    for neighbor in neighbors:
        if neighbor not in visited:
            edge_cost, edge_fun = edges_dict[(current, neighbor)]

            # recursive call
            result = recursive_best_path(
                neighbor,
                goal,
                edges_dict,
                optimize_func,
                path + [neighbor],
                acc_cost + edge_cost,
                acc_fun + edge_fun,
                visited.copy()
            )

            if result is not None:
                _, total_cost, total_fun = result
                score = optimize_func(total_cost, total_fun)

                if score < best_score:
                    best_score = score
                    best_result = result

    return best_result



if __name__ == "__main__":

    # Test 1: normal case
    result = recursive_best_path("A", "F", cat_edges, optimize_weighted)
    assert result is not None
    path, cost, fun = result
    assert path[0] == "A"
    assert path[-1] == "F"
    print("Test 1 passed:", path, cost, fun)

    # Test 2: reach direct neighbor
    result = recursive_best_path("A", "B", cat_edges, optimize_weighted)
    assert result is not None
    path, cost, fun = result
    assert path[0] == "A"
    assert path[-1] == "B"
    print("Test 2 passed:", path, cost, fun)

    # Test 3: negative test
    result = recursive_best_path("A", "Z", cat_edges, optimize_weighted)
    assert result is None
    print("Test 3 passed: No path found")


