from django.db import models

from users.models import UserProfile

# Create your models here.


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.OneToOneField(
        UserProfile, verbose_name='购买人', on_delete=models.CASCADE)
    total_price = models.FloatField(verbose_name='总价')

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id
