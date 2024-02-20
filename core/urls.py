from django.urls import path
from .views.general_pages import (
    home,
    contact
)

app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('contact-us',contact, name='contact')

]