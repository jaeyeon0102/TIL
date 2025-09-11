# History of JavaScript

## ECMAScript

- Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
- 스크립트 언어가 준수해야 하는 규칙, 세부사항 등을 제공

### ECMAScript와 JavaScript

- JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
- ECMAScript의 명세를 기반으로 하여 웹 브라우저나 Node.js와 같은 환경에서 실행
- **ECMAScript**는 **언어의 핵심**을 정의하고,
- **JavaScript**는 **ECMAScript 표준을 따라 구현된 언어**로 사용

### JavaScript의 현재

- 현재는 Chrome, Firefox, Safari, Microsoft Edge 등 다양한 웹 브라우저가 경쟁하고 있으며, 모바일 등 시장이 다양화 되어 있음
- 기존에 JavaScript는 브라우저에서만 웹 페이지의 동적인 기능을 구현하는 데에만 사용됨
    - ex) 사용자의 입력에 따라 웹 페이지의 내용이 동적으로 변경되거나, 애니메이션 효과가 적요되는 등의 기능
- Node.js로 인해 브라우저에서 벗어나 서버 사이드 분야 뿐만 아니라, 클라이언트 사이드 등 다양한 프레임워크와 라이브러리들이 개발되면서, 웹 개발 분야에서는 필수적인 언어로 자리 잡게 됨

# JavaScript

## 변수

### 변수 선언 키워드

**변수명(식별자) 작성 규칙**

- 반드시 문자, 달러(’$’) 또는 밑줄(’_’)로 시작
- 대소문자 구분
- 예약어 사용 불가
    - for, if, function 등
- Naming case
    - 카멜 케이스
        - 변수, 객체, 함수에 사용
    - 파스칼 케이스
        - 클래스, 생성자에 사용
    - 대문자 스네이크 케이스
        - 상수에 사용
1. **let**
    1. **블록 스코프**를 갖는 지역 변수 선언
    2. **재할당 가능** → 해당 변수에 내용을 바꾸는건 가능하지만 
    3. **재선언 불가능** → 동일한 변수를 다시 선언하는건 불가
    4. ES6에 추가
    
    ```jsx
    let number = 10 //1. 선언 및 초기값 할당
    number = 20   //2 재할당 가능
    
    let number = 10  //1. 선언 및 초기값 할당
    let number = 20  //2. 재선언 불가능
    ```
    
2. **const**
    1. **블록 스코프**를 갖는 지역 변수 선언
    2. **재할당 불가능**
    3. **재선언 불가능**
    4. ES6에 추가
    5. **값의 변경은 가능하지만 타입 변경은 불가 ??**
3. var → 안씀

- 블록 스코프
    - if, for, 함수 등의 **‘중괄호({}) 내부’** 를 가리킴
    - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가
    
    ```jsx
    let x = 1
    
    if (x==1) {
    	let x = 2
    	console.log(x)  //2
    }
    console.log(x)  //1
    ```
    

- 기본적으로 const 사용 권장
- 재할당 필요하다면 그때 let으로 변경해서 사용

## 데이터 타입

### 원시 자료형 (Primitive type)

- 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)
- **Number, String, Boolean, null, undefined**
    - undefined : 할당조차 되지 않은 것
- 변수에 할당될 때 값이 복사됨 → **변수 간에 서로 영향 미치지 않음**

```jsx
let a = 10
let b = a
b = 20

console.log(a) // 10
console.log(b) //20
```

### 참조 자료형 (Reference type)

- 객체의 주소가 저장되는 자료형 (가변, 주소가 복사)
- **Objects (Object, Array, Function)**
- 객체를 생성하면 객체의 메모리 주소를 변수에 할당
- **변수 간에 서로 영향을 미침**

```jsx
const obj1 = {name:'Alice', age: 30}
const obj2 = obj1
obj2.age = 40

console.log(obj1.age) //40
console.log(obj2.age) //40
```

### 원시 자료형 종류

- Number
    - 정수 또는 실수형 숫자를 표현하는 자료형
    
    ![image.png](attachment:8a3d39bb-3b0f-49aa-bea0-be93cbc0cf87:image.png)
    
- String
    - 텍스트 데이터를 표현하는 자료형
    - ‘+’ 연산자를 사용해 문자열끼리 결헙
    - 뺄셈, 나눗셈, 곱셉 불가능
