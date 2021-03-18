from django.contrib import admin
from .models import Categori
# Register your models here.


class CategoriAdmin(admin.ModelAdmin):
    product_display = ('id', 'name', 'listing', 'email', 'contact_date')
    product_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Categori, CategoriAdmin)
