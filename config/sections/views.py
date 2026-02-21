from django.shortcuts import render
from sections.models import Page
from sections.services import get_auto_items

def home(request):
    page = Page.objects.prefetch_related("sections__items").get(slug="home")
    sections_data = []

    for section in page.sections.all().order_by("order"):
        items = get_auto_items(section)
        sections_data.append({
            "title": section.title,
            "items": items,
            "more_url": section.more_url,
        })

    return render(request, "main/home.html", {"sections": sections_data})
