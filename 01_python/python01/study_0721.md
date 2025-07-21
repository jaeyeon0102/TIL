# 파이썬

## 배우는 이유

- 쉽고 간결한 문법
    - 읽기 쉽고 쓰기 쉬운 문법을 가지고 있어 쉽게 배우고 활용 가능
- 파이썬 커뮤니티의 지원
    - 세계적인 규모의 풍부한 온라인 포럼 및 커뮤니티 생태계
- 광범위한 응용 분야
    - 웹 개발, 데이터 분석, 인공지능, 머신러닝, 자동화 스크립트 등의 분야에서 사용

## 데이터 분석 활용

- 풍부한 라이브러리
- 데이터 처리 및 시각화
- 머신러닝 및 인공지능

## 알고리즘 구현에 유리

- 직관적인 문법
    - 복잡한 논리 구조의 알고리즘 이해하고 구현하기에 쉬움
- 강력한 표준 라이브러리
    - 다양한 알고리즘 구현에 필요한 도구 제공
- 빠른 프로토타이핑
    - 알고리즘을 빠르게 테스트하고 수정 가능

## 파이썬 실행 방법

- 파이썬 인터프리터 사용하는 2가지 방법

# 데이터 타입

## Numeric Types

- int, float, complex(복소수)

## Sequence Types

- list, tuple, range
- 여러 개의 값들을 **순서대로** 나열하여 저장하는 자료형
- str, list, tuple, range

### 특징

1. **순서** (Sequence)
    1. 값들이 순서대로 저장 (정렬 x)
2. **인덱싱** (Indexing)
    1. 각 값에 고유한 인덱스(번호)를 가지고 있음
    2. 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정 가능
3. **슬라이싱** (Slicing)
    1. 인덱스 범위를 조절해 부분적인 값을 추출 가능
4. **길이** (Length)
    1. len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
5. **반복** (Iteration)
    1. 반복문을 사용하여 저장된 값들을 반복적 처리 가능

### str

- 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형
- 문자열은 단일 문자나 여러 문자의 조합으로 이루어짐
- **f-string**
    - 문자열에 f 또는 F 접두어를 붙이고 표현식을 {expression}로 작성하여 문자열에 파이썬 표현식의 값 삽입 가능

```jsx
my_str = 'hello'
# 인덱싱
print(my_str[1]) # e
# 슬라이싱
print(my_str[2:4]) # ll  # 2부터 4 앞까지 슬라이싱
# negative indexing도 가능
print(my_str[-2:-4]) # 위와 동일
print(my_str[0:5:2]) # he  # 0부터 5 앞까지 2칸씩 건너뛰기    

# 길이
print(len(my_str)) # 5

# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'
```

- 메서드
    - `s.replace(old, new[,count]` : 바꿀 대상 글자를 새로운 글자로 바꿔서 변환
    - `s.strip([chars])` : 공백이나 특정 문자 제거
    - `s.split(sep=None, maxsplit=-1)` : 공백이나 특정 문자를 기준으로 분리
    - ‘`separator’.joi(iterable)` : 구분자로 iterable의 문자열을 연결한 문자열 반환

### list

- 리스트는 **변경 가능**
- 메서드
    - `L.append(x)` : 리스트의 마지막 항목 x 추가
    - `L.extend(m)` : Iterable m의 모든 항목들을 리스트 끝에 추가 (+=과 같은 기능)
    - `L.pop(i)` : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
    - `L.reverse()` : 리스트의 순서를 역순으로 변경 (정렬 x)
    - `L.sort()` : 리스트를 정렬 (매개변수 이용가능)

### tuple

- 여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형
- 0개 이상의 객체를 포함하며 데이터 목록 저장
- 소괄호 (())로 표기
- **개발자가 직접 사용하기 보다 ‘파이썬 내부 동작’에서 주로 사용**

### range

- **연속된 정수** 시퀀스를 생성하는 **변경 불가능한** 자료형
- `range(시작 값, 끝 값, 증가 값)`
- `range(n)` : 0부터 n-1까지의 숫자 시퀀스
- `range(n, m)` : n부터 m-1까지의 숫자 시퀀스
- 특징
    - 증가 값이 없으면 1씩 증가
    - 증가 값이 음수면 감소 , 양수면 증가 → 음수라면 시작 값이 끝 값보다 커야 함
    - 증가 값이 0이면 에러

```jsx
ex)
for i in range(1, 10):
	print(i)
```

## Non-sequence Types

### dict

- key -value 쌍으로 이루어진 **순서와 중복이 없는** 변경 가능한 자료형
- key는 **변경 불가능한** 자료형(str, int, float, tuple, range)만 사용 가능
    - 이유 : 키 값에 할당된 값이 무엇인지를 확인하는 것. 하지만 해당 키 값이 변경되거나 중복된다면 파이썬이 어느 value를 데려와야 할지 모르기 때문에 불가능
- value는 모든 자료형에 사용 가능
- 중괄호 ({})로 표기
- 메서드
    - D.get(k) : 키 k에 연결된 값\
    
    ![image.png](attachment:bdf30413-0330-459e-a7ba-db38ba684be2:image.png)
    
- `D.get(x)`와 `print(my_dict[’x’])`의 차이
    - `D.get(x)`는 해당 키 값이 없을 때 none 반환
    - `print(my_dict[’x’])` : error 발생

### set

- **순서와 중복이 없는** 변경 가능한 자료형
- 수학에서의 집합과 동일한 연산 처리 가능
- 중괄호 ({}) 표기
- 비어있는 세트 생성 시 `set()`

```python
# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}
# 차집합
print(my_set_1 - my_set_2)  # {1, 2}
# 교집합
print(my_set_1 & my_set_2)  # {3}
```

- 메서드
    - s.add(x) : 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 x
    - s.remove(x) : 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 key error

## Other Types

### None

- 파이썬에서 ‘값이 없음’을 표현하는 자료형

### Boolean

- 참과 거짓을 표현하는 자료형
- 비교 / 논리 형태
- 첫 글자만 대문자

## ⭐복사

- 파이썬에서는 데이터에 분류에 따라 복사가 달라짐
- **‘변경 가능한 데이터 타입’**과 **‘변경 불가능한 데이터 타입’**을 다르게 다룸

### **변경 가능한 데이터 타입**

```python
a = [1, 2, 3, 4]
b = a
b[0] = 100
print(a)  # [100, 2, 3, 4]
print(b)  # [100, 2, 3, 4]
```

→ a가 바라보고 있는 대상이 b도 동일한 곳을 바라보고 있기 때문에 둘 다 바뀜

### **변경 불가능한 데이터 타입**

```python
a = 20
b = a
b = 10
print(a)  # 20
print(b)  # 10
```

### 복사 유형

1. 할당 (Assignment)
    1. 할당 연산자(=)를 통한 복사는 해당 객체에 대한 **객체 참조를 복사**
    2. 하나 바뀌면 같이 바뀜
2. 얕은 복사 (Shallow copy)
    1. 슬라이싱을 통해 복사
    2. `b = a[:]`
    
    ```python
    # 얕은 복사
    a = [1, 2, 3]
    b = a[:]
    print(a, b)  # [1, 2, 3] [1, 2, 3]
    b[0] = 100
    print(a, b)  # [1, 2, 3] [100, 2, 3]
    ```
    
    - 한계
        - 2차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우
        - 할당과 동일한 문제 발생
        
        ```python
        # 얕은 복사의 한계
        a = [1, 2, [1, 2]]
        b = a[:]
        print(a, b)  # [1, 2, [1, 2]] [1, 2, [1, 2]]
        b[2][0] = 100
        print(a, b)  # [1, 2, [100, 2]] [1, 2, [100, 2]]
        ```
        
3. 깊은 복사 (deepcopy)
    - 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
        
        ```python
        # 깊은 복사
        import copy
        original_list = [1, 2, [1, 2]]
        deep_copied_list = copy.deepcopy(original_list)
        deep_copied_list[2][0] = 100
        print(original_list)  # [1, 2, [1, 2]]
        print(deep_copied_list)  # [1, 2, [100, 2]]
        ```
        

## Type Conversion

### 암시적 형변환

- 파이썬이 자동으로 형변환 하는 것
- Boolean과 Numeric Type에서만 가능

### 명시적 형변환

- 개발자가 직접 형변환 하는 것
- 암시적 형변환이 아닌 경우 모두 포함

![image.png](attachment:cf574400-0c41-4c15-905e-791e769aaeb8:image.png)

## Operator

![image.png](attachment:88aa6e19-f291-443e-8a87-0d180f7151ed:image.png)

![image.png](attachment:3d04b67c-1362-48c5-93da-489dffd6db05:image.png)

- is 비교 연산자
    - is는 식별성

### 논리 연산자

![image.png](attachment:ca62b495-877a-477c-b201-9f4a6903cd80:image.png)

### 단축 평가

- 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

### 멤버십 연산자

- 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부 확인
- in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지 확인
- not in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인

### 시퀀스형 연산

![image.png](attachment:c35d3d64-ba2a-46be-9b29-89def7c7b393:image.png)

## 제어문 (Control Statement)

- 코드의 실행 흐름을 제어하는 데 사용되는 구문
- 조건에 따라 코드 블록을 실행하거나 반복적으로 코드 실행
- 조건문 : if, elif, else
- 반복문 : for, while
- 반복문 제어 : break, continue, pass

![image.png](attachment:a8a2b3ca-0511-4007-b6ca-40f404e3005e:image.png)

### List Comprehension

- 간결하고 효율적인 리스트 생성 방법
- `[expression for 변수 in iterable]`
- `list(expression for 변수 in iterable)`

## 함수

### 함수의 구조

- input을 받아서 로직에 맞게 실행한 결과를 output으로 출력

### 특징

- def 키워드를 사용하여 정의
- 일급 객체
    - 함수가 변수에 할당될 수 있음
    - 함수가 다른 함수의 인자로 전달 가능
    - 함수가 다른 함수에 의해 반환 가능
- 익명 함수로 사용 가능(람다 표현식)

![image.png](attachment:318d9c2b-c072-4175-8b75-1139821e14c4:image.png)

### 매개변수 (parameter)

- 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

### 인자 (argument)

- 함수를 호출할 때, 실제 전달되는 값

![image.png](attachment:9b7e327d-ef59-40e4-9964-95992958fe6a:image.png)

### 다양한 인자 종류

1. 위치 인자 (Positional Arguments)
    1. 함수 호출 시 인자의 위치에 따라 전달되는 인자
    2. 위치인자는 함수 호출 시 반드시 값 전달해야 함.
2. 기본 인자 값(Default Argument Values)
    1. 함수 정의에서 매개변수에 기본 값을 할당하는 것
    2. 함수 호출 시 인자 전달하지 않으면 기본값이 매개변수에 할당
3. 키워드 인자 (Keyword Arguments)
    1. 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
    2. 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
    3. 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
    4. **단, 호출 시 키워드 인자는 인자 뒤에 위치해야 함** 
    
    → 항상 positional arguments 뒤에 넣어야 한다 .
    
4. 임의의 인자 목록 (Arbitrary Arguments Lists)
    1. 정해지지 않은 개수의 인자를 처리하는 인자
    2. 함수 정의 시 매개변수 앞에 ‘*’를 붙여 사용하며, 여러 개의 인자를 **tuple**로 처리
    
    ```
    # Arbitrary Argument Lists 
    def calculate_sum(*args):
        print(args)
        total = sum(args)
        print(f'합계: {total}')
    calculate_sum(1, 2, 3)
    ```
    
5. 임의의 키워드 인자 목록 (Arbitrary Keyword Arguments Lists)
    1. 정해지지 않은 개수의 키워드 인자 처리하는 인자
    2. 함수 정의 시 매개변수 앞에 ‘**’를 붙여 사용하며, 여러 개의 인자 **dictionary**로 묶어 처리
    
    ```python
    # Arbitrary Keyword Argument Lists 
    def print_info(**kwargs):
        print(kwargs)
    print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30}
    ```
    

### 함수 인자 권장 작성 순서

- 위치 → 기본 → 가변 → 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란 줄이기
- 단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정 가능

## Packing & Unpacking

### Packing

- 여러 개의 값을 하나의 변수에 묶어서 담는 것
- 변수에 담긴 값들은 튜플 형태로 묶임
- ‘*’ 는 남은 요소들을 리스트로 패킹하여 할당

### Unpacking

- 패킹된 변수의 값을 개별적인 변수로 분리하여 할당
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
- ‘*’ 는 리스트의 요소를 언패킹하여 인자로 전달
- ‘**’ 는 딕셔너리 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달

## 람다 표현식 (Lambda expressions

- 익명 함수를 만드는 데 사용되는 표현식
    - 한 줄로 간단한 함수 정의
