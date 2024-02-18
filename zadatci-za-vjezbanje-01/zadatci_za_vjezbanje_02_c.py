# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 2. Zadaci s dictionaryjem - (c)

Napisati funkciju koja generira dictionary na sljedeći način. Za dani
prirodan broj n ključevi su brojevi između 1 i n. Za svaki ključ vrijednost
ključa je pseudoslučajna lista brojeva iz prethodnog zadatka.

@author: Anamarija Papic
"""

from zadatci_za_vjezbanje_02_b import generate

def create_dictionary(n):
    d = dict.fromkeys(range(1, n + 1))
    
    for k, v in d.items():
        d[k] = generate(k)[1]
    
    return d

def main():
    print(create_dictionary(10))

if __name__ == '__main__':
    main()
