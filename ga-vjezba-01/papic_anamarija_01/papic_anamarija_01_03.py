# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 1 - Zadatak 3

Definirati funkciju koja provjerava je li broj prost.

@author: Anamarija Papic
"""

def is_prime_number(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# print(is_prime_number(1))
# print(is_prime_number(2))
# print(is_prime_number(3))
# print(is_prime_number(4))
# print(is_prime_number(5))
# print(is_prime_number(9))
