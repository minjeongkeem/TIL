from django.urls import path
from . import views

app_name = 'mtv'

urlpatterns = [
    # mtv/ - home
    path('', views.index, name='index'),
    # mtv/pk번호/ - 상세 페이지
    path('<int:article_pk>/', views.detail, name='detail'),
    # mtv/new/ - 새로운 글 생성을 위한 페이지
    path('new/', views.new, name='new'),
    # mtv/create/ - 새로운 글을 생성하는 업무 자체를 하는 곳
    path('create/', views.create, name='create'),
    # mtv/pk번호/edit/ - 기존의 글 수정/삭제를 위한 페이지
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    # mtv/pk번호/update/ - 기존의 글 수정 업무 자체를 하는 곳
    path('<int:article_pk>/update/', views.update, name='update'),
    # mtv/pk번호/delete/ - 기존의 글 삭제하는 곳
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]
