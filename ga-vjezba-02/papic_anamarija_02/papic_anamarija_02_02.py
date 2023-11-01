# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 2 - Zadatak 2

Napisati program u kojem korisnik unosi granice dvaju zatvorenih intervala
[a, b] i [c, d] i ispisuje njihov presjek. Primjer: Za intervale [1, 5]
i [-3, 2], presjek je interval [1, 2], a za intervale [-3.5, 2] i [4, 6.5]
presjek je prazan skup.

@author: Anamarija Papic
"""

(a, b) = tuple(float(x) for x in input("Enter the limits of the 1st closed interval [a, b]: ").split(","))
(c, d) = tuple(float(x) for x in input("Enter the limits of the 2nd closed interval [c, d]: ").split(","))

lower_bound = max(a, c)
upper_bound = min(b, d)

if lower_bound < upper_bound:
    print(f'For intervals [{a}, {b}] and [{c}, {d}] the intersection is [{lower_bound}, {upper_bound}].')
else:
    print(f'For intervals [{a}, {b}] and [{c}, {d}] the intersection is the empty set.')
