from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Sticker
from rest_framework.serializers import ListSerializer


class StickerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sticker
        fields = ('id', 'name', 'background_color', 'background_pattern',
                  'image', 'font', 'font_color', 'message', 'creator', 'created_at', 'updated_at', 'draft')


class StickerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sticker
        fields = "__all__"
