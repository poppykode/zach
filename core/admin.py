from django.contrib import admin
from .models import (
    Slider,
    Service,
    Folder,
    Image,
    Enquiry,
    Article
)

# Register your models here.

class FolderAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['name','service','location',]
    list_display =['name','service','location',]
    list_filter = ('name','service')
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("name",)}
    list_display_links = ('name','service')

    class Meta:
        model= Folder

class ServiceAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['name',]
    list_display =['name','description']
    list_filter = ('name','timestamp')
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("name",)}
    list_display_links = ('name',)

    class Meta:
        model= Service

class EnquiryAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['enquiry_id','full_name','phone_number','email_address',]
    list_display =['enquiry_id','full_name','phone_number','email_address','booking_date_time','attended',]
    list_filter = ('service','timestamp')
    readonly_fields = ['enquiry_id','updated','timestamp']
    list_display_links = ('enquiry_id',)

    class Meta:
        model= Enquiry

class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['title',]
    list_display =['title','author']
    list_filter = ('title','timestamp','author')
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("title",)}
    list_display_links = ('title',)

    class Meta:
        model= Article

admin.site.register(Slider)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Folder,FolderAdmin)
admin.site.register(Image)
admin.site.register(Enquiry,EnquiryAdmin)
admin.site.register(Article,ArticleAdmin)