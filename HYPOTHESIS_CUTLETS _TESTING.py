#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib as mpl
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest


# In[2]:


cutlet=pd.read_csv("Cutlets.csv")


# In[3]:


cutlet


# In[4]:


cutlet.shape


# In[5]:


cutlet.dtypes


# In[6]:


cutlet.columns


# In[7]:


cutlet.axes


# In[8]:


cutlet.size


# In[9]:


cutlet.ndim


# In[11]:


cutlet.values


# In[12]:


cutlet['Unit A'].value_counts()


# In[13]:


cutlet.describe()


# In[14]:


cutlet.mean()


# In[15]:


cutlet.median()


# In[16]:


cutlet.std()


# In[18]:


3


# In[19]:


cutlet_CI_A=stats.norm.interval(0.975,loc=7.01909,scale=0.2884)


# In[20]:


cutlet_CI_A


# In[22]:


plt.hist(cutlet["Unit B"],facecolor="orange",edgecolor="blue",bins=10)


# In[23]:


Cutlets_CI_B=stats.norm.interval(0.975,loc=6.96429,scale=0.3434)


# In[24]:


Cutlets_CI_B


# In[26]:


Unit_A=cutlet['Unit A'].mean()
Unit_B=cutlet['Unit B'].mean()

print('Unit A Mean = ',Unit_A, '\nUnit B Mean = ',Unit_B)
print('Unit A Mean > Unit B Mean = ',Unit_A>Unit_B)


# In[28]:


sns.distplot(cutlet['Unit A'])
sns.distplot(cutlet['Unit B'])
plt.legend(['Unit A','Unit B'])


# In[31]:


sns.boxplot(data=[cutlet['Unit A'],cutlet['Unit B']],notch=True)
plt.legend(['Unit A','Unit B'])


# In[38]:


alpha=0.05
UnitA=pd.DataFrame(cutlet['Unit A'])
UnitB=pd.DataFrame(cutlet['Unit B'])
print(UnitA,"\n",UnitB)


# In[39]:


tStat,pValue =sp.stats.ttest_ind(UnitA,UnitB)
print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat))


# In[41]:


two_sided_value=pValue/2
two_sided_value


# In[46]:


if pValue < 0.05:
  print('We can Reject the Null Hypothesis.There is a Significant Diffference in the diameter of the cutlets')
else:
  print('We can not Reject the Null Hypothesis.There is no Significant Difference in the diameter of the cutlets ')


# In[1]:


# Inference is that there is no significant difference in the diameters of Unit A and Unit B


# In[ ]:




