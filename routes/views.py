from django.contrib import messages
from django.shortcuts import render

from .forms import *


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return render(request, 'routes/home.html', {'form': form})
    else:
        messages.error(request, 'Створіть маршрут')
        form = RouteForm
        return render(request, 'routes/home.html', {'form': form})