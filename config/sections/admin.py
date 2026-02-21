from django.contrib import admin
from .models import Section, SectionItem

class SectionItemInline(admin.TabularInline):
    model = SectionItem
    extra = 1

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "page", "order", "mode", "content_type")
    list_filter = ("page", "mode", "content_type")
    ordering = ("page", "order")
    inlines = [SectionItemInline]
