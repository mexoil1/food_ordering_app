# Generated by Django 4.2 on 2023-05-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0015_alter_dish_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(),
        ),
    ]
