from django.http  import HttpResponse
from django.shortcuts import render

# Create your views here.
def LoginFn(request):
    return HttpResponse('My name is Sreehari..')
def DemoFn(request):
    return HttpResponse('Sreehari')
def LogFn(request):
    return render(request,'login.html')     