- lambda 키워드
    - 람다 함수를 선언하기 위해 사용되는 키워드
- 매개변수
    - 함수에 전달되는 매개변수들
    - 여러 개의 매개변수가 있을 경우 쉼표로 구분
- 표현식
    - 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성

## 🚨참고

### map

### zip

### style guide

- 코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장 사항들의 모음
- 변수명은 무엇을 위한 변수인지 직관적인 이름을 가져야 함
- 공백 4칸을 사용하여 코드 블록 들여쓰기
- 한 줄의 길이는 79자로 제한하며, 길어질 경우 줄 바꿈 사용
- 문자와 밑줄(_)을 사용하여 함수, 변수, 속성의 이름 작성
- 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄 추가

### enumerate(iterable, start = 0)

- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')
```

### 함수와 scope

- 함수의 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
    - global scope : 코드 어디에서든 참조 가능한 공간
    - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
- variable
    - global variable : global scope에 정의된 변수
    - local variale : local scope에 정의된 변수

### 변수 수명주기

- built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
- global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
- local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### LEGB Rule 예시

1. Local scope : 지역 범위
2. Enclosed scope : 지역 범위 한 단계 위 범위
3. Global scope : 최상단에 위치한 범위
4. Built-in scope : 모든 것을 담고 있는 범위 

→ 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정 불가

### global 키워드

- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
- 매개변수에는 사용 불가
- global 키워드 선언 전에 참조 불가

### 정리

![image.png](attachment:5baecd7d-ed93-4c0e-b544-8560ac55356a:image.png)

# 질문

## 1. 키워드 인자

```python
# Keyword Arguments
def greet(name, age, greeting='hello'):
    print(f'안녕하세요, {name}님! {age}살이시군요.{greeting}')
greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet('Dave','hello',age=35)
```

해당 함수의 매개변수를 추가해서 임의로 조정해봤습니다

마지막 줄의 함수 호출의 경우 typeError가 발생하는데 이유가 궁금합니다.

`TypeError: greet() got multiple values for argument 'age’`

맨 앞의 인자를 키워드 인자로 사용하고 싶을 때에는 어떤 방식을 사용해야 하는지도 궁금합니다.

### 답변

1. 위와 같은 경우, age 혹은 name등을 키워드 인자로 값을 전달하고자 한다면, positional 인자의 순서를 해치지 않을 수 있도록, 필요한 경우들의 모든 요소들을 키워드 인자로 전달하여야 합니다.
- > 따라서, 매개변수를 정의 할 때, 추후 호출되는 시점에 어떤 값들을 키워드 인자로 전달해야 할 지를 고려하여 정의할 필요가 있습니다.

기본인자로 정의하였으므로 생략은 가능합니다.
`greet('Alice', age=30)`

`TypeError: greet() got multiple values for argument 'age’` 오류 메시지에서 볼 수 있듯

현재 age 매개변수에 여러개의 인자가 전달되어 문제가 발생하는 것입니다.

## 2. map

map object로 반환한다고 하였는데 map object가 무엇을 의미하는지 궁금합니다.

### 답변

1. map object에서 이야기하는 map object는 오늘 수업에서 다뤘던 list, str, range 등과 완전히 동일한 개념입니다.

1. 1. map object에서 이야기하는 map object는 오늘 수업에서 다뤘던 list, str, range 등과 완전히 동일한 개념입니다.
- > map 이라는 파이썬에서 제공하는 객체 타입중에 하나입니다.

Python

```
 print(type(range(3)))
# class 'range'>
```

예로 위와 같이 range의 type을출력하면 `range` 가 나오듯

Python

```
obj = map(int, [1, 2, 3])
print(type(obj))
# <class 'map'>
```

map의 실행 결과의 type을 출력하면 map을 반환합니다.

- > 근데 이상태로는 쓰는데는 문제없지만 눈으로 보기엔 불편하므로 list로 형변환 하여 사용하는 편입니다.

## 3. global 키워드

global 키워드의 경우 함수 내에서 전역변수의 값을 바꿀 때 사용하는 키워드가 맞나요?
전역변수는 어디서든지 사용이 가능한 변수라고 알고 있는데
함수 내에서 해당 변수를 사용은 가능하지만 값을 바꾸려면 global 키워드를 사용해야 한다 정도로 이해하면 될까요

### 답변

정확합니다