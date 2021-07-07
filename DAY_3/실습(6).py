#!/usr/bin/env python
# coding: utf-8

# ### 파일 읽기

# In[5]:


fr = open('./hello.txt', 'r')


# In[8]:


for line in fr:
    print(line)


# In[9]:


fr.close()


# In[10]:


with open('./hello.txt', 'r') as fr:
    for line in fr:
        print(line)


# ### 파일 쓰기

# ##### w : 동일 경로/파일명 존재시 overwrite

# In[43]:


fw = open('./hello_Write.txt', 'w')


# In[44]:


fw.write('Hello world python\n')


# In[45]:


fw.write('welcome to python world')


# In[46]:


fw.close()


# ##### x : 동일 경로/파일명 존재시 error

# In[25]:


# with open('./hello_Write.txt', 'x') as fw:
#     fw.write('아마 오류날 걸')


# ##### a : 동일 경로/파일명 존재시 append

# In[47]:


with open('./hello_Write.txt', 'a') as fw:
    fw.write('new append')


# ### 파일 시스템

# In[51]:


import os
os.listdir('.')


# In[53]:


file_list = os.listdir('.')


# In[54]:


file_ipynb = [f for f in file_list if f.endswith('.ipynb')]


# In[55]:


file_ipynb


# In[56]:


os.getcwd()


# In[58]:


os.mkdir('test')


# In[59]:


os.path.join('.','test')


# In[60]:


os.path.abspath('hello.txt')


# In[61]:


os.path.isfile('hello_Write.txt')


# In[62]:


os.path.isdir('hello_Write.txt')


# In[63]:


os.path.isfile('test')


# In[64]:


os.path.isdir('test')


# In[65]:


os.path.split(os.path.abspath('hello_Write.txt'))


# In[66]:


os.path.splitext('hello_Write.txt')


# In[ ]:




