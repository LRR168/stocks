#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:47:08 2018

@author: liurenrong
"""

import requests
import pandas as pd

def getStockData(stockname):
#    stockname = "000012"
    starttime = "19920107"
    endtime = "20180316"
    code = "1"
    if(stockname[0]=="6"):
        code = "0"
    
    url = "http://quotes.money.163.com/service/chddata.html?code="+ code + stockname + "&start=" + starttime + "&end=" + endtime + "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    print(url)
    
    
    html = requests.get(url)
    content = html.text
    list1 = content.split('\r\n')
    
    stocks = pd.DataFrame(columns=['日期','股票代码','名称','收盘价','最高价','最低价','开盘价','前收盘','涨跌额','涨跌幅','换手率','成交量','成交金额','总市值','流通市值'])
    
    for j in range(1,len(list1)):
        list2 = list1[j].split(',')
        #print(list2)
        if(len(list2[0])>0):
            stocks.loc[j] = list2

    return stocks            
            
    
#    stocks.to_csv("testfoo.csv",encoding="gbk")

data = getStockData("600000")