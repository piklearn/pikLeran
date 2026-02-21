from django.db import models

class SiteSettings(models.Model):
    setting_name = models.CharField(max_length=100, unique=True)
    setting_value = models.TextField()
    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.setting_name
    

class NavbarOption(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    link = models.CharField('آدرس')
    order = models.PositiveIntegerField(default=0) 

    class Meta:
        verbose_name = "گزینه نوبار"
        verbose_name_plural = "گزینه‌های نوبار"
        ordering = ['order']
    def __str__(self):
        return self.name