from django.contrib import admin
from .models import Programme, Course


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "description")


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "programme", "description")


admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Course, CourseAdmin)
