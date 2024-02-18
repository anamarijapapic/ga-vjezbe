# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 7 - Zadatak 0

Dana je udaljenost između gradova u pajek formatu.

1. Napisati program koji traži najkraće putove iz jednog grada do svih drugih gradova
koristeći:
(a) Dijkstra algoritam
(b) Bellman-Ford algoritam

2. Napisati program koji traži najkraći put između dva grada koristeći:
(a) Greedy BFS
(b) A* algoritam

Možete koristiti networkx. Usporedite rezultate različitih algoritama.

Za zadatke treba napraviti i mjerenje vremena izvršavanja algoritama.

@author: Anamarija Papic
"""

import networkx as nx
import time
from papic_anamarija_07_01 import dijkstra_algorithm, bellman_ford_algorithm
from papic_anamarija_07_02 import greedy_bfs_algorithm, a_star_algorithm

def main():
    graph = nx.read_pajek('graph-airports-koord.net')
    
    start_city = 'LHR'
    end_city = 'VIE'

    print('Dijkstra algorithm:')
    start_time = time.time()
    dijkstra_result = dijkstra_algorithm(graph, start_city)
    dijkstra_time = time.time() - start_time
    print(dijkstra_result)
    print(f'Time: {dijkstra_time} seconds\n')

    print('Bellman-Ford algorithm:')
    start_time = time.time()
    bellman_ford_result = bellman_ford_algorithm(graph, start_city)
    bellman_ford_time = time.time() - start_time
    print(bellman_ford_result)
    print(f'Time: {bellman_ford_time} seconds\n')

    print('Greedy BFS algorithm:')
    start_time = time.time()
    greedy_bfs_result = greedy_bfs_algorithm(graph, start_city, end_city)
    greedy_bfs_time = time.time() - start_time
    print(greedy_bfs_result)
    print(f'Time: {greedy_bfs_time} seconds\n')

    print('A* algorithm:')
    start_time = time.time()
    a_star_result = a_star_algorithm(graph, start_city, end_city)
    a_star_time = time.time() - start_time
    print(a_star_result)
    print(f'Time: {a_star_time} seconds')

if __name__ == '__main__':
    main()
