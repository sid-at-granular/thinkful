
# coding: utf-8

# In[1]:

import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''


# In[6]:

data = data.split('\n')


# In[9]:

data = [i.split(',') for i in data]


# In[13]:

df = pd.DataFrame(data[1:], columns=data[0])


# In[22]:

df.head()


# In[24]:

print('Alcohol mean: {}'.format(df.Alcohol.astype(float).mean()))


# In[17]:

df['Alcohol'].median()


# In[15]:

from scipy import stats


# In[16]:

stats.mode(df.Alcohol)


# In[26]:

df.Alcohol.astype(float).var()


# In[27]:

df.Alcohol.astype(float).std()


# In[28]:

max(df.Alcohol.astype(float)) - min(df.Alcohol.astype(float))


# In[34]:

# get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

mean = 0
variance = 1
sigma = np.sqrt(variance)
x = np.linspace(-3,3,100)
plt.plot(x,mlab.normpdf(x,mean,sigma))


# In[ ]:



