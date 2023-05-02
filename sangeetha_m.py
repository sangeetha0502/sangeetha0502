# -*- coding: utf-8 -*-
"""sangeetha.M.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1me6f_vuaQZj9Z9hYMNUzTPiBL4REL7nC
"""

import pandas as pd
import seaborn as sns
data = pd.read_csv("House Price India.csv")
print(data.head())

sns.countplot(data['number of bedrooms'])

sns.histplot(data['living area'])

import numpy as np
import matplotlib.pyplot as plt
x =data['living area']
y =data['Price']
plt.xlabel('Living Area')
plt.ylabel('Price')

plt.title("Relationship between Living Area and Price")
plt.plot(x,y)
plt.show()

pd.plotting.scatter_matrix(data[['Price', 'living area', 'lot area']], figsize=(10,10))
plt.show()
# Create box plots for selected variables
data[['Price', 'living area', 'lot area']].plot(kind='box', figsize=(10,5))
plt.show()

print(data.describe())

data.isnull().sum().sum()