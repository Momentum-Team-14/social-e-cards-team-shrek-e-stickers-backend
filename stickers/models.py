from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


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

IMAGE_CHOICES = [
    ('https://media.istockphoto.com/photos/donut-with-sprinkles-isolated-picture-id538335769?k=20&m=538335769&s=612x612&w=0&h=A1DAZd6aHjfRyq2qKAKuBD9KAf0cq1LXKW8mpvTxKgU=',
     'donut'),
    ('https://cdn.pixabay.com/photo/2015/04/19/08/33/flower-729512__340.jpg',
        'flower'),
    ('https://natureconservancy-h.assetsadobe.com/is/image/content/dam/tnc/nature/en/photos/shutterstock_1512536354.jpg?crop=0%2C317%2C2664%2C1465&wid=4000&hei=2200&scl=0.666',
        'butterfly'),
    ('http://cdn.shopify.com/s/files/1/0641/1521/products/patches-smiley-face-happy-sad-venn.jpg?v=1613156051',
        'happy-sad-face'),
    ('https://img.freepik.com/free-vector/ice-cream-cone-cartoon-icon-illustration-sweet-food-icon-concept-isolated-flat-cartoon-style_138676-2924.jpg?w=360',
        'ice-cream'),
    ('https://illustoon.com/photo/4292.png',
        'thumbs-up'),
    ('https://www.pngitem.com/pimgs/m/595-5957528_black-heart-symbol-outline-love-heart-png-transparent.png',
        'heart'),
]


class Sticker(models.Model):

    class Colors(models.TextChoices):
        BLACK = 'black', _('Black')
        WHITE = 'white', _('White')
        YELLOW = 'yellow', _('Yellow')
        GREEN = 'green', _('Green')
        TURQUOISE = 'turqoise', _('Turqoise')
        BLUE = 'blue', _('Blue')
        PURPLE = 'purple', _('Purple')
        RED = 'red', _('Red')
        FUSCHIA = 'fuschia', _('Fuschia')
        PINK = 'pink', _('Pink')
        ORANGE = 'orange', _('Orange')

    class Fonts(models.TextChoices):
        DANGREK = 'dangrek', _('Dangrek')
        DANCING_SCRIPT = 'dancing+script', _('Dancing+Script')
        DOSIS = 'dosis', _('Dosis')
        EB_GARAMOND = 'eb+garamond', _('EB+Garamond')
        JOSEFIN_SANS = 'josefin+sans', _('Josefin+Sans')
        LOBSTER = 'lobster', _('Lobster')
        MS_MADI = 'ms+madi', _('Ms+Madi')
        PACIFICO = 'pacifico', _('Pacifico')

    title = models.CharField(
        max_length=50,
        help_text="name of your sticker")
    background_color = models.CharField(
        max_length=50,
        choices=Colors.choices,
        default=Colors.WHITE,
    )
    background_pattern = models.URLField(
        max_length=100,
        choices='',
        default='',
        blank=True,
        null=True
    )
    pattern_url = models.URLField(
        max_length=200,
        choices=PATTERN_CHOICES,
        default='',
        blank=True,
        null=True
    )
    image_url = models.URLField(
        max_length=200,
        choices=IMAGE_CHOICES,
        blank=True,
        null=True
    )
    font = models.CharField(
        max_length=50,
        choices=Fonts.choices,
        default=Fonts.PACIFICO,
    )
    font_color = models.CharField(
        max_length=50,
        choices=Colors.choices,
        default=Colors.BLACK,
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
