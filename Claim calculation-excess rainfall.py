#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# using pandas we will read data in python
data= pd.read_excel("InRisk_Labs_Assignment.xlsx")
data.head()


# In[8]:


# Handling anomalies and outliers
# There are some negative values and some extreme positive values which are no possible.


x=data.Rainfall_mm[(data.Rainfall_mm<0) | (data.Rainfall_mm>5000)]
y=x.tolist()
print(y)

# We are replacing such values with zero(0)
data.replace(y,0,inplace=True)


# In[9]:


# Now we will create a separate dataset for all the days with excess rainfall

excess_data= data[data.Rainfall_mm>60]
excess_data.head()


# In[10]:


# Creating a dataset for unique regions

region= excess_data['Region'].unique()
region


# In[13]:


# Now we will count number of days with excess rainfall in each region
excess_rainfall_days=[]

for i in region:
    excess_rainfall_days.append(len(excess_data[excess_data.Region==i]))

excess_rainfall_days


# In[14]:


# Now we will calculate claim amount basis data given

Claim_amount=[]

for i in excess_rainfall_days:
    
    amount=0
    if i<=10:
        pass
    elif 10<i<=30:
        amount= 100*(i-10)
    elif 30<i<50:
        amount=200*(i-30)+100*20
    else:
        amount= 300*(i-50)+200*20+100*20
    Claim_amount.append(amount)
    
Claim_amount


# In[15]:


# Represnting region, excess rainfall days and cliam amount in a separate table

Claim_cal= pd.DataFrame({'Region':region, 'Days of excess rainfall': excess_rainfall_days,'Claim amount': Claim_amount})

Claim_cal


# In[16]:


# Converting final output to excel sheet

Claim_cal.to_excel("Claim_cal.xlsx", index=False)


# In[ ]:




