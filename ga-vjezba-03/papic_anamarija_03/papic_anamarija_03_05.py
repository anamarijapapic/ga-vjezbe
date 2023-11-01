# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 3 - Zadatak 5

Dan je dictionary kojem su ključevi brojevi, a vrijednosti liste brojeva.
Napisati funkciju koja okreće dictionary, na način da brojevi iz value listi
postaju keys, a keys postaju članovi value listi.
Primjer: Za d = {1:[2,3,5], 2:[1, 4], 3:[1,2]} novi dictionary je {1:[2,3],
2:[1,3], 3:[1], 4:[2], 5:[1]}

@author: Anamarija Papic
"""

def reverse_dictionary(d):
    rev_dict = {}
    
    for k, v in d.items():
        for el in v:
            if el in rev_dict:
                rev_dict[el].append(k)
            else:
                rev_dict[el] = [k]
    
    return dict(sorted(rev_dict.items()))

d = {
     1: [2,3,5], 
     2: [1, 4], 
     3: [1,2]
}

print(reverse_dictionary(d))
