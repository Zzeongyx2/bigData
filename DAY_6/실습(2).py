#!/usr/bin/env python
# coding: utf-8

# ## 정규표현식을 이용한 스크래핑

# In[2]:


import re


# In[3]:


re.search(r'a.*c', 'abc123DEF')


# In[4]:


result = re.search(r'a.*D', 'abc123DEF')


# In[5]:


start, end = result.span()
print(start, end)
print(result.string)


# In[6]:


re.search(r'a.*d', 'abc123DEF', re.IGNORECASE)


# In[7]:


m = re.search(r'a(.*)c', 'abc123DEFaddc')
m.group(0)


# In[8]:


m.group(1)


# In[9]:


re.findall(r'\w{2,3}', 'This is a pen')


# In[10]:


re.sub(r'\w{4}', 'That', 'This is a pen')


# In[11]:


result = re.search(r'a.*c', ' abc123DEF')
result


# In[29]:


result = re.match(r'a.*c', 'abc123DEF')
result


# #### 적용 실습

# In[25]:


import re
from html import unescape


# In[26]:


import re
import sys
from urllib.request import urlopen


# In[27]:


with open('dp.html', encoding='utf-8') as f:
    html = f.read()


# In[28]:


f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
bytes_content = f.read()


# In[29]:


text = bytes_content.decode('utf-8')
with open('dp.html', 'w', encoding='utf-8') as wf:
    wf.write(text)


# In[31]:


for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
    url = re.search(r'<a href="(.*?)">', partial_html).group(1)
    url = 'http://www.hanbit.co.kr' + url
    title = re.sub(r'<.*?>', '', partial_html)
    title = unescape(title)
    print('url:', url)
    print('title:', title)
    print('---')


# In[ ]:




