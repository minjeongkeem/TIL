# 식별자

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)이다.

* 식별자의 이름은 영문알파벳(대문자와 소문자), 밑줄(_), 숫자로 구성된다.
* 첫 글자에 숫자가 올 수 없다.
* 길이에 제한이 없다.
* 대소문자(case)를 구별한다.
* 아래의 예약어는 사용할 수 없다. 

```
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

* 내장함수나 모듈 등의 이름으로도 만들면 안됨. -> 되지만 쓰지 않기를 권고 

```
Print, str, del 등
```

# 변수(variable) 및 자료형

* 값의 종류 - number (int, float, complex) / boolean (True or False) / None / String

* 변수는 `=`을 통해 할당(assignment) 된다. 

* 해당 자료형을 확인하기 위해서는 `type()`을 활용한다.

* 해당 값의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.

* CPU - 손: 일처리가 빠르다

* RAM - 책상: 많이 올려둘 수 있다

* 메모리에 직접 할당 혹은 할당 변경 > C/C++/Go만 가능

* del > 다른 것을 할당하는게 아닌 연결을 끊어냄

* 100과 '100'은 다르다 


## swap

### 1st way
x = 1

y = 2

* y를 1로, x를 2로 바꿔보자.
* 추가 변수도 쓰지 않는다.

* z = x 
* x = y
* y = z

x,y = y,x

print(x, y)

## 2nd way

* x, y를 바꾸되
* 추가 변수도 쓰지 않느다.
* 위에 코드도 사용하지 않는다.

 x = 1

 y = 2
* print (x, y)

* x = x + y >  x:3, y:2
* y = x - y > x:3, y:1
* x = x - y > x:2, y:1

print (x, y)

## 3rd way

x, y = y, x

## bool
* 파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있습니다.

* 비교/논리 연산을 수행 등에서 활용됩니다.

* 다음은 `False`로 변환됩니다.
```
0, 0.0, (), [], {}, '', None
```

## 문자형(String)

### 기본 활용법

* 문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능

    - 작은따옴표: `'"큰" 따옴표를 담을 수 있습니다'`

    - 큰따옴표: `"'작은' 따옴표를 담을 수 있습니다"`

    - 삼중 따옴표: `'''세 개의 작은따옴표'''`, `"""세 개의 큰따옴표"""`
  
### 이스케이프 시퀀스

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분

|<center>예약문자</center>|내용(의미)|
|:--------:|:--------:|
|\n|줄 바꿈|
|\t|탭|
|\r|캐리지리턴|
|\0|널(Null)|
|\\\\|`\`|
|\\'|단일인용부호(`'`)|
|\\"|이중인용부호(`"`)|

### String interpolation 

* name = ooo

* `%-formatting` 
  - (ex) '안녕하세요 저는 %s입니다' % name

* [`str.format()` ](https://pyformat.info/)
  - (ex) '안녕하세요 저는 {}입니다'.format(name)

* [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 이후 버전에서 지원
  - (ex) f'안녕하세요 저는 {name}입니다.'

## 연산자

### 비교 연산자

`=`은 항상 뒤에 있음!

|연산자|내용|
|----|---|
|`<`|미만|
|`<=`|이하|
|`>`|초과|
|`>=`|이상|
|`==`|같음|
|`!=`|같지않음|
|`is`|객체 아이덴티티|
|`is not`|부정된 객체 아이덴티티|

### 논리 연산자

|연산자|내용|
|---|---|
|a and b|a와 b 모두 True시만 True|
|a or b|a 와 b 모두 False시만 False|
|not a|True -> False, False -> True|

* print(not 0) == not bool(0) > `True`

### 단축평가 (Short Circuit Evaluation)
* 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않음
* 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상

* print('a' or 'b') # bool('a') 
  - True -> a만보고 끝남 
  - 답:a

* 10 and 11 
  - 11까지 보고 알았으니까 11 return

## 기타 연산자

### Containment Test

`in` 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있음

* (ex) 'a' in 'aeiou'

* (ex) 1 in [4, 3, 1, 2, 3]

* (ex) 11 in range (12)

### Identity

`is` 연산자를 통해 동일한 object인지 확인할 수 있음

 파이썬에서 -5 부터 256 까지의 id는 동일.

자주 사용하는 숫자 메모리 낭비를 막기 위함

* 257 이후의 id 는 다름.

## 암시적 형변환(Implicit Type Conversion)
사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우

아래의 상황에서만 가능 (내가 원한적 없음)
* bool
* Numbers (int, float, complex)

* (ex) True + 3, False * 100
   - 답: (4, 0)

## 명시적 형변환(Explicit Type Conversion)
위의 상황을 제외하고는 모두 명시적으로 형 변환이 필요

* string -> intger  : 형식에 맞는 숫자만 가능 (문자를 숫자로 바꿀 순 없으므로)
* integer -> string : 모두 가능

암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능

* `int()` : string, float를 int로 변환
* `float()` : string, int를 float로 변환
* `str()` : int, float, list, tuple, dictionary를 문자열로 변환