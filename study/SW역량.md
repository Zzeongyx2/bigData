# 파이썬 소개 및 개발환경

## 1. 파이썬 소개
### 파이썬 소개
- 1991년 네덜란드 Guido Van Rossum이 발표한 프로그래밍 언어
  - ~크리스마스 휴가 때 심심해서 만듦~ 
- 컴파일 과정 불필요, 라인단위로 실행되는 인터프리터 언어
- 최근 머신러닝/딥러닝 개발 언어로 각광
- 언어 습득을 위한 진입장벽이 낮아 파이썬 언어 사용자 매년 증가 추세

### 파이썬을 배워야하는 이유
1. Perfect For Rookies
2. Community
3. Career Opportunities
4. Python in Web Development
5. Python in Artifical Intelligence and Machine Learning
6. Raspberyy Pi
7. Startups and corporates- Python for Both

### 파이썬 특징
- 단순하고 최소화된 언어, 쉬운 문법 체계, 가독성 높은 간결한 코드
- 플랫폼 독립적(Write Once Run Anywhere)
- 메모리 관리 등이 불필요한 고수준 언어
- 멀티 패러다임 언어(절차형, 객체지향, 함수형 언어 모두 포함)
- 인터프리터 언어류 Jupyter와 같은 대화형 환경 구성 가능
- 유니코드 지원 (한글 변수 사용 가능)
- 동적 타이핑(런타임 시점에서 자료형 검사) 언어
- 방대한 규모의 라이브러리 제공

## 2. 파이썬 개발환경 설치
### 파이썬 개발환경
- Python
- ANACONDA
- Google Colab
- Pycharm
- Visual Studio Code

-------------

# 파이썬 개발 도구
## 1. 파이썬 개발환경 구성
1. 메모장과 같은 편집기 실행<br>
  jupyter lab 입력<br>
  python 디렉토리에 "jupyter_lab.bat"으로 저장
  <br>
2. 터미널/명령 프롬프트에 jupyter lab입력
3. anaconda와 같은 개발 환경 사용

## 2. 파이썬 개발도구 사용
### 구성
---이미지
1. Main Menu
2. Left Sidebar
3. Main Work Area

### 모드
1. 편집 모드(Edit Mode)
- 입력 셀 활성화 및 커서 깜빡임
- 코드 입력 및 마크다운 입력 가능
2. 명령 모드(Command Mode)
- 입력 셀 비활성화
- 셀 관련 명령 실행 가능
3. 코드 모드(Code Mode)
- Python 소스코드 입력 가능
- 셀 앞에 사각괄호([]) 표시
  - 실행 순서를 나타냄
4. 마크다운 모드(Markdown Mode)
- 마크다운 텍스트 입력 가능
  - 마크다운 : 서식있는 문서 작성을 위해 사용되는 표준 문법
  - Jupyter에서는 Notebook이나 Python 코드의 설명 작성을 위해 사용
- 셀 앞에 사각괄호 미표시

### 단축키
- Ctrl + Enter : 셀 실행, 새로운 셀 생성X
- Shift + Enter : 셀 실행, 새로운 셀 생성O
- Ctrl + Shift + - : 셀 분할
- Shift + M : 셀 병합
- tab : 자동완성 

### 실행 파일
- 파이썬 실행 파일(.py)
- Jupyter Notebook 파일(.ipynb)
  - [File] - [Export Notebook As] - [Export Notebook As Excutable Script] : .py파일로 변환 

---------

# 파이썬 연산자와 키워드
## 1. 파이썬 연산자
### 파이썬 연산자
- 더하기 : +
- 빼기 : -
- 곱하기 : *
- 나누기/몫(실수형) : /
- 정수몫 : //
- 제곱 : **
- 나머지 : %

### 파이썬 주석문
- 한 줄 주석 : #
- 여러 줄 주석 : ''' 코드 '''
- Ctrl + / : 주석 처리/해제

### 파이썬 들여쓰기
- 들여쓰기는 함수 몸체, 조건문 루프, 클래스 등 다양한 코드 블록을 표현
- 들여쓰기로 탭을 사용할 수 있지만 권장하지 않음
- 스페이스 4칸으로 들여쓰기 권장
- 코드 블록의 시작은 콜론(:)
- 들여쓰기를 기준으로 들여쓰기가 없는 곳이 코드 블록의 끝
  - 파이썬은 중괄호({})를 써서 블록을 나타내지 않고, 들여쓰기로 구분함
 
## 2. 파이썬 키워드
### 키워드 == 예약어
- 파이썬 문법에서 이미 예약어로 사용하고 있는 단어는 개발자가 변수명, 함수명 등 식별자로 사용 불가
- 파이썬에는 총 33개의 예약어 존재

