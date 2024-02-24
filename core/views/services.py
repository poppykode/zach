from django.shortcuts import get_object_or_404,  render
from django.core.paginator import Paginator
from core.models import Service, Folder

def services(request):
    template_name = 'services/services.html'
    services = Service.objects.all()
    return render(request, template_name,{'services':services})

def service_details(request, slug):
    template_name = 'services/service_details.html'
    service = get_object_or_404(Service,slug=slug)
    folders_ = Folder.objects.filter(service=service)
    page = request.GET.get('page', 1)
    paginator = Paginator(folders_, 6)
    folders = paginator.page(page)
    context = {
        'folders':folders,
        'obj':service
    }
    return render(request, template_name,context)