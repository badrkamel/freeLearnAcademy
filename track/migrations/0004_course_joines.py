# Generated by Django 2.0.8 on 2019-02-21 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_unit_last_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='joines',
            field=models.PositiveIntegerField(default=0, verbose_name='اجمالي المنضمون'),
        ),
    ]
