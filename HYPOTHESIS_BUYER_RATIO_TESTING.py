#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from scipy import stats as stats


# ### Ho= All Proportionare equal  Ha=All proportion are not equal. 

# In[2]:


sales_data=pd.read_csv("BuyerRatio.csv")
sales_data


# In[3]:


sales=sales_data.iloc[:,1:6]
sales


# In[4]:


sales.values


# In[8]:


val=stats.chi2_contingency(sales)
val


# In[11]:


no_of_rows=len(sales.iloc[0:2,0])
no_of_columns=len(sales.iloc[0,0:4])
degree_of_freedom=(no_of_rows-1)*(no_of_columns-1)
print('Degree of Freedom =',degree_of_freedom)


# In[15]:


from scipy.stats import chi2
critical_value=chi2.ppf(0.95,3)
critical_value


# In[16]:


p_value=0.6603


# In[21]:


if p_value<0.05 :
    print("all proportion are equal")
else:
    print("all the proportion are not equal")


# In[ ]:




