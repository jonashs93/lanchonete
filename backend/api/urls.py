from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lanches/$', views.LancheList.as_view(), name='lanche-list'),
    url(r'^ingredientes/$', views.IngredienteList.as_view(), name='ingrediente-list')

]
