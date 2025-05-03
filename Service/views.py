from django.shortcuts import render


from .models import Service


def show_service(request):
    all_Service = Service.objects.all()

    context = {
    'serv': all_Service
    }
    return render(request, 'Service/service.html', context)