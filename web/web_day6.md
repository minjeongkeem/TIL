# Project 시작

## ENV (가상환경) 설정

- source venv/Scripts/activate >> global이 아닌 자기 내부 폴더에서만 보겠다 (찾겠다) 의미

## DB 모델링 

- 실제 들어올 record먼저 한줄 작성해보기 > Column명으로 대입

## MTV

- Model : Data Base 모델링한다. (더 자세히는 Table / Column명 생성)

- Template : HTML으로 보이는 화면 설정
 
- View : 실제로 어떻게 할 것인지 함수 작성
  - urls.py: view 함수를 실행하기 위한 '주소' 설정


## 1) Model

```
from django.db import models

class Article(models.Model):
    # id는 자동생성됨. 신경 X 
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 생성시 자동으로 채워지도록
    created_at = models.DateTimeField(auto_now_add=True)
    # 생성/수정시 자동으로 채워지도록 
    updated_at = models.DateTimeField(auto_now=True)
```

## 2) CRUD (하고 싶은 것)

## 3) URL Patterns (함수 실행하는 장소 및 결과물 페이지 출력)

(ex) index.html, edit.html 등 

### Create (생성) >> View에서 함수 찾아서 실행

```
from django.shortcuts import render, redirect
from .models import Article

# 글 쓰기 화면 (Create)

def new(request):
    return render(request, 'blog/new.html')

# 글 DB에 실제 저장

def create(request):
    # 새로운 article 객체 생성 (레코드 추가)
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save() # id 생성 시점
    # 뭘 어떻게 할까?
    return redirect('blog:detail', article.pk)
   # return redirect(f'/blog/{article.pk}') 
```
### Read (읽기)

```
# 글 목록 화면 (Read)

def index(request):
    # 글 목록 조회 
    # db/board_article > 모든 레코드 조회
    articles = Article.objects.all()
    context = {'articles': articles,}
    return render(request, 'blog/index.html',context)
    

# 글 상세 화면 (Read)

def detail(request, article_pk):
    # db > articles > 특정 레코드 조회
    article = Article.objects.get(pk=article_pk)
    context = {'article': article,}
    return render(request, 'blog/detail.html', context)
```

### Update (수정)

```
# 글 수정 화면 (Update)

def edit(request, article_pk):
    # 기존 내용을 봐야 수정이 가능함
    article = Article.objects.get(pk=article_pk)
    context = {'article':article,}
    return render(request, 'blog/edit.html', context)

# 실제 글 DB에 실제 저장 

def update(request, article_pk):
    # 기존 article 객체 조회 (레코드 검색)
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save() # id 생성 시점
    # 뭘 어떻게 할까?
    return redirect('blog:detail', article.pk)
```

### Delete (삭제)

```
# 글 삭제 (Delete)

def delete(request, article_pk):
    if request.method == 'POST':
    # 특정 게시글을 지운다.
        article = Article.objects.get(pk=article_pk)
     # 지운다
        article.delete()
    return redirect('blog:index') # 사용자 시나리오에 따라 다름 
```

## Render와 Redirect의 차이점

- Render: 응답의 결과물로 한 페이지를 전달해줌

- Redirect: 응답의 결과물로 새로운 요청을 줌

## GET (내놔) <-> POST (받아)