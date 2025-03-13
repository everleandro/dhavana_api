from django.contrib import admin

# Register your models here.
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    list_display_links=['email','first_name','last_name']
    search_fields = ['email', 'first_name', 'last_name']
    list_per_page = 25
    class Meta:
        model = User

admin.site.register(User, UserAdmin)