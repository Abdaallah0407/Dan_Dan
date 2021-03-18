from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'categori')

    list_display_links = ('id', 'title')
    list_filter = ('categori',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
