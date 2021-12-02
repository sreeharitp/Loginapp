from django.urls import path,include
from . import views

urlpatterns = [
    path('name',views.LoginFn,name='name'),
    path('about',views.DemoFn,name='about'),
    path('login',views.LogFn,name='login')
]