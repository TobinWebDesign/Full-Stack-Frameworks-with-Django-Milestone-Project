from django.contrib import admin
from .models import Class, Level

# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'dificulty',
        'price',
        'level',
        'image',
        'day',
    )

    ordering = ('day',)

class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Class, ClassAdmin)
admin.site.register(Level, LevelAdmin)
