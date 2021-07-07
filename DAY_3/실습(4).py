#!/usr/bin/env python
# coding: utf-8

# ### (사용자 정의) 함수

# In[1]:


#매개변수X, 리턴값X
def add1():   #함수 정의
    print("더하기 함수입니다.")


# In[2]:


add1()  #함수 호출


# In[3]:


#매개변수O, 리턴값X
def add2(x,y):
    print(x+y)


# In[4]:


add2(1,2)


# In[5]:


#매개변수X, 리턴값O
def add3():
    x, y = 2, 4
    return x+y


# In[6]:


add3()


# In[7]:


#매개변수0, 리턴값0
def add4(x, y):
    return x+y


# In[9]:


re_val = add4(2,4)
print(re_val)


# In[10]:


print(add4(2,4))


# ##### 다중 리턴값

# In[11]:


def square(x,y):   #파이썬은 리턴값 여러개 가능
    x = x ** 2
    y = y ** 2
    return x, y


# In[14]:


a, b = square(2,3)
print(a)
print(b)


# ##### 매개변수 기본값

# In[15]:


def square2(x=2,y=3):   #파라미터 안넘겨 주면 기본으로 x=2, y=3 대입
    x = x ** 2
    y = y ** 2
    return x, y


# In[17]:


square2()


# In[19]:


square2(4, 2)


# In[23]:


square2(5)
#square2(,6) #이건 안됨


# In[24]:


square2(y=5, x=4)


# ##### 가변 매개변수

# In[25]:


def changeable(x, *y):
    print(x,y)


# In[26]:


changeable(1)


# In[27]:


changeable(1,2)


# In[28]:


changeable(1,2,3)


# In[29]:


changeable(1,2,3,4,5)


# In[ ]:




