from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def overview(request):
    return render(request, 'accounts/overview.html')

def register(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        user_type = request.POST.get("user_type")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

#       if password != confirm_password:
#            return render(request, "accounts/register.html", {
#                "error": "Passwords do not match"
#            })

        if password != confirm_password:
            return render(request, "accounts/register.html", {
                "error": "Passwords do not match",
                "form_data": request.POST
            })

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            user_type=user_type,
            password=password,
        )

        return redirect("/accounts/login/")

    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')