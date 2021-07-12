#!/usr/bin/env python
# coding: utf-8

# ### XML을 이용한 스크래핑 => RSS 활용

# In[1]:


from xml.etree import ElementTree


# In[2]:


tree = ElementTree.parse('rss.xml')


# In[3]:


root = tree.getroot()


# In[4]:


import pandas as pd


# In[5]:


데이터프레임_리스트 = []
for item in root.findall('channel/item/description/body/location/data'):
    # find() 메서드로 element 탐색, text 속성으로 값을 추출
    tm_ef = item.find('tmEf').text
    tmn = item.find('tmn').text
    tmx = item.find('tmx').text
    wf = item.find('wf').text
    데이터프레임 = pd.DataFrame({
        '일시':[tm_ef],
        '최저기온':[tmn],
        '최고기온':[tmx],
        '날씨':[wf],
    })
    데이터프레임_리스트.append(데이터프레임)
날씨정보 = pd.concat(데이터프레임_리스트)
날씨정보  


# In[6]:


type(날씨정보)


# In[7]:


날씨정보.to_csv('날씨정보.csv')


# In[8]:


엑셀 = pd.ExcelWriter('날씨정보.xlsx')
날씨정보.to_excel(엑셀, '.', index=False )
엑셀.save()


# In[9]:


날씨정보.reset_index(drop=True, inplace=True)


# In[10]:


날씨정보.to_json('날씨정보.json')


# In[11]:


import sqlite3
from pandas.io import sql
import os


# In[12]:


with sqlite3.connect(os.path.join('.','sqliteDB')) as con: # sqlite DB 파일이 존재하지 않는 경우 파일생성
    try:
        날씨정보.to_sql(name = 'WEATHER_INFO', con = con, index = False, if_exists='append') 
        #if_exists : {'fail', 'replace', 'append'} default : fail
    except Exception as e:
        print(str(e))
    
    query = 'SELECT * FROM WEATHER_INFO'
    데이터프레임1 = pd.read_sql(query, con = con)


# In[13]:


데이터프레임1


# In[14]:


엑셀 = pd.ExcelWriter('날씨정보2.xlsx')
데이터프레임1.to_excel(엑셀, '.', index=False )
엑셀.save()


# In[15]:


df = pd.read_excel('날씨정보2.xlsx')


# In[16]:


df

