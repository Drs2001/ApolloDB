from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'position', 'location', 'application_date', 'followed_up']
    list_filter = ['followed_up', 'application_date']
    search_fields = ['company_name', 'position']
    ordering = ['-application_date']
