# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 2 - Zadatak 1

Napisati funkciju koja za dvije liste vraća listu koja se sastoji od 
elemenata koji se nalaze u obje liste bez iteriranja po listama.

@author: Anamarija Papic
"""

def intersect(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(intersect([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]))
