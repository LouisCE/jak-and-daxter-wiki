from cloudinary.models import CloudinaryField
from django.db import models


class HomePage(models.Model):
    hero_image = CloudinaryField(
        "image",
        default="placeholder",
    )
    hero_title = models.CharField(
        max_length=200,
        default="Adventure Awaits in Haven City",
    )
    hero_text = models.TextField(
        default=(
            "Explore Morph Gun mods, Characters, "
            "Collectibles and more!"
        ),
    )
