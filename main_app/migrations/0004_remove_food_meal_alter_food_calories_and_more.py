# Generated by Django 4.1.2 on 2022-10-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_food_meal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='meal',
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbohydrates',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='fiber',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
