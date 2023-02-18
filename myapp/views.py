from django.shortcuts import render, redirect

# Create your views here.

def BaseView(request):
    return render(request, 'myapp/home.html')
    
