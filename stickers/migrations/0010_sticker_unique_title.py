# Generated by Django 4.0 on 2022-09-29 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0009_alter_sticker_background_color_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='sticker',
            constraint=models.UniqueConstraint(fields=('title', 'creator'), name='unique_title'),
        ),
    ]