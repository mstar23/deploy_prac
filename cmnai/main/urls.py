from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('main_page/', views.main_page, name='main_page'),
]