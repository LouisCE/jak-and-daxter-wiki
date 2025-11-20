from django.db import models
from cloudinary.models import CloudinaryField

class Colour(models.Model):
    """Colours under Morph Gun"""
    name = models.CharField(max_length=25, blank=False)

    class Meta:
        verbose_name = 'Colour'
        verbose_name_plural = 'Colours'

    def __str__(self):
        return self.name


class Weapon(models.Model):
    """Weapons under a Colour"""
    name = models.CharField(max_length=100, blank=False)
    colour = models.ForeignKey(
        Colour, on_delete=models.CASCADE, related_name="weapons",
        blank=False
    )
    description = models.TextField(blank=False)
    image = CloudinaryField("image", default="placeholder", blank=False)

    class Meta:
        verbose_name = 'Weapon'
        verbose_name_plural = 'Weapons'

    def __str__(self):
        return self.name
