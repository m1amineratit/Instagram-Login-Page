from django.urls import path
from . import views


urlpatterns = [
    path('', views.take_login_informations, name='login')
]