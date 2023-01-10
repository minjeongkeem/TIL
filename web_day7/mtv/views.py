from django.shortcuts import render, redirect
from .models import Article


def index(request):
    # home - 전체 목록을 다 볼 수 있어야 함
    articles = Article.objects.all()
    content = {'articles':articles, }
    return render(request, 'mtv/index.html', content)

def detail(request, article_pk):
    # detail - 한 개의 pk 번호의 상세 목록을 볼 수 있어야 함
    article = Article.objects.get(pk=article_pk)
    content = {'article': article,}
    return render(request, 'mtv/detail.html', content)

def new(request):
    # new - 새로운 글 작성을 위한 페이지로 이동이 필요함
    return render(request, 'mtv/new.html')

def create(request):
    # create - 새로운 글 작성을 위한 작업 함수 
    # 새로운 글 작성을 위해선 새로운 객체 생성 필요
    # 각 db column에 맞게 request해서 데이터를 받아옴 
    # 객체 저장
    # 작성이 끝났으면 작성된 내용이 무엇인지 볼 수 있는 detail 페이지로 이동
    article = Article()
    article.subject = request.POST['subject']
    article.description =request.POST['description']
    article.save()
    return redirect('mtv:detail', article.pk)

def edit(request, article_pk):
    # edit - 기존의 글 수정/삭제 하는 페이지로 이동
    # 이동을 위해선 기존 페이지 선택이 필요
    article = Article.objects.get(pk=article_pk)
    content = {'article': article,}
    return render(request, 'mtv/edit.html', content)

def update(request, article_pk):
    # update - 기존의 글 수정을 위한 작업 함수 
    # 기존의 글 수정을 위해선 기존 페이지 선택 필요
    # 각 db column에 맞게 수정 데이터들을 request해서 데이터를 받아옴
    # 객체 저장
    # 수정이 끝났으면 수정된 내용이 무엇인지 볼 수 있는 detail 페이지로 이동
    article = Article.objects.get(pk=article_pk)
    article.subject = request.POST['subject']
    article.description = request.POST['description']
    article.save()
    return redirect('mtv:detail', article.pk)

def delete(request, article_pk):
    # delete - 기존의 글 삭제를 위한 작업 함수
    # request를 POST로 한 경우에만 진행
    # 기존의 글 삭제를 위해 페이지 선택 필요
    # 삭제가 완료된 목록을 볼 수 있는 home으로 이동
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        article.delete()
        return redirect('mtv:index')