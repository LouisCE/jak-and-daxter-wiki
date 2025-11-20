from django.apps import AppConfig


class MorphGunConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weapons'          # Keep the real folder name
    verbose_name = 'Morph Gun'  # Display correctly in admin
