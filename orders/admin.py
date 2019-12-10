from django.contrib import admin

from .models import Order
# Register your models here.


class OrderManager(admin.ModelAdmin):
    list_display = ['id', 'owner', 'total_price']
    list_filter = ['id', 'owner']
    search_fields = ['id', 'owner']


admin.site.register(Order, OrderManager)