- **Template literals (템플릿 리터럴)  → python의 f-string과 동일**
    - 내장된 표현식을 허용하는 문자열 작성방식
    - Backtick(``)을 이용하여, 여러 줄에 걸쳐 문자열 정의 가능
    - 표현식은 ‘$’와 중괄호(${expression})로 표기
    
    ![image.png](attachment:c8262783-484e-46f7-b972-4a61b043d325:image.png)
    
- null
    - 변수의 값이 없음을 **의도적으로** 표현할 때 사용
    - **null 타입은 object라고 나옴 (javascript의 실수)**
- undefined
    - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당
    
    ![image.png](attachment:1fc17198-f6cf-49ec-ad00-0e00d1ce67e6:image.png)
    
- Boolean

![image.png](attachment:2e31555a-3fbe-474c-ae5a-9c58df4e7882:image.png)

## 연산자

### 할당 연산자

![image.png](attachment:6f2b2c87-42f1-462b-b4c5-1606778f4b4b:image.png)

### 증가 & 감소 연산자

![image.png](attachment:efb4018b-6b19-4491-91a8-d4d35ae9a30a:image.png)

### 비교 연산자

![image.png](attachment:8a6031d2-0aea-4e30-9c9d-a06ddd700055:image.png)

### 동등 연산자 (==) → 거의 안쓸거임

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- ‘암묵적 타입 변환’ 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자는 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

```jsx
console.log('1' == 1) //true
```

![image.png](attachment:6a45987f-46b6-4efc-9dd3-6ede2c5ea36e:image.png)

### 일치 연산자 (===)

- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
- 특수한 경우를 제외하고는 동등 연산자가 아닌 일치 연산자 사용 권장

![image.png](attachment:f7d9e58f-c19e-457e-82d0-07410ca3c321:image.png)

### 논리 연산자

- and : &&
- or : ||
- not : !
- 단축평가 지원

## 조건문

### if

- 참/거짓 판단

### 삼항 연산자 → 시험 안나옴ㅎ

```jsx
condition ? expression1 : expression2
```

- condition
    - 평가할 조건 (true 또는 false로 평가)
- expression1
    - true일 경우
- expression2
    - false일 경우

## 반복문

### while

### for

- 특정한 조건이 거짓으로 판별될 때까지 반복

```jsx
for (let i = 0; i <6; i++){
	console.log(i)
}
```

### for …in

- **객체의 열거 가능한 속성(property)**에 대해 반복
- object 순회할 때만 사용할 거임

![image.png](attachment:0661c9ee-74d2-466c-ba2e-f5dedf9abe9b:image.png)

### for …of → python의 for문과 동일

- 반복 가능한 객체(배열, 문자열 등)에 대해 반복

![image.png](attachment:4d314b29-48f0-47f4-92de-b7147d46a718:image.png)

### for_in 과 for _of차이

- array를 넣는다고 했을 때 for_in은 키값인 index 번호가 출력되고, for_of는 값이 출력됨

![image.png](attachment:4c1f2513-30a3-4423-b7f7-d40e853768b7:image.png)

# DOM

### 웹 브라우저에서의 JavaScript

- 웹 페이지의 **동적인 기능** 구현

### JavaScript 실행 환경 종류

1. HTML script 태그
2. js 확장자 파일
3. 브라우저 Console

## DOM (The Document Object Model)

- 웹 페이지를 **구조화된 객체**로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법 제공
- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함

### DOM API

- 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작할 수 있도록 페이지 요소들을 객체 형태로 제공하며 이에 따른 메서드 또한 제공

## DOM 특징

- DOM 에서 모든 요소, 속성, 텍스트는 하나의 객체
- 모두 **document 객체**의 하위 객체로 구성

![image.png](attachment:d4032ac8-32a2-4947-9ba0-ce26c97ca482:image.png)

### DOM tree

- 브라우저는 HTML 문서를 해석하여 DOM tree 라는 객체 트리로 구조화
- 객체 간 상속 구조가 존재

### 브라우저가 웹 페이지 불러오는 과정

![image.png](attachment:08fa056f-3f24-4b61-8b7b-fe32f4a39c38:image.png)

### DOM 핵심

- 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API

## document 객체

- 웹 페이지 객체
- DOM tree의 진입점
- 페이지를 구성하는 모든 객체요소 포함

![image.png](attachment:fd5017be-ca77-4034-922c-309a88142073:image.png)

### 예시

- HTML <title> 변경하기

![image.png](attachment:0e482ea8-660f-4cd9-95b8-57a4944e3581:image.png)

## DOM 선택

### DOM 조작 시 기억해야 할 것

**웹 페이지를 동적으로 만들기 == 웹 페이지를 조작하기**

- 조작 순서
    1. 조작하고자 하는 요소를 **선택** (또는 탐색)
    2. 선택된 요소의 콘텐츠 또는 속성 **조작**

### 선택 메서드

- **`document.querySelector(selector)`**
    - 제공한 선택자와 일치하는 element **맨 처음** 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null 반환)
    - 요소 한 개 선택
- **`document.querySelectorAll(selector)`**
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 제공한 CSS selector를 만족하는 NodeList 반환
    - 요소 여러 개 선택

![image.png](attachment:4d07ca0a-61f1-4c3d-95fb-d9946d15dffe:image.png)

## DOM 조작

### 1. 속성(attribute) 조작

1. 클래스 속성 조작
    1. **‘classList’ property**
    2. 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
    - **`element.classList.add()`**
    - **`element.classList.remove()`**
    - **`element.classList.toggle()`**
        - 클래스가 존재한다면 제거하고 false 반환
        - 존재하지 않으면 클래스 추가하고 true반환
2. 일반 속성 조작 → **이거 쓰는게 명시적임**
    - **`Element.getAttribute()`**: 해당 요소에 지정된 값을 반환 (조회)
    - **`Element.setAttribute(name, value)`**
        - 지정된 요소의 속성 값을 설정
        - 속성이 이미 있으면 기존 값을 갱신 (그렇지 않으면 지정된 이름과 값으로 새 속성 추가)
    - **`Element.getAttribute()`**
        - 요소에 지정된 이름을 가진 속성 제거

### 2, HTML 콘텐츠 조작

- ‘`textContent`’ property
- 요소의 텍스트 콘텐츠 표현
- `h1Tag.textContent = ‘내용 수정’`
- `<p>lorem</p>`

### 3. DOM 요소 조작

- 메서드
    - **`document.createElement(tagName)`**
        - 작성한 tagName의 HTML 요소를 생성하여 반환
    - **`Node.appendChild()`**
        - 한 노드를 특정 부모 노드의 자식 NodeList 중 마지막 자식으로 삽입
        - 추가된 Node 객체 반환
    - **`Node.removeChild()`**
        - DOM에서 자식 Node를 제거
        - 제거된 Node를 반환

![image.png](attachment:4cb322e0-f377-4a9b-9c9c-c2726ec56468:image.png)

### 4. 스타일 조작 → 잘 안쓸거  이유 : inner 뭐시기랑 비슷 (찾아보기)

- ‘style’ property
- 해당 요소의 모든 style 속성 목록을 포함하는 속성

# JavaScript

## 함수 (Function)

- 참조 자료형에 속하며 모든 함수는 Function object

### 함수 구조

- function 키워드
- 함수 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statements
- **return값이 없으면 undefined를 반환**

### 함수 정의하는 방법

1. 선언식 (function declaration)
    - 그냥 함수 선언.
    
    ```jsx
    function funcNmae(){
    	statesments
    }
    ```
    
2. 표현식 (function expression) 
    
    → 하나의 값으로 나타낸다(변수에 할당할 수 있다)
    
    → 함수는 객체이기 때문
    
    ```jsx
    const funcName = function(){
    	statesments
    }
    ```
    

![image.png](attachment:743189d6-132f-4478-8757-e9978647be5e:image.png)

## 매개변수

1. **기본 함수 매개변수**
    1. 전달하는 인자가 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
    
    ![image.png](attachment:422e7495-dd45-4c3f-bf61-e35c1b2404c7:image.png)
    
2. **나머지 매개변수**
    1. 임의의 수의 인자를 ‘**배열**’로 허용하여 가변 인자를 나타내는 방법
    2. 작성규칙
        1. 함수 정의 시 나머지 매개변수는 하나만 작성할 수 있음
        2. 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함
    
    ![image.png](attachment:0b1192b6-623d-41bd-8782-6e39e6d5b0dd:image.png)
    
