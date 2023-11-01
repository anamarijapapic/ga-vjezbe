# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 3 - Zadatak 1

Napisati funkciju koja iz datoteke čita matricu sa cjelobrojnim elementima
i vraća zbroj elemenata iznad glavne dijagonale i zbroj elemenata iznad
sporedne dijagonale. Ako matrica nije kvadratna, funkcija vraća nule.

Primjer: Za matricu
2 4 6 8
5 3 4 6
1 3 5 6
0 3 5 7
funkcija vraća (34, 21).

@author: Anamarija Papic
"""

def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        matrix = [[int(num) for num in line.split()] for line in f]
    
    return matrix

def sum_elements_above_matrix_diagonals():
    matrix = read_matrix_from_file('resources/matrica0.txt')
    
    n = len(matrix)
    
    if n != len(matrix[0]):
        return (0, 0)
    
    sum_above_major_d = 0
    sum_above_minor_d = 0
    
    for i in range(n):
        for j in range(n):
            if i < j:
                sum_above_major_d += matrix[i][j]
            if i < n - j - 1:
                sum_above_minor_d += matrix[i][j]
    
    return (sum_above_major_d, sum_above_minor_d)

print(sum_elements_above_matrix_diagonals())
