# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:10:40 2017

@author: SirTobi92
"""


# 1) Count Rows
with open('iris.csv', 'r') as iris:
    iris_reader = csv.reader(iris, delimiter=',')
    row_count = sum(1 for row in iris_reader)  # fileObject is your csv.reader
    print(row_count)
    for i in range(0,row_count):
        print(row[i])
