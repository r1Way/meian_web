from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Comment
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.unregister(User)
admin.site.register(Comment)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    # can_delete = False
    # verbose_name_plural = 'userprofile'

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]#父类就有的为空 将附加信息内联

admin.site.register(User, UserProfileAdmin)