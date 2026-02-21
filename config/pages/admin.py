from django.contrib import admin
from .models import Page
from sections.models import Section

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    inlines = [SectionInline]