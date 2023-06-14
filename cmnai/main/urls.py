from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.first_page, name='test_page'),
    # path('main_page/', views.main_page, name='main_page'),
    path('pose/', views.pose, name='pose'),
    path('hand/', views.hand, name='hand'),

]