from django.contrib import admin
from .models import CustomUser, Package

admin.site.register(CustomUser)
admin.site.register(Package)
