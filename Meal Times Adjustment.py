import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This is graph line style, from Nate silver
plt.style.use('fivethirtyeight')

## Matplotlib Variables
_FIG_SIZE = (16, 12)
_FIG_FORMAT = 'png'
_FIG_DPI = 200

#define the 5 series containing the number of adjusted readings per unit time
#patient 1-5
s1 = pd.Series([42,58,63,66,68,70], index=[0,1,2,3,4,5])
s2 = pd.Series([33,45,52,54,59,65], index=[0,1,2,3,4,5])
s3 = pd.Series([9,12,13,14,15,16], index=[0,1,2,3,4,5])
s4 = pd.Series([49,59,68,73,74,75], index=[0,1,2,3,4,5])
s5 = pd.Series([110,131,136,145,149,156], index=[0,1,2,3,4,5])

x = np.array([i for i in xrange(len(s1))])

plt.figure(figsize=_FIG_SIZE)
plt.plot(s1, 'ro', label="Meal Times")
plt.xlabel('Date')
plt.legend(loc='upper right')
plt.title('Glucose Readings with the meal times');

plt.figure()
s1.plot()

s1.hist()

data = pd.Series(randn(1000))

data.hist(by=randint(0, 4, 1000), figsize=(6, 4))
