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


# In[2]:


import re
import string

def get_detail(url):
    body = []
    punc = '[!"#$%&\'()*+,-./:;<=>?[\]^_`{|}~“”·]'
    response = requests.get(url)
    root = lxml.html.fromstring(response.content)
    for p in root.xpath('//*[@id="harmonyContainer"]/section/p'):
        if p.text: # 체크
            body.append(re.sub(punc, '', p.text)) # 특수문자 제거
    full_body = ' '.join(body)
    
    return full_body

get_detail('https://news.v.daum.net/v/20200505000102404')


# In[ ]:





# In[3]:


import re
import string

def get_detail(url):
    body = []
    punc = '[!"#$%&\'()*+,-./:;<=>?[\]^_`{|}~“”·]'
    response = requests.get(url)
    root = lxml.html.fromstring(response.content)
    for p in root.xpath('//*[@id="harmonyContainer"]/section/p'):
        if p.text: # 체크
            body.append(re.sub(punc, '', p.text)) # 특수문자 제거
    full_body = ' '.join(body)
    
    return full_body


# In[4]:


page = 1
max_page = 0
REG_DATE = '20200819'


# In[5]:


response = requests.get('http://news.daum.net/breakingnews/digital?page={}&regDate={}'                        .format(page, REG_DATE))
root = lxml.html.fromstring(response.content)
for li in root.xpath('//*[@id="mArticle"]/div[3]/ul/li'):
    a = li.xpath('div/strong/a')[0]
    url = a.get('href')
    article = get_detail(url)
    print(f'URL : {url}')
    print(f'TITLE : {a.text}')
    print(f'ARTICLE : {article}')
    print('-' * 100)


# In[ ]:




