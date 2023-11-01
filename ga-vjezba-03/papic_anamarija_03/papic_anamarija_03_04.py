# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 3 - Zadatak 4

U datoteci se u svakom retku nalaze dva cijela broja. Napisati funkciju
koja čita datoteku i sprema podatke u dictionary tako da je prvi broj u
retku ključ, a drugi broj element liste vrijednosti tog ključa.

@author: Anamarija Papic
"""

def save_dictionary_from_file(filename):
    with open(filename, 'r') as f:
        d = dict([int(num) for num in line.split()] for line in f)
    
    return d

print(save_dictionary_from_file('resources/rjecnik.txt'))
