from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from cities.forms import HtmlForm, CityForm
from cities.models import City


def home(request, pk=None):
    cities = City.objects.all()
    paginator = Paginator(cities, 4)
    page = request.GET.get('page')
    cities = paginator.get_page(page)
    context = {'objects_list': cities, }
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Місто успішно додано!'


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Інформацію оновлено!'


class CityDeleteView(SuccessMessageMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Місто видалено!'
