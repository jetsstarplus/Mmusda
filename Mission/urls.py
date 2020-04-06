from django.urls import path
from . import views

app_name = 'mission'

urlpatterns = [
    path('', views.index, name = 'home' ),
    path('index/', views.index, name = 'index'),
    path('success/', views.success, name = 'success'),
    path('home/', views.home, name = 'home'),
    path('calendar/', views.calendar, name = 'calendar'),
]
