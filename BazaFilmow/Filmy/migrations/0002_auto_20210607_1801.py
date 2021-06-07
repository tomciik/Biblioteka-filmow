# Generated by Django 3.2.4 on 2021-06-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filmy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmy',
            name='rok_produkcji',
            field=models.DecimalField(decimal_places=0, default=1990, max_digits=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filmy',
            name='ocena',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
