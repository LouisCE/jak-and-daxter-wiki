from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Colour(models.Model):
    """Colours under Morph Gun"""
    name = models.CharField(max_length=25, blank=False)
    description = models.TextField(blank=False)
    image = CloudinaryField(
        "image",
        default="v1763855318/1e67e5cbe56466efefdbe523de1f023b0a0dc544_hq_grmzpj.jpg"
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Colour'
        verbose_name_plural = 'Colours'
        ordering = ['order']

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
    image = CloudinaryField(
        "image",
        default="v1763855318/1e67e5cbe56466efefdbe523de1f023b0a0dc544_hq_grmzpj.jpg"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Weapon'
        verbose_name_plural = 'Weapons'
        ordering = ['order']

    def __str__(self):
        return self.name


class WeaponRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weapon = models.ForeignKey(
        Weapon,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'weapon')

    def __str__(self):
        return f"{self.weapon.name} — {self.score}/10 by {self.user.username}"


class MorphGunUpgrade(models.Model):
    JAK_II = "jak2"
    JAK_III = "jak3"

    GAME_CHOICES = [
        (JAK_II, "Jak II"),
        (JAK_III, "Jak 3"),
    ]

    name = models.CharField(max_length=120)
    game = models.CharField(max_length=4, choices=GAME_CHOICES)

    effect = models.TextField()
    requirement = models.CharField(max_length=255)

    price = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Jak 3 only (Precursor Orbs)",
    )

    weapons = models.ManyToManyField(
        Weapon,
        related_name="upgrades",
        blank=True,
    )

    class Meta:
        ordering = ["game", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_game_display()})"
