# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 3 - Zadatak 2

Napisati funkciju prima matricu sa cjelobrojnim elementima i vraća listu
u kojoj su elementi sume redaka u matrici.

@author: Anamarija Papic
"""

from papic_anamarija_03_01 import read_matrix_from_file

def sum_matrix_rows(matrix):
    return list(map(sum, matrix))

matrix = read_matrix_from_file('resources/matrica1.txt')

print(sum_matrix_rows(matrix))
