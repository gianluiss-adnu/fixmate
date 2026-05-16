from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Booking
from services.models import Service
from accounts.models import Address

# Create your views here.

@login_required
def booking_page(request):
    services = Service.objects.all()
    addresses = Address.objects.filter(user=request.user)

    return render(request, "booking/booking_page.html", {
        "services": services,
        "addresses": addresses
    })


@login_required
def create_booking(request):
    if request.method == "POST":

        Booking.objects.create(
            customer=request.user,
            service_id=request.POST.get("service"),
            address_id=request.POST.get("address"),
            scheduled_date=request.POST.get("scheduled_date"),
            scheduled_time=request.POST.get("scheduled_time"),
            notes=request.POST.get("notes", "")
        )

        return redirect("customer_dashboard")

# For provider actions
@login_required
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    booking.status = Booking.Status.ACCEPTED
    booking.save()

    return redirect("provider_dashboard")


@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    booking.status = Booking.Status.CANCELLED
    booking.save()

    return redirect("provider_dashboard")