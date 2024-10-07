from django.contrib import admin
from .models import Student, Lecturer, CollegeUser


@admin.register(CollegeUser)
class CollegeUserAdmin(admin.ModelAdmin):
    list_display = ['student_profile', 'user_id', 'is_active', 'last_login']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'programme', 'email', 'date_of_birth']


admin.site.register(Lecturer)
