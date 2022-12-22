# 객체 지향 프로그래밍 (OOP)

## 객체
- 모든 객체는 타입(type), 속성(attribute), 조작법(method)을 가지고 있음

### 객체의 특징

- **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가? 
- **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
- **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?

## class
- 상위에서 묶고있는 개념 ex) int Class, list Class, Tuple Class 등

- 객체를 만들기 전에 추상적인 개념을 먼저 만드는 것임

- 객체와 인스턴스 유사함

- instance: 개념의 예시로서 실존한다 > '객체'와 비슷..? 

## instance

- 특정 클래스의 실제 데이터 예시 (instance) -> 파이썬에서 모든 것은 객체이며, 모든 객체는 특정 클래스의 인스턴스임

## OOP 기초

### 기본 문법

```python
# 클래스 정의
class MyClass:
    pass

# 인스턴스 생성
my_instance = MyClass()

# 속성 접근
my_instance.my_attribute

# 메서드 호출
my_instance.my_method()

# 일반 변수, 함수명은 전부 소문자에 띄어쓰기가 필요하면 _를 사용 => snake_case

# 클래스명만 첫글자 대문자에 띄어쓰기 필요하면 또 대문자를 사용 => PascalCase, UpperCamelCase
```

## 속성(attribute)과 메서드(method)

| type         | attributes       | methods                                |
| -------------| ---------------- | -------------------------------------- |
| `complex`    | `.real`, `.imag` |              _                          |
| `str`        |       _          | `.capitalize()`, `.join()`, `.split()` |
| `list`       |       _          | `.append()`, `.reverse()`, `.sort()`   |
| `dict`       |       _          | `.keys()`, `.values()`, `.items()`     |

### 속성: 객체의 상태 및 데이터

### 메서드: 특정 객체에게만 소속되어 할 수 있는 행위 (함수)


### 인스턴스 메서드

```python
# 클래스 안에 함수를 만든다 => 인스턴스 메서드

class Person:
    def talk(self):
        print('hi!', id(self))
        
#self => talk 메서드를 호출한 주어
```

### 생성자(constructor) 메서드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 함수
- 반드시 `__init__` 이라는 이름으로 정의

---
**활용법**

```python
class MyClass:
    def __init__(self):
        print('생성될 때 자동으로 호출되는 메서드입니다.')
```

```python
class Person:
    def __init__(self, name, age): 
        self.name = name  # 객체 입장에서 중요한 것은 왼쪽, init은 init 안에 내부 함수로 인하여 return 값 없이 가능함
        self.age = age
    
    def talk(self):
        print(f'안녕 난 {self.name}이야!')  # self(객체) 기준 데이터 접근 가능
        
p = Person('Kim', 20)
p.name, p.age
p.qwer = 100
p.qwer
```

### 소멸자(destructor) 메서드
- 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되는 함수
- `__del__` 이라는 이름으로 정의

---

**활용법**

```python
# 소멸자 정의
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
    
# 소멸자 활용
del 인스턴스

- 생성 > 죽음 > 생성 순 
```

## 클래스(Class) 생성

* 클래스 생성은 `class` 키워드와 정의하고자 하는 `<클래스의 이름>`으로 가능


* 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 데이터는 **속성(attribute)** 정의된 함수는 **메서드(method)**로 부른다.

* 클래스도 객체임 (무언가를 만들어내는 객체)


---

**활용법**

```python
class <클래스이름>:
    <statement>
```

```python
class ClassName:
    statement
```

## 클래스 변수
* 클래스의 속성(attribute)
* 모든 인스턴스가 공유
* 클래스 선언 내부에서 정의
* `클래스.변수명`으로 접근 및 할당

---

**활용법**
```python
class Circle:
    pi = 3.14 # 모든 인스턴스가 공유하는 클래스 변수
    
print(Circle.pi)
```
- 예시

```python
class Circle:
    pi = 3.14  # 모든 인스턴스가 공유하는 클래스 변수
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return self.pi * (self.r ** 2 )  # C3가 pi를 가지고 있지 않음, 부모 pi를 가져옴
    
c1 = Circle(2)
c1.pi = 3.141592  #c1은 본인이 c1.pi를 가지고 있으므로 본인의 pi 참조
c3 = Circle(4)
c3.area()
c1.area()
```

## 이름공간 

- 변수는 LEGB 순으로 찾는다.
- 객체의 상태, 메서드는  instance > class > 상위 class 순으로 찾아본다.

- 예시

```python
a = 100

class Sample:
    a = 1
    
    def func(self):
        b = 2
        return self.a + b  # self 붙은 아이들은 클래스 내부에서만 찾아냄

        # 출력결과: 3
    
    def func(self):
        b = 2
        return a + b  # Global은 아예 바깥 (클래스 바깥)
        
        # 출력결과: 102

s = Sample()
s.func()
```

# OOP의 핵심 개념

- 추상화 (Abstraction)
- 상속 (Inheritance)


**활용법**

```python
class ChildClass(ParentClass):
    <code block>
```

### `super()`

* 자식 클래스에 메서드를 추가로 구현할 수 있음.

* 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있음.

---

**활용법**


```python
class ChildClass(ParentClass):
    def method(self, arg):
        super().method(arg) 
```

- 예시

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)  # 상위 클래스의 init으로 대체한다
        self.student_id = student_id
        
        
p1 = Person('홍교수', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
```

- 다형성 (Polymorphism)

### 메서드 오버라이딩
> Method Overriding(메서드 오버라이딩): 자식 클래스에서 `부모 클래스의 메서드를 재정의`하는 것

* 상속 받은 메서드를 `재정의`할 수도 있음
* 상속 받은 클래스에서 **같은 이름의 메서드**로 덮어쓴다.
* `__init__`, `__str__`의 메서드를 정의하는 것 역시, 메서드 오버라이딩이다.
* 
- 캡슐화 (Encapsulation)

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단: ex> 주민등록번호

### 다중 상속.
* 두개 이상의 클래스를 상속받는 경우
    * 상속 받은 모든 클래스의 요소를 활용 가능
    * 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정
- 예시

```python

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'
    
    def swim(self):
        print('어푸어푸')
        
m1 = Mom('봉미선')
m1.greeting()
m1.swim()


class Dad(Person):
    gene = 'XY'
    
    def walk(self):
        print('성큼성큼')
        
d1 = Dad('신형만')
d1.greeting()
d1.gene

class FirstChild(Dad, Mom):  # 상속의 경우 첫번째 상속 받은게 우선순위임
    def swim(self):
        print('첨벙첨벙')
    def dance(self):
        print('부리부리')
```