# Generated by Django 3.1.3 on 2021-06-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210604_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name': 'Билет', 'verbose_name_plural': 'Билеты'},
        ),
        migrations.AlterField(
            model_name='tickets',
            name='number',
            field=models.CharField(blank=True, max_length=400, primary_key=True, serialize=False, verbose_name='Номер билета'),
        ),
    ]
