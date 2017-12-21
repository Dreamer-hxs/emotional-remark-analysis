#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:02:40 2017

@author: huasheng
"""

import re
from collections import Counter

filename = 'cut_pos.txt'
with open(filename, 'r') as fr:
    contents = fr.read()
    nouns = re.findall(r'[a-z]?(\w+)/n', contents)
    c = Counter(nouns)
    print(c.most_common(20))
    with open('nouns.txt', 'w') as fw:
        fw.write(str(c.most_common()))
