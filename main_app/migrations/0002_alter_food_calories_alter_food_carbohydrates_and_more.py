# Generated by Django 4.1.2 on 2022-10-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbohydrates',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='fiber',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(),
        ),
    ]