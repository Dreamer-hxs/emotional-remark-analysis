#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:35:20 2017

@author: huasheng
"""

import re
import os

current_path = os.path.abspath('.')
file_dir = [os.path.join(current_path, i) for i in['JDReviewDatas', 'KaoLaReviewDatas', 'TMallReviewDatas']]
for file in file_dir:
    os.chdir(file)
    filename = 'cut_pos.txt'
    f1 = open('n_a.txt', 'w')  # store pattern /n/a
    f2 = open('n_d_a.txt', 'w') # store pattern /n/d/a
    f3 = open('n_d_d_a.txt', 'w') # store pattern /n/d/d/a
    f4 = open('v_a.txt', 'w') # store pattern /v/a

    with open(filename, 'r') as fr:
        contents = fr.read()
        n_a = re.findall(r'[a-z]*(\w+/n[a-z]?\w+/a)', contents)  # findall /n/a pattern
        n_d_a = re.findall(r'[a-z]*(\w+/n[a-z]?\w+/d[a-z]?\w+/a)', contents)  # findall /n/d/a pattern
        n_d_d_a = re.findall(r'[a-z]*(\w+/n[a-z]?\w+/d\w+/d\w+/a)', contents) # findall /n/d/d/a pattern
        v_a = re.findall(r'[a-z]*(\w+/v\w+/a)', contents)  # findall /v/a pattern
        f1.write(str(n_a))
        f2.write(str(n_d_a))
        f3.write(str(n_d_d_a))
        f4.write(str(v_a))

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    os.chdir('.')