from csv import list_dialects
from django.contrib import admin
from .models import addtech, user1,addgit

# Register your models here.

@admin.register(user1,addtech,addgit)
class useradmin(admin.ModelAdmin):
    list_dis = ('id','name','password')