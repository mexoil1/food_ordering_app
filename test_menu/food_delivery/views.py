from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Dish, Order
from .forms import OrderForm

def index(request):
    dishes = Dish.objects.all()
    form = OrderForm(request.POST)
    context = {
        'form': form,
        'dishes': dishes,
        }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('food_delivery:history')
        else:
            return render(request, 'index.html', context)
    return render(request, 'index.html', context)

def history(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
        }
    return render(request, 'history.html', context)

def reportDates(request):
    dates = Order.objects.values_list('date', flat=True).distinct()
    context = {
        'dates': dates,
        }
    return render(request,'reportDates.html', context)

def report(request, date):
    orders = Order.objects.filter(date=date)
    dishes_count = {}
    total_price = 0
    for order in orders:
        for dish in order.dish.all():
            if dish in dishes_count:
                count += 1
                dishes_count[dish] = {count: int(dish.price) * count}
            else:
                count = 1
                dishes_count[dish] = {count: int(dish.price) * count}
            total_price += int(dish.price)
    context = {
        'orders': orders,
        'dishes_count': dishes_count,
        'total_price': total_price,
        'date': date,
        }
    return render(request,'report.html', context)
