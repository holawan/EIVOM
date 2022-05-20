from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
# Register your models here.

class CustomUserAdmin(UserAdmin) :
    ordering = ('email',)
admin.site.register(User,CustomUserAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'nickname', 'birth', 'gender',)


admin.site.register(Profile, ProfileAdmin)
