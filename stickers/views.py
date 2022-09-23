from django.shortcuts import render
from rest_framework import generics, status
from .models import Sticker, CustomUser
from .serializers import StickerListSerializer, StickerDetailSerializer, UserSerializer
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
