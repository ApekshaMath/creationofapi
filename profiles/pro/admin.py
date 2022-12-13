from django.contrib import admin
from .models import Pro

# Register your models here.

class ProAdmin(admin.ModelAdmin):
    list = ('full_name','email','phone','country')

admin.site.register(Pro, ProAdmin)
