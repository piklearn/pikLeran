from django.shortcuts import render, get_object_or_404
from pages.models import Page

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    sections = page.sections.prefetch_related('items')  # بارگذاری بهینه آیتم‌ها
    return render(request, "pages/page_detail.html", {"page": page, "sections": sections})
