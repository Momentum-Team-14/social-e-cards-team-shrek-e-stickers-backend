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


class StickerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerListSerializer
    permission_classes = []


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()


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


# Example code, not tested
class FollowCreate(generics.ListCreateAPIView):
    pass  # using FollowCreate in urlpatterns so had to pass for now
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer
#     permission_classes = ()

#     def perform_create(self, serializer):
#         queryset = self.queryset.filter(
#             followed_user=self.request.data['follow'],
#             following_user=self.request.user
#             )
#         if len(queryset) == 0:
#             serializer.save(
#                 followed_user=self.request.data['follow'],
#                 following_user=self.request.user
#                 )
#             return Response(status=status.HTTP_201_CREATED)


# prep for unfollow but doesn't do anything yet
class UnFollow(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = ()


# Examples
# class FollowCreate(generics.ListCreateAPIView):
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer
#     permission_classes = ()

#     def perform_create(self, serializer):
#         followed_user = CustomUser.objects.get(pk=self.request.data['follow'])
#         if followed_user.id is not self.request.user.id:
#             serializer.save(following_user=self.request.user, followed_user=followed_user)
#         else:
#             return Response({"error": "Users cannot follow themselves"})
###############################################################################
# example code that may help
# def follow_unfollow_user(request):
#     if request.method=="POST":
#         logged_in_user = CustomUser.objects.get(user=request.user)
#         pk = request.POST.get('user_pk')
#         obj = CustomUser.objects.get(pk=pk)

#         if obj.user in logged_in_user.following.all():
#             logged_in_user.following.remove(obj.user)
#         else:
#             logged_in_user.following.add(obj.user)
#         return Response(status=status.HTTP_201_CREATED)
#     return
###############################################################################
# More example code
# def follow(request):
#     if request.method == 'POST':
#         value = request.POST['value']
#         user = request.POST['user']
#         follower = request.POST['follower']
#         if value == 'follow':
#             add_follow = Follow.objects.create(followed_user=follower, following_user=user)
#             add_follow.save()
#         return Response(status=status.HTTP_201_CREATED)
