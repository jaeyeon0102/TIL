# ⭐Classes

## 객체

### 클래스

- 파이썬에서 **타입**을 표현하는 방법
    - 객체 생성하기 위한 설계도
    - 데이터와 기능을 함께 묶는 방법 제공

### 객체

- 클래스에서 정의한 것을 토대로 메모리에 할당된 것
- **속성**과 **행동**으로 구성된 모든 것

### 예시

- 가수
    - 속성(**변수**) : 직업, 생년월일, 국적
    - 행동(**메서드**) : 랩(), 댄스(), 소몰이()

### 클래스와 객체

- 클래스로 만든 객체를 **인스턴스** 라고 부름
- ex) 정수 123은 인스턴스다. 123은 정수의 인스턴스다.
- 클래스(가수)와 객체(아이유)
    - **클래스**를 만든다 == **타입(list)**을 만든다
- “hello”.upper() → 문자열.대문자로() / 객체.행동() / 인스턴스.메서드()

**하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.**

- 123, 900, 5는 모두 int의 인스턴스
- ‘hello’는 모두 string의 인스턴스
- [232, 89, 1], []은 모두 list의 인스턴스

### 객체 정리

1. 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
2. 속성(attribute) : 어떤 상태(데이터)를 가지는가?
3. 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

### Python의 객체와 클래스

**객체(Object) = 속성(Attribute) + 기능(Method)**

## 클래스

### 정의

- class 키워드
- 클래스 이름은 파스칼 케이스(Pascal Case) 방식으로 작성

```python
class MyClass:
	pass
```

## 클래스 구성 요소

### 🚨생성자 함수

- 객체를 생성할 때 자동으로 호출되는 특별한 메서드
- **__init__**메서드로 정의되며, **객체 초기화** 담당
- 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값 설정

**필요한 이유**

- 인스턴스 생성 시 해당 인스턴스에만 필요한 값이 있다면 이를 위해 값을 초기화 함
- __init__ 생성 시 인스턴스 공간 생성(초기화) : name 속성 생성, singing 메서드 생성

```python
# 클래스 정의
class Person: # 클래스
    blood_color = 'red'       # 속성(attribute)  -> 클래스 변수
    def __init__(self, name): # 메서드(함수)   -> 생성자 함수
        self.name = name       # 인스턴스 변수
    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing())  
# 속성(변수) 접근
print(singer1.blood_color)
```

### 인스턴스 변수

- 인스턴스마다 별도로 유지되는 변수
- 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화

### 클래스 변수

- 클래스 내부에 선언된 변수
- 클래스로 생성된 모든 인스턴스들이 공유하는 변수

### 인스턴스 메서드

- 각 인스턴스에서 호출할 수 있는 메서드
- 인스턴스 변수에 접근하고 수정하는 등의 작업 수행

### 인스턴스 변수와 클래스 변수

1. 클래스 변수 활용
    1. 가수가 몇 명인지 확인하고 싶다면?
        1. 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 설정 가능
2. 클래스 변수와 인스턴스 변수
    1. class.class_variable로 클래스 변수 참조하기
    2. 동일하게 사용되는 변수는 클래스변수
    3. 다르게 사용되는 변수는 인스턴스 변수로 참조
    4. 인스턴스가 클래스 변수를 변경 불가능 → 오류는 안나지만 값이 변하진 않음
    5. 클래스 변수를 바꾸고 싶다면? → 클래스가 직접 변경하도록 함 

## 메서드 (함수)

### 인스턴스 메서드

- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스의 상태를 조작하거나 동작 수행
- 반드시 **첫번째 매개변수**로 **인스턴스 자신(self)**를 전달받음
    - self는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능
    - 하지만 다른 이름을 사용하지 않을 것을 강력히 권장
    
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
            print('인스턴스가 생성되었습니다.')
    ```
    

**self 동작원리**

- upper 메서드를 사용해 문자열 ‘hello’ 대문자로 변경하기
    - `‘hello’.upper()`
- 하지만, 실제 파이썬 내부 동작은 다음과 같이 진행됨
    - `str.upper(’hello’)`
- str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것
- 인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기자신인 이유

### 생성자 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값 설정

### 🚨클래스 메서드

- 클래스가 호출하는 메서드
    - 클래스 변수를 조작하거나 클래스 레벨의 동작 수행
- **@classmethod** : 데코레이터를 사용하여 정의  → 해당 메서드가 클래스 메서드임을 정
- 호출 시, **첫 번째 인자**로 해당 **메서드를 호출**하는 **클래스(cls)**가 전달됨
- 첫번째 매개 변수로 클래스 인스턴스가 아닌 클래스 자체가 넘어오게

```python
# 클래스 메서드
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod    #데코레이터 
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')
```

### 정적 메서드

- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
    - 주로 **클래스와 관련이 있지만** **인스턴스와 상호작용이 필요하지 않은 경우**에 사용
- @staticmethod : 데코레이터 사용하여 정의
- 호추 시 필수적으로 작성해야 할 매개변수가 없음
- util 기능 만들려면 자주 사용
- 단순히 문자열을 조작하는 기능을 제공하는 정적 메서드

### 인스턴스와 클래스 간 이름 공간

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스 만들면, **인스턴스 객체**가 생성되고 **독립적인 이름 공간** 생성
- 인스턴스에서 특정 속성에 접근하면, **인스턴스 → 클래스** 순으로 **탐색**

![image.png](attachment:aa7152f3-91d3-4040-9bc8-6570c2a7a72f:image.png)

## 상속

- 상속을 통해 중복되는 함수를 제거하고 계층 구조를 사용한다.

### 클래스 상속

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')
class Professor(Person):  # Person 클래스 상속받음
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
class Student(Person):   # Person 클래스 상속받음
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)
# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()  # 반갑습니다. 박교수입니다.
# 부모 Person 클래스의 talk 메서드를 활용
s1.talk()  # 반갑습니다. 김학생입니다.
```

- 자식 클래스에 부모 클래스와 동일한 함수가 있을 때에는 자식 클래스의 함수가 호출
    - 탐색 순서 : 내가 속해있는 곳이 먼저.

### 다중 상속

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소 활용 가능
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정

```python
# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return f'안녕, {self.name}'
class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'
class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째가 응애'
baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY
```

### 다이아몬드 문제

- 두 클래스 B와 C가 A에서 상속되고 클래스 D가 B와 C 모두에서 상속될 때 발생하는 모호함

**해결책**

- **MRO (Method Resolution Order) 알고리즘**을 사용하여 클래스 목록을 생성
- 부모 클래스로부터 상속된 속성들의 검색을 C3 선형화 규칙에 맞춰 진행
- 계층 구조에서 겹치는 같은 클래스 두 번 검색 x
- 속성이 D에서 발견되지 않으면 B에서 찾고, 거기에서도 발견되지 않으면 C에서 찾는 순으로 진행

```python
# 99_MRO.py
O = object
class D(O): pass
class E(O): pass
class F(O): pass
class B(D,E): pass
class C(F,D): pass
class A(B,C): pass

# A 클래스의 상속 탐색 순서 출력
print(A.__mro__)
```

### super()

- 부모 클래스(또는 상위 클래스)의 메서드를 호출하기 위해 사용하는 내장 함수
- 다중 상속 시 MRO(메서드 결정 순서)를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # Person의 init 메서드 호출
        super().__init__(name, age, number, email)
        self.student_id = student_id
