from django.contrib import admin
from .models import Price

# Register your models here.

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'created')
    list_display_links = ('id',)
    search_fields = ('id', 'price', 'created')

admin.site.register(Price, PriceAdmin)