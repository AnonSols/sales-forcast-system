# forecast/admin.py
from django.contrib import admin
from .models import HistoricalData

class HistoricalDataAdmin(admin.ModelAdmin):  # Inherits from admin.ModelAdmin
    list_display = ('date', 'product_category', 'sales')
    list_filter = ('date', 'product_category')
    search_fields = ('product_category',)

admin.site.register(HistoricalData, HistoricalDataAdmin)