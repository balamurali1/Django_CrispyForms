# Generated by Django 3.1 on 2021-09-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stuid',
            field=models.IntegerField(default='no available'),
        ),
    ]
