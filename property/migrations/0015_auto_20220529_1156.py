# Generated by Django 2.2.24 on 2022-05-29 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220529_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat', verbose_name='Квартира, на которую жаловались'),
        ),
    ]
