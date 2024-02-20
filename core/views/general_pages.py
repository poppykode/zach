from django.shortcuts import get_object_or_404, redirect, render
from core.models import (
    Slider,
    Service,
    Folder
)

def home(request):
    template_name = 'general_pages/home.html'
    sliders = Slider.objects.all()
    services = Service.objects.all()
    recent_works = Folder.objects.all()[:3]
    context = {
        'sliders':sliders,
        'services':services,
        'recent_works':recent_works
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'general_pages/contact.html'
    return render(request, template_name)