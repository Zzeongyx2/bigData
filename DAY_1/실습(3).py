#!/usr/bin/env python
# coding: utf-8

# ### 파이썬 문자열

# In[1]:


a = '파이썬'


# In[2]:


print(a)


# In[3]:


b = "문자열"


# In[4]:


print(b)


# In[7]:


c = """
파이썬
문자열
"""


# In[8]:


print(c)


# In[10]:


# '파이썬' + 3
#파이썬은 +으로 문자열 연결 불가능


# In[11]:


d = '파이썬' + str(3)


# In[12]:


print(d)


# In[13]:


e = '*' * 10


# In[14]:


print(e)


# In[15]:


a = 'helloWorld'


# In[16]:


a


# In[17]:


a[0]


# In[18]:


a[5]


# In[19]:


a[-1]


# In[20]:


a[-2]


# In[21]:


a[:5]


# In[22]:


a[5:]


# In[23]:


a[:]


# In[24]:


a


# In[25]:


a[::2]


# In[26]:


a[::-1]   #역정렬


# In[28]:


a[::-2]


# ### 파이썬 문자열 함수

# #### len

# In[29]:


len('helloworldpython')


# #### join

# In[30]:


'-'.join("helloworldpython")


# In[31]:


'-'.join('12345')


# #### split

# In[33]:


'Hello-World-Python'.split('-')


# In[34]:


'서울시 마포구 상암동 1586'.split()


# #### strip

# In[35]:


text = '\t 문자열 정리    \n'
text.strip()


# #### startswith / endswith

# In[37]:


'hello world python'.startswith('hello')


# In[38]:


'hello world python'.startswith('Hello')


# In[39]:


'hello world python'.endswith('python')


# In[40]:


'hello world python'.endswith('Python')


# #### count

# In[41]:


text = 'hello world python'
text.count('o')


# In[42]:


text = 'Hello world Python, welcome to Python world'
text.count('Python')


# #### index

# In[43]:


text.index('o')


# In[44]:


text.index('o',5)   #인덱스 5이후의 o의 인덱스 반환


# #### find

# In[45]:


text.find('Python')


# In[46]:


text.find('Python', 20)


# #### capitalize / lower / upper

# In[47]:


"Hello World".capitalize()


# In[48]:


"Hello World".lower()


# In[49]:


"Hello World".upper()


# #### in

# In[50]:


'Python' in 'Hello World Python'


# In[51]:


'Java' in 'Hello World Python'


# ### 파이썬 문자열 포맷팅

# In[52]:


name, age, phone = '홍길동', 25, '010-111-2222'


# #### 포맷 방법 1

# In[53]:


소개 = "이름은 {} 이고, 나이는 {}세 이며, 전화번호는 {} 입니다. ".format(name, age, phone)
소개


# #### 포맷 방법 2

# In[54]:


소개 = "이름은 {0} 이고, 나이는 {2}세 이며, 전화번호는 {1} 입니다. ".format(name, phone, age)
소개


# #### 포맷 방법 3

# In[55]:


소개 = "이름은 {a} 이고, 나이는 {b}세 이며, 전화번호는 {c} 입니다. ".format(c = phone, a = name, b = age)
소개


# #### 포맷 방법 4 (권장)

# In[56]:


소개 = f"이름은 {name} 이고, 나이는 {age}세 이며, 전화번호는 {phone} 입니다. "
소개


# ### 문자열 포맷팅

# In[58]:


jan, dec = 1, 12


# In[59]:


print("한 해의 시작은 {:02d}월".format(jan))
print("한 해의 마지막은 {:02d}월".format(dec))


# In[61]:


val = 123456789
money = "{:,}"
money.format(val)


# In[62]:


'{}, {:f}, {:.1f}, {:.2f}, {:.2%}'.format(3, 3, 3, 3.1415, 1/3)


# In[63]:


1/3


# In[ ]:




