# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:43:34 2021

@author: lotte
"""
'''
import xlrd
workbook = xlrd.open_workbook('group_python.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')

list = worksheet._cell_values

for row in list:
    print(row)

'''

import openpyxl
import pandas as pd

xlsxFile = 'group_python.xlsx'
sheetList = []

wb = openpyxl.load_workbook(xlsxFile)
for i in wb.sheetnames:
    sheetList.append(i)
    
xlsx = pd.ExcelFile(xlsxFile)

for j in sheetList:
    df = pd.read_excel(xlsx,j)
    print('%s 인원들 데이터입니다.' %j)
    print(df)
    print('*' * 50)