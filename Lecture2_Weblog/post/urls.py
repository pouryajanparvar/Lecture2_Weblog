from django.urls import URLPattern, path
from . import views


app_name = 'post'
urlpatterns = [
    path('', views.home_page, name='home')
]