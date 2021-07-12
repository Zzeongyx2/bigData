#!/usr/bin/env python
# coding: utf-8

# ## 웹 크롤링

# #### 웹 페이지 추출

# In[37]:


from urllib.request import urlopen


# In[38]:


f = urlopen("http://www.hanbit.co.kr/store/books/full_book_list.html/")


# In[39]:


type(f)


# In[40]:


# read() : HTTP 응답 본문 추출 -> 별도의 close() 필요
f.read()


# In[41]:


f.status  # 서버 response 반환 (url 없을 시 404 반환, 200은 정상적인 상황)


# In[42]:


f.getheader('Content-Type')


# #### HTTP 헤더에서 인코딩 방식 추출

# In[43]:


import sys
from urllib.request import urlopen


# In[44]:


f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')


# In[45]:


encoding = f.info().get_content_charset(failobj='utf-8')


# In[46]:


print('encoding : ',encoding)


# In[47]:


text = f.read().decode(encoding)


# In[48]:


print(text)


# #### meta 태그에서 인코딩 방식 추출

# In[49]:


import re
import sys
from urllib.request import urlopen


# In[50]:


f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
bytes_content = f.read()


# In[51]:


scanned_text = bytes_content[:1024].decode('ascii', errors='replace')


# In[52]:


match = re.search(r'charset=["\']?([\w-]+)', scanned_text)


# In[53]:


match.group(1)


# In[54]:


if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8'


# In[55]:


print('encoding:', encoding, file=sys.stderr)


# In[56]:


text = bytes_content.decode(encoding)
print(text)


# In[ ]:




