# Generated by Django 5.1.1 on 2024-10-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_student_programme"),
    ]

    operations = [
        migrations.AddField(
            model_name="lecturer",
            name="name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
