from django.db import models
from cloudinary.models import CloudinaryField


class Character(models.Model):
    """Character model."""
    name = models.CharField(max_length=50)
    quote = models.CharField(max_length=250, blank=False)
    image = CloudinaryField("image", default="placeholder")

    # Character bios
    sex = models.CharField(max_length=50, blank=False)
    age = models.CharField(max_length=50, blank=False)
    skin = models.CharField(max_length=50, blank=False)
    hair = models.CharField(max_length=50, blank=False)
    eyes = models.CharField(max_length=50, blank=False)
    height = models.CharField(max_length=50, blank=False)
    weight = models.CharField(max_length=50, blank=False)
    occupation = models.CharField(max_length=50, blank=False)

    appearance = models.TextField(blank=False)
    personality = models.TextField(blank=False)

    # Custom ordering
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
