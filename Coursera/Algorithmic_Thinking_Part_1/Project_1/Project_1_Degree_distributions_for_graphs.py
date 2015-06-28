import random

"""Define const graphs"""
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set([])
}
EX_GRAPH2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set([]),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 3, 4, 5, 6, 7])
}


def make_complete_graph(num_nodes):
    """Takes the number of nodes num_nodes and returns a dictionary
    corresponding to a complete directed graph with the specified number
    of nodes."""
    graph = {}

    for node in range(0, num_nodes):
        values = range(0, num_nodes)
        values.remove(node)
        graph[node] = set(values)

    return graph


def make_probability_directional_graph(num_nodes, probability):
    graph = {}

    for node in range (0, num_nodes):
        values = set()
        possible_values = range(0, num_nodes)
        possible_values.remove(node)

        for value in possible_values:
            if random.random() <= probability:
                values.add(value)

        graph[node] = set(values)

    return graph


def compute_in_degrees(digraph):
    """Takes a directed graph digraph (represented as a dictionary) and
    computes the in-degrees for the nodes in the graph."""
    degrees = {}

    for looked_node in digraph:
        degree = 0

        for node in digraph:
            if node != looked_node:
                if looked_node in digraph[node]:
                    degree += 1

        degrees[looked_node] = degree

    return degrees


def in_degree_distribution(digraph):
    """Takes a directed graph digraph (represented as a dictionary) and
    computes the unnormalized distribution of the in-degrees of the graph."""
    distribution = {}
    degrees = compute_in_degrees(digraph)

    for degree in range(0, len(digraph)):
        count = 0

        for node in degrees:
            if degrees[node] == degree:
                count += 1

        if count != 0:
            distribution[degree] = count

    return distribution


def normalized_in_degree_distribution(digraph):
    distribution = in_degree_distribution(digraph)
    normalized_distribution = {}
    divisor = 0

    for value in distribution:
        divisor += distribution[value]

    for value in distribution:
        normalized_distribution[value] = distribution[value] / float(divisor)

    return normalized_distribution


#print in_degree_distribution(EX_GRAPH0)
#print normalized_in_degree_distribution(EX_GRAPH0)
#print in_degree_distribution(EX_GRAPH1)
#print normalized_in_degree_distribution(EX_GRAPH1)
#print in_degree_distribution(EX_GRAPH2)
#print normalized_in_degree_distribution(EX_GRAPH2)
