#!/usr/bin/env python
# coding: utf-8

# ### 파이썬 리스트

# In[1]:


letter1 = ['A', 'B', 'C']


# In[2]:


letter2 = ['D', 'E', 'F']


# In[3]:


letter1 + letter2


# In[4]:


list_num1 = [1, 2, 3]


# In[5]:


list_num2 = [4, 5, 6]


# In[6]:


list_num1 + list_num2


# In[8]:


'A' in letter1


# In[9]:


'A' in letter2


# In[10]:


letters = ['A', 'B', 'C', 'D', 'E', 'F']


# In[11]:


letters


# In[12]:


letters[0] = 'a'
letters


# In[13]:


letters[0] = 'A'
letters


# In[15]:


# letters[6] = 'a'
#인덱스 벗어나면 안됨


# In[16]:


len(letters)


# In[17]:


letters.count('A')


# In[19]:


letters.append('a')
letters


# In[20]:


letters.insert(2, 'z')
letters


# In[21]:


letters.pop(2)  #꺼낸 후, 제거


# In[22]:


letters


# In[24]:


letters.remove('a')
letters


# In[25]:


letters.sort(reverse = True)


# In[26]:


letters


# In[27]:


letters.sort()


# In[28]:


letters


# ### 파이썬 인덱스와 슬라이싱

# ##### 문자열과 동일

# In[29]:


letters[0]


# In[30]:


letters[5]


# In[31]:


letters[-1]


# In[32]:


letters[-2]


# In[33]:


letters[0:3]


# In[34]:


letters[3:]


# In[35]:


letters[:4]


# In[36]:


letters[::2]


# In[37]:


letters[::-1]


# ### 파이썬 튜플

# In[38]:


tuple1 = ('A', 'B', 'C', 'D', 'E')
tuple1


# In[41]:


# tuple1[0] = 'a'
# 튜플은 read only -> 수정 불가능


# In[42]:


tuple1.index('C')


# In[43]:


tuple1.count('A')


# In[44]:


list1 = list(tuple1)


# In[59]:


list1.append('a')
list1


# In[60]:


tuple2 = tuple(list1)
tuple2

