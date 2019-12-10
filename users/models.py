from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


# Create your models here.
class UserProfile(AbstractUser):
    phone = models.CharField(
        max_length=50, verbose_name='手机', primary_key=True)
    username = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    gender = models.BooleanField(
        '性别', max_length=1, choices=((0, '男'), (1, '女'),), default=0)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email']

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
