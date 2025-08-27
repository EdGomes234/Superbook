
from django.urls import path
from .views import HeroListView
from . import views

urlpatterns = [
    path('lista/', views.lista_herois, name='lista_herois'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
]

