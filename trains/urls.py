from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', TrainCreateView.as_view(), name='add'),
  #  path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
 #   path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
  #  path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
]
