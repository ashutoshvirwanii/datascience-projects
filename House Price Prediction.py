#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[28]:


data = pd.read_csv("D:\Downloads\house-data.csv")
data


# In[5]:


data.tail()


# In[6]:


data.head()


# In[7]:


data.shape


# In[8]:


data.isnull().sum()


# In[9]:


data.describe()


# In[10]:


sns.relplot(x = "price", y = "bathrooms", data = data)


# In[11]:


sns.relplot(x = "price", y = "bedrooms", data = data)


# In[12]:


sns.relplot(x = "price", y = "floors", data = data)


# In[13]:


sns.relplot(x = "price", y = "sqft_living",hue = "waterfront", data = data)


# In[14]:


from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split


# In[15]:


train = data[["bedrooms","bathrooms","sqft_living","sqft_lot"]]
test = data['price']


# In[16]:


train


# In[17]:


X_train, X_test, Y_train, Y_test = train_test_split(train, test, test_size = 0.3, random_state = 2)


# In[18]:


X_train


# In[19]:


regr = LinearRegression()


# In[20]:


regr.fit(X_train, Y_train)


# In[21]:


pred = regr.predict(X_test)


# In[22]:


pred


# In[24]:


regr.score(X_test, Y_test)

