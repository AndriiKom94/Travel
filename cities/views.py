from django.shortcuts import render
from django.views.generic import DetailView

from cities.models import City


def home(request, pk=None):
    if pk:
        city = City.objects.filter(id=pk).first()
        return render(request, 'cities/detail.html', {'object': city})
    cities = City.objects.all()
    context = {'objects_list': cities, }
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'
