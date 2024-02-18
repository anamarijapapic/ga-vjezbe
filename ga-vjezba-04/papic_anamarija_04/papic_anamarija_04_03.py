# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 4 - Zadatak 3

2. Napisati funkcije koje računaju:
— broj vrhova u grafu
— broj bridova u grafu
— stupanj svakog vrha
— vrhove s maksimalnim brojem incidentnih bridova

U drugom i trećem zadatku parametar funkcije je graf. Razmislite u kakvom ga je obliku
najbolje proslijediti kao parametar, tako da funkcija bude što jednostavnija i efikasnija.

@author: Anamarija Papic
"""

from papic_anamarija_04_00 import Graph
from papic_anamarija_04_02 import degree_of_vertex

def is_eulerian(graph):
    for vertex in graph.vertices:
        if degree_of_vertex(graph, vertex) % 2 != 0:
            return False

    visited = set()

    def dfs(v):
        visited.add(v)
        for edge in graph.edges:
            if v in edge:
                neighbor = edge[0] if edge[1] == v else edge[1]
                if neighbor not in visited:
                    dfs(neighbor)

    start_vertex = next(iter(graph.vertices))
    dfs(start_vertex)

    return len(visited) == len(graph.vertices)

def main():
    g1 = Graph(
        {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}, 
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5], [2, 4], [2, 5], [4, 5]]
    )
    
    print(is_eulerian(g1))
    
    g2 = Graph(
        {0, 1, 2, 3, 4}, 
        [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]
    )

    print(is_eulerian(g2))

if __name__=='__main__':
    main()
