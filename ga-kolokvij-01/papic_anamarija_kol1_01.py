# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Kolokvij 1 - Zadatak 1

@author: Anamarija Papic
"""

def read_matrix_from_file(filename):
    matrix = []
    
    with open(filename, 'r') as f:
        for line in f:
            els = []
            for el in line.split():
                els.append(int(el))
            matrix.append(els)
    
    return matrix

# za neki jednostavni neusmjereni graf
def check_if_incidence_matrix(matrix):
    # Matrica incidencije M (incidence matrix) 
    # grafa G je n × m matrica M = M(G) = [mij], 
    # gdje je mij ∈ {0, 1, 2} broj koliko puta su vi i ej incidentni.
    n = len(matrix)
    m = len(matrix[0])
    
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += matrix[i][j]
            
        if sum < 0 or sum > 2:
            return False
    
    return True
    # Expected results: F, F, T, T

# za neki jednostavni neusmjereni graf
def check_if_adjacency_matrix(matrix):
    # Matrica susjedstva A (adjacency matrix) 
    # grafa G je n × n matrica t.d. vrijedi
    # Aij = {
    #   aij, aij broj bridova koji spajaju vi i vj
    #   0, inače
    # Svojstva matrice susjedstva:
    # A je simetrična
    # Ako je graf G jednostavan, onda je aij ∈ {0, 1} i aii = 0.
    # Ako je graf G prazan, onda je aij = 0, ∀i, j ∈ {1, .., n}.
    
    # check if square
    n = len(matrix)
    if n != len(matrix[0]):
        return False
    
    # check if symmetrical and if fulfills 'simple graph' conditions
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
            if matrix[i][i] != 0:
                return False
            if matrix[i][j] < 0 or matrix[i][j] > 1:
                return False
    
    return True

def main():
    m1 = read_matrix_from_file('C1-1.txt')
    m2 = read_matrix_from_file('C1-2.txt')
    m3 = read_matrix_from_file('C1-3.txt')
    m4 = read_matrix_from_file('C1-4.txt')
    
    print(
        check_if_incidence_matrix(m1),
        check_if_incidence_matrix(m2),
        check_if_incidence_matrix(m3),
        check_if_incidence_matrix(m4)
    )
    
    print(
        check_if_adjacency_matrix(m1),
        check_if_adjacency_matrix(m2),
        check_if_adjacency_matrix(m3),
        check_if_adjacency_matrix(m4)
    )

if __name__ == '__main__':
    main()
