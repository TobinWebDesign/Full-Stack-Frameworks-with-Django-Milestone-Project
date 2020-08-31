from django.contrib import admin
from .models import Class, Level

# Register your models here.


def duplicate_event(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_event.short_description = "Duplicate selected record"


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'dificulty',
        'price',
        'level',
        'image',
        'day',
        'time'
    )

    ordering = ('day',)
    actions = [duplicate_event.short_description]

class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Class, ClassAdmin)
admin.site.register(Level, LevelAdmin)
