# Generated by Django 3.1.2 on 2020-11-20 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_post_heaer_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='heaer_image',
            new_name='header_image',
        ),
    ]