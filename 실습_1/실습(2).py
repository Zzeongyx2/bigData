#!/usr/bin/env python
# coding: utf-8

# ### 링크 목록 추출

# In[1]:


import requests
import lxml.html


# In[50]:


def main():
    session = requests.Session()   #여러 페이지 크롤링
    # scrape_list_page()   #이거 실행하면 오류
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)
    for url in urls:
        print(url)
        print('-'*70)


# In[53]:


def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url


# In[54]:


if __name__ == '__main__':
    main()


# #### 상세 페이지 스크래핑

# In[55]:


def main():
    session = requests.Session()  
    # scrape_list_page()
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)
    for url in urls:
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)
        break  


# In[56]:


def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url


# In[57]:


def scrape_detail_page(response):  #위에 코드에서 이거 추가
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [p.text_content()\
            for p in root.cssselect('#tabs_3 .hanbit_edit_view p')]
    }
    return ebook


# In[58]:


if __name__ == '__main__':
    main()


# In[ ]:





# In[35]:


import requests
import lxml.html
import re


# In[36]:


def main():
    session = requests.Session()  
    # scrape_list_page()
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)
    for url in urls:
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)  # 상세 정보 출력
        break  


# In[37]:


def scrape_detail_page(response):
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [normalize_spaces(p.text_content())
            for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
            if normalize_spaces(p.text_content()) != '']
    }
    return ebook


# In[38]:


def normalize_spaces(s):
    return re.sub(r'\s+', ' ', s).strip()  #공백 제거


# In[39]:


if __name__ == '__main__':
    main()


# In[ ]:





# In[40]:


import time
import requests
import lxml.html
import re


# In[41]:


def main():
    # 여러 페이지에서 크롤링을 위해 Session 사용
    session = requests.Session()  
    # scrape_list_page() 함수를 호출해서 제너레이터를 추출
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)
    for url in urls:
        time.sleep(1) # 1초간 대기
        response = session.get(url)  # Session을 사용해 상세 페이지를 추출
        ebook = scrape_detail_page(response)  # 상세 페이지에서 상세 정보를 추출
        print(ebook)  # 상세 정보 출력
#         break  


# In[42]:


def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url


# In[43]:


def scrape_detail_page(response):
    """
    상세 페이지의 Response에서 책 정보를 dict로 추출
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [normalize_spaces(p.text_content())
            for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
            if normalize_spaces(p.text_content()) != '']
    }
    return ebook


# In[44]:


def normalize_spaces(s):
    """
    연결된 공백을 하나의 공백으로 변경
    """
    return re.sub(r'\s+', ' ', s).strip()


# In[45]:


if __name__ == '__main__':
    main()


# In[ ]:




