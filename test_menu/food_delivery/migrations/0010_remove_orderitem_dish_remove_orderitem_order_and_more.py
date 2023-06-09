# Generated by Django 4.2 on 2023-04-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0009_alter_order_date_remove_orderitem_dish_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='dish',
            field=models.ManyToManyField(to='food_delivery.dish'),
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
