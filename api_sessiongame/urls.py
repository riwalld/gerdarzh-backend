
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getSessionGameData),
    #path('', views.test),
    #path('<int:id>', views.getOne),
    #path('Str', views.getProtoCelticStrList),
]