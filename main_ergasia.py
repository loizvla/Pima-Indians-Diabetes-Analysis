# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:31:57 2020

@author: loizvla
"""


import pandas as pd  
import numpy as np  
import seaborn as sn  
import matplotlib.pyplot as plt  
import matplotlib.mlab as mlab  
  
#--- Import dataset---  
data = pd.read_csv("D:\MsC\Μεθοδολογία της Έρευνας\Project\pima-indians-diabetes-database\diabetes.csv")  
data.info()  
data.head()  
data.shape  
data.describe()  
data.hist(figsize=(15,15))  
data.hist(figsize=(10,8))  
data.hist('Glucose')  
data.hist('Age')  
  
#---Print count_of_zero---  
featurelist = []  
count_of_zero_list = []  
for col in data:  
    cnt = 0  
    for i in data[col]:  
        if i==0:  
            cnt = cnt + 1  
    if col!='Outcome':  
        #print (col, "-", cnt)  
        featurelist.append(col)  
        count_of_zero_list.append(cnt)  
          
objects = tuple(featurelist)  
y_pos = np.arange(len(featurelist))  
performance = count_of_zero_list  
   
fig_size = plt.rcParams["figure.figsize"]  
fig_size[0] = 11  
fig_size[1] = 3  
  
plt.bar(y_pos, performance, align='center', alpha=0.9)  
plt.xticks(y_pos, objects)  
  
plt.ylabel('Count of 0 values')  
plt.title('Count of 0 values per feature')  
plt.grid(True)  
plt.show()  
  
#---Print box_plot---  
data.plot(kind= 'box' , subplots=True, layout=(3,3), figsize=(10,8))

#--- Print correlation matrix---
import seaborn as sns
f,ax = plt.subplots(figsize=(15, 10))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()
