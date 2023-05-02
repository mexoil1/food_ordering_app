from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order



        fields = ['employee', 'date', 'dish']
        labels = {
            'employee': 'Имя сотрудника',
            'date': 'Дата',
            'dish': 'Блюдо',
        }
        widgets = {
            'employee': forms.RadioSelect,
            'date': forms.DateInput(attrs={'type': 'date', 'id': "date"}),
            'dish': forms.CheckboxSelectMultiple(),
        }

