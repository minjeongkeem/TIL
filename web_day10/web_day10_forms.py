# board/forms.py
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        exclude = ('user', )
        # user 이름을 지운채로 만들고 싶음 


class CommentForm(forms.ModelForm):

    content = forms.CharField(min_length=2, max_length= 200, widget=forms.TextInput(attrs={'autofocus': True}))
    class Meta:
        model = Comment
        # fields = ('content', )
        exclude = ('article', 'user', )
        # fields = '__all__'
        # fields all로 하면 댓글에 user도 선택할 수 있고, 글도 선택할수 있어버림;;
        # 그래서 exclude로 article과 user를 가려달라고 하는거임
        # 근데 이거의 문제는 is_valid()도 그냥 통과해버림
        # 그러면 form.save()했을 때 내가 가지고 있는 데이터는 댓글의 내용밖에 없음
        # form은 user_id 등등 모든 데이터가 있어야함 (빈 값이면 안됨)
        # 결론적으로 그렇기 때문에 form.save(commit=False)로 자동저장 하지 말라고 하는 것임
        # 자동저장 하지 않고, 그 상태 그대로 냅둔 후 내가 user_id 등등 정보를 추가해서 커밋하겠다의 논리