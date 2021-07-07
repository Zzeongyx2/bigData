#!/usr/bin/env python
# coding: utf-8

# ### SET

# In[11]:


set1 = {'A', 'B', 'C', 'D', 'E', 'F', 'F'}
set1


# In[3]:


# set[0]
# set은 중복을 제거하고, 인덱싱과 슬라이싱 불가능


# In[6]:


# set1[:5]


# In[8]:


set1.remove('a')
# 대소문자 상관없나봄


# In[10]:


set1.pop()
set1
# 마지막 원소 pop


# ### set 집합 연산

# In[13]:


set1 = {'A', 'B', 'C', 'D', 'E', 'F'}
set2 = {'B', 'D', 'G', 'H'}


# ##### 교집합

# In[14]:


set1 & set2


# In[15]:


set1.intersection(set2)


# ##### 합집합

# In[16]:


set1 | set2


# In[17]:


set1.union(set2)


# ##### 차집합

# In[18]:


set1 - set2


# In[19]:


set1.difference(set2)


# ##### 대칭 차집합

# In[20]:


set1 ^ set2
#합집합 - 교집합


# In[21]:


set1.symmetric_difference(set2)


# ### 딕셔너리

# In[24]:


중간고사 = { "수학" : 100,
       "영어" : 90,}
중간고사
#원소 맨 뒤에 , 붙혀줘도 실행됨


# In[25]:


중간고사['국어'] = 85
중간고사


# In[26]:


중간고사['영어']


# In[27]:


중간고사['영어'] = 95
중간고사


# In[28]:


list(중간고사.keys())


# In[29]:


list(중간고사.values())


# In[30]:


중간고사.items()
#각각의 단위들이 키-값 쌍으로 튜플로 저장되어 있음


# In[31]:


중간고사.pop('국어')


# In[32]:


중간고사


# In[ ]:




