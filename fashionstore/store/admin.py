from django.contrib import admin
from .models import Product, Category, Cart, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock']
    list_filter = ['category']
    search_fields = ['name']

admin.site.register(Cart)
admin.site.register(CartItem)
