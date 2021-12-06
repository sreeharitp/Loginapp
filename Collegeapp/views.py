from django.http  import HttpResponse
from django.shortcuts import render

# Create your views here.

def LogFn(request):
    return render(request,'college.html')  