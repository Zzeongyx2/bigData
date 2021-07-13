#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium.webdriver import Chrome
import time
import sqlite3
from pandas.io import sql
import os
import pandas as pd


# In[10]:


from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized");  # 화면 최대 크기로 실행

browser = webdriver.Chrome('C:/Users/user/Downloads/chromedriver.exe', options=options)  # exe 파일 저장 위치 연결


# In[11]:


# 브라우저 열기
browser.get('https://www.data.go.kr/')
browser.implicitly_wait(5)


# In[12]:


# 로그인화면으로 넘어감
browser.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/div/a[1]').click()  #cssselect로도 가능
browser.implicitly_wait(5)


# In[13]:


# 아이디 입력
browser.find_element_by_xpath('//*[@id="mberId"]').send_keys('사용자 아이디')


# In[14]:


# 비밀번호 입력
browser.find_element_by_xpath('//*[@id="pswrd"]').send_keys('사용자 비밀번호')


# In[15]:


# 로그인
browser.find_element_by_xpath('//*[@id="loginVo"]/div[2]/div[2]/div[2]/div/div[1]/button').click()
browser.implicitly_wait(5)


# In[16]:


# 팝업창 닫기
browser.find_element_by_xpath('//*[@id="layer_popup_info_1"]/div[1]/a').click()


# In[17]:


# 정보 공유 클릭
browser.find_element_by_xpath('//*[@id="M000400_pc"]/a').click()


# In[18]:


# 자료실 클릭
browser.find_element_by_xpath('//*[@id="M000402_pc"]/a').click()


# In[19]:


# 자료실 데이터 추출
def db_save(ARTICLE_LIST):
    with sqlite3.connect(os.path.join('.','sqliteDB')) as con: # sqlite DB 파일이 존재하지 않는 경우 파일생성
        try:
            ARTICLE_LIST.to_sql(name = 'ARTICLE_LIST', con = con, index = False, if_exists='append') 
            #if_exists : {'fail', 'replace', 'append'} default : fail
        except Exception as e:
            print(str(e))
        print(len(ARTICLE_LIST), '건 저장완료..')


# In[20]:


trs = browser.find_elements_by_xpath('//*[@id="searchVO"]/div[5]/table/tbody/tr')
df_list = []
for tr in trs:
    df = pd.DataFrame({
            'NO': [tr.find_element_by_xpath('td[1]').text],
            'TITLE': [tr.find_element_by_xpath('td[2]').text],
            'IQRY': [tr.find_element_by_xpath('td[3]').text],
            'REGDT': [tr.find_element_by_xpath('td[4]').text],
            'CHGDT': [tr.find_element_by_xpath('td[5]').text],
        })
    df_list.append(df)
    
ARTICLE_LIST = pd.concat(df_list)
db_save(ARTICLE_LIST)


# In[21]:


# 자료실 첫번째 글 클릭
browser.find_element_by_xpath('//*[@id="searchVO"]/div[5]/table/tbody/tr[1]/td[2]/a').click()
browser.implicitly_wait(3)


# In[22]:


# 첨부파일 다운로드
browser.find_element_by_xpath('//*[@id="recsroomDetail"]/div[2]/div[4]/div/a').click()
time.sleep(10)


# In[23]:


browser.quit()


# #### 브라우저 가동하지 않고 백그라운드 작업 수행

# In[24]:


from selenium.webdriver import Chrome
import time
import sqlite3
from pandas.io import sql
import os
import pandas as pd


# In[25]:


from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')    #백그라운드 작업 수행  #위에 코드에서 여기만 변경된거임
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1280x1024')

browser = webdriver.Chrome('C:/Users/user/Downloads/chromedriver.exe', options=options)


# In[26]:


browser.get('https://www.data.go.kr/')
browser.implicitly_wait(5)


# In[27]:


browser.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/div/a[1]').click()
browser.implicitly_wait(5)


# In[28]:


browser.find_element_by_xpath('//*[@id="mberId"]').send_keys('사용자 아이디')


# In[29]:


browser.find_element_by_xpath('//*[@id="pswrd"]').send_keys('사용자 비밀번호')


# In[30]:


browser.find_element_by_xpath('//*[@id="loginVo"]/div[2]/div[2]/div[2]/div/div[1]/button').click()
browser.implicitly_wait(5)


# In[32]:


browser.find_element_by_xpath('//*[@id="layer_popup_info_1"]/div[1]/a').click()


# In[33]:


browser.find_element_by_xpath('//*[@id="M000400_pc"]/a').click()


# In[34]:


browser.find_element_by_xpath('//*[@id="M000402_pc"]/a').click()


# In[35]:


def db_save(ARTICLE_LIST):
    with sqlite3.connect(os.path.join('.','sqliteDB')) as con: # sqlite DB 파일이 존재하지 않는 경우 파일생성
        try:
            ARTICLE_LIST.to_sql(name = 'ARTICLE_LIST', con = con, index = False, if_exists='append') 
            #if_exists : {'fail', 'replace', 'append'} default : fail
        except Exception as e:
            print(str(e))
        print(len(ARTICLE_LIST), '건 저장완료..')


# In[36]:


trs = browser.find_elements_by_xpath('//*[@id="searchVO"]/div[5]/table/tbody/tr')
df_list = []
for tr in trs:
    df = pd.DataFrame({
            'NO': [tr.find_element_by_xpath('td[1]').text],
            'TITLE': [tr.find_element_by_xpath('td[2]').text],
            'IQRY': [tr.find_element_by_xpath('td[3]').text],
            'REGDT': [tr.find_element_by_xpath('td[4]').text],
            'CHGDT': [tr.find_element_by_xpath('td[5]').text],
        })
    df_list.append(df)
    
ARTICLE_LIST = pd.concat(df_list)
db_save(ARTICLE_LIST)


# In[38]:


browser.find_element_by_xpath('//*[@id="searchVO"]/div[5]/table/tbody/tr[1]/td[2]/a').click()
browser.implicitly_wait(3)


# In[39]:


browser.find_element_by_xpath('//*[@id="recsroomDetail"]/div[2]/div[4]/div/a').click()
time.sleep(10)


# In[40]:


browser.quit()


# In[ ]:




