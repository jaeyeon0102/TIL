# CSS Layout

- 각 요소의 **위치**와 **크기를 조정**하여 웹 페이지의 디자인을 결정하는 것

→ Display, Position, Flexbox

## CSS Box Model

- 웹 페이지의 **모든** HTML **요소**를 감싸는 사각형 상자 모델

→ 내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되어 요소의 크기와 배치를 결정

### BOX 타입

1. Block box
2. Inline box

→ 박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

### 박스 표시 타입

1. Outer display type
    - 박스가 문서 흐름에서 어떻게 동작할지 결정
    - 속성 : **block, inline**
    
    ![image.png](attachment:395a9428-6c3b-4e31-8ba5-0897901b00ba:image.png)
    
    ![image.png](attachment:69c36396-c514-41ad-bd64-45dff5ddbe5b:image.png)
    
2. Inner display type → Flexbox
    - 박스 내부 요소들이 어떻게 배치될 지 결정
    - 속성 : flex

### 박스 구성 요소

![image.png](attachment:35f3159e-f33c-4199-96ca-8d6e9906ef2b:image.png)

- Content box → **내용 적히는 곳**
    - 실제 콘텐츠가 표시되는 영역 크기
    - width 및 height 속성을 사용하여 크기 조정
- Padding box  → **box 안쪽 기준으로 공백**
    - 콘텐츠 주위에 공백
    - padding 관련 속성을 사용하여 크기 조정
- Border box → 박스 래핑
    - **콘텐츠와 패딩을 래핑**
    - border 관련 속성을 사용하여 크기 조정
- Margin box  → **테두리 기준 바깥쪽 공백**
    - 콘텐츠, 패딩 및 테두리를 래핑
    - 박스와 다른 요소 사이의 공백
    - margin 관련 속성을 사용하여 크기 조정

### shorthand 속성 (짧게 간추려 쓸 수 있는 것)

- border
    - border-width, border-style, border-color 를 한 번에 설정하기 위한 속성
    - `border: 2px solid black;`  → **작성 순서에 영향 x**
- margin & padding
    - 4방향의 속성을 각각 지정하지 않고 한 번에 지정할 수 있는 속성
    - margin: 10px 20px 30px 40px → **상/우/하/좌 (4개) → 시계방향**
    - margin: 10px 20px 30px  → **상/좌우/하 (3개)**
    - margin: 10px 20px → **상하/좌우 (2개)**
    - margin: 10px → **공통 (1개)**

### box-sizing 속성

1. The standard CSS box model
    1. **표준 상자 모델에서 width 와 height 속성 값을 설정하면 이 값은 content box의 크기를 조정**
        
        ![image.png](attachment:90779183-4f68-49c6-976d-6c6abf360845:image.png)
        
    2. CSS는 border box가 아닌 content box의 크기를 width 값으로 지정
    
    ![image.png](attachment:6dda730d-d818-47eb-8528-c60d434808b1:image.png)
    
2. 대안

![image.png](attachment:29e8b935-2f10-494c-bc19-02b2ded8d2d3:image.png)

![image.png](attachment:0c5cb61f-8b10-4bb8-abf6-432f1f57d9bb:image.png)

![image.png](attachment:13138756-2699-42ae-a43d-e43dd0cf4297:image.png)

### 기타 display 속성

1. inline-block

![image.png](attachment:a93e48a0-a870-47c2-a213-b904305caa58:image.png)

→ **새로운 행으로 넘어가지 않음**

1. ⭐none
- 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
- 화면에는 보이지 않지만 **렌더링**은 필요할 때

## CSS position (3차원도 가능)

- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
- → 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

### 이동 방향

![image.png](attachment:6dfdd7b5-0862-47da-b3e2-4ff301a88423:image.png)

### Position 유형

1. **static** : 왼쪽 위 기존 자리
    1. 요소를 Normal Flow에 따라 배치
    2. top, right, bottom, left 속성이 적용되지 않음
    3. 기본 값
2. **relative**   : 자신이 차지했던 공간은 **남겨둔 채** 이동 **(내 왼쪽 위 꼭짓점 기준으로 이동)-상대경로**
    1. 요소를 Normal Flow에 따라 배치
    2. 자신의 원래 위치(static)을 기준으로 이동
    3. top, right, bottom, left 속성으로 위치를 조정
    4. 다른 요소의 레이아웃에 영향을 주지 않음(요소가 차지하는 공간은 static일 때와 동일)
3. **absolute** : 자신이 차지했던 공간 **없애고** 이동 **(내 화면 의 왼쪽위 꼭짓점 기준으로 이동)- 절대경로**
    1. 절대경로의 기준(내 화면 왼쪽 위 꼭짓점)은 항상 부모의 왼쪽 위가 기준이 됨
    2. position이 relative인 부모를 기준으로 따라가는 방식을 사용
    3. 요소를 Normal  Flow에서 제거
    4. 가장 가까운 relative 부모 요소를 기준으로 이동
        1. 만족하는 부모 요소가 없다면 body 태그를 기준으로 함
    5. top, right, bottom, left 속성으로 위치를 조정
    6. 문서에서 요소가 차지하는 공간이 없어짐
4. **fixed** : 스크롤 상관없이 동일한 위치에 고정
    1. 요소를 Normal Flow에서 제거
    2. 현재 화면영역(viewport)을 기준으로 이동
    3. 스크롤해도 항상 같은 위치에 유지됨
    4. top, right, bottom, left 속성으로 위치 조정
    5. 문서에서 요소가 차지하는 공간이 없어짐
5. **sticky : 스크롤 내리면서 sticky 부분의 height가 0이 되었을 때 다음 sticky로 바뀜**
    1. relative와 fixed의 특성을 결합한 속성
    2. 스크롤 위치가 임계점에 도달하기 전에는 relative처럼 동작
    3. 스크롤이 특정 임계점에 도달하면 fixed처럼 동작하여 화면에 고정
    4. 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체
        1. 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문

![image.png](attachment:fcc3b789-656a-469d-8d1f-2d0a8b2867e1:image.png)

![image.png](attachment:bea9ed6e-1624-4e5d-ba55-dfa52744f921:image.png)

### z-index

- 요소의 **쌓임 순서**(stack order)를 정의하는 속성
- 정수 값을 사용해 **Z축 순서** 지정
- **값이 클수록** 요소가 위에 쌓이게 됨
- **static이 아닌 요소**에만 적용
- 기본값은 **auto**
- **부모 요소의 z-index 값에 영향 받음**
- **같은 부모 내에서만** z-index 값을 비교
- **부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없음**
- z-index 값이 같으면 HTML 문서 순서대로 쌓임

![image.png](attachment:a9013184-8dac-4a22-b94c-e1a68ec9cf53:image.png)

### Position의 목적

- 전체 페이지에 대한 레이아웃을 구성하는 것보다는 페이지 특정 항목의 위치를 조정하는 것

## ⭐CSS Flexbox → Inner display type

- 요소를 행과 열 형태로 배치하는 **1차원 레이아웃 방식**
- 공간 배열 & 정렬

### Inner display type

- 박스 내부의 요소들이 어떻게 배치될지를 결정
- 속성 : flex

![image.png](attachment:ee078090-6723-4a5b-bd66-f7a82d1aafa8:image.png)

### main axis (주 축)

- flex item들이 배치되는 기본 축
- main start에서 시작하여 main end방향으로 배치 (기본 값)

![image.png](attachment:7cc53c2f-2234-40f6-abc8-736264ad2c56:image.png)

### cross axis (교차 축)

- main axis 에 수직인 축
- cross start에서 시작하여 cross end 방향으로 배치 (기본 값)

![image.png](attachment:f61b821b-70d6-4a0d-a103-3cd6429316ec:image.png)

### Flex Container

- `display: flex;` 혹은 `display: inline-flex;`  가 설정된 부모 요소
- 이 컨테이너의 **1차 자식 요소들이 Flex Item이 됨**
- flexbox 속성 값들을 사용하여 자식 요소 Flex Item들을 배치하는 주체

![image.png](attachment:52d737f0-9b00-4230-b412-fa8f5f139841:image.png)

### Flex Item

- Flex Container 내부에 레이아웃되는 항목

![image.png](attachment:5356f7ae-2743-447b-ba06-4a27b474495f:image.png)

### flex-direction

![image.png](attachment:5bf005c7-1493-4660-b677-07666b242a33:image.png)

### flex-wrap

![image.png](attachment:f82456b2-e2e0-4886-b6fb-67bfed86de54:image.png)

### justify-content

![image.png](attachment:94f66068-a0bd-4957-835c-3b2c216a1aca:image.png)

### align-content

![image.png](attachment:fa7b950c-ab52-4080-92dd-36f8ec954c29:image.png)

### align-items

![image.png](attachment:7b5c91cc-0060-4c4c-af33-264e234c36a0:image.png)

### align-self

![image.png](attachment:f5eac1e3-638d-41a4-9799-08c3cb92a264:image.png)

### 목적에 따른 속성 분류

![image.png](attachment:91f83b2f-1d62-487a-a89d-e35fe9f5b554:image.png)

### 속성명 TIP

- justify : 주 축
- align : 교차 축

![image.png](attachment:0d875548-018c-4f8e-adfe-3fdb3a621c7d:image.png)

### flex-grow

- 남는 행 여백을 비율에 따라 각 flex item에 분배
    - 아이템 컨테이너 내에서 확장하는 비율 지정
    - flex-grow의 반대는 flex-shrink

![image.png](attachment:0e7c7597-29a0-40ff-b846-b5e120a45fca:image.png)

### flex-basis

- flex item의 초기 크기 값 지정
- **flex-basis와 width 값을 동시에 적용한 경우 flex-basis가 우선**

### flex-wrap 응용

- **반응형 레이아웃**
    - 다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식

## ⭐참고

### 마진 상쇄 (Margin collapsing)

- 두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상

![image.png](attachment:c7214c5a-5821-4b26-a697-30bf5f51e857:image.png)

- 이유
    - 복잡한 레이아웃에서 요소 간 간격을 일간되게 유지하기 위함
    - 요소 간의 간격을 더 예측가능하고 관리하기 쉽게 만듦
    - 일관성, 단순화

### 박스 타입 별 수평 정렬

- **Block** 요소의 **수평 정렬**
    - margin : auto 사용
        - 블록 요소의 너비를 지정하고 좌우 마진을 auto로 설정

![image.png](attachment:17d3f14b-143b-4d08-a3a3-8e7587f72491:image.png)

- **Inline** 요소의 **수평 정렬**
    - text-align 사용
        - 부모 요소에 적용

![image.png](attachment:872e90e7-c28b-4d85-92b0-e35c2c9052a2:image.png)

![image.png](attachment:5e5f20c6-862a-484e-bf2c-72abf20dec48:image.png)

### Flexbox Shorthand 속성

- flex-flow

![image.png](attachment:d60c19eb-84ff-41b6-a703-7092702ed566:image.png)

- flex

![image.png](attachment:b7492992-6219-4994-9120-ef7d6b55df90:image.png)

### ⭐flexbox 속성 정리

![image.png](attachment:b0910b82-f1b4-410d-af8a-1bb93287b9fe:image.png)

![image.png](attachment:38c1ad57-d03f-4d87-99fb-179170fb9c09:image.png)

![image.png](attachment:b70147d2-5e69-437f-a39b-21e167087760:image.png)

![image.png](attachment:4a0c5f50-c3f0-455d-bb59-b198028586fd:image.png)

![image.png](attachment:070a204c-0896-49f6-b5e0-a966ae6f67f0:image.png)

![image.png](attachment:57759485-d5ea-4162-913d-70b8ef13da2d:image.png)