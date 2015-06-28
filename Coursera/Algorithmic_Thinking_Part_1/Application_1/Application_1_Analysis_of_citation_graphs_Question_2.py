import math
import matplotlib.pyplot as plt

from Project_1_Degree_distributions_for_graphs import normalized_in_degree_distribution
from Project_1_Degree_distributions_for_graphs import make_probability_directional_graph


def build_plot(distribution):
    xvalues = []
    yvalues = []

    for elem in distribution:
        xvalues.append(float(elem))
        yvalues.append(float(distribution[elem]))

    #print 'xvalues: ', xvalues
    #print 'yvalues: ', yvalues
    #print 'max X: ', max(xvalues)

    plt.loglog(xvalues, yvalues, 'ro')
    #plt.plot(xvalues, yvalues, 'ro')
    plt.axis([-1, math.ceil(max(xvalues)) + 1, 0, 1])
    plt.ylabel('distribution values')
    plt.xlabel('degrees')
    plt.title('in degree graph distribution')
    plt.yscale('log')
    plt.show()

#graph = make_probability_directional_graph(1000, 0.5)
#distribution = normalized_in_degree_distribution(graph)
#print 'graph: ', graph
#print
#print 'distribution: ', distribution
#build_plot(distribution)
