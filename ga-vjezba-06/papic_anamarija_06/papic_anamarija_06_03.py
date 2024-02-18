# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 6 - Zadatak 3

3. koristeći algoritam sortiranih susjeda

- vremenska složenost: O(n^2 * log(n))

@author: Anamarija Papic
"""

def sorted_neighbors(graph, cities):
    n = len(cities)

    current_city = cities[0]
    path = [current_city]

    total_distance = 0

    for i in range(n - 1):
        neighbors = [(city, graph.edges.get(current_city, {}).get(city, 0)) for city in cities if city not in path]
        neighbors.sort(key=lambda x: x[1])
        
        nearest_city = neighbors[0][0]
        
        path.append(nearest_city)
        total_distance += graph.edges.get(current_city, {}).get(nearest_city, 0)
        
        current_city = nearest_city

    path.append(path[0])
    total_distance += graph.edges.get(current_city, {}).get(path[0], 0)

    return path, total_distance
