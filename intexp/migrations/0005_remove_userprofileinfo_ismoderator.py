# Generated by Django 3.2.9 on 2021-11-25 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intexp', '0004_userprofileinfo_ismoderator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='isModerator',
        ),
    ]