```

## 클래스 참고

### 메서드 주의사항

- 클래스가 사용해야 할 것
    - 클래스 메서드
    - 스태틱 메서드
- 인스턴스가 사용해야 할 것
    - 인스턴스 메서드

### 매직 메서드 (magic method)

- 인스턴스 메서드
- 특정 상황에 자동으로 호출되는 메서드
- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
- 스페셜 메서드 혹은 매직 메서드라고 불림
- 예시
    - __str__(self), __len__(self)__ 등

### 데코레이터 (Decorator)

- 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함

## 참고

### 제너레이터

- 이터레이터를 간단하게 만드는 함수

**사용 이유**

1. 메모리 효율성
    1. 한 번에 한 개의 값만 생성
        1. 값을 하나씩 생성하여 반환하므로, 전체 시퀀스를 한 번에 메모리에 로드하지 않아도 됨
    2. 대용량 데이터 처리
        1. 대용량 데이터셋을 처리할 때 메모리 사용 최소화 가능
        2. 예를 들어, 파일의 각 줄을 한 번에 하나씩 읽어 처리 가능
2. 무한 시퀀스 처리
    1. 무한 시퀀스 생성 : 무한 루프를 통해 무한 시퀀스 생성 가능
    2. 이는 끝이 없는 데이터 스트림 처리 시 유용
3. 지연 평가 (Lazy Evaluation)
    1. 필요할 때만 값 생성
        1. 제너레이터는 값이 실제로 필요할 때만 값을 생성. 이를 통해 불필요한 계산을 피하고 성능 최적화 가능
    2. 연산 지연 
        1. 복잡한 연산을 지연하여 수행할 수 있어, 계산이 필요한 시점에만 연산이 이루어짐

**특징**

- 클래스 기반의 이터레이터 만들 필요없이 __iter__() , __next__() 메서드 자동 생성
- sefl.index 나 self.data 와 같은 인스턴스 변수를 사용하는 접근법에 비교해 함수를 쓰기 쉽고 명료하게 만듦

**이터레이터**

- python 내부적으로 반복이 동작하는 원리
1. 내부적으로 for문이 동작할 때 반복가능한 객체에 대해 iter() 호출
2. iter() 함수는 메서드 __next__()를 정의하는 이터레이터 객체 돌려줌
3. __next__() 메서드는 반복 가능한 객체들의 요소들을 한 번에 하나씩 접근
4. 남은 요소가 없으면 StopIteration 예외를 일으켜 for 반복 종료 알림

 

### 제너레이터와 데이터 분석에서의 활용

- 추후 데이터 분석 시 큰 데이터를 한꺼번에 받아서 (메모리에 올려서) 처리할 수 없는 경우 발생
- 데이터를 개발자가 원하는 양만큼만 가져와서 처리하고, 다시 그 양만큼만 가져와서 처리하는 행위 반복하여 데이터 분석 진행

### 예외처리

- try
    - 예외가 발생할 수 있는 코드 작성
- except
    - 예외가 발생했을 때 실행할 코드 작성
- else
    - 예외가 발생하지 않았을 때 실행할 코드 작성
- finally
    - 예외 발생 여부와 상관없이 항상 실행할 코드 작성
- raise
    - 예외 상황 발생시키기

### 모듈 (import)

- 한 파일로 묶인 변수와 함수의 모음
- 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

### 패키지

- 연관된 모듈들을 하나의 디렉토리에 모아둔 것
- 

### 정규 표현식

- 문자열에서 특정 패턴을 찾기 위해 사용되는 기법
- 복잡한 문자열 속에서 특정한 규칙으로 된 문자열을 검색, 치환, 추출 등을 간결하게 수행할 수 있

![image.png](attachment:60431b73-17c1-44dd-b37b-98abffcd853f:image.png)

![image.png](attachment:8aeb4cf6-7b72-4d97-848a-0ffdae8151b2:image.png)

![image.png](attachment:3e37fbbf-1cf4-42f2-aec9-23ed53261a90:image.png)

# 질문

# **클래스 정의 시험에 나옴,,**

## 1. 다중 상속 super() 사용 예시

__init__에 super()를 사용해서 부모 클래스를 호출한 이유가 궁금해요

해당 코드가 없으면 아래에 있는 child.show_value() 진행 시 

`AttributeError: 'Child' object has no attribute 'value_a'. Did you mean: 'value_c'?`

오류가 발생합니다. 부모 클래스는 해당 클래스 내에서 init 함수로 초기화가 되어있으므로 사용이 가능한거 아닌가요,,,

```python
class Child(ParentA, ParentB):
    def __init__(self):
        # super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()
```

```python
# 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')
class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()
```