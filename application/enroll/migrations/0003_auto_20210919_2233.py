# Generated by Django 3.1 on 2021-09-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210919_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='vilage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
