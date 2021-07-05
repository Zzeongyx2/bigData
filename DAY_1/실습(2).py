#!/usr/bin/env python
# coding: utf-8

# ### 파이썬 변수

# In[1]:


num = 0
print(num)


# In[2]:


num2 = 2
print(num2)


# In[3]:


num_3 = 3
print(num_3)


# In[4]:


hello = 'Hello world Python'
print(hello)


# In[5]:


헬로 = 'hello'
print(헬로)


# In[6]:


헬로2 = '안녕'
print(헬로2)


# In[7]:


_hello = 'Hello'
print(_hello)


# In[8]:


hello2 = 'hello world'
print(hello2)


# In[9]:


# 변수명은 숫자로 시작할 수 없음
# 1_hello -> 불가능


# In[10]:


num1 = 10
num2 = 5


# In[11]:


print(num1, num2)


# In[12]:


print(num1 + num2)


# In[13]:


print("sum : ", num1 + num2)


# In[14]:


a = b = 10


# In[15]:


print(a)


# In[16]:


print(b)


# In[23]:


a, b, c = 2, 4, 6   #변수랑 값의 개수가 일치해야 함


# In[24]:


print(a)


# In[25]:


print(b)


# In[26]:


print(c)


# In[17]:


a = 10; b = 5


# In[18]:


print(a, b)


# In[19]:


temp = a; a = b; b = temp;


# In[20]:


print(a,b)


# In[29]:


a = 10; b = 5


# In[30]:


print(a, b)


# In[31]:


a, b = b, a    #파이썬은 temp없이 swap 가능


# In[32]:


print(a, b)


# ### 파이썬 자료형

# In[33]:


price = 1000


# In[34]:


print(price)


# In[35]:


print(type(price))


# In[36]:


rate = 0.05


# In[37]:


print(rate)


# In[38]:


print(type(rate))


# In[39]:


amount = 17e5


# In[40]:


print(amount)


# In[42]:


decimal = 2.65e-3


# In[43]:


print(decimal)


# In[44]:


a = True   #True/False 첫 글자 대문자 주의!!
b = False


# In[45]:


print(a)


# In[46]:


print(type(a))


# In[47]:


print(b)


# In[48]:


print(type(b))


# #### 집합 자료형

# In[49]:


s = 'hello'


# In[50]:


print(s)


# In[51]:


print(type(s))


# In[52]:


l = [1,2,3,4,5]


# In[53]:


print(l)


# In[56]:


print(type(l))


# In[58]:


t = (1,2,3,4,5)


# In[59]:


print(t)


# In[60]:


print(type(t))


# se = {1,2,3,4,5}

# In[62]:


print(se)


# In[63]:


print(type(se))


# In[64]:


d = {'a' : 1,
     'b' : 2,
     'c' : 3
}


# In[65]:


print(d)


# In[66]:


print(type(d))


# ### 파이썬 형변환

# In[69]:


price = price * 0.05


# In[70]:


print(price)


# In[71]:


print(type(price))   #묵시적 형변환


# In[73]:


i1 = 1000


# In[74]:


print(type(i1))


# In[75]:


i1 = i1/4


# In[76]:


print(i1)


# In[77]:


print(type(i1))


# In[80]:


f1 = 3.14


# In[81]:


print(type(f1))


# In[87]:


i1 = int(f1)


# In[88]:


print(i1)


# In[78]:


s1 = '12345'


# In[79]:


print(type(s1))


# In[89]:


i1 = int(s1)


# In[90]:


print(i1)


# In[91]:


print(type(i1))


# In[92]:


s2 = '12345a'


# In[95]:


# int(s2)
#문자열 내에 숫자 외의 문자가 있어서 형변환 불가능


# In[96]:


s2 = '1234 '   #공백은 가능


# In[97]:


int(s2)


# In[98]:


i1 = 100


# In[99]:


print(type(i1))


# In[100]:


f1 = float(i1)


# In[102]:


print(f1)


# In[106]:


s1 = '3.14'


# In[107]:


print(type(s1))


# In[108]:


f1 = float(s1)


# In[109]:


print(f1)


# In[110]:


print(type(f1))


# In[ ]:




