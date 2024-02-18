# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 5 - Zadatak 1

Dana je udaljenost između gradova u pajek formatu. Napišite program koji će naći
minimalno razapinjuće stablo

(a) koristeći Primov algoritam
(b) koristeći Kruskalov algoritam

Algoritmi su opisani u slajdovima sa predavanja. Testirajte na datasetu airports−split.net.

@author: Anamarija Papic
"""

from papic_anamarija_05_00 import read_parse_pajek

def prim(graph):
    parent = [-1] * len(graph.vertices)
    key = [float('inf')] * len(graph.vertices)
    mst_set = [False] * len(graph.vertices)
    
    key[0] = 0
    parent[0] = -1
    
    for i in range(len(graph.vertices) - 1):
        min_key = float('inf')
        
        for v in range(len(graph.vertices)):
            if key[v] < min_key and not mst_set[v]:
                min_key = key[v]
                min_index = v
        
        mst_set[min_index] = True
        
        for edge in graph.edges:
            src, dest, weight = edge
            if src == min_index and not mst_set[dest] and weight < key[dest]:
                parent[dest] = min_index
                key[dest] = weight
    
    return parent

def kruskal(graph):
    graph.edges = sorted(graph.edges, key=lambda item: item[2])
    parent = [-1] * len(graph.vertices)
    
    def find(i):
        if parent[i] == -1:
            return i
        return find(parent[i])
    
    def union(i, j):
        parent[i] = j
    
    mst_edges = []
    i = 0
    
    while len(mst_edges) < len(graph.vertices) - 1:
        src, dest, weight = graph.edges[i]
        i += 1
        x = find(src)
        y = find(dest)
    
        if x != y:
            mst_edges.append([src, dest, weight])
            union(x, y)
    
    return mst_edges

def main():
    g = read_parse_pajek('resources/airports-split.net')
    
    prim_result = prim(g)
    print("Prim's algorithm - Minimum spanning tree (MST):")
    for i in range(1, len(g.vertices)):
        print(f'{prim_result[i]} - {i}')
    
    kruskal_result = kruskal(g)
    print("\nKruskal's algorithm - Minimum spanning tree (MST):")
    for edge in kruskal_result:
        print(f'{edge[0]} - {edge[1]}: {edge[2]}')

if __name__ == '__main__':
    main()
