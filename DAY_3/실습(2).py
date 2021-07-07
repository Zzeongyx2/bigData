#!/usr/bin/env python
# coding: utf-8

# ### 연산자
# ##### 비교 연산자

# In[2]:


x = 10
y = 5


# In[3]:


x == y


# In[4]:


x != y


# In[5]:


x > y


# In[6]:


x < y


# In[7]:


x >= y


# In[8]:


x <= y


# ##### 논리 연산자

# In[9]:


x = True
y = False


# In[10]:


x and y


# In[11]:


x or y


# In[12]:


not x


# ### 조건문

# In[14]:


x, y = 10, 5


# In[15]:


if x > y:
    print('x가 y보다 큽니다.')


# In[16]:


x, y = 5, 10


# In[17]:


if x > y:
    print('x가 y보다 큽니다.')
else:
    print('x가 y보다 작습니다.')


# In[18]:


x, y = 10, 10


# In[19]:


if x > y:
    print('x가 y보다 큽니다.')
elif x == y:
    print('x와 y가 같습니다.')
elif x < y:
    print('x가 y보다 작습니다.')


# In[20]:


score = 90
if score >= 90:
    print('A학점입니다.')
elif score >= 80:
    print('B학점입니다.')
elif score >= 70:
    print('C학점입니다.')
elif score >= 60:
    print('D학점입니다.')
else:
    print('F학점입니다.')


# In[22]:


#조건문 범위 => 들여쓰기에 의해 결정
a = True
if a:
    print('a는 True입니다.')
    print('True end...')
else :
    print('a는 False입니다.')
print('False end...')  #이것도 실행됨


# In[23]:


a = True
if a:
    print('a는 True입니다.')
    print('True end...')
else :
    print('a는 False입니다.')
    print('False end...')


# ##### 중첩/복합 조건문

# In[24]:


a = True
x, y = 5, 10


# In[25]:


if a == True:
    print('a는 True')
    if(x > y):
        print('x보다 y가 큼')
    else:
        print('x가 y보다 작음')
else:
    print('a는 False')


# In[29]:


payment = 0

#교재에는 없음
member = False
age = 12

if member:
    if age > 6 and age <= 13:
        payment = 2500
    elif age > 14 and age <=59:
        payment = 5000
else:
    if age > 6 and age <= 13:
        payment = 5000
    elif age > 14 and age <=59:
        payment = 10000
        
print(f'입장료는 {payment:,}원 입니다.')


# In[35]:


payment = 0

member = True
age = 14

#이 코드는 14를 아무데서도 포함하지 않는데...? => 0출력

if age <=6 or age >= 60:
    payment = 0
elif age > 6 and age <= 13:
    payment = 5000
elif age > 14 and age <=59:   #age >= 14로 바꿔야될 듯
    payment = 10000
    
if member:
    payment = int(payment * 0.5)
    
print(f'입장료는 {payment:,}원 입니다.')


# In[ ]:




