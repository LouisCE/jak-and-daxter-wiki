from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Colour(models.Model):
    """Colour / Category model."""
    name = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    """Weapon model with FK relationship to colour."""
    name = models.CharField(max_length=100, blank=False)
    colour = models.ForeignKey(
        Colour, on_delete=models.CASCADE, related_name="weapons",
        blank=False
    )
    description = models.TextField(blank=False)
    image = CloudinaryField("image", default="placeholder", blank=False)

    def __str__(self):
        return self.name
