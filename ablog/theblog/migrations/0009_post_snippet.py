# Generated by Django 3.1.2 on 2020-11-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_auto_20201119_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above to Read Blog Post....', max_length=255),
        ),
    ]
