# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 1 - Zadatak 3c

Napisati sljedeće funkcije:
(c) funkciju koja ispisuje i vraća sve susjedne proste brojeve do n. Za
dva prosta broja kažemo da su susjedni ako im je razlika jednaka 2.

@author: Anamarija Papic
"""

from papic_anamarija_01_03 import is_prime_number

def find_twin_prime_numbers(n):
    twin_prime_numbers = []

    for i in range(2, n - 1):
        if is_prime_number(i) and is_prime_number(i + 2):
            twin_prime_numbers.append((i, i + 2))
    
    return twin_prime_numbers

print(find_twin_prime_numbers(200))
