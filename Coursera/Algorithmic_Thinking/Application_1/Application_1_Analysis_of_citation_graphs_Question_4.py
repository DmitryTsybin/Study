# -*- coding: utf-8 -*-

import random

from Project_1_Degree_distributions_for_graphs import make_complete_graph
from Project_1_Degree_distributions_for_graphs import normalized_in_degree_distribution
from Application_1_Analysis_of_citation_graphs_Question_2 import build_plot

"""
__init__(num_nodes): Create a DPATrial object corresponding to
a complete graph with num_nodes nodes.

run_trial(num_nodes): Runs num_nodes number of DPA trials (lines 4- 6).
Returns a set of the nodes, computed with the correct probabilities,
that are neighbors of the new node. In the provided code, the DPATrial
class maintains a list of node numbers that contains multiple instances
of the same node number. If the number of instances of each node number is
maintained in the same ratio as the desired probabilities, a call to
random.choice() produces a random node number with the desired probability.
"""

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def make_graph_dpa(n, m):
    graph = make_complete_graph(m)

    # 1. добавляем (n - m) рёбер
    # 2. для каждого нового ребра добавляем m рандомных связей
    for i in xrange(m, n):
        count = 0
        edges = set()
        while count < m-1:
            edge = random.randint(0, n)
            if edge not in edges:
                edges.add(edge)
                count += 1
        graph[i] = edges

    return graph



graph = make_graph_dpa(27770, 13)
#graph = make_graph_dpa(1000, 5)
print 'graph: ', graph
distribution = normalized_in_degree_distribution(graph)
print 'distribution: ', distribution
build_plot(distribution)
