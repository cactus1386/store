from django.urls import path
from . import views

app_name = 'figours'

urlpatterns = [
    path('', views.first_page, name='firstpage'),
    path('<int:id>/', views.details, name='detail'),
    path('about/', views.about, name='about'),
]

