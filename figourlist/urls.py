from django.urls import path
from . import views

app_name = 'figourslist'

urlpatterns = [
    path('product/', views.Page, name='page')
]