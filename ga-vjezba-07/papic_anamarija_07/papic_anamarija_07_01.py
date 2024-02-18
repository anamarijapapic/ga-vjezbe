# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 7 - Zadatak 1

1. Napisati program koji traži najkraće putove iz jednog grada do svih drugih gradova
koristeći:
(a) Dijkstra algoritam
(b) Bellman-Ford algoritam

Možete koristiti networkx.

@author: Anamarija Papic
"""

import networkx as nx

# (a) Dijkstra algoritam
def dijkstra_algorithm(graph, source):
    shortest_path = nx.single_source_dijkstra_path_length(graph, source)
    
    return shortest_path

# (b) Bellman-Ford algoritam
def bellman_ford_algorithm(graph, source):
    shortest_path = nx.single_source_bellman_ford_path_length(graph, source)
    
    return shortest_path
