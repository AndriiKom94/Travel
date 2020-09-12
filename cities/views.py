from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from cities.forms import HtmlForm, CityForm
from cities.models import City


def home(request, pk=None):
    #if request.method == 'POST':
    #    print(request.POST)
    #    print('*' * 10)
    #    print(request.POST.get('name'))
    #if pk:
    #    city = City.objects.filter(id=pk).first()
    #    return render(request, 'cities/detail.html', {'object': city})
    #cities = City.objects.all()
    #context = {'objects_list': cities, }
    #return render(request, 'cities/home.html', context)
    # if request.method == 'POST':
    #    form = CityForm(request.POST or None)
    #    if form.is_valid():
    #        print(form.cleaned_data)
    #        name = form.cleaned_data.get('name')
    #        city = City(name=name)
    #        city.save()
    # form = CityForm()
    # cities = City.objects.all()
    # context = {'objects_list': cities, 'form': form}
    # return render(request, 'cities/home.html', context)
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


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')