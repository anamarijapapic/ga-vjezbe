# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 1. Zadaci s matricama - (a)

Dana je datoteka u kojoj su u svakom retku tri broja i, j, w. Napisati
funkciju koja čita datoteku i iz nje puni matricu A na način da vrijedi
A[i][j]=w.

@author: Anamarija Papic
"""

def read_to_matrix(filename):
    matrix = []
    data = []
    
    with open(filename, 'r') as f:
        for line in f:
            i, j, w = [float(num) for num in line.split()]
            data.append((i, j, w))
    
    max_i = data[0][0]
    max_j = data[0][1]
    
    for el in data:
        max_i = max(max_i, el[0])
        max_j = max(max_j, el[0])
    
    for i in range(int(max_i) + 1):
        matrix.append([])
        for j in range(int(max_j) + 1):
            matrix[i].append(0)
            
    for el in data:
        matrix[int(el[0])][int(el[1])] = el[2]
    
    return matrix

def main():
    m = read_to_matrix('resources/matrica-generator.txt')
    print(m)
    
if __name__ == '__main__':
    main()
