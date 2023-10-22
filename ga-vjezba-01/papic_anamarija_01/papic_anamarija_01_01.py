# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Vjezba 1 - Zadatak 1

Napisati program u kojem se unose trojke brojeva. Za svaku trojku ispitati
da li je pitagorejska trojka (brojevi zadovoljavaju pitagorin teorem).
Unos ponavljati sve dok se ne unese barem jedan negativni broj ili nula.

@author: Anamarija Papic
"""

print('# Pythagorean Triple Checker')
print('# a^2 + b^2 = c^2')

while(True):
    nums = []
    
    nums = [int(x) for x in input('Enter a triple of numbers (separate numbers by a space): ').split()]
    
    if len([x for x in nums if x > 0]) != 3:
        print('Exiting!')
        break
    
    nums.sort()
    print(f'---\na = {nums[0]}\tb = {nums[1]}\tc = {nums[2]}')
    
    if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
        print(f'---\n{nums[0]}^2 + {nums[1]}^2 = {nums[2]}^2')
        print('A pythagorean triple!')
    else:
        print('Not a pythagorean triple.')
