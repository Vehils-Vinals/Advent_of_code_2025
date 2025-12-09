from tools import get_input_list
import heapq
import numpy as np


test = False
points = get_input_list(test)


def get_euclidian_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 +
            (p1[2] - p2[2])**2) ** 0.5


def get_all_distance(points):
    n_points = points.shape[0]
    distances = {}
    for i in range(n_points):
        for j in range(i + 1, n_points):
            dist = get_euclidian_distance(points[i], points[j])
            distances[dist] = (i, j)
    return distances


def modify_circuits(p1, p2, circuits, point_circuit):
    c1 = point_circuit[p1]
    c2 = point_circuit[p2]
    if c1 == c2:
        return circuits, point_circuit

    circuits[c1].extend(circuits[c2])
    for p in circuits[c2]:
        point_circuit[p] = c1
    circuits[c2] = []
    return circuits, point_circuit


def get_len_3_largest(circuits):
    return np.sort([len(c) for c in circuits.values()])[-3:]


def main():
    n_pairs = 10 if test else 1000
    distances = get_all_distance(points)
    heapq_distances = list(distances.keys())
    heapq.heapify(heapq_distances)
    n_points = points.shape[0]
    circuits = {i: [i] for i in range(n_points)}
    point_circuit = {i: i for i in range(n_points)}
    for _ in range(n_pairs):
        dist = heapq.heappop(heapq_distances)
        p1, p2 = distances[dist]
        circuits, point_circuit = modify_circuits(p1, p2, circuits,
                                                  point_circuit)
    largest_circuit = get_len_3_largest(circuits)[:3]
    print(np.prod(largest_circuit))


# main()
