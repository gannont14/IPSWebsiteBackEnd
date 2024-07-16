from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

# photos for photo gallery
class Photo(models.Model):
    # description of image for alt tag FOR ACCESSIBILITY
    description = models.TextField(null=True, blank=True)
    # tag of what service image falls under
    serviceTag = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description