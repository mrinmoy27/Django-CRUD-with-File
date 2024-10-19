from django.contrib import admin
from . models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile_number', 'date_of_birth', 'photo', 'password']

# Register your models here.
admin.site.register(User, UserAdmin)