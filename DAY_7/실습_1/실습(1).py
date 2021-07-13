#!/usr/bin/env python
# coding: utf-8

# ### 기본 웹 크롤러

# In[1]:


import requests
import lxml.html


# In[2]:


response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)
for a in root.cssselect('.view_box a'):
    url = a.get('href')
    print(url)


# #### 파머 링크 목록 추출

# In[3]:


response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)


# In[4]:


root.make_links_absolute(response.url)


# In[5]:


for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    print(url)


# In[ ]:




