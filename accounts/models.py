from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

from core.models import Programme, Course


class CollegeUserManager(BaseUserManager):
    def create_user(self, user_id, password=None):
        if not user_id:
            return ValueError('User ID is required')

        user = self.model(user_id=user_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password=None):
        user = self.create_user(user_id, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CollegeUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'

    objects = CollegeUserManager()

    def __str__(self) -> str:
        return f"{self.user_id}"


class Student(models.Model):
    user = models.OneToOneField(
        CollegeUser, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=255, blank=False, null=True)
    programme = models.ForeignKey(
        Programme, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField(Course, max_length=12)
    date_of_birth = models.DateField(blank=False, null=True)

    def __str__(self) -> str:
        return self.name or self.user.user_id


class Lecturer(models.Model):
    user = models.OneToOneField(
        CollegeUser, on_delete=models.CASCADE, related_name='lecture_profile')
    name = models.CharField(max_length=255, blank=False, null=True)


@receiver(post_save, sender=CollegeUser)
def creat_user_profile(sender, instance: CollegeUser, created, **kwargs):
    if created:
        if instance.is_superuser:
            pass
        if not instance.is_superuser and instance.is_staff:
            Lecturer.objects.create(user=instance)
        if not instance.is_superuser and not instance.is_staff:
            Student.objects.create(user=instance)
