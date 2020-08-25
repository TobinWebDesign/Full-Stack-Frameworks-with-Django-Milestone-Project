from django.contrib import admin

from .models import Product, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product', 'rating', 'user_name', 'comment')
    list_filter = ['product', 'rating']
    search_fields = ['comment']
    
admin.site.register(Product)
admin.site.register(Review, ReviewAdmin)