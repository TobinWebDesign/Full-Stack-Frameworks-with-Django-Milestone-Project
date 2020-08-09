from django.contrib import admin
from .models import Retreat, Category

# Register your models here.

class RetreatAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Retreat, RetreatAdmin)
admin.site.register(Category, CategoryAdmin)