# Generated by Django 4.2.4 on 2023-09-14 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0018_hauptuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='offre',
            name='Offre_img',
            field=models.ImageField(default='/media/WIN_20230411_04_14_39_Pro.jpg', upload_to=''),
        ),
    ]
