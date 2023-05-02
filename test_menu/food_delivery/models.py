from django.db import models


class Employee(models.Model):
    """Модель сотрудника"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    """Модель блюда"""
    name = models.CharField(max_length=100)
    compound = models.TextField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.price}₽: {self.compound}'


class Order(models.Model):
    """Модель заказа"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    dish = models.ManyToManyField(Dish)

    class Meta:
        ordering = ['-date']
