from django.contrib import admin

# Register your models here.
from .models import Gallery, Folder, Media

admin.site.register(Folder)
admin.site.register(Gallery)
admin.site.register(Media)
