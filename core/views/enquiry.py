from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from core.forms import EnquiryForm

def make_enquiry(request):
    template_name = 'enquiries/make_enquiry.html'
    form = EnquiryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Equiry successfully submitted, we will be in touch with you as soon as possible.")
            return redirect('core:make_enquiry')
    return render(request,template_name,{'form':form})
