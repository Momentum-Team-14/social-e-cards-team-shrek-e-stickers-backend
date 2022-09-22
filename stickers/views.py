from django.shortcuts import render
from rest_framework import generics, status
from .models import Sticker
from .serializers import StickerListSerializer, StickerDetailSerializer


class StickerList(generics.ListCreateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerListSerializer
    permission_classes = []


class StickerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerDetailSerializer
    permission_classes = []
