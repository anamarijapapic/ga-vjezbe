# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 6 - Zadatak 2

2. koristeći algoritam najbližeg susjeda

- vremensku složenost: O(n^2)

@author: Anamarija Papic
"""

def nearest_neighbor(graph, cities):
    start_city = cities[0]
    unvisited_cities = set(cities[1:])

    nn_path = [start_city]
    nn_distance = 0

    current_city = start_city

    while unvisited_cities:
        nearest_city = min(
            unvisited_cities,
            key=lambda city: graph.edges[current_city][city]
        )

        nn_path.append(nearest_city)
        nn_distance += graph.edges[current_city][nearest_city]

        unvisited_cities.remove(nearest_city)
        current_city = nearest_city
        
    nn_path.append(nn_path[0])
    nn_distance += graph.edges[current_city][nn_path[0]]   

    return nn_path, nn_distance
