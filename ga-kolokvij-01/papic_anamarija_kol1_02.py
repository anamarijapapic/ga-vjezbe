# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Kolokvij 1 - Zadatak 2

@author: Anamarija Papic
"""

def read_to_dict_from_file(filename):
    d = {
        'vertices': [],
        'edges': []
    }
    
    is_reading_vertices = is_reading_edges = False
    
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('*Vertices'):
                is_reading_vertices = True
                is_reading_edges = False
            elif line.startswith('*Edges'):
                is_reading_vertices = False
                is_reading_edges = True
            elif is_reading_vertices:
                v_id, v_label = line.split()
                d['vertices'].append({int(v_id): v_label})
            elif is_reading_edges:
                v1, v2, w = line.split()
                # undirected graph - *Edges - goes both ways
                d['edges'].append((int(v1), int(v2), int(w)))
                d['edges'].append((int(v2), int(v1), int(w)))
            
    return d

def find_longest_flight(d):
    data = d['edges']
    
    max_distance = data[0][2]
    max_el = data[0]
    for el in data:
        max_distance = max(max_distance, el[2])
        if el[2] == max_distance:
            max_el = el
    
    # 10 0 1523 -> 0 10 1523 (undirected graph - *Edges)
    return max_el[0]

def find_flights_to(d, index):
    data = d['edges']
    
    lst = []
    for el in data:
        if el[1] == index:
            lst.append(el[0])
            
    return sorted(lst)
                
def main():
    d = read_to_dict_from_file('mapa-europa.net')
    
    print(find_longest_flight(d))
    
    print(find_flights_to(d, 4))

if __name__ == '__main__':
    main()
