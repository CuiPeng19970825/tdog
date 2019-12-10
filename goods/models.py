from django.db import models

# Create your models here.


class Good(models.Model):
    id = models.CharField(max_length=100, verbose_name='id', primary_key=True)
    name = models.CharField(max_length=100, verbose_name='商品名称')
    price = models.FloatField(verbose_name='单价')

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
