# Generated by Django 2.2.24 on 2022-05-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190829_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Новостройка'),
        ),
    ]
