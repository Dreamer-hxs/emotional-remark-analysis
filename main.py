#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:22:45 2017

@author: huasheng
"""

import os
from visualization import draw_bar_piece, draw_bar, draw_bar_chart
from score import compute_Score

current_path = os.path.abspath('.')
file_dir = [os.path.join(current_path, i) for i in['JDReviewDatas', 'KaoLaReviewDatas', 'TMallReviewDatas']]
Score = []
for file in file_dir:
    Score.append(compute_Score(file))



result = draw_bar_chart(Score, savefig=True, filename='final_result.png')
