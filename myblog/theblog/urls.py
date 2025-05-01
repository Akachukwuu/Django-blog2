from django.urls  import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('index', views.index, name='index'),
    path('mainlogin', views.mainlogin, name='mainlogin')
]