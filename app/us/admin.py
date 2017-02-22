from django.contrib import admin
from .congress.models import Senator, Representative
from .models import Person

admin.site.register(Senator)
admin.site.register(Representative)
#admin.site.register(Person)