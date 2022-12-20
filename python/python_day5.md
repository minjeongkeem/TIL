# 함수와 스코프(scope)

함수는 코드 내부에 스코프(scope)를 생성함

* **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
* **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간


* **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
* **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

* 전역 스코프에서는 지역 스코프의 변수를 참조할 수 없음

1. 함수 밖의 변수(global var), 함수 안의 변수(local var)
    - 인자는 함수 안의 변수 취급한다.
2. 함수 안(local scope)에서는 함수 밖(global scope)에 접근 가능
    - 함수 안에 `a`가 없으면, 함수 밖에서 `a`를 찾아옴
    - 만약, 함수 안에 `a`가 있다면, 함수 밖 `a`는 접근할 수 없음.
3. 함수 밖에서는 함수 안에 접근이 불가능함.

### 변수의 수명주기(lifecycle)


* **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지


* **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때 까지 유지


* **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)

## 이름 검색(resolution) 규칙


* `L`ocal scope: 함수


* `E`nclosed scope: 특정 함수의 상위 함수 


* `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈


* `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
- 예시 
```python
num = 1

def local_scope():
    # num - 이건 함수 내부에서 찾지 말고 밖에 있는거 말하는거야
    global num 
    num = 100 # 밖에 있는 전역 변수 'num'에 100을 넣어버림
    print(num)
    
print(num)
local_scope()
print(num)
```

- 결과
```python
1
100
100
```

-예시2
```python
total = 0
def add_list(*numbers):
    global total
    for num in numbers:
        total += num
        
add_list(1, 2, 3, 4) # None - return이 없으므로
total # 함수 내부에서 바깥에 있는 global 변수에 직접 연산 
```

- 예시3
```python
l = [1]

def func():
    l = [1, 2] # 다른 값을 할당하면 따로 스코프 생성
    print(l)

- 예시 4    
    
func()
print(1)
```

```python
l = [1]

def func():
    ll = l  #  리스트 같은 애들은 할당을 한 것이 아니라면 바깥에 있는 변수에 영향 줌
    ll[0] = 100
    
func()
print(l)
```

## copy 개념
```python
import copy

# shallow -> 1차원 list

l = [1, 2]
c1 = l[:]  #  주소 값으로 참조
c2 = copy.copy(l)

# deep -> 2 차원 혹은 고차원 list

ll = [[1, 2], [3, 4]]

c3 = ll[:]
c4 = copy.copy(ll)

c5 = copy.deepcopy(ll) # ll 리스트 자체에 진짜 그 값을 할당 (복사)해버림
```
## 재귀함수

**자기자신 호출**

- 예시 1: 팩토리얼
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial (n-1)
```

-예시 2: 피보나치
```python
def fib(n):
    if n <= 2:
        return n 
    else:
        return fib(n-1) + fib(n-2)
```

재귀함수보다 for or while 문이 연산 속도 빠름

  ```python
  def fib_loop_2(n):
    
    if n < 2:
        return n
    
    a, b = 0, 1 # 첫번째, 두번째 값을 0과 1로 초기화
    for _ in range(n-1):
        a, b = b , a+b
    return b

    # (ex) n == 3:
    for _ in range(2):
    1. _ == 0
    a, b = b, a + b
    b == 1 -> new_a == 1, a + b == 1
    return b == 1

    2. _ == 1
   a, b = b, a + b
   b == 1, -> new_a == 1 a + b == 2
   return b == 2

   0 1 1 2
    ```
