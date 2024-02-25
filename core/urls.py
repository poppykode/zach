from django.urls import path
from .views.general_pages import (
    home,
    contact,
    about
)

from .views.gallery import (
    folders,
    folders_images
)
from .views.enquiry import (
    make_enquiry
)
from .views.services import (
    services,
    service_details
)
from .views.articles import (
    articles,
    article_details
)
app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('contact-us',contact, name='contact'),
    path('about-us',about, name='about'),
    path('our-gallery-folders',folders, name='folders'),
    path('folders/images/<slug:slug>',folders_images, name='folders_images'),
    path('make-enquiry',make_enquiry, name='make_enquiry'),
    path('services',services, name='services'),
    path('service/<slug:slug>',service_details, name='service_details'),
    path('articles',articles, name='articles'),
    path('article/<slug:slug>',article_details, name='article_details'),

]