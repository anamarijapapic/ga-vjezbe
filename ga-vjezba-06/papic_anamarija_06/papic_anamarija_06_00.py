# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 6 - Zadatak 0

Dana je udaljenost između gradova u csv formatu. Napišite program kojim ćete obići n
gradova, svaki grad samo jednom uz povratak u polazišni grad, tako da napravite što
kraći put:

1. koristeći brute-force,
2. koristeći algoritam najbližeg susjeda,
3. koristeći algoritam sortiranih susjeda.

Algoritmi su opisani u slajdovima sa predavanja. Za sva tri algoritma procijenite složenost
i izmjerite vrijeme izvršavanja. Testirajte na datasetu distance.csv. Gradove koje želite
obići unosi korisnik ili ih možete zapisati u neku datoteku, pa testni dio programa čita iz
nje.

@author: Anamarija Papic
"""

import time
from papic_anamarija_06_01 import brute_force
from papic_anamarija_06_02 import nearest_neighbor
from papic_anamarija_06_03 import sorted_neighbors

class Graph:
    def __init__(self, vertices=None, edges=None, directed=False):
        self.vertices = vertices or {}
        self.edges = edges or {}
        self.directed = directed
    
    def __str__(self):
        return f'''Graph:
Vertices ({len(self.vertices)}): {self.vertices}
Edges: {self.edges}
Directed: {self.directed}
'''

def read_distance_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        header = lines[0].strip().split(',')
        vertices = {vertex: index for index, vertex in enumerate(header[1:])}
        edges = {}

        graph = Graph(vertices=vertices, edges=edges, directed=True)

        for i in range(1, len(lines)):
            row = lines[i].strip().split(',')
            source_vertex = row[0]

            for j, distance in enumerate(row[1:]):
                end_vertex = header[j + 1]
                try:
                    weight = 0 if distance == '-' else int(distance)
                except ValueError:
                    raise ValueError(f"Invalid distance value '{distance}' at row {i+1}, column {j+2}")

                graph.edges.setdefault(source_vertex, {})[end_vertex] = weight

    return graph

def main():
    file_path = 'distance.csv'
    graph = read_distance_matrix(file_path)
    print(graph)

    cities = input('Enter the cities you want to visit separated by space: ').split()

    # Brute-force
    start_time = time.time()
    bf_path, bf_distance = brute_force(graph, cities)
    bf_execution_time = time.time() - start_time

    print(f'\nBrute-force:\nPath: {bf_path}\nDistance: {bf_distance}\nExecution Time: {bf_execution_time} seconds\n')
    
    # Nearest Neighbor
    start_time = time.time()
    nn_path, nn_distance = nearest_neighbor(graph, cities)
    nn_execution_time = time.time() - start_time

    print(f'Nearest Neighbor:\nPath: {nn_path}\nDistance: {nn_distance}\nExecution Time: {nn_execution_time} seconds\n')

    # Sorted Neighbors
    start_time = time.time()
    sorted_path, sorted_distance = sorted_neighbors(graph, cities)
    sorted_execution_time = time.time() - start_time

    print(f'Sorted Neighbors:\nPath: {sorted_path}\nDistance: {sorted_distance}\nExecution Time: {sorted_execution_time} seconds\n')

if __name__ == '__main__':
    main()
