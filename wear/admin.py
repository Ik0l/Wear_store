# -*- coding:utf-8 -*-

from django.contrib import admin

from wear.models import Category, Cloth, Size, SizeCount, Gallery, Cart


class SizesInLine(admin.TabularInline):
    model = SizeCount
    extra = 1

class GaleryInLine(admin.TabularInline):
    model = Gallery
    extra = 1

class ClothAdmin(admin.ModelAdmin):
    inlines = [SizesInLine, GaleryInLine]
    list_display = ('title', 'price', 'category', )


admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Cloth, ClothAdmin)
admin.site.register(Cart)