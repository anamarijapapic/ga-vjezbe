# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 1. Zadaci s matricama - (b)

Napisati funkciju koja provjerava je li neka matrica kvadratna, drugu
koja provjerava je li simetrična, treću koja provjerava je li matrica
stohastička po stupcima (suma elemenata svakog stupca je 1).

@author: Anamarija Papic
"""

def is_square(matrix):
    return len(matrix) == len(matrix[0])

def is_symmetric(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
           if matrix[i][j] != matrix[j][i]:
               return False
           
    return True

def is_stochastic_by_cols(matrix):
    for j in range(len(matrix[0])):
        sum = 0
        for i in range(len(matrix)):
            sum += matrix[i][j]    
            
        if sum != 1:
            return False
        
    return True

def main():
    m1 = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, -1, -2, -3],
        [-4, -5, -6, -7]
    ]
    
    m2 = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]
    
    m3 = [
        [0.5, 0.2, 0.3],
        [0.3, 0.4, 0.3],
        [0.2, 0.4, 0.4]
    ]
    
    print(is_square(m1))
    print(is_symmetric(m2))
    print(is_stochastic_by_cols(m3))

if __name__ == '__main__':
    main()
