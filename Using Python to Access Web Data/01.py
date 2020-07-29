# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:10:30 2020

@author: Ikhwanul Muslimin
"""
import re

hand = open('regex_sum_826569.txt')
jumlah = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    for word in stuff:
        num = int(word)
        jumlah = jumlah + num
print(jumlah)