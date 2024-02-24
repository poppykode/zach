from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import (
    Slider,
    Service,
    Folder
)
from core.forms import ContactForm

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
    form = ContactForm(request.POST or None)
    template_name = 'general_pages/contact.html'
    if request.method == 'POST':
        if form.is_valid():
            # send email to admin
            print(form)
            messages.success(request,'Message successfully sent, we will contact you shortly.')
            return redirect('core:contact')

    return render(request, template_name,{'form':form})