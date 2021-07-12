#!/usr/bin/env python
# coding: utf-8

# ### 스크래핑

# In[6]:


import re
import sqlite3
from urllib.request import urlopen
from html import unescape
import pandas as pd
import os


# In[7]:


def fetch(url):
    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)
    return html


# In[8]:


def scrape(html):
    books = []
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        books.append(pd.DataFrame({'url': [url], 'title': [title]}))
    return pd.concat(books)


# In[9]:


def save(db_path, books):
    with sqlite3.connect(os.path.join('.', db_path)) as con: # sqlite DB 파일이 존재하지 않는 경우 파일생성
        try:
            books.to_sql(name = 'BOOKS_INFO', con = con, index = False, if_exists='append') 
        except Exception as e:
            print(str(e))
    query = 'SELECT * FROM BOOKS_INFO'
    df = pd.read_sql(query, con = con)
    return df


# In[10]:


html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')


# In[11]:


df = scrape(html)
df.reset_index(drop=True, inplace=True)
df2 = save('books.db', df)
df2


# ### lxml

# In[2]:


get_ipython().system('pip install lxml')


# In[3]:


get_ipython().system('pip install cssselect')


# In[4]:


import lxml.html


# In[5]:


tree = lxml.html.parse('dp.html')
html = tree.getroot()


# In[8]:


for a in html.cssselect('a'):
    print(a.get('href'), a.text)


# ### beautiful Soup

# In[9]:


get_ipython().system('pip install beautifulsoup4')


# In[10]:


from bs4 import BeautifulSoup


# In[22]:


with open('full_book_list/full_book_list.html', encoding='euc-kr') as f:
    soup = BeautifulSoup(f, 'html.parser')


# In[23]:


for a in soup.find_all('a'):
    print(a.get('href'), a.text)


# In[ ]:




