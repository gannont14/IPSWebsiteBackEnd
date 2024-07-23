from django.contrib import admin


# Register your models here.
from .models import Service, Photo, AboutMainContent, BackgroundImage

# Register each of the models into the admin panel for testing
admin.site.register(Service)
admin.site.register(Photo)
admin.site.register(AboutMainContent)
admin.site.register(BackgroundImage)