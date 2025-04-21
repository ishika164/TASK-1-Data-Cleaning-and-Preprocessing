#!/usr/bin/env python
# coding: utf-8

# # TASK-1  Data Cleaning and Preprocessing

# # Importing libraries

# In[1]:


#importing necessary libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# # Loading dataset

# In[2]:


#load dataset
df = pd.read_csv('sales-dataset.csv')


# In[3]:


#display first five rows
df.head()


# In[4]:


#display last five rows
df.tail()


# # Cleaning the data

# In[5]:


df.shape


# In[6]:


#checking for null values
df.isnull().sum()


# In[7]:


#check for duplicates
df.duplicated().sum()


# In[8]:


#Remove duplicates if any
df = df.drop_duplicates()


# In[9]:


#Rename columns to lowercase with underscores (already clean, but let's make it consistent)
df.columns = df.columns.str.lower()


# In[10]:


#Some basic statistical analysis about the data
df.describe()


# # Saving the cleaned dataset

# In[11]:


df.to_csv('cleaned_sales_dataset.csv', index=False)


# In[ ]:




