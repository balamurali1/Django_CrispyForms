# Generated by Django 3.1 on 2021-09-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210918_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cus_phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
