from django.contrib import admin
from .models import SiteSettings, NavbarObtion

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass

@admin.register(NavbarObtion)
class NavbarObtion(admin.ModelAdmin):
    pass