import random
import timeit
import math
import matplotlib.pyplot as plt


import alg_cluster
# import alg_clusters_matplotlib
import alg_project3_viz
from closest_pairs_and_clustering_algorithms import slow_closest_pair, fast_closest_pair

def gen_random_clusters(num_clusters):
    """
    creates a list of clusters where each cluster in this list corresponds to one
    randomly generated point in the square with corners (+-1,+-1).
    Use this function and your favorite Python timing code to compute the running
    times of the functions slow_closest_pairs and fast_closest_pair for lists of
    clusters of size 2 to 200.
    """
    clusters = []

    for _ in xrange(num_clusters):
        clusters.append(alg_cluster.Cluster(
            set(),
            random.randint(-1, 1),
            random.randint(-1, 1),
            0,
            0
        ))
    return clusters


def build_plot(slow, fast):
    slow_line, = plt.plot(slow, label='slow_closest_pair')
    fast_line, = plt.plot(fast, label='fast_closest_pair')
    plt.xlabel('number of initial clusters')
    plt.ylabel('running time')
    plt.legend(handles=[slow_line, fast_line])
    plt.show()


def generate_plot_data(num):
    slow = []
    fast = []

    for num in xrange(200):
        cluster = gen_random_clusters(num)

        start_slow = timeit.default_timer()
        slow_closest_pair(cluster)
        elapsed_slow = timeit.default_timer() - start_slow

        start_fast = timeit.default_timer()
        fast_closest_pair(cluster)
        elapsed_fast = timeit.default_timer() - start_fast

        slow.append(elapsed_slow)
        fast.append(elapsed_fast)

    return(slow, fast)


# plot_data = generate_plot_data(200)
# print "plot_data: "
# print "slow: ", plot_data[0]
# print "fast: ", plot_data[1]

# build_plot(plot_data[0], plot_data[1])
