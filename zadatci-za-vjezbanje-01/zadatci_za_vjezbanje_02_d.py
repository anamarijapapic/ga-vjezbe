# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 2. Zadaci s dictionaryjem - (d)

Iz dictionaryja čiji su ključevi brojevi, a vrijednosti liste brojeva, 
napravite drugi dictionary čiji će ključevi biti jednaki kao u prvom, 
a vrijednosti će biti duljine lista koje su bile vrijednosti odgovarajućih ključeva
u prvom dictionaryju.

@author: Anamarija Papic
"""

def new_dictionary(d):
    new_d = dict.fromkeys(d.keys())
    
    for k, v in d.items():
        new_d[k] = len(v)
        
    return new_d

def main():
    d = {
        1: [1], 
        2: [1, 2], 
        3: [1, 1], 
        4: [1, 1, 2], 
        5: [5, 4, 5]
    }
    
    print(new_dictionary(d))

if __name__ == '__main__':
    main()
