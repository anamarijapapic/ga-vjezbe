# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 1. Zadaci s matricama - (c)

Napisati funkciju koja računa zbroj elemenata na glavnoj dijagonali i zbroj
elemenata na sporednoj dijagonali. Ako matrica nije kvadratna, funkcija
baca iznimku.

@author: Anamarija Papic
"""

def sum_major_and_minor_diagonal(matrix):
    n = len(matrix)
    
    if n != len(matrix[0]):
        raise Exception('Not a square matrix')
    
    sum_major_d = 0
    sum_minor_d = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                sum_major_d += matrix[i][j]
            if i == n - j:
                sum_minor_d += matrix[i][j]
                
    return sum_major_d, sum_minor_d

def main():
    m1 = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]
    
    m2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    
    print(sum_major_and_minor_diagonal(m1))
    print(sum_major_and_minor_diagonal(m2))

if __name__ == '__main__':
    main()
