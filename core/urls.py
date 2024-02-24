from django.urls import path
from .views.general_pages import (
    home,
    contact
)

from .views.gallery import (
    folders,
    folders_images

)

app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('contact-us',contact, name='contact'),
    path('our-gallery-folders',folders, name='folders'),
    path('folders/images/<slug:slug>',folders_images, name='folders_images')

]