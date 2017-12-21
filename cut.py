#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:42:27 2017

@author: huasheng
"""

import os
import jieba.posseg
import re
import glob

current_path = os.path.abspath('.')
filedir = os.path.join(current_path, '*.csv')
file_list = glob.glob(filedir)   # find all .csv files
for file in file_list:
    base, ext = os.path.splitext(file)  # split a filename into base + extension
#    print(base)
#    ideal_path = os.path.join(current_path, base)
    if not os.path.exists(base):  # if not exist the directory, create it.
        os.mkdir(base)
    os.chdir(base)  # change into the directory
    with open(file, 'rb') as f:
        f.readline()
        f2 = open('cut_pos.txt', 'w')  # store the results in cut_pos.txt
        words = jieba.posseg.cut(f.read())
        for i, j in words:
            f2.write("%s/%s" % (i, j))
        f2.close()
    os.chdir('..')

# processing the cut_pos.txt, i.e. to remove '/x'
for file in file_list:
    base, ext = os.path.splitext(file)
    os.chdir(base)
    with open('cut_pos.txt', 'a+') as fw:
        fw.seek(0)  # make file pointer point to first byte
        new_contents = re.sub('/x', '', fw.read())  # /x可能是空格，换行,都删除
        fw.seek(0)  # make file pointer point to first byte
        fw.truncate() # clear the file
        fw.write(new_contents)
    os.chdir('..')

