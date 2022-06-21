from django.contrib import admin
from .models import User, Editor

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','pwd']

@admin.register(Editor)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','body']
