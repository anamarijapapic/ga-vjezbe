# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 2 - Zadatak 5

Napisati iterativnu i rekurzivnu funkciju koja za listu vraća element
najveće brojčane vrijednosti. Vrijednosti u listi koji nisu brojevi ignorira.
Primjer: Za listu lst = [7, 18, 3, 'a', True, (2,3)] funkcija vraća 18.

@author: Anamarija Papic
"""

def find_max_i(lst):
    max_element = None
    
    for x in lst:
        if type(x) in (float, int):
            if max_element is None or x > max_element:
                max_element = x
    
    return max_element

def find_max_r(lst):
    if not lst:
        return
    
    if type(lst[0]) in (float, int):
        max_element = find_max_r(lst[1:])
        
        if max_element is None or lst[0] > max_element:
            return lst[0] 
        else:
            return max_element
    
    return find_max_r(lst[1:])

print(find_max_i([7, 18, 3, 'a', True, (2,3)]))
print(find_max_i(['a', True, (2,3)]))

print(find_max_r([7, 18, 3, 'a', True, (2,3)]))
print(find_max_r(['a', True, (2,3)]))
