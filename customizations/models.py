from django.db import models


# Create your models here.
class BaseCustomizationModel(models.Model):
    class Meta:
        abstract = True
        ordering = ["-created_at"]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class screenSides(BaseCustomizationModel):
    name = models.CharField(max_length=255)
    prop = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):  # type: ignore
        return self.name

    @property
    def property_value(self):  # type: ignore
        return f"{self.prop}: {self.value}"


class fontFamilies(BaseCustomizationModel):
    name = models.CharField(max_length=255)
    prop = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):  # type: ignore
        return self.name

    @property
    def property_value(self):  # type: ignore
        return f"{self.prop}: {self.value}"


class colors(BaseCustomizationModel):
    name = models.CharField(max_length=255)
    prop = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):  # type: ignore
        return self.name

    @property
    def property_value(self):  # type: ignore
        return f"{self.prop}: {self.value}"
