#!/usr/bin/env python
# coding: utf-8

# ### 파이썬 연산자

# In[1]:


2 + 4


# In[2]:


4 - 2


# In[3]:


2 * 4


# In[4]:


4 / 2


# In[5]:


4 ** 2


# In[6]:


7 / 2


# In[7]:


7 // 2


# In[9]:


7 % 2


# ### 파이썬 주석문

# In[12]:


# ctrl + /


# In[13]:


# 파이썬 주석문


# In[14]:


# 파이썬
# 주석문


# In[17]:


"""
파이썬
블럭
주석문
"""

'''
이것도 가능
'''
print(1)


# ### 들여쓰기

# In[18]:


a = True
if a:
    print("True")
else:
    print("False")


# In[20]:


a = True
if a:
    print("True")
    print("True end...")
else:
    print("False")
print("end...")


# ### 파이썬 내장함수

# #### print 함수

# In[21]:


print('hello world python')


# In[22]:


print('a', 1)


# In[23]:


print('a', 1, sep = ':')


# In[24]:


print('a', 1, sep = ':', end = '.')


# In[26]:


hello = 'Hello World Python'


# In[27]:


print(hello)


# In[29]:


hello


# In[43]:


hello
hello


# In[44]:


print(hello)
print(hello)


# #### input 함수

# In[39]:


input()


# In[40]:


input("프로그램 언어 : ")


# #### round 함수

# In[31]:


round(3.141592)


# In[32]:


round(3.141592, 2)


# In[33]:


round(3.141592, 5)


# #### 기타 내장 함수

# In[34]:


max(10, 100, 1000)


# In[35]:


min(10, 100, 1000)


# In[36]:


pow(2,4)


# In[37]:


len('hello world python')


# In[41]:


zip('abc', '123')


# In[42]:


list(zip('abc','123'))


# In[ ]:




