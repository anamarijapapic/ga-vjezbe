# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 1. Zadaci s matricama - (e)

Napisati funkciju koja transponira matricu.

@author: Anamarija Papic
"""

def transpose(matrix):
    matrix_t = []
    
    for i in range(len(matrix[0])):
        matrix_t.append([0] * len(matrix))
        
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_t[j][i] = matrix[i][j]

    return matrix_t
            

def main():
    m = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    print(transpose(m))

if __name__ == '__main__':
    main()
