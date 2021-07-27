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

## 2. 파이썬 자료형

## 3. 파이썬 형변환
