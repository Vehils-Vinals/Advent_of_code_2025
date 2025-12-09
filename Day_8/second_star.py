from tools import get_input_list
from first_star import get_all_distance, \
    modify_circuits
import heapq
import numpy as np

test = False
points = get_input_list(test)


def main():
    distances = get_all_distance(points)
    heapq_distances = list(distances.keys())
    heapq.heapify(heapq_distances)
    n_points = points.shape[0]
    circuits = {i: [i] for i in range(n_points)}
    point_circuit = {i: i for i in range(n_points)}
    while heapq_distances:
        dist = heapq.heappop(heapq_distances)
        p1, p2 = distances[dist]
        if point_circuit[p1] != point_circuit[p2]:
            last = [points[p1][0], points[p2][0]]
        circuits, point_circuit = modify_circuits(p1, p2, circuits,
                                                  point_circuit)

    print(np.prod(last))


main()
