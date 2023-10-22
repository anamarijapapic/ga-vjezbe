# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 1 - Zadatak 3a

Napisati sljedeće funkcije:
(a) funkciju koja vraća koliko je prostih brojeva između dva decimalna
broja,

@author: Anamarija Papic
"""

from papic_anamarija_01_03 import is_prime_number
import math

def count_prime_numbers_between(x, y):
    count = 0
    
    lower_bound = math.ceil(min(x, y))
    upper_bound = math.floor(max(x, y))
    
    for i in range(lower_bound, upper_bound + 1):
        if is_prime_number(i):
            count += 1
    
    return count

print(count_prime_numbers_between(2, 10))
print(count_prime_numbers_between(4.5, 2.1))
