from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    departure_city = forms.ChoiceField(widget=AjaxInputWidget(
            url='api/city_ajax',
            attrs={'class': 'inline right-margin'}
            ),
            label='Город отправления')
    city_of_arrival = forms.ModelChoiceField(queryset=City.objects.all(), label='Город прибытия')
    flight_date = forms.DateField(widget=forms.SelectDateWidget(), label='Дата')
    pass
