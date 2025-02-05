# Generated by Django 2.2 on 2019-11-23 15:04

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_learn_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='课程内容'),
        ),
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程名'),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('course', 'name')},
        ),
    ]
