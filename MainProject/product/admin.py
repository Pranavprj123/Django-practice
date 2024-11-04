from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([HsnCode,Product,ProductImages,Category,Brand])

admin.site.site_header="My Site"
admin.site.site_title="My Page"