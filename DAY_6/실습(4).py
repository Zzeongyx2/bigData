#!/usr/bin/env python
# coding: utf-8

# ### CSV 형식으로 저장

# In[1]:


import csv


# In[25]:


with open('top_cities.csv', 'w', newline='') as f:
    writer = csv.writer(f)  
    writer.writerow(['rank', 'city', 'population'])  
    writer.writerows([
        [1, '상하이', 24150000],
        [2, '카라치', 23500000],
        [3, '베이징', 21516000],
        [4, '텐진', 14722100],
        [5, '이스탄불', 14160467],
    ])


# In[28]:


with open('top_cities.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])
    writer.writeheader()
    writer.writerows([
        {'rank': 1, 'city': '상하이', 'population': 24150000},
        {'rank': 2, 'city': '카라치', 'population': 23500000},
        {'rank': 3, 'city': '베이징', 'population': 21516000},
        {'rank': 4, 'city': '텐진', 'population': 14722100},
        {'rank': 5, 'city': '이스탄불', 'population': 14160467},
    ])


# In[27]:


with open('top_cities.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])
    writer.writeheader()
    writer.writerows([
        {'rank': 1, 'city': '상하이', 'population': 24150000},
        {'rank': 2, 'city': '카라치', 'population': 23500000},
        {'rank': 3, 'city': '베이징', 'population': 21516000},
        {'rank': 4, 'city': '텐진', 'population': 14722100},
        {'rank': 5, 'city': '이스탄불', 'population': 14160467},
    ])


# In[5]:


import chardet


# In[6]:


char_dic = chardet.detect(open('top_cities.csv', 'rb').read())


# In[7]:


char_dic['encoding']


# ### json 형식으로 저장

# In[8]:


import json


# In[9]:


cities = [ 
{'rank': 1, 'city':'상하이', 'population': 24150000},
{'rank': 2, 'city':'카라치', 'population': 23500000},
{'rank': 3, 'city':'베이징', 'population': 21516000},
{'rank': 4, 'city':'텐진', 'population': 14722100}, 
{'rank': 5, 'city':'이스탄불', 'population':14160467},
]


# In[10]:


with open('top_cities.json', 'w') as fw:
    json.dump(cities, fw)


# In[11]:


with open('top_cities.json', 'r') as fr:
    json_file = json.load(fr)
    print(json_file)


# ### SQLite3 DBMS로 저장

# In[12]:


import pandas as pd
import sqlite3
from pandas.io import sql
import os


# In[13]:


DB_NAME = 'top_cities.db'
TABLE_NAME = 'TOP_CITIES'


# In[14]:


def db_save(df, db_name, table_name):
    with sqlite3.connect(db_name) as con:
        try:
            df.to_sql(name = table_name, con = con, index = False, if_exists='append') 
            #if_exists : {'fail', 'replace', 'append'} default : fail
        except Exception as e:
            print(str(e))
        print(len(df), '건 저장완료..')


# In[15]:


def db_select(db_name, table_name):
    with sqlite3.connect(db_name) as con: 
        try:
            query = 'SELECT * FROM {}'.format(table_name)
            df = pd.read_sql(query, con = con)
        except Exception as e:
            print(str(e)) 
        return df  


# In[16]:


def db_delete(db_name, table_name):
    with sqlite3.connect(db_name) as con: 
        try:
            cur = con.cursor()
            sql = 'DELETE FROM {}'.format(table_name)
            cur.execute(sql)
        except Exception as e:
            print(str(e)) 


# In[20]:


top_cites = pd.read_csv('top_cities.csv')
db_save(top_cites, DB_NAME, TABLE_NAME)


# In[21]:


df = db_select(DB_NAME, TABLE_NAME)
df


# In[ ]:




