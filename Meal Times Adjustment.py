# %load "Meal Times Adjustment.py"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#if using interactive python, add line below (inline, notebook, or nbaagg are all possible)
#%matplotlib inline

#This is graph line style, from Nate silver
plt.style.use('fivethirtyeight')

## Matplotlib Variables
_FIG_SIZE = (10, 8)
_FIG_FORMAT = 'png'
_FIG_DPI = 100

#define the 5 series containing the number of adjusted readings per unit time
#patient 1-5
#index=[0,1,2,3,4,5])
#The following series has the total meal times per patient
s_Total_Meal_times = pd.Series ([91,89,25,110,201])
s1 = pd.Series([0,42,58,63,66,68,70], index=[0,5,10,15,20,25,30])
s2 = pd.Series([0,33,45,52,54,59,65], index=[0,5,10,15,20,25,30])
s3 = pd.Series([0,9,12,13,14,15,16], index=[0,5,10,15,20,25,30])
s4 = pd.Series([0,49,59,68,73,74,75], index=[0,5,10,15,20,25,30])
s5 = pd.Series([0,110,131,136,145,149,156], index=[0,5,10,15,20,25,30])

plt.figure(figsize=_FIG_SIZE)
plt.xlabel('Minutes')
plt.ylabel('# of Meal Times Adjustments')
#plt.legend(loc='upper right')
plt.title('');
s1.plot(label = "s1")
#or we plot using the line below
#plt.plot(s1, 'ro', label="Meal Times")
s2.plot(label = "s2")
s3.plot(label = "s3")
s4.plot(label = "s4")
s5.plot(label = "s5")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

plt.figure(figsize=_FIG_SIZE)
plt.xlabel('Minutes')
plt.ylabel('Ratio of Meal Times Adjustments')
plt.title('');
s1_ratio = pd.Series(s1/s_Total_Meal_times[0])
s2_ratio = pd.Series(s2/s_Total_Meal_times[1])
s3_ratio = pd.Series(s3/s_Total_Meal_times[2])
s4_ratio = pd.Series(s4/s_Total_Meal_times[3])
s5_ratio = pd.Series(s5/s_Total_Meal_times[4])
s1_ratio.plot(label = "s1")
s2_ratio.plot(label = "s2")
s3_ratio.plot(label = "s3")
s4_ratio.plot(label = "s4")
s5_ratio.plot(label = "s5")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.axis((0,30,0,1))
plt.show()