from django.contrib import admin
from .models import *


class FoodDeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'food_name', 'food_price',
                    'food_quantity', 'food_delivery_date')


admin.site.register(Employee)
admin.site.register(Dish)
admin.site.register(Order)
