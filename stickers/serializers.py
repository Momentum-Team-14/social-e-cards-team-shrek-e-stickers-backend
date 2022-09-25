from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Sticker, CustomUser
from rest_framework.serializers import ListSerializer


class StickerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sticker
        fields = ('id', 'title', 'background_color', 'pattern_url', 'image_url', 'font',
                  'font_color', 'message', 'creator', 'created_at', 'updated_at', 'draft')


class StickerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sticker
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'bio', 'avatar', 'display_name',)
