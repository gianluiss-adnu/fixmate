from django.shortcuts import render

# Create your views here.

# def register(request):
#    return render(request, 'accounts/register.html')

def register_user(request):
    return render(request, 'accounts/register_user.html')

def register_handyman(request):
    return render(request, 'accounts/register_handyman.html')

def login(request):
    return render(request, 'accounts/login.html')