#!/usr/bin/env python
# coding: utf-8

# ### 고급 웹 크롤러 (다음 뉴스)

# In[1]:


import requests
import lxml.html
import pandas as pd
import sqlite3
from pandas.io import sql
import os


# In[3]:


REG_DATE = '20200819'


# In[5]:


response = requests.get('https://news.daum.net/breakingnews/digital?regDate={}'.format(REG_DATE))                   
root = lxml.html.fromstring(response.content)
for li in root.xpath('//*[@id="mArticle"]/div[3]/ul/li'):
    a = li.xpath('div/strong/a')[0]
    url = a.get('href')
    print(url, a.text)


# In[ ]:




