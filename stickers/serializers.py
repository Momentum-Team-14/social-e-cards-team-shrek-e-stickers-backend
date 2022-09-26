from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Sticker, CustomUser, Follow
from rest_framework.serializers import ListSerializer


class StickerListSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
        slug_field="username", read_only=True)

    class Meta:
        model = Sticker
        fields = ('id', 'title', 'background_color', 'pattern_url', 'image_url', 'font',
                  'font_color', 'message', 'creator', 'created_at', 'updated_at', 'draft')


class StickerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sticker
        fields = "__all__"


# serializer for Follow pages that uses CustomUser model fields
class FollowListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'display_name', 'avatar',)


class UserSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    followed_count = serializers.SerializerMethodField()
    stickers = StickerListSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'bio', 'avatar', 'display_name',
                  'following_count', 'followed_count', 'stickers',)

    def get_following_count(self, obj):
        count = len(Follow.objects.filter(following_user=obj.id))
        return count

    def get_followed_count(self, obj):
        count = len(Follow.objects.filter(followed_user=obj.id))
        return count


# serializer just for the Follow model fields if we need it?
class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ('following_user', 'followed_user',)
