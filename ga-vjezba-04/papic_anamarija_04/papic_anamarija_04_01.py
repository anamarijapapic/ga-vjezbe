# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 4 - Zadatak 1

Napisati funkcije koje će raditi konverzije zapisa grafa u matricu susjedstva, 
matricu incidencije i listu susjedstva grafa (iz svake strukture radi se 
konverzija u ostale dvije).

@author: Anamarija Papic
"""

def adjacency_matrix_to_adjacency_list(adjacency_matrix):
    n = len(adjacency_matrix)
    
    adjacency_list = []
    for i in range(n):
        adjacency_list.append([])

    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                adjacency_list[i].append(j)

    return adjacency_list

def adjacency_matrix_to_incidence_matrix(adjacency_matrix):
    n = len(adjacency_matrix)
    m = sum(sum(row) for row in adjacency_matrix) // 2

    incidence_matrix = []
    for i in range(n):
        incidence_matrix.append([0] * m)

    edge_index = 0
    for i in range(n):
        for j in range(i + 1, n):
            if adjacency_matrix[i][j] == 1:
                incidence_matrix[i][edge_index] = 1
                incidence_matrix[j][edge_index] = 1
                edge_index += 1

    return incidence_matrix

def adjacency_list_to_adjacency_matrix(adjacency_list):
    n = len(adjacency_list)
    
    adjacency_matrix = []
    for i in range(n):
        adjacency_matrix.append([0] * n)

    for i in range(n):
        for neighbor in adjacency_list[i]:
            adjacency_matrix[i][neighbor] = 1

    return adjacency_matrix

def adjacency_list_to_incidence_matrix(adjacency_list):
    n = len(adjacency_list)
    m = sum(len(neighbors) for neighbors in adjacency_list) // 2

    incidence_matrix = []
    for i in range(n):
        incidence_matrix.append([0] * m)

    edge_index = 0
    for i in range(n):
        for neighbor in adjacency_list[i]:
            if i < neighbor:
                incidence_matrix[i][edge_index] = 1
                incidence_matrix[neighbor][edge_index] = 1
                edge_index += 1

    return incidence_matrix

def incidence_matrix_to_adjacency_matrix(incidence_matrix):
    n = len(incidence_matrix)
    m = len(incidence_matrix[0])

    adjacency_matrix = []
    for i in range(n):
        adjacency_matrix.append([0] * n)

    for edge_index in range(m):
        connected_vertices = [i for i in range(n) if incidence_matrix[i][edge_index] == 1]
        adjacency_matrix[connected_vertices[0]][connected_vertices[1]] = 1
        adjacency_matrix[connected_vertices[1]][connected_vertices[0]] = 1

    return adjacency_matrix

def incidence_matrix_to_adjacency_list(incidence_matrix):
    n = len(incidence_matrix)
    m = len(incidence_matrix[0])

    adjacency_list = []
    for i in range(n):
        adjacency_list.append([])

    for edge_index in range(m):
        connected_vertices = [i for i in range(n) if incidence_matrix[i][edge_index] == 1]
        adjacency_list[connected_vertices[0]].append(connected_vertices[1])
        adjacency_list[connected_vertices[1]].append(connected_vertices[0])

    return adjacency_list

def main():
    pass

if __name__=='__main__':
    main()
