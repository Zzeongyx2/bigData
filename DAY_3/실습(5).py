#!/usr/bin/env python
# coding: utf-8

# ### 모듈

# In[1]:


get_ipython().system('pip list')


# In[2]:


help('sys')


# In[3]:


import os


# In[4]:


os.getcwd()  #현재 디렉토리 위치 (pwd)


# In[5]:


os.listdir()


# In[7]:


import numpy as np
np.absolute(-3)


# In[8]:


np.sqrt(16)


# In[9]:


from scipy import stats   #from은 디렉터리


# In[10]:


stats.hmean([1,2,3])  #평균


# In[11]:


stats.variation([1,2,3])  #분산


# In[12]:


from datetime import datetime
now = datetime.now()
now.year


# In[13]:


now.month


# In[14]:


import sys
sys.path   #모듈 물리적 위치


# ##### 사용자 정의 모듈

# In[9]:


import myprint
#만들고 .py로 변환 필요


# In[10]:


hello = 'Hello world python'


# In[11]:


myprint.print1(hello)


# In[6]:


myprint.print2(hello)


# In[7]:


myprint.print3(hello)


# In[8]:


myprint.print4(hello)


# In[ ]:




