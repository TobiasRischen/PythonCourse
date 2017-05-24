# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:10:54 2017

@author: SirTobi92
"""

import math
import csv
import statistics
import os

IRIS_FILE = 'iris.csv'
SEPAL_LENGTH = 'sepal length in cm'
SEPAL_WIDTH = 'sepal width in cm'
PETAL_LENGTH = 'petal length in cm'
PETAL_WIDTH = 'petal width in cm'
CLASS = 'class'

# 1) Count Rows
with open('iris.csv', 'r') as iris:
    iris_reader = csv.reader(iris, delimiter=',')
    row_count = sum(1 for row in iris_reader)  # fileObject is your csv.reader
    print(row_count)

 
def read_with_csv(filename):
    """Reads the iris file using the csv module.
    Args:
    filename: The filename.
    Returns:
    A list of dictionaries mapping the features to their values.
    10
    """
    with open(filename, 'r') as iris_file:
        reader = csv.DictReader(iris_file, [SEPAL_LENGTH, SEPAL_WIDTH,
                                            PETAL_LENGTH, PETAL_WIDTH, CLASS])
        return list(reader)
    
def make_data_numeric(data, *features):
    """For each entry in data, all features in features are cast to float.
    Args:
    data: The dataset to modify.
    features: The features to cast to float.
    """
    for date in data:
        for feature in features:
            date[feature] = float(date[feature])
        return data

def count_occurences(data, feature):
    """Counts how often each unique value of a feature occurs in the whole
    dataset.
    Args:
    data: The dataset to count.
    11
    feature: The feature to count.
    Returns:
    A dictionary where the keys are the data values and the values are the
    occurences.
    """
    values = [d[feature] for d in data] # it's crazy to me that this works
    print(values)
    return {k: values.count(k) for k in set(values)}

iris_data = read_with_csv(IRIS_FILE)
print(iris_data)

iris_data = make_data_numeric(iris_data, SEPAL_LENGTH, SEPAL_WIDTH,
                             PETAL_LENGTH, PETAL_WIDTH)
print(iris_data)

tabulation = count_occurences(iris_data,CLASS)
print(tabulation)

# Calculating mean sepal length
sepal_lengths = [d[SEPAL_LENGTH] for d in iris_data]
print(sepal_lengths)
sepal_lengths = [float(i) for i in sepal_lengths] # why do I need this step? what am I doing wrong?
print(sepal_lengths)
mean_sepal_length = statistics.mean(sepal_lengths)
print(mean_sepal_length)

#calculating mean sepal length of iris setosa
sepal_lengths_setosa = [d[SEPAL_LENGTH] for d in iris_data if 'Iris-setosa' in d[CLASS]]
print(sepal_lengths_setosa)
sepal_lengths_setosa = [float(i) for i in sepal_lengths_setosa] # why do I need this step? what am I doing wrong?
print(sepal_lengths_setosa)
mean_sepal_lengths_setosa = statistics.mean(sepal_lengths_setosa)
print(mean_sepal_lengths_setosa)

# Calculating median sepal width 
sepal_widths = [d[SEPAL_WIDTH] for d in iris_data]
print(sepal_widths)
sepal_widths = [float(i) for i in sepal_widths] # why do I need this step? what am I doing wrong?
print(sepal_widths)
median_sepal_width = statistics.median(sepal_widths)
print(median_sepal_width)

#calculating median sepal length of iris virginica
sepal_widths_virginica = [d[SEPAL_WIDTH] for d in iris_data if 'Iris-virginica' in d[CLASS]]
print(sepal_widths_virginica)
sepal_widths_virginica = [float(i) for i in sepal_widths_virginica] # why do I need this step? what am I doing wrong?
print(sepal_widths_virginica)
median_sepal_width_virginica = statistics.median(sepal_widths_virginica)
print(median_sepal_width_virginica)

# Calculating mode petal length of iris versicolor
petal_length_versicolor = [d[PETAL_LENGTH] for d in iris_data if 'Iris-versicolor' in d[CLASS]]
print(petal_length_versicolor)
petal_length_versicolor = [float(i) for i in petal_length_versicolor] # why do I need this step? what am I doing wrong?
print(petal_length_versicolor)
mode_petal_length_versicolor = statistics.mode(petal_length_versicolor)
print(mode_petal_length_versicolor)



    


