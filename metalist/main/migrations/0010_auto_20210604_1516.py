# Generated by Django 3.1.3 on 2021-06-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210604_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='place',
            field=models.CharField(default='0', max_length=6, verbose_name='Место'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='sector',
            field=models.CharField(default='0', max_length=4, verbose_name='Сектор'),
        ),
    ]