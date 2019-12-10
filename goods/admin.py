from django.contrib import admin

from .models import Good
# Register your models here.


class GoodManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_filter = ['id', 'name', 'price']
    search_fields = ['id', 'name']


admin.site.register(Good, GoodManager)
