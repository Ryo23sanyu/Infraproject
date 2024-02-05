from django.contrib import admin
from .models import Infra, Article, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Infra)
admin.site.register(Article)