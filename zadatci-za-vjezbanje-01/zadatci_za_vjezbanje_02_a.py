# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 2. Zadaci s dictionaryjem - (a)

Napisati funkciju koja iz matrice a takve da je A[i][j]=w kreira dictionary
u kojem su oznake redaka i ključevi, a vrijednosti lista uređenih parova
(j, w) za svaki j za koji je w razlicit od 0.

@author: Anamarija Papic
"""

def create_dictionary_from_matrix(matrix):
    d = {}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                if i in d.keys():
                    d[i].append((j, matrix[i][j]))
                else:
                    d[i] = [(j, matrix[i][j])]
                
    return d
            

def main():
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [-1, 0, 1]
    ]
    
    print(create_dictionary_from_matrix(m))

if __name__ == '__main__':
    main()
