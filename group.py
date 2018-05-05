#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 12:31:49 2018

@author: liurenrong
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1':['a','a','b','b','a'],'key2':['one','two','one','two','one'],'data1':np.random.randn(5),'data2':np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])

#for name, group in df.groupby('key1'):
#    print(name)
#    print(group)

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
     'd': 'blue', 'e': 'red', 'f' : 'orange'}
print(pd.Series(mapping))
