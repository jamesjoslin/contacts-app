from django.contrib import admin
from .models import Person
# Register your models here.
#for what you see on /admin. helps if i need to go into the back door for some reason

class PersonAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('first', 'last', 'phone')

admin.site.register(Person, PersonAdmin)
