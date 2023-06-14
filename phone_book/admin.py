from django.contrib import admin
from .models import *

admin.site.register(PlaceOfWork)
admin.site.register(Location)
admin.site.register(DepartmentName)
admin.site.register(Position)


@admin.register(PhoneBook)
class PhoneBookAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'place_of_work',
        'mobile_phone',
        'work_phone',
        'birthday'
    )
    list_display_links = ('first_name',)

