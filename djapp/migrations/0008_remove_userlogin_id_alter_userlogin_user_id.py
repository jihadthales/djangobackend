# Generated by Django 4.2.4 on 2023-08-31 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0007_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='id',
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='user_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
