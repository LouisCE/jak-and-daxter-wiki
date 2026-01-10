from django.db import models
from cloudinary.models import CloudinaryField


class Collectable(models.Model):

    name = models.CharField(max_length=20, blank=False)
    description = models.TextField(blank=False)
    image = CloudinaryField("image", default="placeholder", blank=False)

    # Custom ordering
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
