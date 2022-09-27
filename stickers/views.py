from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .models import Sticker, CustomUser, Follow
from .serializers import StickerListSerializer, StickerDetailSerializer, UserSerializer, FollowSerializer, FollowListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'stickers/': reverse('all-stickers', request=request, format=format),
    })


class StickerList(generics.ListCreateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerListSerializer
    permission_classes = []


class UserStickerList(generics.ListCreateAPIView):
    serializer_class = StickerListSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.stickers.all()
        return queryset


class FollowListStickers(generics.ListAPIView):
    queryset = Sticker.objects.none()
    serializer_class = StickerListSerializer
    permission_classes = ()

    def get_queryset(self):
        queryset = super().get_queryset()
        list_of_followed_users = Follow.objects.filter(following_user=self.request.user)
        for user in list_of_followed_users:
            stickers = Sticker.objects.filter(creator=user.followed_user)
            queryset = queryset | stickers
        return queryset


class StickerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerListSerializer
    permission_classes = []


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()

    def get_queryset(self):
        user_id = CustomUser.objects.get(id=self.request.user.id)
        queryset = CustomUser.objects.filter(username=user_id.username)
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()


# List of User's logged in user is following
class FollowingList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = FollowListSerializer
    permission_classes = ()

    def get_queryset(self):
        user_username = self.request.user.username
        user = get_object_or_404(CustomUser, username=user_username)
        users_following = user.following.all()
        return users_following


# List of User's logged in user is followed by
class FollowedList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = FollowListSerializer
    permission_classes = ()

    def get_queryset(self):
        user_username = self.request.user.username
        user = get_object_or_404(CustomUser, username=user_username)
        user_followers = user.followed_by.all()
        return user_followers


class FollowCreate(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = ()

    def perform_create(self, serializer):
        user_to_follow = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        user = self.request.user
        serializer.save(followed_user=user_to_follow, following_user=user)


class UnFollowDestroy(generics.RetrieveDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = ()

# need to get the pk of the Follow instance in order to destroy it
# something like if Follow.followed_user = user_to_unfollow
    def destroy(self, request, *args, **kwargs):
        user_to_unfollow = self.get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        list_of_followed_users = Follow.objects.filter(following_user=self.request.user)
        for user in list_of_followed_users:
            if user.followed_user == user_to_unfollow:
                self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

