from django.shortcuts import render

def error_404_view(request, exception):
    return render(request,'errors/404.html')