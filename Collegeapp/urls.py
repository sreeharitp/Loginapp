from django.urls import path,include
from . import views

urlpatterns = [
    path('emea',views.LogFn,name='emea')
]