import urllib2
import os.path
import json
import math
import matplotlib.pyplot as plt

from Project_1_Degree_distributions_for_graphs import normalized_in_degree_distribution
from Project_1_Degree_distributions_for_graphs import in_degree_distribution

# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL for a text representation of the
    graph. Returns a dictionary that models a graph
    """

    #if os.path.isfile('source_graph.txt'):
    #    print 'source_graph.txt is exist'
    #    graph_file = open('source_graph.txt')
    #else:
    #    print 'source_graph.txt is not exist'
    #    with open('source_graph.txt', 'w') as outfile:
    #        graph_file = urllib2.urlopen(graph_url)
    #        outfile.write()

    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def build_plot(distribution):
    """question 1"""

    xvalues = []
    yvalues = []

    for elem in distribution:
        xvalues.append(float(elem))
        yvalues.append(float(distribution[elem]))

    print 'xvalues length: ', len(xvalues)
    print 'xvalues: ', xvalues
    print 'yvalues: ', yvalues
    print 'max X: ', max(xvalues)

    plt.loglog(xvalues, yvalues, 'ro')
    plt.axis([int(min(xvalues)), math.ceil(max(xvalues)), 0, 1])
    plt.ylabel('distribution values')
    plt.xlabel('degrees')
    plt.title('in degree graph distribution')
    plt.yscale('log')
    #plt.xscale('log')
    plt.show()


def restore_graph_params(graph):
    """question 3"""

    n = len(graph)
    m = 0

    for node in graph:
        m += len(graph[node])

    return n, m / float(n)


if os.path.isfile('graph_distribution.txt'):
    print 'graph_distribution.txt is exist'
    file = open('graph_distribution.txt', 'r')
    distribution = eval(open('graph_distribution.txt').read())
    #distribution = file.read()
    file.close()
else:
    print 'graph_distribution.txt is not exist'
    citation_graph = load_graph(CITATION_URL)
    distribution = normalized_in_degree_distribution(citation_graph)
    with open('graph_distribution.txt', 'w') as outfile:
        json.dump(distribution, outfile)
    outfile.close()


#distribution = normalized_in_degree_distribution(citation_graph)
print 'distribution: ', distribution
print
print 'n and m for citation graph: ', restore_graph_params(load_graph(CITATION_URL))
build_plot(distribution)
