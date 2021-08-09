from django.contrib import admin
from .models import Employee

admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')