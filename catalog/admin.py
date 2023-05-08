from django.contrib import admin
from catalog.models import Product, Category, Contacts


# admin.site.register(Product)  -   по дефолту - __str__

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category')
    search_fields = ('product_name', 'product_info')
    list_filter = ('product_category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('id', 'category_name')
    list_filter = ('category_name',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'contact_number')
    search_fields = ('id', 'contact_name', 'contact_number')
    list_filter = ('contact_name',)