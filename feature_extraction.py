#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:09:25 2017

@author: huasheng
"""

import re


def set_default(keys):
    dic = {}
    for k in keys:
        dic.setdefault(k, [])
    return dic

def modify_feature(features):
    # remove some unreasonable words
    price, quality = features[0], features[1]
    express, customer_service = features[2], features[3]
    quality['东西'].remove('s好')
    quality['喷雾'].remove('镇静')
    quality['补水'].remove('阔')
    quality['正品'].remove('大')
    quality['东西'].remove('直接')
    quality['东西'].remove('确实')
    quality['效果'].remove('确实')
    quality['效果'].remove('重')
    customer_service['人'].remove('凉快')
    return [price, quality, express, customer_service]






price = ['价格']
quality = ['性价比', '补水', '效果', '东西', '宝贝', '产品', '喷雾', '正品', '质量', '生产日期', '保湿', '吸收', '包裹', '包装', '扭曲']
express = ['发货', '物流', '速度', '快递', '送货']
customer_service = ['客服', '服务态度', '态度', '人', '服务', '回复']

# 用字典存储特征词和情感词对
price = set_default(price)
quality = set_default(quality)
express = set_default(express)
customer_service = set_default(customer_service)
features = [price, quality, express, customer_service]
 # 提取情感词
files = ['n_a.txt', 'n_d_a.txt', 'n_d_d_a.txt', 'v_a.txt']
for file in files:
    with open(file, 'r') as f:
        contents = f.read()
        for feature in features:
            for k in feature:
                result = re.findall(r'%s[\w/]*?[a-z]?(.{1,2})/a'%k, contents)   # 这行代码把我折磨哭了
                feature[k] += result

#file = 'n_d_a.txt'
#with open(file, 'r') as f:
#    contents = f.read()
#    for k in express:
#        expressions = re.findall(r'%s/[nv][\w/]*?d?(.{1,2})/a'%k, contents)
#        express[k] += expressions

for feature in features:
    for k in feature:
        feature[k] = list(set(feature[k]))

# 人工修改情感词，因为有一些不符合逻辑
features = modify_feature(features)

# store these features
with open('features.txt', 'w') as fw:
    for feature in features:
        fw.write(str(feature))
