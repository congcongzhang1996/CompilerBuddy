# Generated by Django 2.2 on 2019-11-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='file_path',
            field=models.CharField(default='users_file/default_user/', max_length=50, verbose_name='用户文件夹路径'),
        ),
    ]
