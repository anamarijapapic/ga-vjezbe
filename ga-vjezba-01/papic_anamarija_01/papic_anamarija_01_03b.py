# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 1 - Zadatak 3b

Napisati sljedeće funkcije:
(b) funkciju koja vraća n-ti prosti broj,

@author: Anamarija Papic
"""

from papic_anamarija_01_03 import is_prime_number

def find_nth_prime_number(n):
    count = 0
    candidate = 2
    
    while True:
        if is_prime_number(candidate):
            count += 1
            
            if count == n:
                return candidate
        
        candidate += 1

print('{}-ti prosti broj je: {}'.format(10, find_nth_prime_number(10)))
print('{}-ti prosti broj je: {}'.format(100, find_nth_prime_number(100)))
