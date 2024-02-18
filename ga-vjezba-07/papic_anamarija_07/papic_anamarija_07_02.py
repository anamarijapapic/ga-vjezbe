# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 7 - Zadatak 2

2. Napisati program koji traži najkraći put između dva grada koristeći:
(a) Greedy BFS
(b) A* algoritam

Možete koristiti networkx.

@author: Anamarija Papic
"""

import networkx as nx

# (a) Greedy BFS
def greedy_bfs_algorithm(graph, source, target):
    visited = set()
    queue = [(source, [source])]
    
    def heuristic(graph, node1, node2):
        # Custom heuristic function (distance between nodes in this case)
        return graph[node1][node2].get('weight', 1)
    
    while queue:
        current_node, shortest_path = queue.pop(0)
        if current_node == target:
            return shortest_path
        
        if current_node not in visited:
            visited.add(current_node)
            neighbors = list(graph.neighbors(current_node))
            
            # Sort neighbors based on a heuristic (distance in this case)
            neighbors.sort(key=lambda neighbor: heuristic(graph, current_node, neighbor))
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, shortest_path + [neighbor]))
    
    return None

# (b) A* algoritam
def a_star_algorithm(graph, source, target):
    shortest_path = nx.astar_path(graph, source, target)
    
    return shortest_path
