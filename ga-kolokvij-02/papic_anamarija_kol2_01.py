# -*- coding: utf-8 -*-
"""
[Graf algoritmi: Kolokvij 2 - Zadatak 1]

@author: Anamarija Papic
"""

def read_pajek(filename):
    d = {
        'vertices': [],
        'edges': []
    }
    
    with open(filename, 'r') as f:
        is_reading_vertices = False
        is_reading_edges = False
        for line in f:
            if line.startswith('*Vertices'):
                is_reading_vertices = True
                is_reading_edges = False
            elif line.startswith('*Edges'):
                is_reading_vertices = False
                is_reading_edges = True
            elif is_reading_vertices:
                v_id, v_label = line.split()
                d['vertices'].append(v_label)
            elif is_reading_edges:
                src, dest, weight = line.split()
                d['edges'].append([int(src), int(dest), int(weight)])
    
    return d

def mst_prim(d):
    parent = []
    key = []
    mst_tmp = []
    
    for i in range(len(d['vertices'])):
        parent.append(-1)
        key.append(float('inf'))
        mst_tmp.append(False)
    
    key[0] = 0
    
    for i in range(len(d['vertices']) - 1):
        min_key = float('inf')
        
        for node_i in range(len(d['vertices'])):
            if key[node_i] < min_key and not mst_tmp[node_i]:
                min_key = key[node_i]
                min_i = node_i
        
        mst_tmp[min_i] = True
        
        for edge in d['edges']:
            src, dest, weight = edge
            if src == min_i and not mst_tmp[dest] and weight < key[dest]:
                parent[dest] = min_i
                key[dest] = weight
    
    return parent

def sorted_neighbours_salesman(d):
    shortest_path = []
    cities = d['vertices']
    
    curr_city = cities[0]
    shortest_path.append(curr_city)
    
    for i in range(len(cities) - 1):
        curr_neighbours = []
        for edge in d['edges']:
            src, dest, weight = edge
            if i == src:
                curr_neighbours.append(edge)
        curr_neighbours.sort(key=lambda x: x[2])
        
        nearest_city = curr_neighbours[0][1]
        
        if cities[nearest_city] not in shortest_path:
            shortest_path.append(cities[nearest_city])
        
        curr_city = cities[nearest_city]
    
    # way home
    shortest_path.append(cities[0])
    
    print(shortest_path)

def main():
    d = read_pajek('mapa-europa-2.net')
    print(d)
        
    for i in range(1, len(d['vertices'])):
        print(f'{mst_prim(d)[i]} - {i}')
        
    sorted_neighbours_salesman(d)

if __name__ == '__main__':
    main()
