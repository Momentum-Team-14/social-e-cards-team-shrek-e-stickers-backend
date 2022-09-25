from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    bio = models.TextField(
        max_length=200, help_text='Enter a bio', blank=True, null=True)
    avatar = models.URLField(max_length=100, blank=True, null=True)
    display_name = models.CharField(
        max_length=25,
        help_text='Enter the name you want to display',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'username={self.username}: displayname={self.display_name}'


class Follow(models.Model):
    following_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='following', blank=True, null=True)
    followed_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='followed_by', blank=True, null=True)

    def __str__(self):
        return f'Follower:{self.following_user.username} Following:{self.followed_user.username}'


COLOR_CHOICES = [
    ('black', 'Black'),
    ('white', 'White'),
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('turqoise', 'Turqoise'),
    ('blue', 'Blue'),
    ('purple', 'Purple'),
    ('red', 'Red'),
    ('fuschia', 'Fuschia'),
    ('pink', 'Pink'),
    ('orange', 'Orange'),
]

PATTERN_CHOICES = [
    ('https://www.transparenttextures.com/patterns/black-thread.png',
     'black-thread'),
    ('https://www.transparenttextures.com/patterns/bo-play.png',
        'bo-play'),
    ('https://www.transparenttextures.com/patterns/brick-wall.png',
        'brick-wall'),
    ('https://www.transparenttextures.com/patterns/clean-textile.png',
        'clean-textile'),
    ('https://www.transparenttextures.com/patterns/crisp-paper-ruffles.png',
        'crisp-paper-ruffles'),
    ('https://www.transparenttextures.com/patterns/cutcube.png',
        'cutcube'),
    ('https://www.transparenttextures.com/patterns/diagmonds-light.png',
        'diagmonds-light'),
    ('https://www.transparenttextures.com/patterns/dimension.png',
        'dimensions')
]

FONT_CHOICES = [
    ('dancing+script', 'Dancing+Script'),
    ('dangrek', 'Dangrek'),
    ('dosis', 'Dosis'),
    ('eb+garamond', 'EB+Garamond'),
    ('josefin+sans', 'Josefin+Sans'),
    ('lobster', 'Lobster'),
    ('ms+madi', 'Ms+Madi'),
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

    def __str__(self):
        return f'{self.name}'
