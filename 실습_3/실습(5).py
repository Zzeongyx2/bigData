#!/usr/bin/env python
# coding: utf-8

# ### 셀레니움 크롤러

# In[1]:


import requests
import lxml.html
import pandas as pd
import sqlite3
from pandas.io import sql
import os
import time


# In[2]:


def db_save(NEWS_LIST):
    with sqlite3.connect(os.path.join('.','sqliteDB')) as con:
        try:
            NEWS_LIST.to_sql(name = 'NEWS_LIST', con = con, index = False, if_exists='append') 
            #if_exists : {'fail', 'replace', 'append'} default : fail
        except Exception as e:
            print(str(e))
        print(len(NEWS_LIST), '건 저장완료..')


# In[3]:


def db_delete():
    with sqlite3.connect(os.path.join('.','sqliteDB')) as con: 
        try:
            cur = con.cursor()
            sql = 'DELETE FROM NEWS_LIST'
            cur.execute(sql)
        except Exception as e:
            print(str(e)) 


# In[4]:


def db_select():
    with sqlite3.connect(os.path.join('.','sqliteDB')) as con: 
        try:
            query = 'SELECT * FROM NEWS_LIST'
            NEWS_LIST = pd.read_sql(query, con = con)
        except Exception as e:
            print(str(e)) 
        return NEWS_LIST   


# In[5]:


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


# In[6]:


page = 58
max_page = 0
REG_DATE = '20200819'


# In[7]:


while(True):
    df_list = []
    response = requests.get('http://news.daum.net/breakingnews/digital?page={}&regDate={}'                            .format(page, REG_DATE))
    root = lxml.html.fromstring(response.content)
    for li in root.xpath('//*[@id="mArticle"]/div[3]/ul/li'):
        a = li.xpath('div/strong/a')[0]
        url = a.get('href')
        article = get_detail(url)
        df = pd.DataFrame({'URL' : [url],'TITLE':[a.text],'ARTICLE' : [article]})
        df_list.append(df)   
        
    if df_list:   
        df_10 = pd.concat(df_list)
        db_save(df_10)

    # 페이지 번호 중에서 max 페이지 가져오기    
    for a in root.xpath('//*[@id="mArticle"]/div[3]/div/span/a'):
        try:
            num = int(a.text)
            if max_page < num:
                max_page = num       
        except:
            pass

    # 마지막 페이지 여부 확인     
    span = root.xpath('//*[@id="mArticle"]/div[3]/div/span/a[@class="btn_page btn_next"]')

    if (len(span) <= 0) & (page > max_page):
        break
    else:
        page = page + 1
        
    time.sleep(1)   


# In[8]:


# db_delete()


# In[9]:


print(db_select())

