# Generated by Django 3.1 on 2021-09-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0008_auto_20210919_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='amenity',
            field=models.ManyToManyField(related_name='amenity', to='enroll.Amenity'),
        ),
    ]
