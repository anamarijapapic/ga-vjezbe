# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 6 - Zadatak 1

1. koristeći brute-force

- vremenska složenost: O(n!)

@author: Anamarija Papic
"""

import itertools

def brute_force(graph, cities):
    all_permutations = itertools.permutations(cities)

    best_path = None
    best_distance = float('inf')

    for perm in all_permutations:
        total_distance = 0

        for i in range(len(perm) - 1):
            city1 = perm[i]
            city2 = perm[i + 1]

            edge_distance = graph.edges[city1][city2]

            total_distance += edge_distance

        last_city = perm[-1]
        starting_city = perm[0]
        return_distance = graph.edges[last_city][starting_city]
        total_distance += return_distance

        if total_distance < best_distance:
            best_distance = total_distance
            best_path = perm
            
    return best_path, best_distance
