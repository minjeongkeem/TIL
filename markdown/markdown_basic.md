``
# markdown 기초 문법

##### 가장 큰 제목은 1번만 써야함

## Information

### 목적
### Target Audience
### 

## 2번째 큰 제목

### 3번째 큰 제목

#### 4번째 큰 제목

##### 5번째 큰 제목

###### 6번째 큰 제목


## 리스트

### 순서가 있는 리스트 (ordered list)
 1. 손씻기
    1. 물을 튼다
       1. 손을 뻗는다
    2. 물을 적신다
    3. 비누를 칠한다 
 2. 식당에 가기
 3. 밥 먹기
 4. 계산하기
 5. 양치하기
### 순서가 없는 리스트 (unordered list)
- 짜장면
- 짬뽕
- 돈까스
- 김밥 

## 인라인 강조
중요한 것은 **굵게** 표시하고, 주의할 것은 *기울이고*, `코드 혹은 명령어`는 따로 표시하고 싶다.
- 굵게할 때는 *두개로 감싼다(**bold**)
- 이탤릭 체는 *한개로 감싼다(*italic*)
- 코드 강조는 두개로 감싼다(`code`)

---

## 블럭 강조

### 표
파이프로 구분하여 테이블 헤더를 생성한다

|명령어|설명|예시|
|-|-|-|
|`$`|터미널에 명령어 입력 준비| |
|`mkdir`|폴더를 생성한다|`$ mkdir my_dir`|
|`touch`|파일을 생성한다|`$ touch a.txt` |
|`rm`|파일을 삭제한다|`$ rm a.txt` |
|`rm -r`|폴더를 삭제한다 |`$ rm -r my_dir` |
|`ls`|현재 위치 폴더의 모든 하위 항목 표시 |`$ ls`|
|`cd`|폴더 이동 |`$ cd my_dir` |
|`ctrl + l` |터미널 정리(c`l`ear) | |
|`ctrl + c` |취소(`c`ancle)| |
|`~`|홈(Home) 폴더 상징 기호 |`$ cd ~`|
|`/`|최상단(Root) 폴더 상징 기호 |`$ cd /`|
|`.`|현재 위치 상징 기호 |`$ code .`|
|`..`|현재 기준 상위 폴더 상징 기호|`$ cd ..`|


### 코드

아래와 같이 진행한다
```
$ mkdir my_directory
$ cd my_directory
$ touch a.txt
$rm a.txt
```

## 기타
### 인용문

> 일단 유명해져라, 그러면 사람들이 박수를 쳐줄 것이다.
> -김민정

### 수식 블럭
latex - 레이텍

- 인라인 수식 $x + y$
- 블럭 수식

$$
\mathbb{N} = \{ a \in \mathbb{Z} : a > 0 \}
$$

### 이미지 / 하이퍼링크
```
link
[표시 텍스트](링크) 

image
![대체 텍스트](링크)
```

[구글](https://google.com)

![img](https://cdn.travie.com/news/photo/first/201710/img_19975_1.jpg)