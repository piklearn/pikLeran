from .models import NavbarOption

def navbar_options(request):
    return {'navbar_options': NavbarOption.objects.all()}