#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# AND 게이트 구현
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# In[3]:


def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# In[4]:


def NAND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5]) # Not AND
    b = 0.7
    tmp = sum(w*x) + b
    
    if tmp <= 0:
        return 0
    else:
        return 1


# In[5]:


# XOR 구현하기
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




