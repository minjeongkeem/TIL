# 시퀀스(sequence) 자료형

`시퀀스`는 데이터가 순서대로 나열된 형식

* **주의! 순서대로 나열된 것이 `정렬되었다`라는 뜻은 아니다.**

* 리스트(list)

* 튜플(tuple)

* 레인지(range)

* 문자열(string)

* 바이너리(binary) 

## 리스트

**활용법**
```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 및 `list()` 를 통해 만들 수 있다.

값에 대한 접근은 `list[i]`를 통해 한다.

list()의 경우 형변환 시 주로 사용

* 예제

locations = ['강남', '서초', '송파', '광진', '마포',[1]] 

locations.append('동탄') # 리스트 값 추가


locations.append(1)

locations.append(True)

locations.append([1,2,3])


locations[5] = [1,2,3]

x = locations[5] 

 - 이중리스트 값 변경

locations

x[0] = 2

locations[5][0] = 2 

locations

결과: ['강남', '서초', '송파', '광진', '마포', [2], '동탄', 1, True, [1, 2, 3]]

## `tuple`

**활용법**
```python
(value1, value2)
```

튜플은 리스트와 유사하지만, `()`로 묶어서 표현

그리고 tuple은 수정 불가능(불변, immutable)하고, 읽을 수 밖에 없다.

직접 사용하기 보다는 파이썬 내부에서 사용.

* 예제
  
1. a = 1, 2, 3

결과: (1, 2, 3) - 튜플로 묶어서 처리

##  `range()`

`range` 는 숫자의 시퀀스를 나타내기 위해 사용

기본형 : `range(n)` 

n : 인자

함수 : 인자를 넘긴다


> 0부터 n-1까지 값을 가짐


범위 지정 : `range(n, m)` 

> n부터 m-1 (m 미만) 까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다 - 양수

> n부터 m+1까지 -s만큼 감소한다 - 음수


## 시퀀스에서 활용할 수 있는 연산자/함수 

|operation|설명|
|---------|---|
|x `in` s	|containment test|
|x `not in` s|containment test|
|s1 `+` s2|concatenation|
|s `*` n|n번만큼 반복하여 더하기
|`s[i]`|indexing|
|`s[i:j]`|slicing|
|`s[i:j:k`]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|

* list[x:y] -> idx x ~ idx y-1
* list[x:y:z] -> idx x ~ idx y-1 인데, step z
* list[x::z] -> idx x ~ 끝까지, step z
* list[::z] -> 처음부터 끝까지, step z
* list[x:y:] -> idx x ~ idx y-1, step 1
* list [::] -> 그대로 

# set, dictionary

`set`은 순서가 없는 자료구조

-> 시퀀스가 아님

`dictionary`는 아이템이 삽입되는 순서를 가지고 있음

## `set`

* 세트는 수학에서의 집합과 동일하게 처리된다. 

* 세트는 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없다.

* 빈 집합을 만들려면 `set()`을 사용해야 합니다. `{}`로 사용 불가능.

**활용법**
```python
{value1, value2, value3}
```

|연산자/함수|설명|
|---|---|
|a `-` b|차집합|
|a `\|` b|합집합|
|a `&` b|교집합|
|a`.difference(b)`|차집합 (메서드)|
|a`.union(b)`|합집합 (메서드)|
|a`.intersection(b)`|교집합 (메서드)|

## `dictionary`

**활용법**
```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

|메소드명|설명|
|---|---|
|`.keys()`|key 확인|
|`.values()`|value 확인|
|`.items()`|key, value 확인|

* 딕셔너리는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조이다. 
* `{}`를 통해 만들며, `dict()`로 만들 수도 있다.
* `key`는 불변(immutable)한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)
* `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.


* 예시

phone_book = {'서울' : '02', '경기': '031', '경주' : '053'}

print(phone_book)

phone_book['서울'] 

 - key값으로 value값 접근
  
 - 결과: {'서울': '02', '경기': '031', '경주': '053'}

 - value 변경

 - phone_book['경주'] = '054'
 
 - phone_book

 - 결과: {'서울': '02', '경기': '031', '경주': '054'}

 - value 추가

 - phone_book['부산'] = '051' 
  
 - phone book에 '부산'이라는 key, value가 없으니 추가

 - 결과: {'서울': '02', '경기': '031', '경주': '054', '부산': '051'}

