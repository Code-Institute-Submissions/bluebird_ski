from django.shortcuts import render, get_object_or_404
from .models import Service, Category
# Create your views here.


def all_services(request):
    ''' A view to show all services '''

    services = Service.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = [request.GET['category']]
            services = services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'services': services,
        'current_categories': categories
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    ''' A detail view of service '''

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service
    }

    return render(request, 'services/service_detail.html', context)
