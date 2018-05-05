#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:32:56 2018

@author: liurenrong
"""

import pandas as pd

path = "000012.csv"
stock = pd.read_csv(path, encoding="gbk")


stock = stock.loc[:,'日期':'前收盘']

stock = stock.sort_values(by='日期',ascending=True)

stock = stock[stock['收盘价']>0]

stock['最大值'] = 0.00
stock['最小值'] = 0.00
stock['RSV'] = 0.00
stock['K'] = 0.00
stock['D'] = 0.00
stock['J'] = 0.00
stock['SIGNAL'] = 0

stock = stock.reset_index()

lenRow = stock.shape[0] #有多少行
for j in range(lenRow):
    stock.iat[j,9] = stock['最高价'][max(0,j-8):j+1].max()  # max
    stock.iat[j,10] = stock['最低价'][max(0,j-8):j+1].min()  # min
#    print(j) #728
    stock.iat[j,11] = (stock['收盘价'][j]-stock['最小值'][j])/(stock['最大值'][j]-stock['最小值'][j])*100   # RSV

    
    if j>0:
        # 计算K
        stock.iat[j,12] = 2/3*stock.iat[j-1,12] + 1/3*stock.iat[j,11]
        # 计算D
        stock.iat[j,13] = 2/3*stock.iat[j-1,13] + 1/3*stock.iat[j,12]
        
        # 计算SIGNAL
        if (stock.iat[j-1,12]<stock.iat[j-1,13]) & (stock.iat[j,12]>stock.iat[j,13]):
            #K上穿D，买入
            stock.iat[j,15] = 1
        elif (stock.iat[j-1,12]>stock.iat[j-1,13]) & (stock.iat[j,12]<stock.iat[j,13]):
            #K下穿D，卖出
            stock.iat[j,15] = -1
            
    else:
        stock.iat[j,12] = 50
        stock.iat[j,13] = 50
    
    
    # 计算J
    stock.iat[j,14] = 3*stock.iat[j,12] - 2*stock.iat[j,13]
    
    
    








