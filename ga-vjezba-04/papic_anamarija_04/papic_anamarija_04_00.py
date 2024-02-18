# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 4 - Zadatak 0

Napisati funkciju koja čita datoteku u kojoj je zapisan graf u pajek formatu i sprema
podatke o grafu u strukturu podataka po volji (matricu susjedstva, matricu incidencije
ili listu susjedstva grafa).

@author: Anamarija Papic
"""

class Graph:
    def __init__(self, vertices = None, edges = None, directed = False):
        self.vertices = vertices or {}
        self.edges = edges or []
        self.directed = directed
        
    def __str__(self):
        return f'''Graph:
Vertices ({len(self.vertices)}): {self.vertices}
Edges: {self.edges}
Directed: {self.directed}
'''

    def to_adjacency_matrix(self):
        max_vertex = max(max(self.vertices, default=0), *map(lambda x: max(x) if isinstance(x, list) else x, self.edges), default=0)
        n = max(max_vertex, len(self.vertices))
        
        adjacency_matrix = []
        for i in range(n):
            adjacency_matrix.append([0] * n)

        for edge in self.edges:
            if len(edge) == 2:
                i, j = edge
                adjacency_matrix[i - 1][j - 1] = 1
                if not self.directed:
                    adjacency_matrix[j - 1][i - 1] = 1

        return adjacency_matrix

    def to_incidence_matrix(self):
        n = len(self.vertices)
        m = len(self.edges)
        
        incidence_matrix = []
        for i in range(n):
            incidence_matrix.append([0] * m)

        for edge_index, edge in enumerate(self.edges):
            for vertex_index, vertex in enumerate(self.vertices, start=1):
                if vertex in edge:
                    incidence_matrix[vertex_index - 1][edge_index] = 1 if vertex == edge[0] else -1

        return incidence_matrix

    def to_adjacency_list(self):
        adjacency_list = {}

        for edge in self.edges:
            if len(edge) == 2:
                i, j = edge
            elif len(edge) == 3:
                i, j, weight = edge
            
            label_i = self.vertices.get(i, str(i))
            label_j = self.vertices.get(j, str(j))

            adjacency_list.setdefault(label_i, []).append(label_j)

            if not self.directed:
                adjacency_list.setdefault(label_j, []).append(label_i)

        return adjacency_list

def read_parse_pajek(filename, encoding = 'utf-8'):
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
    g = read_parse_pajek('resources/pajek_example.net')
    # g = read_parse_pajek('resources/euler.net')
    # g = read_parse_pajek('resources/football.net')
    # g = read_parse_pajek('resources/airports-split.net')
    # g = read_parse_pajek('resources/eva.net')
    
    print(g)

if __name__=='__main__':
    main()
