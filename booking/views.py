from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Booking
from services.models import Service
from accounts.models import Address

# Create your views here.

@login_required
def create_booking(request, service_id):

    service = get_object_or_404(Service, id=service_id)
    addresses = Address.objects.filter(user=request.user)

    if request.method == "POST":
        address_id = request.POST.get("address")

        # ensure address belongs to user
        address = get_object_or_404(
            Address,
            id=address_id,
            user=request.user
        )

        Booking.objects.create(
            customer=request.user,
            service=service,
            address=address,
            scheduled_date=request.POST.get("scheduled_date"),
            scheduled_time=request.POST.get("scheduled_time"),
            notes=request.POST.get("notes", ""),
            status=Booking.Status.PENDING
        )
        return redirect("customer_dashboard")

    return render(request, "booking/booking_page.html", {
        "service": service,
        "addresses": addresses
    })



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