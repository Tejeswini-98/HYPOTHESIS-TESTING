#!/usr/bin/env python
# coding: utf-8

# ### ===============================LABTAT DATA==================

# In[16]:


import pandas as pd
import numpy as np
import scipy as sp
import seaborn as sns
from matplotlib import pyplot as plot
import warnings
warnings.filterwarnings('ignore')


# ###  HO:There is no significant difference the mean of the lab test u1=u2=u3=u4.
# ###  Ha:There is a Significant difference the mean of the lab test u1 != u2!=u3!=u4.

# In[2]:


lab_data=pd.read_csv("LabTAT.csv")


# In[3]:


lab_data


# In[4]:


lab_data.describe()


# In[5]:


lab_data.mean()


# In[6]:


lab_data.std()


# In[8]:


lab_data.median()


# In[17]:


sns.displot(lab_data["Laboratory 1"])
sns.displot(lab_data["Laboratory 2"])
sns.displot(lab_data["Laboratory 3"])
sns.displot(lab_data["Laboratory 4"])
plot.legend(["Laboratory 1","Laboratory 2","Laboratory 3","Laboratory 4"])


# In[19]:


alpha=0.05
lab1=pd.DataFrame(lab_data["Laboratory 1"])
lab2=pd.DataFrame(lab_data["Laboratory 2"])
lab3=pd.DataFrame(lab_data["Laboratory 3"])
lab4=pd.DataFrame(lab_data["Laboratory 4"])


# In[22]:


tStat,pvalue=sp.stats.f_oneway(lab1,lab2,lab3,lab4)
print("P-value:{0}  T -Statistics:{1}".format(pvalue,tStat))


# ### P-value is 0.00 < 0.05= Accept Ha, hence Average of atleast 1 laboratory are different As per results we can say that these are not equal i.e Average of atleast 1 laboratory are different
# 

# ### Anova Test-One way H0:Average of all laboratory are same Ha:Average of atleast 1 laboratory are different

# In[27]:


if pvalue < 0.05:
  print('We can Accept the Null Hypothesis.There is a Significant Diffference in the labortory ')
else:
  print('We can reject the Null Hypothesis.There is no Significant Difference in the laboratory ')


# In[ ]:




