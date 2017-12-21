#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:02:04 2017

@author: huasheng
此文件只要看最后一个函数即可，或者一个都不看，只要知道实现的功能是什么
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties


def draw_bar_piece(dic, savefig=False, filename=None):
    """ Draw bar chart with dictionary-like data."""
    font_set = FontProperties(fname=r"/home/huasheng/Downloads/simsun/simsun.ttc", size=12)
    plt.clf()
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    xticklabels = dic.keys()
    print(xticklabels)
    scores = dic.values()
    width = 0.4
    ind = np.linspace(0.5,9.5,len(xticklabels))
    ax.bar(ind, scores, width, color='g')
    ax.set_xticks(ind)
    ax.set_xticklabels(xticklabels, fontproperties=font_set, rotation=45)
#    ax.set_xticklabels(['u性价比', u'补水', u'效果', u'东西', u'宝贝', u'产品', u'喷雾', u'正品', u'质量', u'生产日期', u'保湿', u'吸收', u'包裹', u'包装', u'扭曲'])
    ax.set_xlabel(u'特征词', fontproperties=font_set)
    ax.set_ylabel(u'情感值', fontproperties=font_set, fontstyle='italic', fontsize=15)
    ax.set_title(u'还没想好叫什么', fontproperties=font_set, fontstyle='italic', fontsize=20)
#    plt.grid(True)
    if savefig == True:
        plt.savefig(filename, dpi=480)
    plt.show()
    plt.close()


def draw_bar(score, savefig=False, filename=None):
#    font_set = FontProperties(fname=r"/home/huasheng/Downloads/simsun/simsun.ttc", size=12)
    Scores = {}
    xticklabels = score.keys()
    for xlabel in xticklabels:
        feature_dict = score[xlabel]
        feature_scores = 0
        for feature in feature_dict:
            feature_scores += feature_dict[feature]
        Scores[xlabel] = feature_scores

    draw_bar_piece(Scores, savefig, filename)


def draw_bar_chart(Score, savefig=False, filename=None):
    length = len(Score)
    xlabelticks = Score[0].keys()
    result = {0:[], 1:[], 2:[]}
    for i in range(length):
        score = Score[i]
        for tick in xlabelticks:
            result[i].append(sum(score[tick].values()))

    font_set = FontProperties(fname=r"/home/huasheng/Downloads/simsun/simsun.ttc", size=12)
    plt.clf()
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    width = 0.4
    ind0 = np.linspace(0.5, 8, len(xlabelticks))
    ind1 = np.linspace(1, 8.5, len(xlabelticks))
    ind2 = np.linspace(1.5, 9, len(xlabelticks))
    b1 = ax.bar(ind0, result[0], width, color='g')
    b2 = ax.bar(ind1, result[1], width, color='b')
    b3 = ax.bar(ind2, result[2], width, color='r')

#, legend='京东', legend='考拉', legend='天猫'
    ax.set_xticks(ind1)
    ax.set_xticklabels(['价格因素', '物流因素', '质量因素', '客服态度'], fontproperties=font_set, rotation=0)
#    ax.set_xticklabels(['u性价比', u'补水', u'效果', u'东西', u'宝贝', u'产品', u'喷雾', u'正品', u'质量', u'生产日期', u'保湿', u'吸收', u'包裹', u'包装', u'扭曲'])
    ax.set_xlabel(u'特征词', fontproperties=font_set)
    ax.set_ylabel(u'情感值', fontproperties=font_set, fontstyle='italic', fontsize=15)
#    ax.set_title(u'', fontproperties=font_set, fontstyle='italic', fontsize=20)
#    plt.grid(True)
    ax.legend([b1, b2, b3], ['京东', '考拉', '天猫'], loc=2, prop=font_set)
    if savefig == True:
        plt.savefig(filename, dpi=480)
    plt.show()
    plt.close()
#    return result
