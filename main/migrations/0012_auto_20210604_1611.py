# Generated by Django 3.1.3 on 2021-06-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210604_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='ticket',
            field=models.IntegerField(blank=True, max_length=10, verbose_name='Билеты'),
        ),
    ]
