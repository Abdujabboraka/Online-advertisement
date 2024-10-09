from django.contrib import admin
from .models import Category, Ad

# Register your models here.


class AdAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'created')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'created')
    list_display_links = ('id', 'name',)



admin.site.register(Category)
admin.site.register(Ad, AdAdmin)


