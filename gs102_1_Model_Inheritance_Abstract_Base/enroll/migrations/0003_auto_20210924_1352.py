# Generated by Django 3.1 on 2021-09-24 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210924_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itema',
            options={'ordering': ['-created', 'title']},
        ),
    ]
