from django.contrib import admin

from customizations import models

# Register your models here.


@admin.register(models.screenSides)
class screenSidesAdmin(admin.ModelAdmin):
    list_display = ("name", "property_value")


@admin.register(models.fontFamilies)
class fontFamiliesAdmin(admin.ModelAdmin):
    list_display = ("name", "property_value")


@admin.register(models.colors)
class colorsAdmin(admin.ModelAdmin):
    list_display = ("name", "property_value")
