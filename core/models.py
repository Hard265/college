from django.db import models


class Programme(models.Model):
    name = models.CharField(max_length=100, blank=False,)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, blank=False,)

    def __str__(self) -> str:
        return self.name
