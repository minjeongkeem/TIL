# 조건문(Conditional Statement)

`if` 문은 반드시 **참/거짓을 판단할 수 있는 조건**과 함께 사용

## `if` 조건문의 구성

### 활용법

- **문법**

```python
if <expression>:
    <코드 블럭>
else:
    <코드 블럭>
```

- **예시**

```python
if a > 0:
    print('양수입니다.')
else:
    print('음수입니다.')
```
* `expression`에는 일반적으로 참/거짓에 대한 조건식이 있음

* **조건**이 **참**인 경우 `:` 이후의 문장을 수행

* **조건**이 **거짓**인 경우 `else:` 이후의 문장을 수행

* 여러 개의 `elif` 부가 있을 수 있고(없거나), `else`는 선택적으로 사용

### 주의사항
* 이때 반드시 **들여쓰기** 필요
    - 파이썬에서는 코드 블록을 자바나 C언어의 `{}`와 달리 **들여쓰기**로 판단하기 때문

- **예시 2)**

* 나머지가 참이면 1이고 거짓이면 0이니까 

* boolean 변환 시 0만 빼고 다 True니까

* `boolean` : None, [], () 등 모두 False 처리

```python
num = 4

if num % 2:
    print('홀수입니다.')
else:
    print('짝수입니다.')
```

- **예시 3)**

*  l = [] -> 비어있는 리스트면 boolean 처리시 False이고 비어있지 않다면 True이기 때문


```python
l = []

if l:
    print('안비어있음')
else:
    print('비어있음')
```

- **예시 4)**

* l 리스트의 길이가 0이 아닐때와 0일때 (명시적으로 작성)


```python
l = []

if len(l) != 0:
    print('안비어있음')
else:
    print('비어있음')
```


## `elif` 복수 조건

2개 이상의 조건을 활용할 경우 `elif <조건>:`을 사용한다.

* 조건문은 순서대로 조건식을 검증하므로 순서에 유의


## 조건 표현식(Conditional Expression)

* 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용

* **삼항 연산자(Ternary Operator)**라고 부르기도 한다.

* `삼항 연산자`: 값이 3개 필요함

* if - else 한줄씩 있을 때만 가능함 

---

**활용법**

```python
true_value if <조건식> else false_value
```
* print (궁금한게 맞았을 때) if (내가 궁금한것) else print (아닐 때)


# 반복문(Loop Statement)

- while
- for

## While 반복문
while 문은 조건식이 참(True)인 경우 반복 실행

### 활용법
- **문법**

```python
while <조건식>:
    <코드 블럭>
```

- 예시

```python
while True:
    print('조건식이 참일 때까지')
    print('계속 반복')
```

### 주의사항
* `while` 문 역시 조건식 뒤에 콜론(`:`)이 반드시 필요하며, 이후 실행될 코드 블럭은 **4spaces**로 **들여쓰기** 함
* **반드시 종료조건을 설정해야 함.**

* 예시 1)


```python
menus = ['돈까스', '떡볶이', '닭칼국수', '햄버거', '탕수육']
i = 0
while i < 5:
    print(menus[i])  # 종료 조건이 없다면 i가 0에서만 무한 실행
    i += 1  # 'while문'은 종료 조건이 반드시 필요함, while문이 무한루프에 빠지지 않도록 해줌
print('메롱 이거 안먹을거지롱')
```
* 결과
```
돈까스
떡볶이
닭칼국수
햄버거
탕수육
메롱 이거 안먹을거지롱
```

* 예시 2) 한자리씩 출력

```python
user_num = int(input())
div = 10
result = 0

while user_num > 0:
    result = user_num % div 
    user_num = user_num // div  # 몫 
    print(result)
```
* 결과
```
if user_num == 185:
5
8
1
```
* 다른 방법 (string)
```python
user_num = input()

i = len(user_num) -1

while i >= 0:
    print(user_num[i])
    i-= 1
```

## for 문

for 문은 시퀀스 (string, tuple, list, range)를 포함한 순회가능한 객체 (iterable) 요소들을 순회함

* 예시 1)
  
```python
# 3개의 숫자로 이루어진 리스트
numbers = [1, 2, 3]
mine = [2, 4, 5]

#numbers와 mine이 몇개가 같은지 판별하는 코드 

e = 0

for i in range (len(numbers)):
    if mine[i] in numbers:
        e += 1
print (e)
```

* 결과
```
1
```

### 딕셔너리 순회(반복문 활용)

딕셔너리에 `for` 문을 실행하면 기본적으로 다음과 같이 동작

```python
grades = {'john':  80, 'eric': 90}
1)
for key in grades:
    print(key)
2)
for key in grades:
    print(f'{key} => {grades[key]}')
3)
for x in grades.items():
    print(x) #자료형 튜플임 
4)
for x in grades.items():
    print(x[0], x[1]) #튜플 자료형을 인덱스로 접근
5)
for key, value in grades.items():  #튜플 자료형 자동으로 unpack
    print(key, value)
```
* 결과
  
```python
1)
john => 80
eric => 90
2)
john => 80
eric => 90
3)
('john', 80)
('eric', 90)
4)
john 80
eric 90
5)
john 80
eric 90
```

## 반복제어(`break`, `continue`, `for-else`)

### `break` 

반복문을 종료

* `for` 나 `while` 문에서 탈출

* 예시 1)
  
```python
# 종료 조건이 없는 while 문을 break 를 활용해서 종료시키는 코드
# n의 초기값을 0으로 할당하고,
# 종료조건 없이 n을 1씩 증가시키는 while 반복문 안에서 
# n이 3이 되는 경우에 break되어 반복문을 종료
n = 0
while True:  # 무한루프
    if n == 3:
        break
    print(n)
    n += 1
```
### `pass`와 `continue`의 차이

```python
# pass
# 0부터 4의 범위를 순회하며 출력하는 반복문 안에서
# 3이 나오는 경우 pass 하는 조건문

for num in range(5):
    if num == 3:
        pass
    print(num)
```
* 결과
```python
0
1
2
3
4
```

```python
# continue
# 0부터 4의 범위를 순회하며 출력하는 반복문 안에서 
# 3이 나오는 경우 continue 하는 조건문

for num in range(5):
    if num == 3:
        continue  #3을 프린트하기 전에 하나 더 넘어감
    print(num)
```
* 결과
```python
0
1
2
4
```

### `for-else` 활용

*예시 1)
* numbers 리스트에 4가 있을 경우 `True`를 출력하고, 없을 경우 `False`를 출력한다.
  
```python
numbers = [1, 3, 7, 9]
for number in numbers:
    if number == 4:
        print('True')
        break # for 문 종료 조건
else:
    print('False')
# 결과: False
```