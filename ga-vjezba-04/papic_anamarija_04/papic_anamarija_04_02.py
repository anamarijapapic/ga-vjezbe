# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 4 - Zadatak 2

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

def number_of_vertices(graph):
    return len(graph.vertices)

def number_of_edges(graph):
    return len(graph.edges)

def degree_of_vertex(graph, vertex):
    degree = 0
    for edge in graph.edges:
        if vertex in edge:
            degree += 1
    return degree

def vertices_with_max_degree(graph):
    degrees = {vertex: 0 for vertex in graph.vertices}
    for edge in graph.edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    max_degree = max(degrees.values())
    max_degree_vertices = [vertex for vertex, degree in degrees.items() if degree == max_degree]

    return max_degree_vertices

def main():
    g = Graph(
        {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}, 
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5], [2, 4], [2, 5], [4, 5]]
    )
    
    print(number_of_vertices(g))
    print(number_of_edges(g))
    print(degree_of_vertex(g, 1))
    print(vertices_with_max_degree(g))
    
if __name__=='__main__':
    main()
