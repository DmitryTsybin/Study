"""
File with functions to calculate different pairs and clustering algorythms.
"""


import math
import alg_cluster


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    if len(cluster_list) < 2:
        return -1

    min_distance = pair_distance(cluster_list, 0, 1)

    for idx1 in range(len(cluster_list)):
        for idx2 in range(len(cluster_list)):
            if idx1 != idx2:
                distance = pair_distance(cluster_list, idx1, idx2)
                if distance[0] < min_distance[0]:
                    min_distance = distance

    return min_distance


def return_min_tuple(tuple1, tuple2):
    """
    implement function min for tuples (dist, i, j)
    """
    ret_tuple = tuple1
    if tuple2[0] < tuple1[0]:
        ret_tuple = tuple2
    return ret_tuple


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """

    if len(cluster_list) < 2:
        return -1

    points_in_strip = []
    for point in cluster_list:
        if abs(point.horiz_center() - horiz_center) < half_width:
            points_in_strip.append(point)

    points_in_strip.sort(key = lambda x: x.vert_center())
    strip_point_count = len(points_in_strip)
    ret_tuple = (float('inf'), -1, -1)

    for coordinate in points_in_strip:
        if points_in_strip.index(coordinate) == strip_point_count - 1:
            break
        else:
            for check in range(1, 4):  # check 3 points
                rt_index = points_in_strip.index(coordinate)+check
                if (rt_index) == strip_point_count:
                    break
                else:
                    strip_tuple = slow_closest_pair([coordinate, points_in_strip[rt_index]])
                    if strip_tuple[0] < ret_tuple[0]:
                        answer_list = []
                        answer_list.append(strip_tuple[0])
                        #put the indices in increasing order
                        if cluster_list.index(coordinate) < cluster_list.index(points_in_strip[rt_index]):
                            answer_list.append(cluster_list.index(coordinate))
                            answer_list.append(cluster_list.index(points_in_strip[rt_index]))
                        else:
                            answer_list.append(cluster_list.index(points_in_strip[rt_index]))
                            answer_list.append(cluster_list.index(coordinate))
                        ret_tuple = tuple(answer_list)

    return ret_tuple


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """

    size = len(cluster_list)

    if size < 4:
        ret_tuple = slow_closest_pair(cluster_list)
    else:
        # divide
        split = size / 2
        left = cluster_list[:split]
        rigth = cluster_list[split:]
        left_tuple = fast_closest_pair(left)
        right_tuple = fast_closest_pair(rigth)

        right_list = list(right_tuple)
        right_list[1] += split
        right_list[2] += split
        right_tuple = tuple(right_list)

        # merge
        left_and_right_min_tuple = return_min_tuple(left_tuple, right_tuple)

        print 'cluster_list[split]: ', cluster_list[split]

        middle = 0.5 * (cluster_list[split - 1].horiz_center() + cluster_list[split].horiz_center())
        ret_tuple = return_min_tuple(
            left_and_right_min_tuple,
            closest_pair_strip(cluster_list, middle, left_and_right_min_tuple[0]))

    return ret_tuple


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    return []


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations

    return []

# As one important coding note, you will need to sort a list of clusters by the horizontal
# (as well as vertical) positions of the cluster centers. This operation can be done in a single line
# of Python using the sort method for lists by providing a key argument of the form:
# cluster_list.sort(key = lambda cluster: cluster.horiz_center())

print closest_pair_strip([
    alg_cluster.Cluster(set([]), 0, 0, 1, 0),
    alg_cluster.Cluster(set([]), 1, 0, 1, 0),
    alg_cluster.Cluster(set([]), 2, 0, 1, 0),
    alg_cluster.Cluster(set([]), 3, 0, 1, 0)
    ], 1.5, 1.0)

print closest_pair_strip([
    alg_cluster.Cluster(set([]), 0, 0, 1, 0),
    alg_cluster.Cluster(set([]), 0, 1, 1, 0),
    alg_cluster.Cluster(set([]), 0, 2, 1, 0),
    alg_cluster.Cluster(set([]), 0, 3, 1, 0)
    ],0.0, 1.0)

print fast_closest_pair([
    alg_cluster.Cluster(set([]), 0, 0, 1, 0),
    alg_cluster.Cluster(set([]), 1, 0, 1, 0),
    alg_cluster.Cluster(set([]), 2, 0, 1, 0),
    alg_cluster.Cluster(set([]), 3, 0, 1, 0)
    ])

print fast_closest_pair([
    alg_cluster.Cluster(set([]), 1.0, 0.0, 1, 0),
    alg_cluster.Cluster(set([]), 4.0, 0.0, 1, 0),
    alg_cluster.Cluster(set([]), 5.0, 0.0, 1, 0),
    alg_cluster.Cluster(set([]), 7.0, 0.0, 1, 0)
    ])
