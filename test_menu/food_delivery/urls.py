from django.urls import path
from . import views

app_name = 'food_delivery'

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('reportDates/', views.reportDates, name='reportDates'),
    path('report/<date>', views.report, name='report'),
]
