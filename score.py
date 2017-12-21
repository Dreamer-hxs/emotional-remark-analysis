#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:09:15 2017

@author: huasheng
"""

import re
import os
from feature_extraction import features
from global_values import adverb_score, adj_score

def set_default(keys):
    dic = {}
    for k in keys:
        dic.setdefault(k, 0)
    return dic



price, quality = features[0], features[1]
express, customer_service = features[2], features[3]


def compute_Score(dirname):
    S = {}   # A big dict holding all the score values. It has basic shape like S['price'], S['quality'], S['express'], S['customer_service'], and each of them is another dict, such as S['quality']['东西'], S['express']['物流'] stores scores on feature '东西' '物流'
    S['price'] = set_default(price.keys())
    S['express'] = set_default(express.keys())
    S['quality'] = set_default(quality.keys())
    S['customer_service'] = set_default(customer_service.keys())


    os.chdir(dirname)
    files = ['n_a.txt', 'n_d_a.txt', 'n_d_d_a.txt', 'v_a.txt']
    for file in files:
        with open(file, 'r') as fr:
            contents = fr.read()
            # in this two cases we dont need to consider adverb_score
            if file == 'n_a.txt' or file == 'v_a.txt':
                for feature in features:
                    if feature == price:
                        s = 'price'
                    elif feature == quality:
                        s = 'quality'
                    elif feature == express:
                        s = 'express'
                    elif feature == customer_service:
                        s = 'customer_service'
    #TODO: change the regular expression
                    for k in feature:
                        result = re.findall(r'%s/n?[a-z]?(.{1,2})/a'%k, contents)
    #                    if k=='包装':
    #                        print(result)
                        scores = 0
                        if len(result) == 0:
                            continue
                        for r in result:
                            score = adj_score[s][k].get(r, 0)
                            scores += score
                        scores /= len(result)
                        S[s][k] += scores
            # in this two cases we should carefully consider adverb_score
            elif file == 'n_d_a.txt':
                for feature in features:
                    if feature == price:
                        s = 'price'
                    elif feature == quality:
                        s = 'quality'
                    elif feature == express:
                        s = 'express'
                    elif feature == customer_service:
                        s = 'customer_service'
                    for k in feature:
                        result = re.findall(r'%s/n[a-z]?(.{1,2})/d(.{1,2}?)/a'%k, contents)
                        scores = 0
                        if len(result) == 0:
                            continue
                        for r in result:
                            score = adverb_score.get(r[0], 0) * adj_score[s][k].get(r[1], 0)
                            scores += score
                        scores /= len(result)
                        S[s][k] += scores
            elif file == 'n_d_d_a.txt':
                for feature in features:
                    if feature == price:
                        s = 'price'
                    elif feature == quality:
                        s = 'quality'
                    elif feature == express:
                        s = 'express'
                    elif feature == customer_service:
                        s = 'customer_service'
                    for k in feature:
                        result = re.findall(r'%s/n[a-z]?(.{1,2})/d(.{1,2})/d(.{1,2})/a'%k, contents)
                        scores = 0
                        if len(result) == 0:
                            continue
                        for r in result:
                            score = adverb_score.get(r[0], 0) * adverb_score.get(r[1], 0) * adj_score[s][k].get(r[2], 0)
                            scores += score
                        scores /= len(result)
                        S[s][k] += scores

    return S