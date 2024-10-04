from django.contrib import admin
from .models import Student, Lecturer, CollegeUser

admin.site.register(CollegeUser)
admin.site.register(Student)
admin.site.register(Lecturer)