|False|None|True|and|as|assert|async|await|break|class|continue|
|---|---|---|---|---|---|---|---|---|---|---|
|def|del|elif|else|except|finally|for|from|global|if|import|
|in|is|lambda|nonlacal|not|or|pass|raise|return|try|while|with|yield|

## 3. 파이썬 내장함수
### 파이썬 내장함수
- 파이썬에서 기본적으로 제공되는 함수
- [내장함수 목록](https://docs.python.org/ko/3/library/functions.html)
  - print()
  - round()
  - max()/min()
  - pow()
  - len() 

-----------

# 파이썬 변수와 자료형
## 1. 파이썬 변수
### 변수(Variable)
- 데이터를 저장하기 위한 메모리 영역에 대한 명명
- 알파벳 대소문자, 숫자, under bar, 한글, 한자 등 변수명 사용 가능
- 첫 글자는 숫자로 시작 불가
- 공백이나 특수문자, 문장 부호는 변수명으로 사용 불가
- 대소문자 구별
- 33개의 파이썬 예약어는 변수명으로 사용 불가
~~~python
num = 1
hello = 'Hello World Python'
~~~

### 여러 변수 동시 할당
~~~python
a = b = 10
a, b = 2, 4
~~~

### 여러 변수 값 교환(swap)
~~~python
a = 10; b = 5
a, b = b, a
~~~
- temp 변수 불필요

## 2. 파이썬 자료형
자료형 확인 : print(type(변수명))
### 숫자 자료형
- int(정수형)
- float(실수형)
- 지수표현
~~~python
17e5 //실행결과 : 1700000.0
~~~

### 불리언 자료형
~~~python
a = True
~~~

### 집합 자료형
- str(문자열) : "..."
- list(리스트) : [...]
- tuple(튜블) : (...)
- set(셋) : {...}
- dictionary(딕셔너리) : {key : value, key : value...}

## 3. 파이썬 형변환
### 묵시적 형변환
### 명시적 형변환
- str -> int : 문자열에 숫자 외의 문자 존재시 형변환 안됨, 공백 자동 제거

-----

# 파이썬 문자열
## 1. 파이썬 문자열
### 파이썬 문자열
- "..." , '...'
- 문자열에 숫자 연결
~~~python
'파이썬' + str(3) //출력결과 : 파이썬3
e = '*' * 10   //출력결과 : **********
~~~

### 파이썬 문자열 인덱스
|문자열|h|e|l|l|o|!|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|인덱스|0|1|2|3|4|5|
|역인덱스|-6|-5|-4|-3|-2|-1|

### 문자열 슬라이싱
- a[시작인덱스 : 종료인덱스]    //시작인덱스부터 종료인덱스 직전까지
- a[시작인덱스 : 종료인덱스 : step(건너뛰기)]   //step = -1이면 역정렬
- 종료인덱스가 -1이면 마지막까지 출력

## 2. 파이썬 문자열 함수
### 내장함수 len()
- 문자열 길이 출력
~~~python
len('HelloWorldPython')   //출력결과 : 16
~~~

### 파이썬 문자열 함수
- 문자.함수명(문자열)
- 문자열.함수명(문자)
- 문자열.함수명(문자열)

#### join() 함수
- 지정된 문자로 문자열을 연결
~~~python
'-'.join('12345')
~~~
- 실행결과 : 1-2-3-4-5

#### split() 함수
지정된 분할하여 리스트로 반환
~~~python
'Hello-World-Python'.split('-')
~~~
- 실행결과 : ['Hello', 'World', 'Python']
~~~python
'서울시 마포구 상암동 1585'.split()
~~~
- 실행결과 : ['서울시', '마포구', '상암동', ' 1585']
- split()에 파라미터가 없으면 공백을 기준으로 나눔

#### strip()
지정된 문자를 문자열로부터 제거
~~~python
text = '\t 문자열 정리   \n'
text.strip()
~~~
- 실행결과 : '문자열 정리'
- 특수문자 제거시 strip()의 파라미터로 작성

#### replace() 함수
문자열내 특정 문자를 다른 문자로 대체
~~~python
생일 = '2016/08/30'
생일.replace('/', '-')
~~~
- 실행결과 : '2016-08-30'

#### startswith() / endswith() 함수
특정 문자열로 시작/종료 여부 검사
- bool 자료형으로 반환
~~~python
'Hello World Python'.startswith('Hello')    //True
'Hello World Python'.startswith('hello')    //False
'Hello World Python'.endswith('Python')    //True
'Hello World Python'.endswith('python')    //False
~~~

#### count() 함수
문자열 내 지정된 문자의 개수
~~~python
text = 'Hello World Python'
text.count('o')               //실행결과 : 3
text = 'Hello World Python, Welcome to Python World'
text.count('Python')        //실행결과 : 2
~~~

#### index() / find() 함수
문자열 내 지정된 문자/문자열 위치 인덱스
~~~python
text = 'Hello World Python, Welcome to Python World'
text.index('o')     //실행결과 : 4
text.index('o', 5)    //실행결과 : 7
text.find('Python')   //실행결과 : 12
text.find('Python', 20)   //실행결가 : 31
~~~

#### capitalize() / lower() / upper() 함수
문자열을 첫 글자만 대문자/소문자/대문자로 반환
~~~
'Hello World'.capitalize()    //실행결과 : 'Hello world'
'Hello World'.lower()         //실행결과 : 'hello world'
'Hello World'.upper()         //실행결과 : 'HELLO WORLD'
~~~

#### 문자열 in / not in 연산자
문자열 내 특정 문자열이 포함 여부를 bool wkfyguddmfh qksghks
- A in B : A 문자열이 B 문자열 내 포함 여부
~~~python
'Python' in 'Hello World Python'      //True
'Java' in 'Hello World Python'        //False
~~~

## 3. 파이썬 문자열 포맷팅
### 문자열 포맷팅 방법
1. 
~~~python
name, age, phone = '홍길동', 25, '010-111-2222'
소개 = "이름은 {}이고, 나이는 {}세 이며, 전화번호는 {} 입니다".format(name, age, phone)
소개
~~~

2. 
~~~python
name, age, phone = '홍길동', 25, '010-111-2222'
소개 = "이름은 {0}이고, 나이는 {1}세 이며, 전화번호는 {2} 입니다".format(name, age, phone)
소개
~~~

3. 
~~~python
name, age, phone = '홍길동', 25, '010-111-2222'
소개 = "이름은 {a}이고, 나이는 {b}세 이며, 전화번호는 {c} 입니다".format(c = phone, a = name, b = age)
소개
~~~

4. 추천방법
~~~python
name, age, phone = '홍길동', 25, '010-111-2222'
소개 = "이름은 {name}이고, 나이는 {age}세 이며, 전화번호는 {phone} 입니다"
소개
~~~
- 출력결과 : '이름은 홍길동 이고, 나이는 25세 이며, 전화번호는 010-111-2222 입니다'

### 문자열 포맷팅
~~~python
jan, dec = 1, 12
print("한 해의 시작은 {:02d}월".format(jan))
print("한 해의 마지막은 {:02d}월".format(dec))
~~~
- 실행결과
> 한 해의 시작은 1월
> 한 해의 마지막은 12월

~~~python
val = 123456789
money = "{:,}"
money.format(val)
~~~
- 실행결과 : '123,456,789

~~~python
'{}, {:f}, {:.1f}, {:.2f}, {:.2%}'.format(3, 3, 3, 3.1415, 1/3)
~~~
- 실행결과 : '3, 3.000000, 3.0, 3.14, 33.33%'

-------

# 파이썬 리스트와 튜플
## 1. 파이썬 리스트
### 파이썬 리스트
~~~python 
letters = ['A', 'B', 'C', 'D', 'E', 'F']
letters
~~~
#### 파이썬 리스트 연산
~~~python
letter1 = ['A'. 'B', 'C']
letter2 = ['D', 'E']

# 리스트와 리스트의 결합 연산
letter1 + letter2       //실행결과 : ['A', 'B', 'C', 'D', 'E']

# 원소 존재여부 확인을 위한 in 연산
'A' in letter1      //True
'A' in letter2      //False
~~~

#### 리스트의 원소 변경
~~~python
letters = ['A', 'B', 'C', 'D', 'E', 'F']
letters[0] = 'a'
letters               //실행결과 : ['a', 'B', 'C', 'D', 'E', 'F']
letters[6] = 'a'      //error - 인덱스 범위 넘는 곳에 새로 추가 불가능
~~~

#### 내장함수
~~~python
letters = ['A', 'B', 'C', 'D', 'E', 'F']

# 1. len()
len(letters)          //실행결과 : 6

# 2. count()
letters.count('A')    //실행결과 : 1

# 3. append()
letters.append('a')
letters               //실행결과 : ['A', 'B', 'C', 'D', 'E', 'F', 'a']

# 4. insert()
letters.insert(2, 'z')
letters               //실행결과 : ['A', 'B', 'z', 'C', 'D', 'E', 'F', 'a']

# 5. pop()
letters.pop(2)        //실행결과 : 'z'
letters               //실행결과 : ['A', 'B', 'C', 'D', 'E', 'F', 'a']

# 6. remove()
letters.remove('a')
letters               //실행결과 : ['A', 'B', 'C', 'D', 'E', 'F']

# 7. sort()
letters.sort(reverse = True)
letters             //실행결과 : ['F', 'E', 'D', 'C', 'B', 'A']
letters.sort()
letters             //실행결과 : ['A', 'B', 'C', 'D', 'E', 'F']
~~~

## 2. 파이썬 리스트 인덱싱과 슬라이싱
### 파이썬 리스트 인덱싱
|문자열|'A'|'B'|'C'|'D'|'E'|'F'|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|인덱스|0|1|2|3|4|5|
|역인덱스|-6|-5|-4|-3|-2|-1|
~~~python
letters[0:3]        //실행결과 : ['A', 'B', 'C']
letters[3:]         //실행결과 : ['D', 'E', 'F']
letters[:]          //실행결과 : ['A', 'B', 'C', 'D', 'E', 'F']
letters[::2]        //실행결과 : ['A', 'C', 'E']
letters[::-1]       //실행결과 : ['F', 'E', 'D', 'C', 'B', 'A']
~~~

## 3. 파이썬 튜플
~~~python
tuple1 = ('A', 'B', 'C', 'D', 'E')
tuple1        //실행결과 : ('A', 'B', 'C', 'D', 'E')

tuple1[0] = 'a'     //error
~~~
- 튜플의 원소 변경은 불가
  - 튜플은 read only
  - 리스트는 변경 가능
- 튜플은 index() 함수와 count() 함수만 사용 가능

### 파이썬 튜플의 리스트 변환
튜플은 list() 함수를 사용하여 리스트로 변환 가능
리스트는 tuple() 함수를 사용하여 튜플로 변환 가능

-----

# 파이썬 셋과 딕셔너리
## 1. 파이썬 셋
### 파이썬 셋
- 중복을 허용하지 않고 원소들의 순서가 없어 인덱싱과 슬라이싱 불가
~~~python
set1 = {'A', 'B', 'C', 'D', 'E', 'F', 'B'}
set1

set1[0]   //error
set1[:4]  //error
~~~
- 실행결과 : {'A', 'B', 'C', 'D', 'E', 'F'}

### remove() / pop()
~~~python
set1 = {'A', 'B', 'C', 'D', 'E', 'F'}

# 지정 원소 제거
set1.remove('A')
set1              //실행결과 : {'B', 'C', 'D', 'E', 'F'}

# 마지막 원소 제거
set1.pop()
set1            //실행결과 : {'B', 'C', 'D', 'E'}
~~~

## 2. 파이썬 셋의 집합 연산
### 함수
- 파이썬 셋은 교집합, 합집합, 차집합 등의 집합 연산자 및 연산 함수 기능
~~~python
set1 = {'A', 'B', 'C', 'D', 'E', 'F'}
set2 = {'B', 'D', 'G', 'H'}

# 교집합     # 실행결과 : {'B', 'D'}
set1 & set2
set1. intersection(set2)

# 합집합   # 실행결과 : {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
set1 | set2
set1.union(set2)

# 차집합   # 실행결과 : {'A', 'C', 'E', 'F'}
set1 - set2
set1.difference(set2)

# 대칭 차집합    # 실행결과 : {'A', 'C', 'E', 'F', 'G', 'H'}
set1 ^ set2
setq.symmetric_difference(set2)
~~~

## 3. 파이썬 딕셔너리
### 파이썬 딕셔너리
~~~python
중간고사 = {
  "수학" : 100,
  "영어" : 90,
}
중간고사
~~~
- 실행결과 : {'수학' : 100, '영어' : 90}

### 원소 추가, 확인, 변경, 삭제
~~~python
# 원소 추가
중간고사['국어'] = 85
중간고사              //실행결과 : {'수학' : 100, '영어' : 90, '국어' : 85}

# 원소 확인
중간고사['영어']      //실행결과 : 90

# 원소 변경
중간고사['영어'] = 95
중간고사              //실행결과 : {'수학' : 100, '영어' : 95, '국어' : 85}

#원소 삭제
중간고사.pop('국어')
중간고사              //실행결과 : {'수학' : 100, '영어' : 95}
~~~

### keys(), values(), items()
~~~python
중간고사 = {
  "수학" : 100,
  "영어" : 90,
  "국어" : 85
}

list(중간고사.keys())     //실행결과 : ['수학', '영어', '국어']
list(중간고사.values()    //실행결과 : [100, 90, 85]
중간고사.items()          //실행결과 : dict_items([('수학', 100), ('영어', 90), ('국어', 85)])
~~~

-------

# 파이썬 조건문
## 1. 파이썬 비교 연산자와 논리 연산자
## 2. 파이썬 조건문
## 3. 파이썬 중첩/복합 조건문
