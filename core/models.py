from django.db import models
from django.conf import settings


class Programme(models.Model):
    name = models.CharField(max_length=100, blank=False,)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False,)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Midterm", "Final"
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField(choices=[(1, "First"), (2, "Second")])

    def __str__(self):
        return f"{self.name} - Year {self.year} - Semester {self.semester}"


class Result(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)

    def name(self):
        return f"{self.student.student_profile}"

    def percentage(self):
        return round((self.marks_obtained / self.total_marks) * 100)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.exam}"
