# Generated by Django 3.1 on 2021-09-17 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20210917_1839'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Things',
            new_name='Tag',
        ),
    ]