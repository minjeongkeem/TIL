from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# models.py에서 ForeignKey가 User 일 때만, settings.AUTH_USER_MODEL
# 나머지 경우에 User 클래스 필요시 get_user_model()로 접근 
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # user model을 cumstom 했기때문에 클래스 생성 필요(mbti 추가했음)
    first_name = forms.CharField(required=False)
    # required=False >> 선택사항으로 지정하기
    last_name = forms.CharField(required=False)
    # forms.py에 mbti를 CharField로 지정해버리면 selection형태가 안됨
    # mbti = forms.CharField(min_length=4, max_length=4)
    
    class Meta:
        model = User
        # 회원 가입시 필요 정보 custom 가능
        fields = ('username', 'mbti', 'first_name', 'last_name',)