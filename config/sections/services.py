from courses.models import Course, Category

def get_auto_items(section):
    if section.mode == "manual":
        
        return [item.course or item.category for item in section.items.all().order_by("order")][:section.limit]

    # حالت اتوماتیک
    if section.content_type == "course":
        return Course.objects.filter(status="published").order_by("-created_date")[:section.limit]

    elif section.content_type == "category":
        return Category.objects.all().order_by("name")[:section.limit]

    return []