from django.db import models
from cloudinary.models import CloudinaryField

class Character(models.Model):
    """Character model."""
    name = models.CharField(max_length=100)
    quote = models.CharField(max_length=255, blank=True)
    image = CloudinaryField("image", default="placeholder", blank=True)

    # Stats
    sex = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=20, blank=True)
    skin = models.CharField(max_length=50, blank=True)
    hair = models.CharField(max_length=50, blank=True)
    eyes = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    occupation = models.CharField(max_length=100, blank=True)

    appearance = models.TextField(blank=True)
    personality = models.TextField(blank=True)

    def __str__(self):
        return self.name
