✔ 입력한 태그 별로 게시글과 날짜를 얻어온 후 CSV 파일로 변환해준다. 

✔ After obtaining posts and dates for each hash tag entered, it is converted into a csv file.

<BR>

### 목적 Purpose

***사람들의 기분과 SNS의 연관관계를 알기 위함.***

***To know the relationship between people's mood and SNS***.

- 내가 크롤링 한 해시태그

1. #행복한 하루 <-> #슬픈 하루
2. #행복햄 <-> #우울해
3. #행복해요 <-> #슬프다

<BR>

### 폴더 구조 folder structure

- **`crawler`**

  - **main.py**

    처음 시작하는 main 함수가 있다.

    There is a main function.

  - chromedriver.exe

    selenium을 사용하기 위한 chromedriver이다.

    It is a chromedriver for using selenium.

  - **login.py**

    인스타그램에 로그인 시 필요한 함수들이 있다.

    There are functions required when logging in to Instagram.

  - **crawling.py**

    실제 크롤링 시 필요한 함수들이 있다.

    There are functions necessary for actual crawling.

- `csv`

  크롤링 한 값을 저장한 csv 파일이 들어있다.

  Csv file that stores crawling values.

- `setting`

  env 파일이 들어있다. ignore 했다.

- `visualization`

  * count.py

    csv파일의 content에서 글자 갯수, 태그 갯수, 이모티콘 갯수를 가져온다.

    Get the number of characters, tags, and emoticons from the contents of the csv file.

  * graph.py

    다양한 그래프를 그린다.

    Draw various graphs.

  * main.py

    필요한 그래프를 호출하는 메인 함수이다.

    It is the main function that calls the required graph.

<br>

[blog 🌟🌟](https://try-it-and-try-it-again.tistory.com/3)

