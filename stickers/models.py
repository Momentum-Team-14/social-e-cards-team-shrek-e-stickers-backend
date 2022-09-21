from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


COLOR_CHOICES = [
    ('red', 'Red'),
    ('pink', 'Pink'),
    ('black', 'Black')
]

PATTERN_CHOICES = [
    ('argyle', 'Argyle'),
    ('stripes', 'Stripes'),
]

FONT_CHOICES = [
    ('ms+madi', 'Ms+Madi'),
    ('josefin+sans', 'Josefin+Sans'),
    ('dosis', 'Dosis'),
    ('dangrek', 'Dangrek'),
    ('dancing+script', 'Dancing+Script'),
    ('eb+garamond', 'EB+Garamond'),
    ('lobster', 'Lobster'),
    ('pacifico', 'Pacifico'),
]


class Sticker(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="name of your sticker")
    background_color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='white',
    )
    background_pattern = models.URLField(
        max_length=100,
        choices=PATTERN_CHOICES,
        default='',
        blank=True,
        null=True
    )
    image = models.URLField(
        max_length=100,
        blank=True,
        null=True
    )
    font = models.CharField(
        max_length=50,
        choices=FONT_CHOICES,
        default='pacifico',
    )
    font_color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='black',
    )
    message = models.CharField(
        max_length=200,
        help_text='enter your message here',
        blank=True,
        null=True
    )
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="stickers"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True)
