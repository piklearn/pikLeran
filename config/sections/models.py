from django.db import models
from pages.models import Page

class Section(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    limit = models.PositiveIntegerField(default=6)
    more_url = models.CharField(max_length=255, blank=True)

    # نوع محتوایی که Section نمایش میده
    TYPE_CHOICES = [
        ("course", "Course"),
        ("category", "Category"),
    ]
    content_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    MODE_CHOICES = [
        ("auto", "Automatic"),
        ("manual", "Manual"),
    ]
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default="auto")

    def __str__(self):
        return self.title

class SectionItem(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="items")
    # برای حالت دستی، یه course خاص یا category انتخاب می‌کنیم
    course = models.ForeignKey('courses.Course', null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey('courses.Category', null=True, blank=True, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        if self.course:
            return self.course.title
        if self.category:
            return self.category.name
        return f"Item in {self.section.title}"
