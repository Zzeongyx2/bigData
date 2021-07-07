#!/usr/bin/env python
# coding: utf-8

# ### 조건문

# ##### for문

# In[2]:


for num in [1, 2, 3]:
    print(num)


# In[4]:


for st in ['hello', 'world', 'python']:
    print(st)


# In[5]:


score = {'korean' : 95,
        'english' : 90,
        'math' : 80}


# In[6]:


for item in score.keys():
    print(item)


# In[7]:


for item in score.values():
    print(item)


# In[9]:


for key, value in score.items():
    print(f'{key} 과목 점수는 {value}점 입니다')


# ##### range()

# In[10]:


list(range(10))  #0부터 10전까지


# In[11]:


list(range(1,11))   #1부터 11전까지


# In[13]:


list(range(10, 0, -1))   #10부터 1전까지 -1씩 증가(1씩 감소)


# In[14]:


for i in range(1, 11, 2):
    print(i)


# In[15]:


for i in range(0, 11, 2):
    print(i)


# ##### for & else

# In[17]:


for i in range(1,10):
    ans = 2 * i
    print(f'2 X {i} = {ans}')
else:
    print('구구단 2단을 종료합니다.')   #for문 끝나면 실행(근데 그냥 for문 뒤에 들여쓰기 안하고 출력하면 되는거 아닌가...? 굳이 else...?)


# ##### while문

# In[19]:


a = 0


# In[20]:


while a<10:
    print(a)
    a += 1
else:
    print(f'a가 {a}이므로 종료합니다.')


# In[21]:


x = 0
while True:   #무한루프
    x += 3
    print(x)
    if x>100 and x%3==0:  #종료 조건
        break;


# ### 리스트 컴프리헨션 (리스트 원소들에 대해 연산 수행)

# In[23]:


list1 = list(range(1,11))
print(list1)


# In[27]:


list2 = [i*2 for i in list1]
list2


# In[26]:


list3 = [i**2 for i in list1 if i%2 == 1]  #이게 리스트 컴프리헨션
list3


# In[ ]:




