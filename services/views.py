from django.shortcuts import render
from .models import Service

# Create your views here.
def service_list(request):
    services = Service.objects.all()

    return render(request, 'services/list.html', {
        'services': services
    })

def service_detail(request, id):
    service = Service.objects.get(id=id)

    return render(request, 'services/detail.html', {
        'service': service
    })


def service_detail_test(request):
    return render(request, 'services/detail.html')