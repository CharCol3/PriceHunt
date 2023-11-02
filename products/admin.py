from django.contrib import admin
from .models import Store, Product, PriceEntry, UserPoints


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'address')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'barcode', 'created_at', 'updated_at')
    search_fields = ('name', 'barcode')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)


@admin.register(PriceEntry)
class PriceEntryAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'price', 'date_reported', 'reported_by', 'created_at', 'updated_at')
    search_fields = ('product__name', 'store__name', 'price')
    list_filter = ('date_reported', 'store', 'product')
    ordering = ('-date_reported', 'store', 'product')


@admin.register(UserPoints)
class UserPointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points', 'created_at', 'updated_at')
    search_fields = ('user__username', 'total_points')
    list_filter = ('total_points', 'created_at')
    ordering = ('-total_points',)
