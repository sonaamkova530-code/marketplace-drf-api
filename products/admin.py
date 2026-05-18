from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Review, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['get_html_photo', 'name', 'price', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']

    def get_html_photo(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="border-radius: 5 px;" />', obj.image.url)
        return "Немає фото"
    get_html_photo.short_description = "photo"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']