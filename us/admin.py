from django.contrib import admin
from .models import Senator, Representative

admin.site.register(Senator)
admin.site.register(Representative)