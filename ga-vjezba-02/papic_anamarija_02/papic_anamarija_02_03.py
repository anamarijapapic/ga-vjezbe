# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 2 - Zadatak 3

Napisati funkciju koja u stringu nalazi koliko ima susjednih samoglasnika.

@author: Anamarija Papic
"""

def count_neighbour_vowels(string):
    neighbour_vowels = ['ae', 'ei', 'io', 'ou']
    neighbour_vowels_r = [''.join(reversed(pair)) for pair in neighbour_vowels]
    neighbour_vowels_all = neighbour_vowels + neighbour_vowels_r
    
    return sum(string.lower().count(pair) for pair in neighbour_vowels_all)

print(count_neighbour_vowels('Queueing')) # 1
print(count_neighbour_vowels('Aerosmith')) # 1
print(count_neighbour_vowels('aeiou')) # 4
print(count_neighbour_vowels('aeiouoiea')) # 8
