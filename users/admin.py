from django.contrib import admin

from .models import UserProfile
# Register your models here.


class UserProfileManager(admin.ModelAdmin):
    list_display = ['username', 'phone', 'password']
    list_filter = ['username', 'phone']
    search_fields = ['username', 'phone']


admin.site.register(UserProfile, UserProfileManager)
