# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 1. Zadaci s matricama - (d)

Napisati funkciju koja računa umnožak matrica i drugu koja računa zbroj.
Ako dimenzije matrica nisu ispravne, funkcije bacaju iznimke.

@author: Anamarija Papic
"""

def matrix_multiplication(m1, m2):
    if len(m1[0]) != len(m2):
        raise Exception('Dimensions error')
        
    result = []
    
    for i in range(len(m1)):
        result.append([0] * len(m2[0]))
    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
            
    return result

def matrix_addition(m1, m2):
    if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):
        raise Exception('Dimensions error')
        
    result = []
    
    for i in range(len(m1)):
        result.append([])
    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i].append(m1[i][j] + m2[i][j])
            
    return result

def main():
    m1 = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]
    
    m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    m3 = [
        [1, 5, 4],
        [9, 3, 8]
    ]

    m4 = [
        [6, 7],
        [1, 3],
        [5, 9]
    ]

    try:
        print(matrix_addition(m1, m2))
        print(matrix_multiplication(m1, m2))
        print(matrix_multiplication(m3, m4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
