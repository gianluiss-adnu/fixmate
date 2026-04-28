from django.shortcuts import render

# Create your views here.
def service_list(request):
    return render(request, 'services/list.html')

def service_detail(request, id):
    return render(request, 'services/detail.html', {'id' : id})