# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 5 - Zadatak 0

@author: Anamarija Papic
"""

class Graph:
    def __init__(self, vertices=None, edges=None, directed=False):
        self.vertices = vertices or {}
        self.edges = edges or []
        self.directed = directed
    
    def __str__(self):
        return f'''Graph:
Vertices ({len(self.vertices)}): {self.vertices}
Edges: {self.edges}
Directed: {self.directed}
'''

def read_parse_pajek(filename, encoding='utf-8'):
    g = Graph()
    
    is_reading_vertices = is_reading_arcs = is_reading_edges = False
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
    
            if line.lower().startswith('*vertices'):
                split_result = line.split(None, 1)
                if len(split_result) == 2:
                    label, num_nodes = line.split(None, 1)
                is_reading_vertices = True
                is_reading_arcs = is_reading_edges = False
                next_line = next(f, '').rstrip()
                if next_line.lower().startswith(('*arcs', '*edges')):
                    g.vertices = dict.fromkeys(range(1, int(num_nodes) + 1))
                    is_reading_vertices = False
                    is_reading_arcs = next_line.lower().startswith('*arcs')
                    is_reading_edges = not is_reading_arcs
                else:
                    v_id, v_label = next_line.split(None, 1)
                    g.vertices[int(v_id)] = v_label.replace('"', '')
            elif line.lower().startswith(('*arcs', '*edges')):
                is_reading_vertices = False
                is_reading_arcs = line.lower().startswith('*arcs')
                is_reading_edges = not is_reading_arcs
                next_line = next(f, '').rstrip()
                g.directed = not (is_reading_arcs and next_line.lower().startswith('*'))
            elif is_reading_vertices:
                v_id, v_label = line.split(None, 1)
                g.vertices[int(v_id)] = v_label.replace('"', '')
            elif is_reading_edges or is_reading_arcs:
                e_data = line.split()
                g.edges.append([int(i) for i in e_data])

    return g

def main():
    pass

if __name__ == '__main__':
    main()
