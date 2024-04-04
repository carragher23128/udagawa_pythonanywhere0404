# Generated by Django 3.1.1 on 2020-09-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_blocked',
            field=models.BooleanField(default=False, help_text='button to toggle employee block and unblock', verbose_name='Is Blocked'),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='button to toggle employee deleted and undelete', verbose_name='Is Deleted'),
        ),
    ]