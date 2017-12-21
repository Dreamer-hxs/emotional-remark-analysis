#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:42:27 2017

@author: huasheng
"""

import sys
import os
#import chardet
import urllib

current_path = os.path.abspath('.')
filename = current_path + '/cleaned_data/TMallReviewDatas.csv'
#f = open(filename, 'rb')
#f_read = f.read()
#f_charInfo = chardet.detect(f_read)
#f_read_decode = f_read.decode(f_charInfo['encoding'])
#print(f_read_decode[:100])
#with open(filename, 'rb') as f:
##    print(len(f))
#    for line in f:
#        print(line.decode('utf-8')[:20])

with open(filename, 'rb') as f:
    f.readline()
    url_get_base = "http://api.ltp-cloud.com/analysis/?"
    args = {
        'api_key' : 'Z1q5D7h2h12Q8q0VMh4ZON4qfDfYigyAILbnWnJQ',
        'text' : urllib.request.quote(f.readline()),
        'pattern' : 'dp',
        'format' : 'xml'
    }

    result = urllib.request.urlopen(url_get_base + urllib.parse.urlencode(args)) # POST method
    content = result.read().decode('utf-8').strip()
    print(content)


#
#url      = (uri_base
#               + "api_key=" + api_key + "&"
#               + "text="    + text    + "&"
#               + "format="  + format  + "&"
#               + "pattern=" + "all")
#
#    try:
#        response = urllib2.urlopen(url)
#        content  = response.read().strip()
#        print content
#    except urllib2.HTTPError, e:
#print >> sys.stderr, e.reason
