# Generated by Django 3.1.2 on 2020-11-05 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20201105_0836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
