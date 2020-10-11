from django import forms
from .models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(
        label='Поїзд',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Введіть номер поїзда'}))
    from_city = forms.ModelChoiceField(
        label='Звідки',
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'placeholder': 'Звідки'}))
    to_city = forms.ModelChoiceField(
        label='Куди',
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'placeholder': 'куди'}))
    travel_time = forms.IntegerField(
        label='Час в дорозі',
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Час в дорозі'}))

    class Meta(object):
        model = Train
        fields = ('name', 'from_city', 'to_city', 'travel_time')