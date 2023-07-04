from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

@admin.register(PlaceOfWork)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title', 'id')
    mptt_level_indent = 20


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

