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

        # print 'cluster_list[split]: ', cluster_list[split]

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

    num = len(cluster_list)
    while num > num_clusters:
        cluster_list.sort(key = lambda clu: clu.horiz_center())
        idx = fast_closest_pair(cluster_list)
        cluster_list[idx[1]].merge_clusters(cluster_list[idx[2]])
        cluster_list.pop(idx[2])
        num -= 1
    return cluster_list


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
    num = len(cluster_list)

    print "num_clusters: ", num_clusters

    points = [idx for idx in xrange(num)]
    points.sort(reverse = True, key = lambda idx:
                cluster_list[idx].total_population())
    points = [[cluster_list[points[idx]].horiz_center(),
               cluster_list[points[idx]].vert_center()]
              for idx in xrange(num_clusters)]
    clusters = [-1 for _ in xrange(num)]
    population = [0 for _ in xrange(num_clusters)]
    for _ in xrange(num_iterations):
        for cidx in xrange(num):
            mind = (float("inf"), -1, -1)
            for idx in xrange(num_clusters):
                dist = cluster_point_distance(cluster_list,
                                              points,
                                              cidx, idx)
                if mind > dist:
                    mind = dist
            clusters[cidx] = mind[2]
        for idx in xrange(num_clusters):
            points[idx][0] = 0.0
            points[idx][1] = 0.0
            population[idx] = 0
        for cidx in xrange(num):
            idx = clusters[cidx]
            cpopul = cluster_list[cidx].total_population()
            population[idx] += cpopul
            points[idx][0] += cluster_list[cidx].horiz_center() * cpopul
            points[idx][1] += cluster_list[cidx].vert_center()  * cpopul
        for idx in xrange(num_clusters):
            if population[idx] != 0:
                points[idx][0] /= population[idx]
                points[idx][1] /= population[idx]
    result = [0 for _ in xrange(num_clusters)]
    for cidx in xrange(num):
        idx = clusters[cidx]
        if result[idx] == 0:
            result[idx] = cluster_list[cidx].copy()
        else:
            result[idx].merge_clusters(cluster_list[cidx])
    return result

def cluster_point_distance(cluster_list, points, cidx, idx):
    """
    Helper function that computes Euclidean distance between cluster and point
    Input: cluster_list is list of clusters, points is list of points,
    cidx1 and idx are integer indices for cluster and point

    Output: tuple (dist, cidx, idx) where dist is distance between
    cluster_list[cidx] and points[idx]
    """
    d_x = cluster_list[cidx].horiz_center() - points[idx][0]
    d_y = cluster_list[cidx].vert_center()  - points[idx][1]
    return (math.sqrt(d_x ** 2 + d_y ** 2), cidx, idx)


def compute_distortion(cluster_list, data_table):
    distortion = 0
    for cluster in cluster_list:
        if type(cluster) == 'instance' and cluster != 0:
            distortion += cluster.cluster_error(data_table)
    return distortion






