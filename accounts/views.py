from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from booking.models import Booking
from django.contrib.auth import logout

User = get_user_model()

# Create your views here.
@login_required
def customer_dashboard(request):

    bookings = Booking.objects.filter(customer=request.user).order_by("-created_at")

    context = {
        "pending": bookings.filter(status=Booking.Status.PENDING),
        "accepted": bookings.filter(status=Booking.Status.ACCEPTED),
        "in_progress": bookings.filter(status=Booking.Status.IN_PROGRESS),
        "completed": bookings.filter(status=Booking.Status.COMPLETED),
        "cancelled": bookings.filter(status=Booking.Status.CANCELLED),
    }
    return render(request, "accounts/customer_dashboard.html", context)

@login_required
def provider_dashboard(request):

    bookings = Booking.objects.filter(service__provider=request.user)

    context = {
        "pending": bookings.filter(status=Booking.Status.PENDING),
        "accepted": bookings.filter(status=Booking.Status.ACCEPTED),
        "in_progress": bookings.filter(status=Booking.Status.IN_PROGRESS),
        "completed": bookings.filter(status=Booking.Status.COMPLETED),
    }
    return render(request, "accounts/provider_dashboard.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")

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
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            if user.user_type == "CUSTOMER":
                return redirect("customer_dashboard")

            elif user.user_type == "SERVICE_PROVIDER":
                return redirect("provider_dashboard")

            else:
                return render(request, "accounts/login.html", {
                    "error": f"User type invalid: {user.user_type}"
                })

        return render(request, "accounts/login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "accounts/login.html")