#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


companies = pd.read_csv('D://Downloads/Companies.csv')


# In[3]:


companies.head(10)


# In[4]:


companies.shape


# In[5]:


companies.info()


# In[6]:


companies.describe()


# In[7]:


companies.isnull().sum()


# In[8]:


companies.notnull().sum()


# In[9]:


companies.dropna()


# In[10]:


companies[['R&D Spend','Administration','Marketing Spend']].corr()


# In[11]:


sns.heatmap(companies.corr())


# In[12]:


companies.drop(['Marketing Spend'],axis=1,inplace=True)


# In[13]:


companies


# In[14]:


dummies=pd.get_dummies(companies.State)


# In[15]:


companies=pd.concat([companies,dummies],axis=1)


# In[16]:


companies


# In[17]:


companies.drop(['State'],axis=1,inplace=True)
companies


# In[18]:


from sklearn.preprocessing import MinMaxScaler
scale=MinMaxScaler()
companies[['R&D Spend','Administration']]=scale.fit_transform(companies[['R&D Spend','Administration']])


# In[19]:


y=companies.iloc[:,2].values
y


# In[20]:


companies.drop(['Profit'],axis=1,inplace=True)
companies


# In[21]:


X=companies.iloc[:,:].values
X.shape


# In[22]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)


# In[23]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


# In[24]:


y_pred = regressor.predict(X_test)
y_pred


# In[25]:


print(regressor.coef_)
print(regressor.intercept_)


# In[26]:


from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

