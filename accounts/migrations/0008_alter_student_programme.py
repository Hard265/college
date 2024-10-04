# Generated by Django 5.1.1 on 2024-10-04 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_alter_student_programme"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="programme",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.programme"
            ),
        ),
    ]
