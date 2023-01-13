# board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (require_http_methods,
                                          require_POST,
                                          require_safe, )

from django.contrib.auth.decorators import login_required                                         
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@login_required
# 로그인 해야만 보여야 할 때 사용
# 로그인 하지 않고 접근했을 때 로그인 페이지로 자동으로 넘겨줌
# 그냥 articles/create로 가면 '응 로그인 해야돼' 하고 로그인 페이지로 보내버림
# account.views에서 login 함수 자체에 'next' 값을 받아서 어떻게 처리할건지 결정함 

# forms.py와 연결해서 생각필요

# fields = '__all__'
#  fields all로 하면 댓글에 user도 선택할 수 있고, 글도 선택할수 있어버림;;
# 그래서 exclude로 article과 user를 가려달라고 하는거임
# 근데 이거의 문제는 is_valid()도 그냥 통과해버림
# 그러면 form.save()했을 때 내가 가지고 있는 데이터는 댓글의 내용밖에 없음
# form은 user_id 등등 모든 데이터가 있어야함 (빈 값이면 안됨)
# 결론적으로 그렇기 때문에 form.save(commit=False)로 자동저장 하지 말라고 하는 것임
# 자동저장 하지 않고, 그 상태 그대로 냅둔 후 내가 user_id 등등 정보를 추가해서 커밋하겠다의 논리




@require_http_methods(['GET', 'POST'])
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)        
        if form.is_valid():
             # 완전 저장하려고 하면 NOT NULL 에러 뜨니까, 직전에 멈춰 주세요
             # create의 경우는 form.save()하는 순간에 user_id 정보가 생성된다.
             # 따라서 request.user와 article.user가 같은지 아닌지 확인은 form.save 이후에 가능하다
            article = form.save(commit=False)
            # user 값 할당 (추가)
            article.user = request.user
            # 직접 저장 
            article.save()
            return redirect('board:article_detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'board/form.html', context)

# New article 버튼을 누르는거 자체가 get 요청이잖아
# get일때는 create 화면 자체를 보여줘라 (form.html)
# 요청이 post (form.html에서 'GO' 버튼을 누르는 순간 post 요청으로 간다) 이면 새로운 글을 저장한다.


@require_safe  # GET, (HEAD) 요청만 허용하겠다.
def article_index(request):
    articles = Article.objects.all()
    context = {'articles': articles, }
    return render(request, 'board/index.html', context)


@require_safe  # GET, (HEAD) 요청만 허용하겠다.
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'board/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update_article(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        # 이미 article.user 정보를 가지고 있으니까 create랑 다르게 바로
        # request.user와 article.user를 비교할 수 있음 
        if request.user != article.user:
            return redirect ('board:article_detail', article.pk)
        if request.method=='POST':
            form = ArticleForm(request.POST, instance=article)

            if form.is_valid():
        # 기존에 저장된 user_id 갱신할 필요가 없기때문에 commit=False 필요 X
        # 이미 user_id 데이터 가지고 있음 (create랑 상황이 다르다)
                article = form.save()
                return redirect('board:article_detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        # form 생성시 비어있는 form이 아니라 기존에 찾아놨던 article을 보여준다
        
        context = {'form': form,}
        return render(request, 'board/form.html', context)


# get일때는 내가 이미 쓴 내용을 보여준다
# >> 이말이 '수정'버튼을 누르면 'get' 요청으로 내가 썼던 글을 보여줘야한다는 말임
# 요청이 post (form.html에서 'GO' 버튼을 누르는 순간 post 요청으로 간다) 이면 새로운 글로 (내가 쓴 글로) 바꿔준다.
# 그러니까 결론은 get과 post를 둘다 받아야지 왜냐? 이미 써있는 글도 봐야하고 (get), 새로운 글을 다시 업데이트 해야하니까 (post)

@login_required
@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
        return redirect('board:article_index')
    else:
        return redirect('board:article_detail', article.pk)

@login_required
@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    
    if form.is_valid():
        # 완전 저장하려고 하면 NOT NULL 에러 뜨니까, 직전에 멈춰 주세요.
        comment = form.save(commit=False)
        # 나머지는 직접 할게요
        comment.user = request.user
        comment.article = article
        comment.save()

    return redirect('board:article_detail', article.pk)

    # 댓글 작성은 detail 페이지에 들어가는 순간 작성하는 공간 (content)이 있음
    # 따라서 페이지 이동이 필요 없음
    # 그러므로 get 요청으로 받을 필요가 없음
    # 그리고 저장도 사실 get으로 할 수 있으나,
    # get으로 저장하는 순간 1) url에 다보여서 보안 불가임
    # 그러니까 통상 db를 저장 혹은 변경하는것은 post로 하는 것이 국룰이다 

@login_required
@require_POST
def delete_comment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = get_object_or_404(Article, pk=article_pk)
    # 2중 보호, html에서 안된다고 했는데 찾아내서 하는 사람들을 막기 위함
    if request.user == comment.user:
        comment.delete()
    return redirect('board:article_detail', article.pk)
