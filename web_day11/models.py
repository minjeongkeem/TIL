from django.db import models
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=200)
    # 표수
    # 알아서 db 컬럼은 user_id
    # on_delete == 순장 >> 1:N 관계에서 User가 사라지면 얘도 사라진다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Reply(models.Model):
    content = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
