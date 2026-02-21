from django.contrib import admin
from .models import SiteSettings, NavbarOption

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass

@admin.register(NavbarOption)
class NavbarOption(admin.ModelAdmin):
    list_display = ['name', 'link', 'order']