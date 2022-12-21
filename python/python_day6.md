## 함수 응용

## `map(function, iterable)`

* 양식: map(모두 할 일, 자료들)

* cf) join 메소드

 - 양식: 조인할기준.join(대상)


## `filter(function, iterable)`

* iterable에서 function의 반환된 결과가 `True` 인 것만 반환

## lambda 함수

* 표현식을 계산한 결과 값을 반환하는 함수로, 이름이 없는 함수

* 예시 

```python
def f1(x, y):
    return x + y

f1(1, 2)

# 한줄짜리 함수는 간략하게 만들 수 있다.
# 1. def를 지우고 그 자리에
# 2. lamda라고 쓴다.
# 3. 소괄호와 함수 이름을 지운다.
# 4. : 뒤 엔터와 return 키워드를 지운다.

l = [1, 2, 3]
l[0]

print([1, 2, 3][0])

f2 = lambda x, y: x + y
(lambda x, y: x + y)(1, 2)
# lambda에 묶인 것이 함수 
```

# 데이터 구조

## 데이터 분류 
- 순서가 있는 데이터 구조(Orderd)
    - 문자열
    - 리스트
    - 튜플
- 순서가 없는 데이터 구조(Unorderd)
    - 셋(Set)
    - 딕셔너리(Dictionary)


## 중요 method
- 문자열 변경: `.replace(old, new[, count])`

  - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

  - count를 지정하면 해당 갯수만큼만 시행

- cf> dir 함수 사용 시 해당 컨테이너가 가지고 있는 메서드 확인 가능함
```python
(ex) dir(str) 등
```

- 리스트 변경


`.append(x)`: 리스트 끝에 값 추가, 원본 변경

`.extend(x)`: 리스트에 리스트, 튜플 등의 복수 값 추가 가능, 추가 시 자료형 빼고 값으로만 추가해줌, 문자열의 경우 다 해체해서 한글자씩 추가


`.insert(i, x)`: 정해진 위치 i에 값을 추가 함


`.remove(x)`: 리스트에서 값이 x인 첫번째 항목 삭제, 해당 값이 없을 시 에러

`.pop(x)`: 정해진 위치 x에 있는 값 삭제, 그 항목을 반환함

정해진 위치가 없는 경우 마지막 항목을 리턴하고 삭제함 

`.clear(x)`: 모든 항목 삭제

`.index(x)`: x 값을 찾아서 해당 index 값 리턴

`.count(x)`: 원하는 값의 개수를 반환

`.sort()`: 리스트를 정렬하며, 원본 변경

cf> `sorted()`: 원본 변경 X, 정렬 결과만 리턴해줌
