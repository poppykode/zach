from django.db import models
import random
import string
import datetime

# Create your models here.

class Slider(models.Model):
    header_top = models.CharField(max_length=255)
    header_bottom = models.CharField(max_length=255)
    button_link = models.URLField()
    button_text = models.CharField(max_length=50)
    button_border_color = models.CharField(max_length = 50, default='#55000c')
    banner_image = models.ImageField(upload_to='banners')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.header_top} {self.header_bottom}"
    
    class Meta:
        ordering = ["-timestamp", ]

class Service(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons')
    description = models.TextField()
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp", ]

class Folder(models.Model):
    service = models.ForeignKey(Service,on_delete = models.CASCADE, related_name = 'service_folder')
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='cover_image')
    location = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp", ]


class Image(models.Model):
    folder = models.ForeignKey(Folder,on_delete = models.CASCADE, related_name = 'image_folder')
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"image caption {self.caption} :folder {self.folder.name}"
    
    class Meta:
        ordering = ["-timestamp", ]

# ZACH2024TYG

class Enquiry(models.Model):
    enquiry_id = models.CharField(max_length = 12)
    service = models.ManyToManyField(Service, related_name = 'service_enquiry')
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=100)
    attachment = models.ImageField(upload_to='attachments/%Y/%m/%d/',null=True,blank=True)
    booking_date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    expected_number_of_guests = models.PositiveIntegerField()
    budget= models.FloatField(default=0.00,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    attended = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    
    def save(self, *args, **kwargs):
        if not self.enquiry_id:
            self.enquiry_id = self.__generate_enquiry_number()
        super().save(*args, **kwargs)

    def __generate_enquiry_number(self,size=3, chars=string.ascii_uppercase + string.digits):
        enquiry_number = ''
        random_text = "".join(random.choice(chars) for x in range(size))
        year  = str(datetime.date.today().year)
        enquiry_number = 'ZACH'+year+random_text
        try:
            Enquiry.objects.get(enquiry_id=enquiry_number)
            self.__generate_enquiry_number()
        except:
            return enquiry_number

   


    def __str__(self):
        return f"{self.full_name} - {self.phone_number} - {self.email_address}"
    
    class Meta:
        ordering = ["-timestamp", ]


