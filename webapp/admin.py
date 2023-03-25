from django.contrib import admin

from webapp.models import Product, Review


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'pic')
    list_filter = ('name', 'category')
    search_fields = ('name', 'category')
    fields = ('name', 'category', 'description', 'pic')
    readonly_fields = ('id', 'created_at', 'updated_at', 'deleted_at')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'review', 'rating')
    list_filter = ('author', 'product', 'rating')
    search_fields = ('author', 'product', 'rating')
    fields = ('author', 'product', 'review', 'rating')
    readonly_fields = ('id', 'created_at', 'updated_at', 'deleted_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)