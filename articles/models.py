from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model 

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    # 유저모델을 참조하는 방법
    # 1. 직접참조(권장X)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 2. settings의 변수 활용
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 3. get_user_model이라는 내장함수 실행
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)    # 부모가 지워지면 자식요소도 지워진다
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



