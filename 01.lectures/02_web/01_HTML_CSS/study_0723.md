# 웹

## World Wide Web

- 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

## Web

- Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

### Web site

- 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간

### Web page

- HTML, CSS 등의 웹 기술을 이용하여 만들어진, ‘Web site’를 구성하는 하나의 요소
- 구성요소 : HTML, CSS, Javascript

## HTML

- HyperText Markup Language : 웹 페이지의 **의미**와 **구조**를 정의하는 언어

### Hypertext

- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- **비선형성 / 상호연결성 / 사용자 주도적 탐색**

### Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조 명시하는 언어
- ex) HTML, Markdown

### HTML 구조

```html
<!DOCTYPE html>   # 해당 문서가 html 문서라는 것을 나타냄
<html lang="en">   # <html></html> 전체 페이지의 콘텐츠 포함

<head>
  <meta charset="UTF-8">
  <title>My page</title>   # <title> </title> 브라우저 탭 및 즐겨찾기 시 표시되는 제목
</head>                    # </head></head> HTML 문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 
														 메타 데이터 작성
													 # 사용자에게 보이지 않음

<body>                     #<body></body> HTML 문서 내용 나타냄./페이지에 표시되는 모든 콘텐츠 작성
													# 한 문서에 하나의 BODY 요소만 존재
  <p>This is my page</p>
  <a href="https://www.google.co.kr/">Google로 이동</a>
  <img src="images/sample.png" alt="sample-img">
  <img src="https://random.imagecdn.app/500/150/" alt="sample-img">
</body>

</html>
```

### HTML Elements

- 하나의 요소는 **여는 태그**와 **닫는 태그** 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 앞에 슬러시 포함

### HTML Attributes(속성)

- 사용자가 원하는 기준에 맞도록 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값
- 목적
    - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
    - CSS에서 스타일 적용을 위해 해당 요소를 선택하기 위한 값으로 활용

![image.png](attachment:b6c88e80-7a32-4f9f-b5fe-cec1bf7c62d3:image.png)

- **작성 규칙**
    1. 속성은 **요소 이름과 속성 사이에 공백**이 있어야 함
    2. 하나 이상의 속성들이 있는 경우엔 **속성 사이에 공백**으로 구분함
    3. 속성 값은 **열고 닫는 따옴표**로 감싸야 함

### HTML Text structure

- HTML의 주요 목적 중 하나는 **텍스트 구조와 의미** 제공하는 것
- ex) h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것
- Heading & Paragraphs
    - h1~6, p
- Lists
    - ol, ul, li
- Emphasis & Importance
    - em, strong

# 웹 스타일링

## CSS

- Cascading Style Sheet
- 웹 페이지의 **디자인**과 **레이아웃**을 구성하는 언어

![image.png](attachment:c6672ad6-9439-4c5c-868f-d6ded3704c13:image.png)

- 선택자 (Selector)
- 속성 (Property)
- 선언 (Declaration)
- 값 (Value)

### CSS 적용 방법

1. 인라인 스타일 → 쓰지마
2. 내부 스타일 시트
    1. head 태그 안에 style 태그에 작성
3. 외부 스타일 시트
    - 별도 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기
    - `<link rel=’stylesheet’ href=’style.css’>`

### CSS Selectors

- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

1. 기본 선택자
    1. **전체(*)** 선택자 : HTML 모든 요소 선택
    2. **요소(tag)** 선택자 : 지정한 모든 태그 선택 
    3. **클래스(class)** 선택자**(’.’ (dot))** : 주어진 클래스 속성을 가진 모든 요소 선택 
    4. **아이디(id)** 선택자**(’#’)** 
        1. 주어진 아이디 속성을 가진 요소 선택
        2. 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함 
    5. **속성(attr)** 선택자

1. 결합자 (Combinators)
    1. 자손 결합자**(” “ space))**
        1. 첫 번째 요소의 자손 요소들 선택
        2. 예) p span은 <p> 안에 있는 모든 <span>를 선택 (하위 레벨 상관없이)
    2. 자식 결합자 **(”>”)**
        1. 첫 번째 요소의 직계 자식만 선택
        2. 예) ul > li은 <ul> 안에 있는 모든 <li>를 선택 (한단계 아래 자식들만)

- 자손과 자식 차이
    - 자식은 직계 자식만 선택
    - 

### ⭐명시도(Specificity)

- 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
- CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
- 동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우 가장 높은 명시도를 가진 Selector가 승리하여 스타일 적용

![아래 색이 적용됨](attachment:3eb40cb5-bd78-4d94-80d8-12c708a35ba3:image.png)

아래 색이 적용됨

![위의 색이 적용됨](attachment:183c723d-cdf6-4e76-99e9-41ce80328e2b:image.png)

위의 색이 적용됨

- ⭐명시도 높은 순서
    - **!important : 다른 우선순위 규칙보다 우선하여 적용하는 키워드**
        - 디버깅할 때 사용

![5번은 상속 속성](attachment:47f00791-7398-4a5a-8265-aed507966a22:image.png)

5번은 상속 속성

### CSS 상속

- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임

1. 상속되는 속성
    1. Text 관련 요소(font, color, text-align), opacity, visibility
2. 상속되지 않는 속성
    1. Box model 관련 요소(width, height, border, box-sizing)
    2. position 관련 요소(position, top/right/bottom/left, z-index)

### CSS Box Model

- 웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

1. 박스 타입

1. 박스 표시 (Display) 타입

1. Outer display type
    1. block 특징
        1. 항상 새로운 행으로 나뉨
        2. width와 height 속성 사용 가능
        3. padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
        4. width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간 모두 차지함
            1. 상위 컨테이너 너비 100%로 채우는 것
        5. 대표적인 block 타입 태그
            1. h1~6, p, div
    2. inline 특징
        1. 새로운 행으로 넘어가지 않음
        2. width와 height 속성 사용 불가
        3. 수직 방향
            1. padding, margin, border가 적용되지만 다른 요소 밀어낼 수 없음
        4. 수평 방향
            1. padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
        5. 대표적인 inline 타입 태그
            1. a, img, span, strong, em
    3. inline block 도 있음
        1. 장점 : 

1. Normal flow
    - 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹페이지 요소가 배치되는 방식
    
    ![image.png](attachment:c15ac5db-5837-49f4-a26f-b49959cd8bad:image.png)
    

![image.png](attachment:86894850-a6dd-47c5-a578-24038bae5f53:image.png)

## 참고

### 명시도 관련 문서

![image.png](attachment:da094cec-dc39-4d81-aec6-1ef8e624fcdd:image.png)

### HTML 스타일 가이드

![image.png](attachment:77eb7f75-f0e3-4cf5-a9b8-510483b6e7d6:image.png)

![image.png](attachment:b03c0d00-6a42-4a82-9e8e-a8865b948156:image.png)

### CSS 스타일 가이드