# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 1 - Zadatak 2

Napisati funkciju koja će za prirodan broj n < 20 ispisati brojevni trokut
prema sljedećem primjeru (za n = 9):

1
2 3 2
3 4 5 4 3
4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
6 7 8 9 0 1 0 9 8 7 6
7 8 9 0 1 2 3 2 1 0 9 8 7
8 9 0 1 2 3 4 5 4 3 2 1 0 9 8
9 0 1 2 3 4 5 6 7 6 5 4 3 2 1 0 9

@author: Anamarija Papic
"""

print('# Number Triangle (Incrementing Palindrome Triangle)\n')

def number_triangle(n):
    if n < 1 or n >= 20:
        print('Invalid input.')
        return
    
    for i in range(1, n + 1):
        for j in range(i, 2 * i):
            print(j % 10, end = '')
        
        for j in reversed(range(i, 2 * i - 1)):
            print(j % 10, end = '')
        
        print()

number_triangle(9)
# number_triangle(19)
# number_triangle(20)
