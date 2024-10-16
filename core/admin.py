from django.contrib import admin
from .models import Programme, Course, Exam, Result

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "description")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "programme", "description")


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'semester')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'exam', 'percentage', 'marks_obtained', 'total_marks')
