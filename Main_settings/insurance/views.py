from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'dashboard.html')

def maindashboardV(request):
    return render(request,'pages/maindashboard.html')
