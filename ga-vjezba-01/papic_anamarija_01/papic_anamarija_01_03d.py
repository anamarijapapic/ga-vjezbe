# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 1 - Zadatak 3d

Napisati sljedeće funkcije:
(d) funkciju koja za uneseni paran broj ispisuje sve različite načine na
koje se on može prikazati kao zbroj dva prosta broja. Pretpostavka
je da se svaki parni broj može napisati u obliku zbroja dva prosta
broja (Goldbachova slutnja).

@author: Anamarija Papic
"""

from papic_anamarija_01_03 import is_prime_number

def goldbach_conjecture(n):
    if n <= 2 or n % 2 != 0:
        return
    
    prime_numbers = [i for i in range(2, n) if is_prime_number(i)]
    
    for x in prime_numbers:
        y = n - x
        
        if y < x:
            break
        
        if y in prime_numbers:
            print(f"{n} = {x} + {y}")

goldbach_conjecture(200)
