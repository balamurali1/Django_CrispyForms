# Generated by Django 3.1 on 2021-09-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20210919_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='state',
            field=models.CharField(max_length=20),
        ),
    ]