- 매개변수와 인자 개수가 불일치할 때
    - 매개변수 개수 > 인자개수
        - 누락된 인자 : undefined
        
        ![image.png](attachment:55c7c764-f456-4be9-b637-df5d7f6db767:image.png)
        
    - 매개변수 개수 < 인자 개수
        - 초과 입력한 인자는 사용 불가
        
        ![image.png](attachment:7b8e7fa6-ba04-4124-885c-9486d5910340:image.png)
        

## Spread syntax

- 전개 구문
- ‘…’
- 배열이나 문자열과 같이 반복 가능한 항목 펼치는 것 (확장, 전개)

![image.png](attachment:fb94f9bd-63c5-47a4-ae0f-06d86e17f3b3:image.png)

![image.png](attachment:57262423-022c-4054-aa42-58b095035d83:image.png)

![image.png](attachment:4aa82ca6-cc8f-4c59-9052-d71ab0821f5f:image.png)

## 화살표 함수

- 함수 표현식의 간결한 표현법
- 사용 이유 : 단순히 function 키워드 줄이는 게 아니라 객체를 다룰 때 신경써야하는 부분을 없앨 수 있다

```jsx
const arrow = name -> 'hello, ${name}'
```

![image.png](attachment:bb3f0b31-af9a-42cc-9b1d-f0a0379ed341:image.png)

### 참고

- 세미콜론
    - 자바스크립트는 문장 마지막 세미콜론을 선택적으로 사용 가능
    - 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론 삽입됨
    - JavaScript를 만든 Brendan Eich 또한 세미콜론 작성 반대

## 이벤트

- 일상 속 이벤트
    - 컴퓨터 키보드를 눌러 텍스트를 입력하는 것
    - 손 흔들어 인사하는 것 등

### 웹 에서의 이벤트

- 화면 스크룰
- 버튼 클릭시 팝업 창 출렭되는 것
- **웹의 모든 동작은 이벤트 발생과 함께 함.**

### event

- 무언가 일어났다는 신호, 사건
- **모든 DOM 요소는 이러한 event를 만들어 냄**
- 종류
    - mouse, input, keyboard, touch

**DOM 요소는 event를 받고 받은 event를 ‘처리’할 수 있음**

### event handler (이벤트 처리기)

- 이벤트가 발생했을 때 실행되는 함수
- 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것

![image.png](attachment:40650369-52bd-4697-b812-075e1eefbeec:image.png)

![image.png](attachment:aac01479-fef7-49be-b2db-ce6140b1eb69:image.png)

- type
    - 수신할 이벤트 이름
    - 문자열로 작성
- handler
    - 발생한 이벤트 객체를 수신하는 **콜백 함수**
    - 콜백 함수는 발생한 **event object**를 유일한 매개변수로 받음

![image.png](attachment:ae6f5a39-4b8e-41b0-8adb-03de3473978c:image.png)

- **`addEventListener` 의 콜백 함수 특징**
    - 발생한 이벤트를 나타내는 event 객체를 유일한 매개변수로 받음
    - 반환 값 없음

### 🚨버블링

- form > div > p 형태의 중첩된 구조에 각각 이벤트 핸들러가 있을 때 만약 <p>요소를 클릭하면?
    - <p> 요소만 클릭했음에도 모든 핸들러가 동작함
- 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상
- 가장 최상단의 조상 요소(document)를 만날 때까지 이 과정이 반복되며 요소 각각에 할당된 핸들러 동작

### 이벤트가 정확히 어디서 발생했는지 접근할 수 있는 방법

- `event.currentTarget`
    - ‘현재’ 요소
    - 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
    - ‘this’와 같음
- `event.target`
    - 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성
    - 실제 이벤트가 시작된 요소
    - 버블링이 진행되어도 변함 x

![image.png](attachment:f9c70da1-b206-4da5-abf0-2e185050f615:image.png)

![image.png](attachment:1c274a39-0435-4a22-ac54-0af4ff6ac7bf:image.png)

**버블링이 필요한 이유**

![image.png](attachment:cf7803f5-d857-4860-a1bd-37d3ae0ae1cf:image.png)

### 캡처링 (참고)

![image.png](attachment:0218371d-39bd-473f-86ed-462b2f45cc44:image.png)

### 이벤트의 기본 동작 취소

- HTML의 각 요소가 기본적으로 가지고 있는 이벤트가 때로는 방해가 되는 경우가 있어 이벤트의 기본 동작을 취소할 필요가 있음
- `.preventDefault()` : 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정
    - copy 이벤트 동작 취소
    - form제출 시 페이지 새로고침 동작 취소