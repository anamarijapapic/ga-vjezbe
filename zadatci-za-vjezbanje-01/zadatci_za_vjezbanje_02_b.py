# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 2. Zadaci s dictionaryjem - (b)

Napisati funkciju koja generira pseudoslučajni prirodni broj k, te listu
od k pseudoslučajnih elemenata čije su vrijednosti u rasponu 1...n.

@author: Anamarija Papic
"""

import random

def generate(n):
    k = random.randint(1, n)
    lst = [random.randint(1, n) for el in range(k)]
    
    return k, lst  

def main():
    print(generate(2))

if __name__ == '__main__':
    main()
