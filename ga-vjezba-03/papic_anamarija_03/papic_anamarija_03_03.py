# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 3 - Zadatak 3

Napisati funkciju prima matricu sa cjelobrojnim elementima i provjerava
ima li matrica točno dvije jedinice u svakom stupcu, a ostale elemente
stupca nula. Ako postoji stupac koji ne zadovoljava taj uvjet, funkcija
vraća False, inače True.

@author: Anamarija Papic
"""

from papic_anamarija_03_01 import read_matrix_from_file

def check_matrix(matrix):
    for j in range(len(matrix[0])):
        count_1s = 0
        
        for i in range(len(matrix)):
            if matrix[i][j] == 1:
                count_1s += 1
            elif matrix[i][j] != 0:
                return False
        
        if count_1s != 2:
            return False
    
    return True

matrix0 = read_matrix_from_file('resources/matrica0.txt')
matrix1 = read_matrix_from_file('resources/matrica1.txt')
matrix2 = read_matrix_from_file('resources/matrica2.txt')
matrix3 = read_matrix_from_file('resources/matrica3.txt')
matrix4 = read_matrix_from_file('resources/matrica4.txt')
matrix5 = read_matrix_from_file('resources/matrica5.txt')

print(check_matrix(matrix0))
print(check_matrix(matrix1))
print(check_matrix(matrix2))
print(check_matrix(matrix3))
print(check_matrix(matrix4))
print(check_matrix(matrix5))

