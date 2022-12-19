# 함수(function)

> 특정한 기능(function)을 하는 코드의 묶음

## 함수를 쓰는 이유

- 가독성
- 재사용성
- 유지보수
  
## 함수의 선언과 호출

* 함수의 선언 (정의)은 `def` 키워드를 활용


* `들여쓰기(4spaces)`로 함수의 body(코드 블록)를 작성


* 함수는 `매개변수(parameter)`를 넘겨줄 수도 있음.


* 함수는 동작후에 `return`을 통해 결과값을 전달.
    * 반드시 하나의 객체를 반환 (`return` 값이 없으면, `None`을 반환)


* 함수는 호출은 `함수명()`으로 함. 
    * 예) `func()` / `func(val1, val2)`

---

### 활용법

```python
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```

### 예시

```python
# 선언부 (input 관리)
# input (n) - 선언시 input 값은 (매개변수) 매개변수

def cube(n):  # n = 매개변수 = parameter = 인자 (상황에 따라 정의됨)
    
    # 로직 (주요 기능)
    result = n ** 3
    
    #최종 return 결과
    return result
cube(2)
```

```python
x = cube(2)  # output (result) - 호출 시 input을 부를 때는 인자 (argument) 라고 함
y = cube(100)
print(x, y)
```

### 예시 2)

- 내장함수와 비슷하게 동작하는 my_max 함수를 직접 작성해보기

```python
def 함수이름(숫자a, 숫자b):
    if문을 활용하여 입력 받은 두 숫자 중 큰 수를 리턴.
```

```python
def my_max(a, b):
    if a > b:
        return a
    else:
        return b

def my_max(a, b):
    if a > b:
        result = a
    else:
        result = b
    return result

def my_max(a, b):
    print(3)
    result = a  # 일단 a가 크다고 가정
    
    if b > a:
        retult = b
        
    return result

def my_max(a, b):
    print(4)  # my_max가 실행될 때 print 해야함 
    return a if a > b else b
```

```python
my_max  # 이름만 쓰면 함수 로직에 대해서 알려줌
print(my_max)  # 함수가 실행되는 시점은 '호출'했을 시점임 
```

# 함수의 Output

## 함수의 `return`

-  **오직 한 개의 객체**만 반환됨
- 함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아감
  


### 예시 3) 리스트 비교

```python
def my_list_max(list_a, list_b):
    total_a, total_b = sum(list_a), sum(list_b)  # 같은 연산을 막기 위해서
    if total_a > total_b:
        return list_a
    elif total_a < total_b:
        return list_b
    else:
        return '같음'
```


# 함수의 입력(Input)

## 매개변수(parameter) & 전달인자(argument)

### 매개변수(parameter)

```python
def func(x):
      return x + 2
```

* `x` 는 매개변수(parameter)
* 입력을 받아 함수 내부에서 활용할 `변수`.
* **함수를 정의하는 부분에서 확인 가능.**


### 전달인자(argument)

```python
func(2)
```

* `2` 는 전달인자(argument).
* 실제로 전달되는 `값`
* **함수를 호출하는 부분에서 확인 가능.**

## 함수의 인자

함수는 입력값(input)으로 `인자(argument)`를 넘겨줄 수 있음

### 위치 인자 (Positional Arguments)

기본적으로 인자는 위치에 따라 함수 내에 전달됨

### 기본 인자 값 (Default Argument Values)

**함수를 정의할 때,** 기본값을 지정하여 함수를 호출

---

**활용법**
```python
def func(p1=v1):
    return p1
```

**\*주의\* 단, 기본 인자를 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수 없음.**

### 키워드 인자 (Keyword Arguments)

**함수를 호출할 때** 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자를 전달할 수 있음

**예시**
```python
def greeting(age, name, address, major):
    return f'{name}은 {age}살입니다. 전공은 {major}, 주소는 {address}입니다.'

greeting(20, '밍', '서울', '국통')

greeting(name='밍',age=20,major='국통',address='서울') # 키워드 인자 사용

greeting(20, '밍', major='국통', address='서울') # 위치 인자와 함께 사용
```

## 정해지지 않은 여러 개의 인자 처리

### 가변(임의) 인자 리스트

앞서 설명한 `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 **함수를 정의할 때** 가변 인자 리스트`*args`를 활용

가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현

---

**활용법**

```python
def func(a, b, *args):
```
 `*args` : 임의의 개수의 위치인자를 받음을 의미

보통, 이 가변 인자 리스트는 매개변수 목록의 마지막에 사용

### 예시 4: 가변 인자

- 리스트 내 최댓값 찾기 

```python
def my_max(*n):
    return max(n)
```

```python
def my_max(*numbers):
    max_value = numbers[0]
    for num in numbers:
        # 만약 num 가 max_value 보다 크다면
        if num > max_value:
         # max_value는 까먹고 num 를 기억 
            max_value = num
    return max_value
        # max_value는 지역변수임 (함수 안에서만 호출)
```

### 가변(임의) 키워드 인자

정해지지 않은 키워드 인자들은 **함수를 정의할 때** 가변 키워드 인자 `**kwargs`를 활용

가변 키워드 인자는 **`dict`** 형태로 처리가 되며, 매개변수에 `**`로 표현 

---

**활용법**

```python
def func(**kwargs):
```
> `**kwargs` : 임의의 개수의 키워드 인자를 받음을 의미

### 예시 5
```python
def my_func(a, b=1, *c, **d):
    print(a, b, c, d)

my_func(1)
my_func(1, 2)
my_func(1, 2, True, False, 'a')
my_func(1, 2, True, False, 'a', x=1, y=2, z=3)
```

```python
- 출력 결과
1 1 () {}
1 2 () {}
1 2 (True, False, 'a') {}
1 2 (True, False, 'a') {'x': 1, 'y': 2, 'z': 3}
```

