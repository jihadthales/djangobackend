# Generated by Django 4.2.4 on 2023-09-10 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0016_rename_madminlogin_madlogin_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Madlogin',
        ),
    ]